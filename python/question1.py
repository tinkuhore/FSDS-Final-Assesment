# Question 1: -
# Write a program that takes a string as input, and counts the frequency of each word in the string, there might
# be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
# highest-frequency word.

# Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
# an explanation for the same.

# Example input - string = “write write write all the number from from from 1 to 100”
# Example output - 5
# Explanation - From the given string we can note that the most frequent words are “write” and “from” and
# the maximum value of both the values is “write” and its corresponding length is 5


def find_highest_frequency_word_length(string: str)-> int:

    '''Find the length of highest frequency word in the given string'''

    # Split the string into words
    words = string.split()

    # Count the frequency of each word using a dictionary
    word_frequency = {}
    for word in words:
        if word.lower() in word_frequency:
            word_frequency[word.lower()] += 1
        else:
            word_frequency[word.lower()] = 1


    # Find the word(s) with the highest frequency
    max_frequency = max(word_frequency.values())
    highest_frequency_words = [word for word, freq in word_frequency.items() if freq == max_frequency]

    # Find the length of the highest-frequency word
    if len(highest_frequency_words) == 1:
        return len(highest_frequency_words[0])
    else:
        return max([len(word) for word in highest_frequency_words])
    

# Test case 1
string1 = "write write write all the number from from from 1 to 100"
print(f"String -> {string1} \n Lenght -> {find_highest_frequency_word_length(string1)} \n")
# Output: 5
# Explanation: From the given string we can note that the most frequent words are “write” and “from” and
# the maximum value of both the values is “write” and its corresponding length is 5


# Test case 2
string2 = "a a a b b c c c c d d d d d"
print(f"String -> {string2} \n Lenght -> {find_highest_frequency_word_length(string2)} \n")
# Output: 1
# Explanation: From the given string we can note that the most frequent word is "d" and
# its corresponding length is 1

# Test case 3
string3 = "Hello world hello world hello"
print(f"String -> {string3} \n Lenght -> {find_highest_frequency_word_length(string3)} \n")
# Output: 5
# Explanation: From the given string we can note that the most frequent word is "hello" and
# its corresponding length is 5