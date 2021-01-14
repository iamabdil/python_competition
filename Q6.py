'''
Question 6: A magic index in an array A is an index x such that A[x] = x, given a SORTED array A find a magic index.

Args:
    List: sorted list

Returns:
    magic: a list of magic indices

'''
# sorted list
sorted_list = sorted([10, 5, 1, 1, 2, 6, 9])

def abracadabra(list):
    magic = [num for index, num in enumerate(sorted_list) if num == index]
    return magic

def main():
    print(abracadabra(sorted_list))
    
if __name__ == "__main__":
    main()

'''

Joke of the Question:

Why should you take a data scientist with you into the jungle? Answer: They can take care of Python problems

'''