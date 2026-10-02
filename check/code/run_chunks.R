# One session of the code gate (check/code_gate.py): every step in order, in this one R process.
#
#     Rscript --no-save --no-restore --no-init-file check/code/run_chunks.R in.json out.json
#
# in.json:  {"root": "<scratch project>", "steps": [{"kind": "r"|"sh"|"file", "code": "...",
#            "file": "code/x.R"}]}
# out.json: {"results": [{"output": "...", "errored": true|false}]}
#
# An r step is evaluated with the evaluate package in the global environment, so later steps
# see what earlier ones made, exactly as a reader's console does. Its output is rebuilt as the
# console prints it: printed values as they are; messages as their text; warnings after the
# top-level call that raised them ("Warning message:" and "In <call> : <message>", or the message
# alone when there is no call, wrapped by R's own 75-column rule); errors as
# "Error in <call> : <message>" or "Error: <message>", and for rlang/cli errors (dplyr, readr) the
# text rlang prints, without the backtrace. Plots are not text and are ignored.
# A sh step runs with bash in the project root, stdout and stderr together. A file step writes
# its code to a file under the root (a script the reader saves). Nothing here decides pass or
# fail; check/code_gate.py compares the outputs with the record.
#
# Everything below lives inside local(): the chunks run in the global environment, which must be
# exactly what a fresh `Rscript --no-init-file` session has - no objects, the same search() path.
# A helper left in globalenv() made `library(readr)` print "masked _by_ '.GlobalEnv': write_file"
# and `ls()` list the gate's own functions (found by the conductor, 2 Oct 2026). evaluate and
# jsonlite are only ever called with ::, so neither is attached.

local({
args <- commandArgs(trailingOnly = TRUE)
inp <- jsonlite::fromJSON(args[1], simplifyVector = FALSE)
root <- normalizePath(inp$root, mustWork = TRUE)
setwd(root)

options(width = 72, cli.num_colors = 1, crayon.enabled = FALSE, pillar.bold = FALSE,
        tibble.width = 72, rlang_backtrace_on_error = "none", cli.dynamic = FALSE,
        readr.show_progress = FALSE)

LONGWARN <- 75                     # R's errors.c: where a condition's message drops a line
wd <- function(s) nchar(s, type = "width")
first_line <- function(s) {
  if (!nzchar(s)) return("")
  strsplit(s, "\n", fixed = TRUE)[[1]][1]
}
EVAL_CALL <- quote(eval(expr, envir, enclos))   # evaluate's own frame, not the reader's call

call_text <- function(cnd) {
  call <- conditionCall(cnd)
  if (is.null(call) || identical(call, EVAL_CALL)) return(NULL)
  deparse(call, nlines = 1L)[1]
}

fmt_error <- function(e) {
  if (inherits(e, "rlang_error")) return(rlang::cnd_message(e, prefix = TRUE))
  msg <- conditionMessage(e)
  dc <- call_text(e)
  if (is.null(dc)) return(paste0("Error: ", msg))
  sep <- if (14 + wd(dc) + wd(first_line(msg)) > LONGWARN) " : \n  " else " : "
  paste0("Error in ", dc, sep, msg)
}

fmt_warnings <- function(ws) {
  n <- length(ws)
  one <- function(w, i = NULL) {
    msg <- conditionMessage(w)
    dc <- call_text(w)
    lead <- if (is.null(i)) "" else paste0(i, ": ")
    if (is.null(dc)) return(paste0(lead, msg))
    width <- (if (is.null(i)) 6 else 10) + wd(dc) + wd(first_line(msg))
    paste0(lead, "In ", dc, " :", if (width > LONGWARN) "\n " else "", " ", msg)
  }
  if (n == 1) return(paste0("Warning message:\n", one(ws[[1]])))
  if (n <= 10) {
    items <- vapply(seq_len(n), function(i) one(ws[[i]], i), "")
    return(paste0("Warning messages:\n", paste(items, collapse = "\n")))
  }
  if (n < 50) return(paste0("There were ", n, " warnings (use warnings() to see them)"))
  "There were 50 or more warnings (use warnings() to see the first 50)"
}

run_r <- function(code) {
  res <- evaluate::evaluate(code, envir = globalenv(), new_device = TRUE, stop_on_error = 1L,
                            keep_warning = TRUE, keep_message = TRUE)
  out <- character()
  pending <- list()
  errored <- FALSE
  flush <- function(prefix = "") {
    if (length(pending)) {
      out <<- c(out, paste0(prefix, fmt_warnings(pending), "\n"))
      pending <<- list()
    }
  }
  for (x in res) {
    if (inherits(x, "source")) {
      flush()
    } else if (is.character(x)) {
      out <- c(out, x)
    } else if (inherits(x, "error")) {
      errored <- TRUE
      out <- c(out, paste0(fmt_error(x), "\n"))
      flush("In addition: ")
    } else if (inherits(x, "warning")) {
      pending[[length(pending) + 1]] <- x
    } else if (inherits(x, "message")) {
      m <- conditionMessage(x)
      # cli messages (readr's column report) carry no final newline; the console still ends the line.
      if (!endsWith(m, "\n")) m <- paste0(m, "\n")
      out <- c(out, m)
    }
  }
  flush()
  list(output = paste(out, collapse = ""), errored = errored)
}

run_sh <- function(code) {
  old <- setwd(root)
  on.exit(setwd(old))
  out <- suppressWarnings(system2("bash", c("-c", shQuote(code)), stdout = TRUE, stderr = TRUE))
  status <- attr(out, "status")
  list(output = if (length(out)) paste0(paste(out, collapse = "\n"), "\n") else "",
       errored = !is.null(status) && status != 0)
}

write_file <- function(path, code) {
  full <- file.path(root, path)
  dir.create(dirname(full), recursive = TRUE, showWarnings = FALSE)
  writeLines(code, full, useBytes = TRUE)
  list(output = "", errored = FALSE)
}

results <- lapply(inp$steps, function(s) {
  tryCatch(
    switch(s$kind,
           r = run_r(s$code),
           sh = run_sh(s$code),
           file = write_file(s$file, s$code),
           list(output = paste("unknown step kind", s$kind), errored = TRUE)),
    error = function(e) list(output = paste0("code gate driver failed: ", conditionMessage(e), "\n"),
                             errored = TRUE))
})

txt <- jsonlite::toJSON(list(results = results), auto_unbox = TRUE, null = "null")
con <- file(args[2], open = "w", encoding = "UTF-8")
writeLines(txt, con, useBytes = TRUE)
close(con)
})
