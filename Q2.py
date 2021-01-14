'''
Question 2: Given a string check if its characters can be permuted into a palindrome, a palindrome is word that is the same forward and backward, for example “aabaa”

Args:
    input_string: string to be checked

Returns:
    Boolean: True if palindrome, False if not
'''

palim = 'mum'
def is_palindrome(input_string):
    #removing the whitespace between the characters
    input_string = input_string.replace(" ", "")
    #convert everything to the lower case
    input_string = input_string.lower()
    d = dict()

    #looping through the string to check if character is present in the dict

    for i in input_string:
        #if it is in the dictionary increment the value of the key by 1
        if i in d:
            d[i]+= 1
        else:
            d[i] = 1
    # keeping track of how many odd elements encountered in the dict, this is imp to check that at most the contents of dict will have 1 odd value
    odd_count = 0
    #looping through the keys and values in the dictionary
    for k,v in d.items():
        #if value is odd and the odd count is zero
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        # if value is also odd but odd count is not zero
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

def main():
    print(is_palindrome(palim))
    
if __name__ == "__main__":
    main()


'''

Joke of The Question:

There are 10 kinds of people in this world. Those who understand binary and those who don’t.

'''