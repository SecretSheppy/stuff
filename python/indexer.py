# !/usr/bin/env python3

# Sorts files in a directory into folders aphabetically
# Run as:
# Windows -> indexer.py c:/...
# Linux -> python3 indexer.py ~/...
# Author: SecretSheppy

import os
from os import listdir
from os.path import join, isfile
import sys
import shutil

def main():

    path = sys.argv[1]

    files = [f for f in listdir(path) if isfile(join(path, f))]

    for file in files:
        try:
            shutil.move(path + "/" + file, path + "/" + file[0] + "/" + file)
        except OSError:
            os.mkdir(path + "/" + file[0].lower())
            shutil.move(path + "/" + file, path + "/" + file[0] + "/" + file)

    print("files moved")

if __name__ == "__main__":
    main()
