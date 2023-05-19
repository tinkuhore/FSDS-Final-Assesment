# Question 10 -
# Write a program to count the number of verbs, nouns, pronouns, and adjectives in a given particular phrase or
# paragraph, and return their respective count as a dictionary.

# Note -
# 1. Write code comments wherever required for code
# 2. You have to write at least 2 additional test cases in which your program will run successfully and provide
# an explanation for the same.

# -----------------------------------------------------------------------------------------------------------------------------------------
# Solution:
# we are using the spaCy library, which is a popular NLP library in Python, 
# to perform part-of-speech tagging on the given text
import spacy

def count_pos_tags(text):
    # load the pre-trained English model (en_core_web_sm) and process the text using the nlp object.
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    
    pos_counts = {
        'VERB': 0,
        'NOUN': 0,
        'PRON': 0,
        'ADJ': 0
    }
    
    for token in doc:
        if token.pos_ in pos_counts:
            pos_counts[token.pos_] += 1
    
    return pos_counts

# Example 1
text1 = "The quick brown fox jumps over the lazy dog."
print(f"Given text: {text1}\n")
print(f"Parts of speach found : {count_pos_tags(text1)}\n")

# Example 2
text2 = "I am running in the park and enjoying the beautiful weather."
print(f"Given text: {text2}\n")
print(f"Parts of speach found : {count_pos_tags(text2)}\n")