# S52-R1 intake group d: counts, in the .xpt files read with haven 2.5.4, every row of the printed
# NHANES codebook tables (parsed by parse_codebook.py) and prints printed vs computed. Run from the
# repository root:
#   Rscript books/S52-R1/intake/build-d/compare.R > books/S52-R1/intake/raw/nchs_nhanes_2021_2023_bmx_demo-printed-vs-computed.txt
# Rule: a code ("1", "77") counts values equal to it; a range ("2.7 to 248.2") counts non-missing
# values between its ends inclusive, excluding any value that has its own printed code row for the
# same variable (e.g. WTMEC2YR 0, INDFMPIR 5); "." counts NA. Cumulative is recomputed as the
# running sum of the computed counts.
suppressPackageStartupMessages(library(haven))
p <- read.delim("books/S52-R1/intake/build-d/codebook-printed.tsv", colClasses = "character")
d <- list(BMX_L = read_xpt("sources/data/BMX_L.xpt"), DEMO_L = read_xpt("sources/data/DEMO_L.xpt"))
p$computed <- NA_integer_
p$computed_cum <- NA_integer_
for (k in unique(paste(p$dataset, p$variable))) {
  idx <- which(paste(p$dataset, p$variable) == k)
  ds <- p$dataset[idx[1]]; v <- p$variable[idx[1]]
  y <- d[[ds]][[v]]
  codes <- p$code_or_value[idx]
  single <- suppressWarnings(as.numeric(codes[!grepl(" to ", codes) & codes != "." & codes != ""]))
  run <- 0L
  for (i in idx) {
    cv <- p$code_or_value[i]
    if (cv == "") next
    if (cv == ".") n <- sum(is.na(y))
    else if (grepl(" to ", cv)) {
      lim <- as.numeric(strsplit(cv, " to ")[[1]])
      n <- sum(!is.na(y) & y >= lim[1] & y <= lim[2] & !(y %in% single))
    } else n <- sum(!is.na(y) & y == as.numeric(cv))
    run <- run + n
    p$computed[i] <- n; p$computed_cum[i] <- run
  }
}
ok <- !is.na(p$computed) & p$computed == as.integer(p$count) & p$computed_cum == as.integer(p$cumulative)
p$agree <- ifelse(is.na(p$computed), "-", ifelse(ok, "yes", "NO"))
options(width = 250)
cat("haven", as.character(packageVersion("haven")), "\n")
print(p[, c("dataset", "variable", "code_or_value", "description", "count", "computed", "cumulative",
            "computed_cum", "agree")], row.names = FALSE, right = FALSE)
cat("\nrows compared:", sum(p$agree != "-"), " agree:", sum(p$agree == "yes"), " disagree:", sum(p$agree == "NO"), "\n")
cat("variables with no printed code table:", paste(p$dataset[p$agree == "-"], p$variable[p$agree == "-"]), "\n")
