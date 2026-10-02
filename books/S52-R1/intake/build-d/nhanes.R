# S52-R1 intake group d: records the facts of the two NHANES 2021-2023 files Harsh supplied
# (BMX_L.xpt, DEMO_L.xpt) as held in sources/data/, read with haven::read_xpt().
# Run from the repository root:
#   Rscript books/S52-R1/intake/build-d/nhanes.R > books/S52-R1/intake/raw/nchs_nhanes_2021_2023_bmx_demo-facts.txt
# The first block of output is quoted whole in the source file's header; the second block
# ("FREQUENCIES IN THE CODEBOOK'S FORM") is what build.py compares with the printed codebook counts.
suppressPackageStartupMessages(library(haven))
options(width = 200)

files <- c(BMX_L = "sources/data/BMX_L.xpt", DEMO_L = "sources/data/DEMO_L.xpt")
cat("R version:", R.version.string, "\n")
cat("haven version (packageVersion):", as.character(packageVersion("haven")), "\n")
d <- list()
for (nm in names(files)) {
  f <- files[[nm]]
  x <- read_xpt(f)
  d[[nm]] <- x
  cat("\n== ", nm, "\n", sep = "")
  cat("file:", f, "\n")
  cat("bytes:", file.size(f), "\n")
  cat("md5:", unname(tools::md5sum(f)), "\n")
  cat("rows:", nrow(x), "\n")
  cat("columns:", ncol(x), "\n")
  cat("variables (name: label as read by read_xpt; class):\n")
  for (v in names(x)) {
    lab <- attr(x[[v]], "label")
    cat("  ", v, ": ", if (is.null(lab)) "(no label)" else lab, "; ", class(x[[v]])[1], "\n", sep = "")
  }
}

b <- d$BMX_L; m <- d$DEMO_L
cat("\n== BMX_L: missing values (sum(is.na())) for four measures\n")
for (v in c("BMXWT", "BMXHT", "BMXBMI", "BMXWAIST")) cat("  ", v, ": ", sum(is.na(b[[v]])), "\n", sep = "")

cat("\n== DEMO_L: counts\n")
cat("  RIDSTATR (table, NA included):\n")
print(table(m$RIDSTATR, useNA = "always"))
cat("  RIAGENDR (table, NA included):\n")
print(table(m$RIAGENDR, useNA = "always"))
cat("  RIDAGEYR range (min, max):", range(m$RIDAGEYR, na.rm = TRUE), "\n")
cat("  RIDAGEYR missing:", sum(is.na(m$RIDAGEYR)), "\n")
cat("  RIDAGEYR == 80 (top code):", sum(m$RIDAGEYR == 80, na.rm = TRUE), "\n")

cat("\n== Join BMX_L to DEMO_L on SEQN (dplyr-free: merge, all.x = TRUE)\n")
cat("  SEQN unique in BMX_L:", !anyDuplicated(b$SEQN), "; SEQN unique in DEMO_L:", !anyDuplicated(m$SEQN), "\n")
cat("  BMX_L SEQNs found in DEMO_L:", sum(b$SEQN %in% m$SEQN), "of", nrow(b), "\n")
j <- merge(b, m, by = "SEQN", all.x = TRUE)
cat("  rows after join:", nrow(j), "\n")
cat("  RIDSTATR among joined BMX rows (table):\n")
print(table(j$RIDSTATR, useNA = "always"))
cat("  BMX rows with RIDAGEYR >= 20:", sum(j$RIDAGEYR >= 20, na.rm = TRUE), "\n")
a <- j[!is.na(j$RIDAGEYR) & j$RIDAGEYR >= 20, ]
cat("  of these, missing BMXWT / BMXHT / BMXBMI / BMXWAIST:",
    sum(is.na(a$BMXWT)), "/", sum(is.na(a$BMXHT)), "/", sum(is.na(a$BMXBMI)), "/", sum(is.na(a$BMXWAIST)), "\n")
cat("  of these, RIDEXPRG == 1 (pregnant at exam):", sum(a$RIDEXPRG == 1, na.rm = TRUE), "\n")

# ---------------------------------------------------------------------------------------------
cat("\n== FREQUENCIES IN THE CODEBOOK'S FORM (every variable; for comparison with the printed tables)\n")
cat("   numeric variables with many values: non-missing count with min and max, then missing count\n")
cat("   coded variables (<= 12 distinct values): count per value, then missing count\n")
for (nm in names(d)) {
  x <- d[[nm]]
  for (v in names(x)) {
    if (v == "SEQN") next
    y <- x[[v]]
    u <- sort(unique(y[!is.na(y)]))
    if (length(u) <= 12) {
      tab <- table(y)
      s <- paste(paste0(names(tab), "=", as.integer(tab)), collapse = " ")
      cat(nm, " ", v, ": ", s, " NA=", sum(is.na(y)), "\n", sep = "")
    } else {
      cat(nm, " ", v, ": range ", format(min(y, na.rm = TRUE), digits = 12), " to ",
          format(max(y, na.rm = TRUE), digits = 12), " n=", sum(!is.na(y)), " NA=", sum(is.na(y)), "\n", sep = "")
    }
  }
}
cat("   split ranges where the codebook prints a separate code inside a range:\n")
w <- m$WTMEC2YR
cat("DEMO_L WTMEC2YR: >0 range ", format(min(w[w > 0]), digits = 12), " to ", format(max(w[w > 0]), digits = 12),
    " n=", sum(w > 0, na.rm = TRUE), " ==0 n=", sum(w == 0, na.rm = TRUE), " NA=", sum(is.na(w)), "\n", sep = "")
p <- m$INDFMPIR
cat("DEMO_L INDFMPIR: <5 range ", min(p[p < 5], na.rm = TRUE), " to ", max(p[p < 5], na.rm = TRUE),
    " n=", sum(p < 5, na.rm = TRUE), " ==5 n=", sum(p == 5, na.rm = TRUE), " NA=", sum(is.na(p)), "\n", sep = "")
a <- m$RIDAGEYR
cat("DEMO_L RIDAGEYR: 0-79 n=", sum(a <= 79, na.rm = TRUE), " ==80 n=", sum(a == 80, na.rm = TRUE), "\n", sep = "")
h <- m$DMDHHSIZ
cat("DEMO_L DMDHHSIZ: 1-6 n=", sum(h <= 6, na.rm = TRUE), " ==7 n=", sum(h == 7, na.rm = TRUE), "\n", sep = "")
