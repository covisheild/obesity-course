"""Book 0 wrapper. The tool now lives at check/compress/validate.py and takes --subject; this runs
it with --subject B0 so the commands in Book 0's handovers still work as written."""
import os
import runpy
import sys

TOOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..",
                    "check", "compress", "validate.py")
if "--subject" not in sys.argv and not any(a.startswith("--subject=") for a in sys.argv):
    sys.argv[1:1] = ["--subject", "B0"]
sys.argv[0] = os.path.normpath(TOOL)
runpy.run_path(sys.argv[0], run_name="__main__")
