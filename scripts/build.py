#!/usr/bin/env python3
import os
import subprocess
import time

# exclude these directories from being zipped
exclude = [".git", "template", ".idea", "scripts", "flat_template","tmp","acef_template"]

path = "/data/col/data-unit-tests"
os.chdir(path)

for subdir, directories, files in os.walk(path):

    for dir in directories:

        if dir not in exclude:

            os.chdir(dir)

            # convert ods to tsv
            p = subprocess.Popen(['soffice','macro:///Standard.Module1.ExportAllToCsv','Template.ods'])
            time.sleep(5) # TODO: find a better way to export ODS
            p.kill()
            os.system("mv /data/col/data-unit-tests/tmp/* .")

            # purge the zip archive of tsv files
            os.system("zip -d ../" + dir + ".zip *.tsv")

            # add tsv files to zip archive
            os.system("zip ../" + dir + ".zip *.tsv")

            os.chdir(path)

    break # stops os.walk from recursing through subdirectories
