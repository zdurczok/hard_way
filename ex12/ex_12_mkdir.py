import os, sys

# implementation of bash mkdir command without any options
# informing user that folders already exist needs to be implemented

path = input("Please provide the path where a new folder/folders are to be created: ")

folders = list(input("Please provide a name/names of a folder/folders to be created: ").split())


for folder in folders:
    if os.path.isdir(os.path.join(path, folder)) == False:
        os.mkdir(os.path.join(path, folder))
