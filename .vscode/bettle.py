import os

current_dir = os.getcwd()

print(current_dir)

folder = os.listdir(current_dir)

def check_file_cwd(name):
    files = []
    get_files