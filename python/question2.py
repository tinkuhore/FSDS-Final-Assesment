# Question 2: -
# Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
# he can remove just one character at the index in the string, and the remaining characters will occur the same
# number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .

# Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
# an explanation for the same.

# Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }
# Example output 1- YES

# Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves
# character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
# Example output 2 - NO


def count_alphabet_frequency(word: str)-> dict:
    frequency = {}

    # Iterate over each character in the word
    for char in word:
        # Check if the character is an alphabet
        if char.isalnum():
            # Convert the character to lowercase for case-insensitive counting
            if char.isalpha():
                char = char.lower()

            # Update the frequency count in the dictionary
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return frequency


def string_validation(string: str)-> bool:
    '''
    Check if string is valid based on given condition and return YES or NO

    Conditions are:

    1. All characters in the string appear the same number of times. 
    This means that each character occurs with an equal frequency in the string. 
    For example, "aabcc" is valid because 'a' appears twice, 'b' appears once, and 'c' appears twice.

    2. It is possible to remove exactly one character from the string in such a way that 
    the remaining characters will occur the same number of times. In other words, 
    after removing a single character, the string should satisfy the condition mentioned in the first point. 
    For example, "abcc" is valid because removing one 'c' will result in "abc," where 'a' appears once and 'b' appears once.
    '''
    print(f"Given String --> {string}")

    # count the frequency of each character in the string
    char_frequency = count_alphabet_frequency(string)
    print(f"Frequency: {char_frequency}")

    # Extract the frequencies and convert them into a set
    frequencies_set = set(char_frequency.values())

    # Check if all frequencies are the same
    if len(frequencies_set) == 1:
        print(f"Explanation: All the characters in the string have the same frequency.")
        return "YES"
    # Check if we can make the string valid by removing any one of the characters
    elif len(frequencies_set) == 2:
        
        if (max(list(frequencies_set)) - min(list(frequencies_set)) == 1) and (list(char_frequency.values()).count(max(list(frequencies_set))) == 1):
            print("condition 2")
            for key, val in char_frequency.items():
                if val == max(list(frequencies_set)):
                    print(f"Explanation: By removving 1 '{key}' from `{string}`, we can make it a valid String.")
                    return "YES"
                
    else:
        print(f"Explanation: All the characters in the string don't have the same frequency.")
        return "NO"
    

s1 = "abc"
print(f"Valid String? --> {string_validation(s1)}\n")

s2 = "abcc"
print(f"Valid String? --> {string_validation(s2)}\n")

s3 = "abcdefghijklmnopqrstuvwxyz"
print(f"Valid String? --> {string_validation(s3)}\n")

s4 = "aabbaaaacccddd"
print(f"Valid String? --> {string_validation(s4)}\n")