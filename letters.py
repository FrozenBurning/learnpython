
def search4letters(phrase:str,letters:str='aeiou')->set:
    """Display any letters wanted found in a supplied word."""
    return set(letters).intersection(set(phrase))
