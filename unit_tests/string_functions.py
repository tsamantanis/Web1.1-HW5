"""Functions to manipulate strings."""

def greet_by_name(name):
    """Returns a greeting to the given person."""
    greeting = "Hello, " + name + "!"
    return greeting

def reverse(str):
    """Reverses the characters in a string."""
    return str[::-1]

def reverse_words(str):
    """Reverses the letters in each word of a string."""
    words = str.split()
    new_words = reverse(words[0])
    for word in words[1:]:
        new_words += ' ' + reverse(word)
    return new_words

def sarcastic(str):
    """ReTuRnS tHe SaRcAsTiC vErSiOn Of A sTrInG"""
    new_string = ''
    capitalize = True
    for letter in str:
        if letter.isalpha():
            new_string += letter.upper() if capitalize else letter.lower()
            capitalize = not capitalize
        else:
            new_string += letter
    return new_string

def find_longest_word(sentence):
    """Returns the longest word in a sentence."""
    if sentence == '':
        return ''
    words_list = sentence.split()
    print(words_list)
    longest_word = words_list[0]
    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word
    return word
