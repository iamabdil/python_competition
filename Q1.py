'''
# Q1: Compute Product of two non-negative numbers without arithmetic operator. You are only allowed to use: bitwise operators <<, >>, |, &, ~, ^.
'''

# multiplying using the russian peasant algorithm; double first number and halve second number repeatedly till the second number isnt 1. When second number (b) becomes odd, add first number (a) to the 'product'
def multiply_bitwise(a, b):   
    # initialize product
    product = 0  
    # While second number doesn't become 1
    while (b > 0):  
        #If second number becomes odd, add the first number to result
        if (b & 1):  
            product = product + a
        #double the first number
        a = a << 1 
        #halve the second number
        b = b >> 1 
    return product

def main():
    print(multiply_bitwise(2,10))

if __name__ == "__main__":
    main()

'''
Joke of The Question:

Data science is 80% preparing data, 20% complaining about preparing data.

'''