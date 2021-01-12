'''
# Q9: Write function integers_in_brackets that finds from a given string all integers that are enclosed in brackets. Example run: integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx") returns [12, -43, 12]. So there can be whitespace between the number and the brackets, but no other character besides those that make up the integer. Use regular expressions to do this. 

Args:
    string: 

Returns:
    s: string containing integers in brackets
'''

import re

def integers_in_brackets(string):
    # creating empty list to store integers
    s= []
    # compiling regular expression pattern
    pattern = re.compile(r'\[\s*(\+?-?\d+)\s*\]')
    for i in pattern.findall(string):
        s.append(int(i))
    return s

def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))
    
if __name__ == "__main__":
    main()

'''

Joke of the Question:

Did you hear the one about the statistician? Probably….

'''