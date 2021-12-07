"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    read_file = open(file_path).read().split()
    return read_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    gram = 3

    # for i in range(gram):
    #     current_key += text_string[gra]

    for i in range(len(text_string) - gram):
        current_key = (text_string[i], text_string[i+1], text_string[i+2])
        chosen_word = text_string[i+gram]
        # get value at current key, if theres no value/key, return empty list, otherwise return value
        # append chosen_word to whatever is returned
        # chains.get(current_key, [])
        list_of_current_key = chains.get(current_key,[])
        list_of_current_key.append(chosen_word)
        chains[current_key] = list_of_current_key
    
   
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    # words.append(choice(list(chains)))
    
    # upper_keys = []
    # for key in chains.keys():
    #     if key[0].islower():
    #         continue
    #     else:
    #         upper_keys.append(key)

    current_key = choice(list(chains))

    # while current_key[0].islower():
    #     current_key = choice(list(chains))
    #     print(current_key)
    # words.append(current_key[0])
    
    while current_key in chains:
        chosen = choice(chains[current_key])
        words.append(chosen)
        new_key = (current_key[-2],current_key[-1], chosen)
        current_key = new_key
        
    
    
        # chosen = choice(val)
        # words.append(chosen)
        # new_key = (key[1], chosen)

    
    return ' '.join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
