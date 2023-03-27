![PyPI - Downloads](https://img.shields.io/pypi/dm/pypiglatin?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/pypiglatin?style=for-the-badge)
![PyPI - License](https://img.shields.io/pypi/l/pypiglatin?style=for-the-badge)

# PyPigLatin

PyPigLatin is a module which can convert words or strings of words from English, into Pig Latin

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyPigLatin.

```bash
pip install pypiglatin
```

## Usage

```python
import pypiglatin as p

# Example showing translation of a single word
single_word = "Hello"

print(p.translate_word(single_word)
# This would print 'ellohay'


# To trnalsate a larger string, use the translate_string function
larger_string = "Pig Latin is hard to speak"

print(p.translate_string(larger_string))
# This would print 'igpay atinlay isway ardhay otay eakspay'
```

View the docs [Here](https://pypiglatin.readthedocs.io/en/latest/)

## License

[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
