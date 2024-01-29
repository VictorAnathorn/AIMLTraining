def find_longest_word(filename):
    longest_word = ""
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word


filename = "test_data/text.txt"
longest_word = find_longest_word(filename)
print("The longest word in the file is:", longest_word)
