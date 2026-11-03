import matplotlib.pyplot as plt
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
    return(n_lines, n_words, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences, longest_sentence, shortest_sentence)

def basic_stats(letters, digits, punctuation, n_lines, n_words, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences, longest_sentence, shortest_sentence):
    back = False
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
    print("\nPress 0 to go back")
    print("Press 1 to open the text composition graph")
    print("Press 2 to open the character type distribution graph")
    while not back:
        answer = int(input("Select one of the options above: "))
        if answer == 0:
            menu()
            back = True
        if answer == 1:
            matplotlib_text_composition(n_lines, u_words, n_paragraphs, n_sentences)
        if answer == 2:
            matplotlib_character_distribution(letters, digits, punctuation)
        else:
            print("Invalid selection :(")

def word_analysis(words):
    list_words = []
    for i in words:
        if i.isalpha():
            list_words.append(i.lower())
    # Finding the most common words and their counts by using set and count methods
    # The first one is found by using max with set and count, the rest are found by sorting the set based on count in reverse order
    w_1 = max(set(list_words), key=list_words.count)
    w_l_1 = list_words.count(max(set(list_words), key=list_words.count))
    w_2 = sorted(set(list_words), key=list_words.count, reverse=True)[1]
    w_l_2 = list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[1])
    w_3 = sorted(set(list_words), key=list_words.count, reverse=True)[2]
    w_l_3 = list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[2])
    w_4 = sorted(set(list_words), key=list_words.count, reverse=True)[3]
    w_l_4 = list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[3])
    w_5 = sorted(set(list_words), key=list_words.count, reverse=True)[4]
    w_l_5 = list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[4])
    w_6 = sorted(set(list_words), key=list_words.count, reverse=True)[5]
    w_l_6 = list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[5])
    w_7 = sorted(set(list_words), key=list_words.count, reverse=True)[6]
    w_l_7 = list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[6])
    w_8 = sorted(set(list_words), key=list_words.count, reverse=True)[7]
    w_l_8 = list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[7])
    w_9 = sorted(set(list_words), key=list_words.count, reverse=True)[8]
    w_l_9 = list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[8])
    w_10 = sorted(set(list_words), key=list_words.count, reverse=True)[9]
    w_l_10 = list_words.count(sorted(set(list_words), key=list_words.count, reverse=True)[9])
    return (w_1, w_l_1, w_2, w_l_2, w_3, w_l_3, w_4, w_l_4, w_5, w_l_5, w_6, w_l_6, w_7, w_l_7, w_8, w_l_8, w_9, w_l_9, w_10, w_l_10)

def word_analysis_menu(w_1, w_l_1, w_2, w_l_2, w_3, w_l_3, w_4, w_l_4, w_5, w_l_5, w_6, w_l_6, w_7, w_l_7, w_8, w_l_8, w_9, w_l_9, w_10, w_l_10, words):
    back = False
    os.system("clear")
    print("\n==================================================")
    print("                Word Analysis                     ")
    print("==================================================")
    print("Most common words (top 10): ")
    print(f"    {w_1} ({w_l_1} times)")
    print(f"    {w_2} ({w_l_2} times)")
    print(f"    {w_3} ({w_l_3} times)")
    print(f"    {w_4} ({w_l_4} times)")
    print(f"    {w_5} ({w_l_5} times)")
    print(f"    {w_6} ({w_l_6} times)")
    print(f"    {w_7} ({w_l_7} times)")
    print(f"    {w_8} ({w_l_8} times)")
    print(f"    {w_9} ({w_l_9} times)")
    print(f"    {w_10} ({w_l_10} times)")
    print("\nPress 0 to go back")
    print("Press 1 to open the top 10 most common words graph")
    print("Press 2 to open the word length distribution graph")
    while not back:
        answer = int(input("Press one of the options above: "))
        if answer == 0:
            menu()
            back = True
        if answer == 1:
            matplotlib_top10_words(w_1, w_l_1, w_2, w_l_2, w_3, w_l_3, w_4, w_l_4, w_5, w_l_5, w_6, w_l_6, w_7, w_l_7, w_8, w_l_8, w_9, w_l_9, w_10, w_l_10)
        if answer == 2:
            matplotlib_word_length_distribution(words)
        else:
            print("Invalid selection :(")

def sentence_analysis(words, n_sentences, longest_sentence, shortest_sentence):
    n_words = 0
    for i in words:
        n_words += 1
    sentence_lengths = []
    for i in words:
        if ('.' in i) or ('!' in i) or ('?' in i):
            sentence_lengths.append(len(i))
    # Same concept as in word_analysis, finding the most common sentence lengths and their counts
    # The first one is found by using max with set and count, the rest are found by sorting the set based on count in reverse order
    s_t_1 = max(set(sentence_lengths), key=sentence_lengths.count)
    s_l_1 = sentence_lengths.count(max(set(sentence_lengths), key=sentence_lengths.count))
    s_t_2 = sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[1]
    s_l_2 = sentence_lengths.count(sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[1])
    s_t_3 = sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[2]
    s_l_3 = sentence_lengths.count(sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[2])
    s_t_4 = sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[3]
    s_l_4 = sentence_lengths.count(sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[3])
    s_t_5 = sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[4]
    s_l_5 = sentence_lengths.count(sorted(set(sentence_lengths), key=sentence_lengths.count, reverse=True)[4])
    return (sentence_lengths, n_sentences, n_words, longest_sentence, shortest_sentence, s_t_1, s_l_1, s_t_2, s_l_2, s_t_3, s_l_3, s_t_4, s_l_4, s_t_5, s_l_5)

def sentence_analysis_menu(sentence_lengths, n_words, n_sentences, longest_sentence, shortest_sentence, s_t_1, s_l_1, s_t_2, s_l_2, s_t_3, s_l_3, s_t_4, s_l_4, s_t_5, s_l_5):
    back = False
    os.system("clear")
    print("\n==================================================")
    print("                Sentence Analysis                 ")
    print("==================================================")
    print(f"Number of sentences: {n_sentences}")
    print(f"Average words per sentence: {n_words/n_sentences}")
    print(f"Longest sentence: {longest_sentence}, {len(longest_sentence.split())} words")
    print(f"Shortest sentence: {shortest_sentence}, {len(shortest_sentence.split())} words")
    print(f"Sentence length distribution (top 5): ")
    print(f"  {s_t_1} words: {s_l_1} times")
    print(f"  {s_t_2} words: {s_l_2} times")
    print(f"  {s_t_3} words: {s_l_3} times")
    print(f"  {s_t_4} words: {s_l_4} times")
    print(f"  {s_t_5} words: {s_l_5} times")
    print("Press 0 to go back")
    print("Press 1 to open the sentence length distribution graph")
    print("Press 2 to open the most common sentence lengths graph")
    while not back:
        answer = int(input("Press one of the options above: "))
        if answer == 0:
            menu()
            back = True
        if answer == 1:
            matplotlib_sentence_length_distribution(sentence_lengths)
        if answer == 2:
            matplotlib_top5_sentence_lengths(s_t_1, s_l_1, s_t_2, s_l_2, s_t_3, s_l_3, s_t_4, s_l_4, s_t_5, s_l_5)
        else:
            print("Invalid selection :(")

def character_analysis(words):
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
    letters_list = []
    for i in words:
        for j in i:
            if j.isalpha():
                letters_list.append(j.lower())
    # Same concept as in word_analysis, finding the most common letters and their counts
    # The first one is found by using max with set and count, the rest are found by sorting the set based on count in reverse order
    t_1 = max(set(letters_list), key=letters_list.count)
    l_1 = letters_list.count(max(set(letters_list), key=letters_list.count))
    t_2 = sorted(set(letters_list), key=letters_list.count, reverse=True)[1]
    l_2 = letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[1])
    t_3 = sorted(set(letters_list), key=letters_list.count, reverse=True)[2]
    l_3 = letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[2])
    t_4 = sorted(set(letters_list), key=letters_list.count, reverse=True)[3]
    l_4 = letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[3])
    t_5 = sorted(set(letters_list), key=letters_list.count, reverse=True)[4]
    l_5 = letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[4])
    t_6 = sorted(set(letters_list), key=letters_list.count, reverse=True)[5]
    l_6 = letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[5])
    t_7 = sorted(set(letters_list), key=letters_list.count, reverse=True)[6]
    l_7 = letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[6])
    t_8 = sorted(set(letters_list), key=letters_list.count, reverse=True)[7]
    l_8 = letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[7])
    t_9 = sorted(set(letters_list), key=letters_list.count, reverse=True)[8]
    l_9 = letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[8])
    t_10 = sorted(set(letters_list), key=letters_list.count, reverse=True)[9]
    l_10 = letters_list.count(sorted(set(letters_list), key=letters_list.count, reverse=True)[9])
    return (letters, digits, punctuation, t_1, l_1, t_2, l_2, t_3, l_3, t_4, l_4, t_5, l_5, t_6, l_6, t_7, l_7, t_8, l_8, t_9, l_9, t_10, l_10)
    

def character_analysis_menu(n_words, letters, digits, punctuation, t_1, l_1, t_2, l_2, t_3, l_3, t_4, l_4, t_5, l_5, t_6, l_6, t_7, l_7, t_8, l_8, t_9, l_9, t_10, l_10):
    back = False
    os.system("clear")
    print("\n==================================================")
    print("                Character Analysis                ")
    print("==================================================")
    print("Character distribution: ")
    print(f"    Number of letters: {letters}")
    print(f"    Number of digits: {digits}")
    print(f"    Number of punctuation marks: {punctuation}")
    print("Most common letters (top 10): ")
    print(f"    {t_1} ({l_1} times)")
    print(f"    {t_2} ({l_2} times)")
    print(f"    {t_3} ({l_3} times)")
    print(f"    {t_4} ({l_4} times)")
    print(f"    {t_5} ({l_5} times)")
    print(f"    {t_6} ({l_6} times)")
    print(f"    {t_7} ({l_7} times)")
    print(f"    {t_8} ({l_8} times)")
    print(f"    {t_9} ({l_9} times)")
    print(f"    {t_10} ({l_10} times)")
    print("\nPress 0 to go back")
    print("Press 1 to open the top 10 most common letters graph")
    print("Press 2 to open the character type distribution graph")
    while not back:
        answer = int(input("Press one of the options above: "))
        if answer == 0:
            menu()
            back = True
        if answer == 1:
            matplotlib_top10_letters(t_1, l_1, t_2, l_2, t_3, l_3, t_4, l_4, t_5, l_5, t_6, l_6, t_7, l_7, t_8, l_8, t_9, l_9, t_10, l_10)
        if answer == 2:
            matplotlib_character_distribution(letters, digits, punctuation)
        else:
            print("Invalid selection :(")

def export_results(file, n_lines, n_words, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences, longest_sentence, shortest_sentence):
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

def matplotlib_text_composition(n_lines, u_words, n_paragraphs, n_sentences):
    x = ['Lines', 'Paragraphs', 'Unique words', 'Sentences']
    count = [n_lines, n_paragraphs, len(u_words), n_sentences]
    plt.bar(x, count)
    plt.title('Text Composition')
    plt.xlabel('Text Elements')
    plt.ylabel('Count')
    plt.show()

def matplotlib_character_distribution(letters, digits, punctuation):
    x = ['Letters', 'Digits', 'Punctuation']
    count = [letters, digits, punctuation]
    plt.pie(count, labels=x, autopct='%1.1f%%', shadow=True, startangle=140, explode=(0.1, 0.1, 0.1))
    plt.title('Character Distribution')
    plt.show()

def matplotlib_top10_words(w_1, w_l_1, w_2, w_l_2, w_3, w_l_3, w_4, w_l_4, w_5, w_l_5, w_6, w_l_6, w_7, w_l_7, w_8, w_l_8, w_9, w_l_9, w_10, w_l_10):
    x = [w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8, w_9, w_10]
    count = [w_l_1, w_l_2, w_l_3, w_l_4, w_l_5, w_l_6, w_l_7, w_l_8, w_l_9, w_l_10]
    plt.bar(x, count)
    plt.title('Top 10 Most Common Words')
    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.show()

def matplotlib_word_length_distribution(words):
    x = []
    for i in words:
        if i.isalpha():
            x.append(len(i))
    count = []
    for j in x:
        count.append(x.count(j))
    plt.bar(x, count)
    plt.title("Word Length Distribution")
    plt.xlabel('Word Length (characters)')
    plt.ylabel('Count')
    plt.show()

def matplotlib_sentence_length_distribution(sentence_lengths):
    x = sentence_lengths
    count = []
    for j in x:
        count.append(x.count(j))
    plt.bar(x, count)
    plt.title("Sentence Length Distribution")
    plt.xlabel('Sentence Length (words)')
    plt.ylabel('Count')
    plt.show()

def matplotlib_top5_sentence_lengths(s_t_1, s_l_1, s_t_2, s_l_2, s_t_3, s_l_3, s_t_4, s_l_4, s_t_5, s_l_5):
    x = [s_t_1, s_t_2, s_t_3, s_t_4, s_t_5]
    count = [s_l_1, s_l_2, s_l_3, s_l_4, s_l_5]
    plt.bar(x, count)
    plt.title("Most Common Sentence Lengths")
    plt.xlabel('Sentence Length (words)')
    plt.ylabel('Count')
    plt.show()

def matplotlib_top10_letters(t_1, l_1, t_2, l_2, t_3, l_3, t_4, l_4, t_5, l_5, t_6, l_6, t_7, l_7, t_8, l_8, t_9, l_9, t_10, l_10):
    x = [t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8, t_9, t_10]
    count = [l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8, l_9, l_10]
    plt.bar(x, count)
    plt.title('Top 10 Most Common Letters')
    plt.xlabel('Letters')
    plt.ylabel('Count')
    plt.show()

def menu():
    os.system("clear")
    print("\n==================================================")
    print("                 TEXT ANALYSER                    ")
    print("==================================================")
    print("1. Load text file")
    print("2. Display basic statistics")
    print("3. Word analysis")
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
                n_lines, n_words, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences, longest_sentence, shortest_sentence = open_basic_stats(file)
                w_1, w_l_1, w_2, w_l_2, w_3, w_l_3, w_4, w_l_4, w_5, w_l_5, w_6, w_l_6, w_7, w_l_7, w_8, w_l_8, w_9, w_l_9, w_10, w_l_10 = word_analysis(words)
                sentence_lengths, n_sentences, n_words, longest_sentence, shortest_sentence, s_t_1, s_l_1, s_t_2, s_l_2, s_t_3, s_l_3, s_t_4, s_l_4, s_t_5, s_l_5 = sentence_analysis(words, n_sentences, longest_sentence, shortest_sentence)
                letters, digits, punctuation, t_1, l_1, t_2, l_2, t_3, l_3, t_4, l_4, t_5, l_5, t_6, l_6, t_7, l_7, t_8, l_8, t_9, l_9, t_10, l_10 = character_analysis(words)
                menu()
            case 2:
                basic_stats(letters, digits, punctuation, n_lines, n_words, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences, longest_sentence, shortest_sentence)
            case 3:
                word_analysis_menu(w_1, w_l_1, w_2, w_l_2, w_3, w_l_3, w_4, w_l_4, w_5, w_l_5, w_6, w_l_6, w_7, w_l_7, w_8, w_l_8, w_9, w_l_9, w_10, w_l_10, words)
            case 4:
                sentence_analysis_menu(sentence_lengths, n_words, n_sentences, longest_sentence, shortest_sentence, s_t_1, s_l_1, s_t_2, s_l_2, s_t_3, s_l_3, s_t_4, s_l_4, s_t_5, s_l_5)
            case 5:
                character_analysis_menu(n_words, letters, digits, punctuation, t_1, l_1, t_2, l_2, t_3, l_3, t_4, l_4, t_5, l_5, t_6, l_6, t_7, l_7, t_8, l_8, t_9, l_9, t_10, l_10)
            case 6:
                export_results(file, n_lines, n_words, words, n_chars_spcs, n_chars_no_spcs, u_words, n_paragraphs, n_sentences, longest_sentence, shortest_sentence)
            case 7:
                return 0
            case _:
                print("Choose one of the options above please :(")


main()