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
        if selection >= "0" and selection < "a":
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
    longest_sentence = ""
    shortest_sentence = ""
    with open(file, encoding="utf-8") as f:
        for line in f:
            n_lines += 1
            if line == '\n':
                n_paragraphs += 1
            if ('.' in line) or ('!' in line) or ('?' in line):
                n_sentences += 1
                if len(line) > len(longest_sentence):
                    longest_sentence = line
                if len(line) < len(shortest_sentence) or shortest_sentence == "":
                    shortest_sentence = line
            words.extend(line.split(' '))
            for j in line:
                n_chars_spcs += 1
                if j != ' ':
                    n_chars_no_spcs += 1
    return(n_lines, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences, longest_sentence, shortest_sentence)

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
    print(f"Number of unique words: {len(u_words)}")
    print(f"Number of sentences: {n_sentences}")
    while not back:
        answer = int(input("Press 0 to go back: "))
        if answer == 0:
            menu()
            back = True

def word_analysis(words):
    back = False
    list_words = []
    os.system("clear")
    print("\n==================================================")
    print("                Word Analysis                     ")
    print("==================================================")
    for i in words:
        if i.isalpha():
            list_words.append(i.lower())
    # Finding the most common words and their counts by using set and count methods
    # The first one is found by using max with set and count, the rest are found by sorting the set based on count in reverse order
    print(f"Most common word: {max(set(list_words), key=list_words.count)} ({list_words.count(max(set(list_words), key=list_words.count))} times)")
    print(f"2nd most common word: {sorted(set(list_words), key=list_words.count, reverse=True)[1]} ({list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[1])} times)")
    print(f"3rd most common word: {sorted(set(list_words), key=list_words.count, reverse=True)[2]} ({list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[2])} times)")
    print(f"4th most common word: {sorted(set(list_words), key=list_words.count, reverse=True)[3]} ({list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[3])} times)")
    print(f"5th most common word: {sorted(set(list_words), key=list_words.count, reverse=True)[4]} ({list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[4])} times)")
    print(f"6th most common word: {sorted(set(list_words), key=list_words.count, reverse=True)[5]} ({list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[5])} times)")
    print(f"7th most common word: {sorted(set(list_words), key=list_words.count, reverse=True)[6]} ({list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[6])} times)")
    print(f"8th most common word: {sorted(set(list_words), key=list_words.count, reverse=True)[7]} ({list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[7])} times)")
    print(f"9th most common word: {sorted(set(list_words), key=list_words.count, reverse=True)[8]} ({list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[8])} times)")
    print(f"10th most common word: {sorted(set(list_words), key=list_words.count, reverse=True)[9]} ({list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[9])} times)")
    while not back:
        answer = int(input("Press 0 to go back: "))
        if answer == 0:
            menu()
            back = True

def sentence_analysis(words, n_sentences, longest_sentence, shortest_sentence):
    back = False
    os.system("clear")
    print("\n==================================================")
    print("                Sentence Analysis                 ")
    print("==================================================")
    n_words = 0
    for i in words:
        n_words += 1
    print(f"Number of sentences: {n_sentences}")
    print(f"Average words per sentence: {n_words/n_sentences}")
    print(f"Longest sentence: {longest_sentence}, {len(longest_sentence.split())} words")
    print(f"Shortest sentence: {shortest_sentence}, {len(shortest_sentence.split())} words")
    print(f"Sentence length distribution (top 5): ")
    sentence_lengths = []
    for i in words:
        if ('.' in i) or ('!' in i) or ('?' in i):
            sentence_lengths.append(len(i))
    # Same concept as in word_analysis, finding the most common sentence lengths and their counts
    # The first one is found by using max with set and count, the rest are found by sorting the set based on count in reverse order
    print(f"{max(set(sentence_lengths), key=sentence_lengths.count)} words ({sentence_lengths.count(max(set(sentence_lengths), key=sentence_lengths.count))} times)")
    print(f"{sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[1]} words ({sentence_lengths.count(sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[1])} times)")
    print(f"{sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[2]} words ({sentence_lengths.count(sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[2])} times)")
    print(f"{sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[3]} words ({sentence_lengths.count(sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[3])} times)")
    print(f"{sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[4]} words ({sentence_lengths.count(sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[4])} times)")
    while not back:
        answer = int(input("Press 0 to go back: "))
        if answer == 0:
            menu()
            back = True

def character_analysis(words):
    back = False
    os.system("clear")
    print("\n==================================================")
    print("                Character Analysis                ")
    print("==================================================")
    punctuation = 0
    digits = 0
    letters = 0
    for i in words:
        for j in i:
            if j.isalpha():
                letters += 1
            elif j.isdigit():
                digits += 1
            elif not j.isalnum():
                punctuation += 1
    print("Character distribution: ")
    print(f"    Number of letters: {letters}")
    print(f"    Number of digits: {digits}")
    print(f"    Number of punctuation marks: {punctuation}")
    print("Most common letters (top 10): ")
    letters_list = []
    for i in words:
        for j in i:
            if j.isalpha():
                letters_list.append(j.lower())
    # Same concept as in word_analysis, finding the most common letters and their counts
    # The first one is found by using max with set and count, the rest are found by sorting the set based on count in reverse order
    print(f"    {max(set(letters_list), key=letters_list.count)} ({letters_list.count(max(set(letters_list), key=letters_list.count))} times)")
    print(f"    {sorted(set(letters_list), key=letters_list.count, reverse=True)[1]} ({letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[1])} times)")
    print(f"    {sorted(set(letters_list), key=letters_list.count, reverse=True)[2]} ({letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[2])} times)")
    print(f"    {sorted(set(letters_list), key=letters_list.count, reverse=True)[3]} ({letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[3])} times)")
    print(f"    {sorted(set(letters_list), key=letters_list.count, reverse=True)[4]} ({letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[4])} times)")
    print(f"    {sorted(set(letters_list), key=letters_list.count, reverse=True)[5]} ({letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[5])} times)")
    print(f"    {sorted(set(letters_list), key=letters_list.count, reverse=True)[6]} ({letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[6])} times)")
    print(f"    {sorted(set(letters_list), key=letters_list.count, reverse=True)[7]} ({letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[7])} times)")
    print(f"    {sorted(set(letters_list), key=letters_list.count, reverse=True)[8]} ({letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[8])} times)")
    print(f"    {sorted(set(letters_list), key=letters_list.count, reverse=True)[9]} ({letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[9])} times)") 
    while not back:
        answer = int(input("Press 0 to go back: "))
        if answer == 0:
            menu()
            back = True

def export_results(file):
    back = False
    os.system("clear")
    print("\n==================================================")
    print("                Export Results                    ")
    print("==================================================")
    print("Exporting results to results.txt...")
    with open(f"{file}_results.txt", "w") as f:
        f.write("Results of text analysis\n")
        f.write("========================\n")
        f.write(f"Number of lines: {n_lines}\n")
        f.write(f"Number of paragraphs: {n_paragraphs}\n")
        f.write(f"Number of words: {n_words}\n")
        f.write(f"Number of characters (with spaces): {n_chars_spcs}\n")
        f.write(f"Number of characters (without spaces): {n_chars_no_spcs}\n")
        f.write(f"Average number of words per line: {n_words/n_lines}\n")
        f.write(f"Average characters per word: {n_chars_no_spcs/n_words}\n")
        f.write(f"Number of unique words: {len(u_words)}\n")
        f.write(f"Number of sentences: {n_sentences}\n")
        f.write(f"Average words per sentence: {n_words/n_sentences}\n")
        f.write(f"Longest sentence: {longest_sentence}, {len(longest_sentence.split())} words\n")
        f.write(f"Shortest sentence: {shortest_sentence}, {len(shortest_sentence.split())} words\n")
    print(f"Results exported to {file}_results.txt successfully!")
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
                n_lines, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences, longest_sentence, shortest_sentence = open_basic_stats(file)
            case 2:
                basic_stats(n_lines, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences)
            case 3:
                word_analysis(words)
            case 4:
                sentence_analysis(words, n_sentences, longest_sentence, shortest_sentence)
            case 5:
                character_analysis(words)
            case 6:
                export_results(file)
            case 7:
                return 0
            case _:
                print("Choose one of the options above please :(")


main()