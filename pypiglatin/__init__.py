__version__ = '0.1.2'
__author__ = 'owenway imerplay '

vowels = "aeiou"

def translate_word(word):
    """Translate a string conatining a single word from English to Pig Latin

    Args:
        word (str): A string containing a single word in plain English

    Returns:
        str: A string containing a translated copy of the original string
    """
    ret = ""
    
    if word[0].lower() in vowels:
        ret = (word + "way").lower()
        
    elif word[0].lower() not in vowels and word[1].lower() not in vowels:
        ret = (word[2:] + word[0] + word[1] + "ay").lower()
        
    elif word[0] not in vowels and word[1] in vowels:
        ret = (word[1:] + word[0] + "ay").lower()

    return ret

def translate_string(string):
    """A function which can translate an entire string of words from English to Pig Latin

    Args:
        string (str): A string which can consist of a single word, or as many as required. They should be in plain English

    Returns:
        str: A string containing a translated copy of the original string
    """
    
    out_str = ""
    
    for word in string.split():
        out_str = out_str + translate_word(word) + " "
    
    return out_str
        
    
