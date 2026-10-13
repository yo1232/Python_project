import matplotlib as plt
import os

def list_files():
    try:
        files = os.listdir(path="./Python_project")
        print(files)
        file = file_selector(files)
        return file
    except OSError:
        return OSError 

def file_selector(files):
    os.system("clear")
    print("--- File Selector ---")
    print("Available text files: ")
    print(files)
    selection = input("Enter file name or number from list above: ")
    for i in files:
        if selection == i:
            return selection
    if i != selection:
        agree = False
        while not agree:
            print("Invalid selection :(")
            agree = input("Write 'True' to continue: ")
    return 0

def menu():
    os.system("clear")
    print("\n==================================================")
    print("                 TEXT ANALYSER                    ")
    print("==================================================")
    print("1. Load text file")
    print("2. Display basic statistics")
    print("3. Word frequency analysis")
    print("4. Sentence analysis")
    print("5. Character analysis")
    print("6. Export results")
    print("7. Exit")
    print("==================================================")

def main():
    file = 0
    menu()
    while True:
        if file == 0:
            print("No file loaded")
        else:
            print(f"Current file {file}")
        option = int(input("Select an option: "))
        match option:
            case 1:
                file = list_files()
                menu()
            case _:
                print("Choose one of the options above please :(")

    return 0

main()