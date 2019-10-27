# Spoken_to_Written

# Features Implemented

1. All the numbers in words are converted into digits.
2. Abbrevations are converted into their proper form. (eg: C M - CM)
3. Words like Triple A, Double P converted to AAA, PP.
4. Currency words converted to Currency Signs. (eg: 2 dollars to $2) - Only implemented for Dollars. Other currency symbols can be added easily


# Features to-be implemented

1. Convert first letter of Nouns to Upper Case. Use NLTK Parts of Speech tagging to recognise nouns.
2. Write the text converted to Written format in to a new file.

# Instructions to Use

1. Download the repository
2. run the command
```
python setup.py install

```
3. To use the library
```
from spoken2written.agn import *

read_and_process("text_file_path")

```
