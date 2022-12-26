#Create Zip
import zipfile # imports the zipfile module so you can make use of it
## Instantiate a new zipfile object creating the single_zip.zip archive.
zf = zipfile.ZipFile('single_file.zip', mode='w')

## Add a file to the archive
zf.write('all_black.bmp')

## Close the archive releasing it from memory
zf.close()

#Compress Archive
import zipfile

## Instantiate a new zipfile object creating the single_zip.zip archive and compressing it
zf = zipfile.ZipFile('single_file.zip', mode='w', compression=zipfile.ZIP_DEFLATED)

## Add a file to the archive
zf.write('all_black.bmp')

## Close the archive releasing it from memory
zf.close()

#Applying Filters
# imports the zipfile module so you can make use of it
import zipfile

# for manipulating directories
import os

# for deleting any prefix up to the last slash character of a pathname file from a given directory that matches the filter
from os.path import basename

# zip the files from given directory that matches the filter
def filter_and_zip_files (destination_file, source_foulder, filter):
   with zipfile.ZipFile(destination_file, mode="w", compression=zipfile.ZIP_DEFLATED) as new_zip:
       # Iterate over all the files in the folder
       test = os.walk(source_foulder)
       for folder, subfolders, filenames in os.walk(source_foulder):
           for filename in filenames:
               if filter(filename):
                   # create complete filepath of file in directory
                   file_path = os.path.join(folder, filename)
                   # Add file to zip
                   new_zip.write(file_path, basename(file_path))

# zipping only colors that start with b to only_b_colors by using_filters
filter_and_zip_files("only_b_colors.zip", ".", lambda name : name.startswith("all_b"))
list_zip_file_contents("only_b_colors.zip")

