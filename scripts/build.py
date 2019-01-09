import os

# exclude these directories from being zipped
exclude = [".git", "template", ".idea", "scripts"]

path = "/data/col/data-unit-tests"
os.chdir(path)

for subdir, directories, files in os.walk(path):

    for dir in directories:

        if dir not in exclude:

            os.chdir(dir)

            # convert ods to tsv
            os.system("ods2tsv Template.ods")
            os.system("mv Template.d/* .")
            os.system("rmdir Template.d")

            # purge the zip archive of tsv files
            os.system("zip -d ../" + dir + ".zip *.tsv")

            # add tsv files to zip archive
            os.system("zip ../" + dir + ".zip *.tsv")

            os.chdir(path)

    break # stops os.walk from recursing through subdirectories