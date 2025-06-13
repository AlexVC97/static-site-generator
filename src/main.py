import os
import shutil
import sys

# Importing my own files
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

# Directory paths
dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

# Functions
def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        
    print("Deleting doc directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying static files to doc directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


# Program starts here
if __name__ == "__main__":
    main()