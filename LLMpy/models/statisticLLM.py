# #################################################################################################
# Description: statisticLLM implementaion for LLMpy
# Author: AstroQuantumphysicist, 2023
# #################################################################################################

import random


def create_keyword_dict(text):
    """
    This funktion creates a dictionary of all keys and their next possible values.

    Parameters
    ----------
    text : str
        The text to be analyzed.
    """
    # split text into words and lowercase
    words = text.lower().split()
    # create dictionary
    keyword_dict = {}
    # loop through all words
    for i in range(len(words) - 1):
        # create keyword
        keyword = words[i]
        # check next word
        next_word = words[i + 1]
        # check if key already exists
        if key in keyword_dict:
            # append next word
            keyword_dict[key].append(next_word)
        else:
            # create new key
            keyword_dict[key] = [next_word]

    # return dictionary
    return keyword_dict

def generate_text(start_word, keyword_dict):
    """
    This funktion generates a text based on the keyword_dict.

    Parameters
    ----------
    start_word : str
        The start word for the text.

    keyword_dict : dict
        The dictionary of all keys (with context_length) and their next possible values.
    """
    # set current word
    current_word = start_word
    # set generated text
    generated_text = current_word.copy()

    # loop through all words till end of text
    while current_word.lower() != "none":
        # choose next word
        next_word = random.choice(keyword_dict[current_word.lower()]
        # append next word
        generated_text.append(next_word)
        # set current words
        current_words = next_word

    # return generated text
    return " ".join(generated_text)
