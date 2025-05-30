import os
import shutil

# Importing my own files
from copystatic import copy_files_recursive

# Directory paths
dir_path_static = "./static"
dir_path_public = "./public"

# Functions
def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


# Program starts here
if __name__ == "__main__":
    main()