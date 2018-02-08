# find duplicates
import os
import hashlib

files = [file for file in os.listdir() if file.endswith(".png")]

old_file = None
old_file_checksum = None

for file in files:
    checksum = hashlib.md5(open(file,'rb').read()).hexdigest()
    if checksum == old_file_checksum:
        print(old_file, file)
        os.rename(old_file, "XXX {}".format(old_file))

    old_file = file
    old_file_checksum = checksum
