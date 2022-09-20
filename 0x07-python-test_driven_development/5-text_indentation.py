#!/usr/bin/python3
"""fn that prints a text with 2 new lines after each of these: ., ? and :"""
def text_indentation(text):
    """Prints indentations for a string
    """
    special = ['.', '?', ':']
    if type(text) != str:
        raise TypeError("text must be string")
    for x in text:
        print(x, end='')
        if x in special:
            print('\n\n', end='')
