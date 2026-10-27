import matplotlib as plt
import os

def list_files():
    try:
        files = os.listdir(path=".")
        print(files)
        file = file_selector(files)
        return file
    except OSError:
        return OSError 

def file_selector(files):
    os.system("clear")
    print("--- File Selector ---")
    print("Available text files: ")
    for i in range(len(files)):
        print(f"{i}: {files[i]}")
    selection = input("Enter file name or number from list above: ")
    for i in files:
        if selection == i:
            return files[files.index(i)]
        if selection > "0" and selection < "a":
            if int(selection) <= len(files):
                return files[int(selection)]
    if i != selection:
        agree = False
        while not agree:
            print("Invalid selection :(")
            agree = input("Write 'True' to continue: ")
    return 0

def open_file(file):
    n_lines = 0
    n_words = 0
    n_chars_spcs = 0
    n_chars_no_spcs = 0
    with open(file, encoding="utf-8") as f:
        for line in f:
            n_lines += 1
            words = line.split(' ')
            for j in words:
                n_words += 1
            for j in line:
                n_chars_spcs += 1
                if j != ' ':
                    n_chars_no_spcs += 1
    return(n_lines, n_words, n_chars_spcs, n_chars_no_spcs)
            
def basic_stats(n_lines, n_words, n_chars_spcs, n_chars_no_spcs):
    back = False
    os.system("clear")
    print("\n==================================================")
    print("                 Basic Statistics                 ")
    print("==================================================")
    print(f"Number of lines: {n_lines}")
    print(f"Number of words: {n_words}")
    print(f"Number of characters (with spaces): {n_chars_spcs}")
    print(f"Number of characters (without spaces): {n_chars_no_spcs}")
    print(f"Average number of words per line: {n_words/n_lines}")
    print(f"Average characters per word: {n_chars_no_spcs/n_words}")
    while not back:
        answer = int(input("Press 0 to go back: "))
        if answer == 0:
            menu()
            back = True


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
            case 2:
                n_lines, n_words, n_chars_spcs, n_chars_no_spcs = open_file(file)
                basic_stats(n_lines, n_words, n_chars_spcs, n_chars_no_spcs)
            case 7:
                return 0
            case _:
                print("Choose one of the options above please :(")


main()