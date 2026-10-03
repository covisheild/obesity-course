# S52-R1 intake, group c: render version-matched help pages, vignettes, DESCRIPTION and LICENSE
# files from the packages installed in this sandbox into books/S52-R1/intake/raw/.
# Run (UTF-8 locale required): LANG=C.UTF-8 LC_ALL=C.UTF-8 Rscript /home/claude/work/obesity-course/books/S52-R1/intake/build-c/render.R
# Every file written here is the raw text from which build.py cuts the stored passages.
options(useFancyQuotes = FALSE, width = 80)
RAW <- "/home/claude/work/obesity-course/books/S52-R1/intake/raw"
tools::Rd2txt_options(underline_titles = FALSE, width = 80)

# package -> topics (aliases) needed; extras marked in build.py
topics <- list(
  base      = c("mean", "NA", "c", "is.na", "stopifnot", "source", "set.seed", "round", "library"),
  utils     = c("sessionInfo", "Rscript", "packageVersion", "install.packages"),
  stats     = c("median", "sd", "quantile", "IQR"),
  dplyr     = c("filter", "select", "mutate", "summarise", "group_by", "arrange", "count",
                "if_else", "case_when", "left_join", "anti_join", "across", "n_distinct",
                "rename", "desc", "n"),
  tidyr     = c("pivot_longer", "pivot_wider", "drop_na"),
  readr     = c("read_csv", "problems"),
  readxl    = c("read_excel"),
  haven     = c("read_sav", "read_xpt"),
  ggplot2   = c("ggplot", "aes", "geom_histogram", "geom_boxplot", "ggsave", "facet_wrap"),
  forcats   = c("fct_recode", "fct_relevel", "fct_infreq"),
  lubridate = c("ymd", "dmy", "mdy"),
  stringr   = c("str_trim", "str_to_lower"),
  here      = c("here")
)

map <- data.frame(pkg = character(), topic = character(), rd = character(), raw = character())
for (p in names(topics)) {
  for (t in topics[[p]]) {
    h <- help(t, package = (p), help_type = "text")
    path <- as.character(h)
    if (length(path) != 1) stop("help not found: ", p, "::", t)
    rdname <- basename(path)
    out <- file.path(RAW, sprintf("rdocs_s52r1_%s-%s.txt", p, rdname))
    if (!file.exists(out) || !(rdname %in% map$rd[map$pkg == p])) {
      rd <- utils:::.getHelpFile(path)
      tools::Rd2txt(rd, out = out, package = p,
                    options = list(underline_titles = FALSE, width = 80))
    }
    map[nrow(map) + 1, ] <- c(p, t, rdname, basename(out))
  }
  # DESCRIPTION and LICENSE, copied byte for byte
  d <- system.file("DESCRIPTION", package = p)
  file.copy(d, file.path(RAW, sprintf("rdocs_s52r1_%s-DESCRIPTION.txt", p)), overwrite = TRUE)
  l <- system.file("LICENSE", package = p)
  if (nzchar(l)) file.copy(l, file.path(RAW, sprintf("rdocs_s52r1_%s-LICENSE.txt", p)), overwrite = TRUE)
}
write.csv(map, file.path(RAW, "rdocs_s52r1-topic-map.csv"), row.names = FALSE)

# versions, read with packageVersion(), and R's own licence statement
vers <- sapply(names(topics), function(p) as.character(packageVersion(p)))
writeLines(c(R.version.string,
             paste0(names(vers), " ", vers),
             "", system2(file.path(R.home("bin"), "R"), "--version", stdout = TRUE)),
           file.path(RAW, "rdocs_s52r1-versions.txt"))

# vignettes: installed HTML rendered to text, block by block in document order
vig <- list(dplyr = c("dplyr", "two-table"), tidyr = c("tidy-data", "pivot"),
            readr = c("readr"), forcats = c("forcats"))
library(xml2)
for (p in names(vig)) for (v in vig[[p]]) {
  vi <- vignette(v, package = p)
  html <- file.path(vi$Dir, "doc", vi$PDF)
  doc <- read_html(html)
  nodes <- xml_find_all(doc, "//body//*[self::h1 or self::h2 or self::h3 or self::h4 or self::p or self::pre or self::li[not(ancestor::li)] or self::table]")
  # drop nodes nested inside an already-taken node (p inside li, pre inside li)
  keep <- vapply(nodes, function(n) length(xml_find_all(n, "ancestor::*[self::li or self::table or self::pre]")) == 0, logical(1))
  txt <- vapply(nodes[keep], function(n) {
    nm <- xml_name(n)
    s <- xml_text(n)
    if (nm %in% c("h1", "h2", "h3", "h4")) s <- paste0(strrep("#", as.integer(substr(nm, 2, 2))), " ", trimws(s))
    if (nm == "li") s <- paste0("- ", trimws(s))
    if (nm == "table") s <- paste(vapply(xml_find_all(n, ".//tr"), function(r) paste(trimws(xml_text(xml_find_all(r, "./th|./td"))), collapse = " | "), ""), collapse = "\n")
    s
  }, "")
  writeLines(c(sprintf("[vignette %s, package %s %s, rendered from %s]", v, p, packageVersion(p), basename(html)), "", paste(txt, collapse = "\n\n")),
             file.path(RAW, sprintf("rdocs_s52r1_%s-vignette-%s.txt", p, v)))
}
cat("done\n")
