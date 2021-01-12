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
    # empty list to append magic indexes
    magic = []
    # looping through list and appending indexes that equal number
    for index, nums in enumerate(sorted_list):
        if nums == index:
            magic.append(nums)
    return magic

def main():
    print(abracadabra(sorted_list))
    
if __name__ == "__main__":
    main()

'''

Joke of the Question:

Why should you take a data scientist with you into the jungle? Answer: They can take care of Python problems

'''