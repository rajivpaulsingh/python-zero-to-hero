"""
Unzipping and Zipping Files
"""
# Create files to Compress
f = open("fileone.txt", 'w+')
f.write("ONE FILE")
f.close()

f = open("filetwo.txt", 'w+')
f.write("TWO FILE")
f.close()


"""
Zipping Files
"""
import zipfile

#  Create Zip file first , then write to it (the write step compresses the files.)
comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write("fileone.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("filetwo.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()


"""
Unzip - Extract from Zip files
"""
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")


"""
Using shutil library
"""
import shutil
dir_to_zip = "/Users/singh2rajiv/Python/python-zero-to-hero"

# Creating a zip archive
output_filename = 'example'

# Fill in the details
shutil.make_archive(output_filename, 'zip', dir_to_zip)

# Extract a zip archive
shutil.unpack_archive('example.zip', 'file_unzip', 'zip')