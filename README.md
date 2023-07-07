# LLMpy

![LLMpy Logo](https://github.com/AstroQuantumphysicist/LMMpy/blob/main/RepoData/IMG_4306.jpeg)

LLMpy is a package that allows to easily create advanced Large Language Models. It uses its on implementation of all the models, from statistical to transformer-based.

The Package is stable but it has only the statisticLLM implemented yet.

## Example
```python
# import the library
import LLMpy as llm
from LLMpy import statLLM

# define text or load it from a file
input_text = "This is a example for the LLMpy package. This code workes! You will wonder about the output because this is a LLM"

# define a input
input_words = "This is"
# define a context length
context_legth = 2 # the context length must match the number of input words

# create a learn dict
keyword_dict = statLLM.create_keyword_dict(input_text, context_length)

# generate a text
generated_text = statLLM.generate_text(input_words.lower(), keyword_dict, context_length)

# print the result
print(generated_text)

# you also can save the keyword_dict in a file an use it in many sessions
```

## Installation
You can install the package with pip:
```pip install LLMpy```

## Compabilytie
You can use this package on all devices with Python 3.10 or higher.
