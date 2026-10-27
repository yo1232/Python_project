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

def open_basic_stats(file):
    print(f"Opening file {file}, please wait...")
    n_lines = 0
    n_words = 0
    n_chars_spcs = 0
    n_chars_no_spcs = 0
    u_words = []
    b_words = []
    words = []
    n_paragraphs = 0
    n_sentences = 0
    with open(file, encoding="utf-8") as f:
        for line in f:
            n_lines += 1
            if line == '\n':
                n_paragraphs += 1
            if ('.' in line) or ('!' in line) or ('?' in line):
                n_sentences += 1
            words.extend(line.split(' '))
            for j in line:
                n_chars_spcs += 1
                if j != ' ':
                    n_chars_no_spcs += 1
    return(n_lines, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences)

def basic_stats(n_lines, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences):
    back = False
    n_words = 0
    b_words = []
    u_words = []
    for j in words:
        n_words += 1
        if j.lower() in u_words and j.isalpha():
            u_words.remove(j.lower())
            b_words.append(j.lower())
        if j.lower() not in u_words and j.isalpha() and j.lower() not in b_words:
            u_words.append(j.lower())
    os.system("clear")
    print("\n==================================================")
    print("                 Basic Statistics                 ")
    print("==================================================")
    print(f"Number of lines: {n_lines}")
    print(f"Number of paragraphs: {n_paragraphs}")
    print(f"Number of words: {n_words}")
    print(f"Number of characters (with spaces): {n_chars_spcs}")
    print(f"Number of characters (without spaces): {n_chars_no_spcs}")
    print(f"Average number of words per line: {n_words/n_lines}")
    print(f"Average characters per word: {n_chars_no_spcs/n_words}")
    print(f"Average words per sentence: {n_words/n_sentences}")
    print(f"Number of unique words: {len(u_words)}")
    print(f"Number of sentences: {n_sentences}")
    while not back:
        answer = int(input("Press 0 to go back: "))
        if answer == 0:
            menu()
            back = True

def word_analysis(words):
    back = False
    t_1 = 0
    w_1 = ''
    t_2 = 0
    w_2 = ''
    t_3 = 0
    w_3 = ''
    t_4 = 0
    w_4 = ''
    t_5 = 0
    w_5 = ''
    t_6 = 0
    w_6 = ''
    t_7 = 0
    w_7 = ''
    t_8 = 0
    w_8 = ''
    t_9 = 0
    w_9 = ''
    t_10 = 0
    w_10 = ''
    os.system("clear")
    print("\n==================================================")
    print("                Word Analysis                     ")
    print("==================================================")
    for i in words:
        if i.isalpha():
            if words.count(i) > t_1:
                t_10 = t_9
                w_10 = w_9
                t_9 = t_8
                w_9 = w_8
                t_8 = t_7
                w_8 = w_7
                t_7 = t_6
                w_7 = w_6
                t_6 = t_5
                w_6 = w_5
                t_5 = t_4
                w_5 = w_4
                t_4 = t_3
                w_4 = w_3
                t_3 = t_2
                w_3 = w_2
                t_2 = t_1
                w_2 = w_1
                t_1 = words.count(i)
                w_1 = i.lower()
    print(f"Most common word: {w_1} ({t_1} times)")
    print(f"2nd most common word: {w_2} ({t_2} times)")
    print(f"3rd most common word: {w_3} ({t_3} times)")
    print(f"4th most common word: {w_4} ({t_4} times)")
    print(f"5th most common word: {w_5} ({t_5} times)")
    print(f"6th most common word: {w_6} ({t_6} times)")
    print(f"7th most common word: {w_7} ({t_7} times)")
    print(f"8th most common word: {w_8} ({t_8} times)")
    print(f"9th most common word: {w_9} ({t_9} times)")
    print(f"10th most common word: {w_10} ({t_10} times)")
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
                n_lines, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences = open_basic_stats(file)
            case 2:
                basic_stats(n_lines, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences)
            case 3:
                word_analysis(words)
            case 7:
                return 0
            case _:
                print("Choose one of the options above please :(")


main()