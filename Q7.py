'''
Question 7: Given two sorted arrays  A and B, merge into a single array: A[3, 7, 10], B=[1, 2, 4, 5, 6, 9, 11] ==> [1,2,3,5,6,7,9,10,11]

Args:
    A: first sorted array
    B: second sorted array

Returns:
    merged array
'''
# arrays
A = [3, 7, 10]
B = [1, 2, 4, 5, 6, 9, 11]

# merhing and sorting the arrays
def sort_palin(A, B):
    return sorted(A+B)

def main():
    print("the merged sorted list is:", sort_palin(A, B))
    
if __name__ == "__main__":
    main()


'''

Joke of the Question:

Old data analysts never die – they just get broken down by age

'''