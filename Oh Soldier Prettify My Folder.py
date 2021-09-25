# Oh Soldier Prettify My Folder
import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i += 1

# Here txt file is that file in which file name is written so that those file name doesn't change.
soldier(r"C:\Users\REX TERIA\Desktop\pic", r"C:\Users\REX TERIA\Desktop\pic\that.txt", ".png")




