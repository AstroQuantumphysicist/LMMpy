from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.1.0'
DESCRIPTION = 'A package that allows to easily create advanced Large Language Models.'
LONG_DESCRIPTION = 'A package that allows to easily create advanced Large Language Models. It uses its on implementation of all the models, from statistical to transformer-based.'

# Setting up
setup(
    name="LLMpy",
    version=VERSION,
    author="Lino Brendler",
    author_email="<linobrendler@linoia.net>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['random'],
    keywords=['python', 'language', 'model', 'large', 'language model', 'large language model', 'LLM', 'LLMpy', 'llmpy',],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
