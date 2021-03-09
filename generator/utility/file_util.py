import os

def clear_and_create_output_dir(dir_name="./output"):
    # Start by clearing out the output directory if it exists
    try:
        os.rmdir(dir_name)
    except:
        print("Output directory was not present.")

    os.mkdir(dir_name)
