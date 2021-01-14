'''
Q15: Make function powers_of_series that takes a Series and a positive integer k as parameters and returns a DataFrame. The resulting DataFrame should have the same index as the input Series. The first column of the dataFrame should be the input Series, the second column should contain the Series raised to power of two. The third column should contain the Series raised to the power of three, and so on until (and including) power of k. The columns should have indices from 1 to k.
	The values should be numbers, but the index can have any type. Test your function from the main function. Example of usage:
	s = pd.Series([1,2,3,4], index=list("abcd"))
	print(powers_of_series(s, 3))
	Should print:
	   1   2   3
	a  1   1   1
	b  2   4   8
	c  3   9  27

'''

import pandas as pd

def powers_of_series(s, k):
    df = pd.DataFrame(index=s.index)
    for i in range(k):
        df[i+1] = [x**(i+1) for x in s]
    return(df)

def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()


'''

Joke of the Question:

Why did the programmer quit their job? Answer: Becauses they didn’t get arrays.

'''