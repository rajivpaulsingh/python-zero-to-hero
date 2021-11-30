# Working with files and folders

# Initial way in jupyter notebook to see present working directory
"""
REVIEW
"""
# print(pwd)

# Working with files in jupyter notebook
"""
CREATE FILE
"""
f = open('practice.txt', 'w+')
f.write('This is a test string')
f.close()

"""
os mudule
GETTING DIRECTORIES
"""
import os

print(os.getcwd()) # To see the current working directory

"""
LISTING FILES IN A DIRECTORY
"""
print(os.listdir()) # To see the directory list

print(os.listdir('/Users')) # To see the directory list in a particular directory

"""
shutil module
MOVING FILES
"""
import shutil

shutil.move('practice.txt', 'to-location') # Move a file or directory to another location

"""
DELETING FILES
"""
import send2trash
os.listdir()

send2trash.send2trash('practice.txt')


"""
WALKING THROUGH A DIRECTORY
os.walk
"""
for folder , sub_folders , files in os.walk("Example_Top_Level"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')