import pytest

from .string_functions import *

def test_greeting_jeremy():
    """Test for greet_by_name"""
    # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

    # Step 2: Decide what the expected outcome is for the scenario
    expected = 'Hello, Jeremy!'

    # Step 3: Call the function being tested to get its actual output
    actual = greet_by_name('Jeremy')

    # Step 4: Compare expected & actual outcomes. If they match, the test passes
    assert actual == expected

def test_greeting_dani():
    """Test for greet_by_name"""
    expected = 'Hello, Dani!'
    actual = greet_by_name('Dani')
    assert actual == expected

def test_reverse_long():
    """Test reversing a long string."""
    expected = 'asdfghjklzxcvbnm'
    actual = reverse('mnbvcxzlkjhgfdsa')
    assert actual == expected

def test_reverse_short():
    """Test reversing a short string."""
    expected = 'abc'
    actual = reverse('cba')
    assert actual == expected

def test_reverse_words_long():
    """Test reversing words in a long string."""
    expected = 'Pinapple hat rocket'
    actual = reverse_words('elppaniP tah tekcor')
    assert actual == expected

def test_reverse_words_short():
    """Test reversing words in a short string."""
    expected = 'What is it'
    actual = reverse_words('tahW si ti')
    assert actual == expected

def test_sarcastic_long():
    """Test sarcastic-ifying a long string."""
    expected = 'SpOnGeBoB aNd PaTrIcK'
    actual = sarcastic('spongebob and patrick')
    assert actual == expected

def test_sarcastic_short():
    """Test sarcastic-ifying a short string."""
    expected = 'BlUe'
    actual = sarcastic('blue')
    assert actual == expected

def test_find_longest_word():
    """Test finding the longest word of a sentence"""
    expected = ''
    actual = find_longest_word('')
    assert actual == expected

# run the tests
if __name__ == '__main__':
    unittest.main()
