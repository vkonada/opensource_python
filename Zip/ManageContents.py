import zipfile

## Open the zip file for reading
zip_read = zipfile.ZipFile('single_file.zip', mode='r')

## Inspect the contents of single_file.zip
zip_read.namelist()

## Close the archive releasing it from memory
zip_read.close()

#########
import zipfile

## Open the zip file for reading
zip_read = zipfile.ZipFile('single_file.zip', mode='r')

## Inspect the contents of single_file.zip
files = zip_read.namelist()

for file_name in files:
    # prints the name of files within, with a tab for better readability
    print("\t", file_name)

## Close the archive releasing it from memory
zip_read.close()

##Adding files to existing Zip

import zipfile

## Open the zip file for appending
zip_file = zipfile.ZipFile('single_file.zip', mode='a')

## Optionally see the files in the zip before the addition
zip_read.namelist()

## Add the file to the zip
zip_file.write('all_blue.bmp')

## Optionally see the files in the zip before after the addition
zip_read.namelist()

## Close the archive releasing it from memory
zip_read.close()


#Extracting contents of Zip
import zipfile

## Open the zip file for reading
zip_file = zipfile.ZipFile('single_file.zip', mode='r')

## Extract a single file from the zip file to your home directory
zip_file.extract('all_blue.bmp', path='~')

## Extract all files from the zip file to your home directory
zip_file.extractall('path='~')

## Close the archive releasing it from memory
zip_read.close()

#Applying Filters when Unzipping file

import zipfile

# unzip only files withtin the zip file that match the filter 
def unzip_filtered_files (source_file, destination_folder, filter):
		with zipfile.ZipFile(source_file, "r") as source:
		   list_of_file_names = source.namelist() # you'll get an iterable object
		   for file_name in list_of_file_names:
		       # checks if the file matches the filter 
		       if  filter(file_name):
		           # Extract the files to destination_folder
		           source.extract(file_name,path=destination_folder)

unzip_filtered_files("multiple_files.zip", "not_b_colors", lambda name : not name.startswith("all_b"))
