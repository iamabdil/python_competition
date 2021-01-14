'''
# Q13: Write function multiplication_table that gets a positive integer n as parameter. The function should return an array with shape (n,n). The element at index (i,j) should be i*j. Don’t use for loops! In your solution, rely on broadcasting, the np.arange function, reshaping and vectorized operators. Example of usage:
# print(multiplication_table(4))
# [[0 0 0 0]
#  [0 1 2 3]
#  [0 2 4 6]
#  [0 3 6 9]]

'''

import numpy as np

def multiplication_table(n):
    # creating a n by n matrix, each row populated by 0 to n 
    a = np.full((n,n), 0) + np.arange(n)
    # creating a vertical vector with 0 to n 
    b = np.arange(n).reshape((n,1))
    # returning multiplication of a and b to give answer
    return a*b

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()

'''

Joke of the Question:

What did one support vector say to another support vector? Answer: I feel so marginalized

'''