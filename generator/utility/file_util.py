import os
import shutil

def clear_and_create_output_dir(dir_name="./output"):
    # Start by clearing out the output directory if it exists
    try:
        shutil.rmtree(dir_name, ignore_errors=True)
    except:
        print("Output directory was not present.")

    os.mkdir(dir_name)
