# Do this work in a new file, ***words.py***.

# 1. For a list of words, print out each word on a separate line,
#  but in all uppercase. How can you change a word to uppercase?
#  Ask Python for help on what you can do with strings!
# 2. Turn that into a function, ***print_upper_words***. Test it out. 
# (Don’t forget to add a docstring to your function!)
# 3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
# 4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.
    
test_string = "hello world"
test_list = ["hello","goodbye","mipso"]
test_e_words = ["everybody","elephant","easel","lemons"]
def print_upper_words(list_of_words):
    """For a list of words, print out each word in all uppercase"""
    for word in list_of_words:
        print(word.upper())

def print_e_words(e_word_list):
    for word in e_word_list:
        if word[0] == "e":
            print(word)

def print_desired_word(desired_start_letter, word_list):
    for word in word_list:
        if word[0] == desired_start_letter:
            print(word)
        else: print(f"not a {desired_start_letter} word")
    