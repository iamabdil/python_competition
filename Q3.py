'''
Question 3: Write a function to partition a list around a given value x, such that all numbers smaller than x comes before x and all numbers greater than x comes after x.  Ex. [ 3, 5, 1, 10, 4, 6, 9], x = 5 ==> [3, 1, 4, 5, 6, 9, 10]

Args:
    List: list to be partitioned
    x: value at which the list is partitioned

Returns:
    List: a partioned list

'''

List = [ 3, 5, 1, 10, 4, 6, 9]

def list_partioner(List, x):
    # creating empty lists to store the x value and the numbers smaller and larger than x
    x_smaller = []
    x_larger = []
    x_list = []

    # assigning numbers to above lists depending on if they are smaller, larger or equal to x
    for nums in List:
        if nums == x:
            x_list.append(nums)
        elif nums < x:
            x_smaller.append(nums)
        else:
            x_larger.append(nums)
    # returning the addition of all three lists        
    return x_smaller + x_list + x_larger

def main():
    print(list_partioner(List, 5))
    
if __name__ == "__main__":
    main()

'''

Joke of The Question:

Why did the chicken cross the road? The answer is trivial and is left as an exercise for the reader.

'''