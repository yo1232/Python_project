import matplotlib as plt
import os

def list_files():
    try:
        files = os.listdir(path="./Python_project")
        return files
    except OSError:
        return OSError 


def main():
    files = list_files()
    #file_selector(files)

    return 0

main()