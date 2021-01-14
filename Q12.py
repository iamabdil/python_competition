'''
# Q12: Write function vector_lengths that gets a two dimensional array of shape (n,m) as a parameter. Each row in this array corresponds to a vector. The function should return an array of shape (n,), that has the length of each vector in the input. The length is defined by the usual Euclidean norm. Don’t use loops at all in your solution. Instead use vectorized operations. You must use at least the np.sum and the np.sqrt functions. You can’t use the function scipy.linalg.norm. Test your function in the main function.

'''

import numpy as np

def vector_lengths(x):
    # euxlidean norm calculation
    return np.sqrt((x**2).sum(axis=1))

def main():
    # testing function with 3x3 matric
    two_dim_array = np.array([[5, 2, 7], [7, 3, 5], [3, 1, 9]])
    print(vector_lengths(two_dim_array))

if __name__ == "__main__":
    main()


'''

Joke of the Question:

Do Neural Networks Dream of Strictly Convex Sheep?

'''