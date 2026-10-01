# S52-R1 intake group c: copy palmerpenguins penguins_raw.csv byte for byte and describe it by script.
# Run (UTF-8 locale): LANG=C.UTF-8 LC_ALL=C.UTF-8 Rscript /home/claude/work/obesity-course/books/S52-R1/intake/build-c/penguins.R
src <- system.file("extdata", "penguins_raw.csv", package = "palmerpenguins")
dst <- "/home/claude/work/obesity-course/sources/data/penguins_raw.csv"
RAW <- "/home/claude/work/obesity-course/books/S52-R1/intake/raw"
stopifnot(file.copy(src, dst, overwrite = TRUE, copy.date = TRUE))
m1 <- unname(tools::md5sum(src)); m2 <- unname(tools::md5sum(dst))
stopifnot(identical(m1, m2))
file.copy(system.file("DESCRIPTION", package = "palmerpenguins"),
          file.path(RAW, "horst_2020_palmerpenguins-DESCRIPTION.txt"), overwrite = TRUE)
suppressPackageStartupMessages(library(readr))
d <- read_csv(dst, show_col_types = FALSE)
spec_txt <- capture.output(print(spec(d)))
na <- vapply(d, function(x) sum(is.na(x)), integer(1))
lines_raw <- readLines(dst, warn = FALSE)
out <- c(
  paste0("source: ", src),
  paste0("copied to: sources/data/penguins_raw.csv"),
  paste0("palmerpenguins version (packageVersion): ", packageVersion("palmerpenguins")),
  paste0("readr version used to read it: ", packageVersion("readr")),
  paste0("bytes: ", file.size(dst)),
  paste0("md5 (installed file): ", m1),
  paste0("md5 (copy): ", m2),
  paste0("text lines in file (readLines, including header): ", length(lines_raw)),
  paste0("header line: ", lines_raw[1]),
  paste0("rows (read_csv): ", nrow(d)),
  paste0("columns (read_csv): ", ncol(d)),
  "column types as guessed by read_csv (spec):",
  spec_txt,
  "missing values per column (sum(is.na()) after read_csv with default na = c(\"\", \"NA\")):",
  paste0("  ", names(na), ": ", na),
  paste0("total missing cells: ", sum(na)),
  paste0("complete rows (all 17 columns present): ", sum(complete.cases(d))),
  paste0("rows with Comments missing: ", sum(is.na(d$Comments))),
  paste0("range of Date Egg: ", paste(format(range(d$`Date Egg`, na.rm = TRUE)), collapse = " to ")),
  paste0("Species counts: ", paste(names(table(d$Species)), table(d$Species), sep = " = ", collapse = "; ")),
  paste0("Sex counts (NA excluded): ", paste(names(table(d$Sex)), table(d$Sex), sep = " = ", collapse = "; "))
)
writeLines(out, file.path(RAW, "horst_2020_palmerpenguins-facts.txt"))
cat(out, sep = "\n")
# dataset help page and the package's own citation
options(useFancyQuotes = FALSE)
h <- as.character(help("penguins_raw", package = "palmerpenguins"))
tools::Rd2txt(utils:::.getHelpFile(h), out = file.path(RAW, "horst_2020_palmerpenguins-help-penguins_raw.txt"),
              package = "palmerpenguins", options = list(underline_titles = FALSE, width = 80))
writeLines(c(capture.output(print(citation("palmerpenguins"), style = "text")), "",
             capture.output(print(citation("palmerpenguins"), style = "bibtex"))),
           file.path(RAW, "horst_2020_palmerpenguins-citation.txt"))
