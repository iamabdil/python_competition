'''
Question 2: Given a string check if its characters can be permuted into a palindrome, a palindrome is word that is the same forward and backward, for example “aabaa”

Args:
    input: string to be checked

Returns:
    Boolean: True if palindrome, False if not
'''

palim = 'mum'
def is_palindrome(input):
    input = input.replace(" ", "")
    input = input.lower()
    d = dict()

    for i in input:
        if i in d:
            d[i]+= 1
        else:
            d[i] = 1
    odd_count = 0
    for k,v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
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