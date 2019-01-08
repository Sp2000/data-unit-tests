import os


exclude = ["../coldp/", "../scripts/", "../template/", "0"]
directories = os.system("ls -d ../*/")
print(directories)

for dir in directories:
    print(str(dir))
