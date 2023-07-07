# #################################################################################################
# Description: statisticLLM implementaion for LLMpy
# Author: Lino Brendler, 2023
# #################################################################################################

import random


def create_keyword_dict(text, context_length):
    """
    This funktion creates a dictionary of all keys (with context_length) and their next possible values.

    Parameters
    ----------
    text : str
        The text to be analyzed.

    context_length : int
        The length of the context.
    """
    # split text into words and lowercase
    words = text.lower().split()
    # create dictionary
    keyword_dict = {}
    # loop through all words
    for i in range(len(words) - context_length):
        # create key
        key = tuple(words[i:i + context_length])
        # check next word
        next_word = words[i + context_length]
        # check if key already exists
        if key in keyword_dict:
            # append next word
            keyword_dict[key].append(next_word)
        else:
            # create new key
            keyword_dict[key] = [next_word]

    # return dictionary
    return keyword_dict

def generate_text(start_words, keyword_dict, context_length):
    """
    This funktion generates a text based on the keyword_dict.

    Parameters
    ----------
    start_words : str
        The start words for the text.

    keyword_dict : dict
        The dictionary of all keys (with context_length) and their next possible values.

    context_length : int
        The length of the context.
    """
    # set current words
    current_words = start_words.split()
    # set generated text
    generated_text = current_words.copy()

    # loop through all words till end of text
    while tuple(current_words[-context_length:]) != ("none",):
        # choose next word
        next_word = random.choice(keyword_dict.get(tuple(current_words[-context_length:]), ["None"]))
        # append next word
        generated_text.append(next_word)
        # set current words
        current_words.append(next_word)
        # remove first word
        current_words = current_words[1:]

    # return generated text
    return " ".join(generated_text)
