import sys
import os
from PIL import Image

# Give the path you want to grab the images, and directory you want to save it.
# As folder_name/
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check is /output_folder exists, if not create it.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through the folder I given, convert images into png, save them to new folder.
for filename in os.listdir(image_folder): # List all file or directory in the folder.
    if filename.endswith('.jpg'): # We only want the file with .jpg
        img = Image.open(f'{image_folder}{filename}') # Open the file to get an Img object {this is the file path}
        img.save(f'{output_folder}{filename.split(".")[0]}.png', 'png')
        # 1st {} means the path I want to save the file because the string contain \.
        # 2st {} means I keep the first part of file's name to rename it with .png, and I split it with "."
    else:
        print('Something went wrong!')
print('Enjoy your png files!')