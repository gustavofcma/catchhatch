import glob
import os
import shlex
import sys
import subprocess
import pandas as pd


def check_tesseract():
    """Returns true if tesseract is found, else False"""
    try:
        subprocess.run("which tesseract", shell=True)
    except Exception:
        return False
    return True


def sanity_check(dirname):
    """Check if tesseract is available, check if input directory is available
    """
    if not check_tesseract():
        print("tesseract is not available, exiting")
        sys.exit(1)

    if not os.path.isdir(dirname):
        print("Directory {} does not exist".format(dirname))
        sys.exit(2)


def main(dirname):
    sanity_check(dirname)
    img_files = glob.glob(os.path.join(dirname, "*.png"))
    output = []
    for fname in img_files:
        proc = subprocess.run(shlex.split("tesseract {} stdout".format(fname)), stdout=subprocess.PIPE)
        output.append(proc.stdout)


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: ")
    main(sys.argv[1])