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
input_text = "This is a example for the LLMpy package. This code workes! You will wonder about the output because this is a LLM."

# define a input
input_word = "This"

# create a learn dict
keyword_dict = statLLM.create_keyword_dict(input_text)

# generate a text
generated_text = statLLM.generate_text(input_word.lower(), keyword_dict)

# print the result
print(generated_text)

# you also can save the keyword_dict in a file an use it in many sessions
```

## Installation
You can install the package like in the wiki with pip
