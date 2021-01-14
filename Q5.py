'''
Question 5: Write a method that returns all subset of a set of numbers, don’t use builtin functions.
'''

set_nums = {0, 1, 2, 3}
list_nums = list(set_nums)

def sub_sets(sset):
        return subsetsRecur([], sorted(sset))
    
def subsetsRecur(current, sset):
    # using recursion to generate subsets for a given list of numbers
    if sset:
        return subsetsRecur(current, sset[1:]) + subsetsRecur(current + [sset[0]], sset[1:])
    return [current]

def main():
    print(sub_sets(list_nums))
    
if __name__ == "__main__":
    main()


'''

Joke of the Question:

A SQL query walks into a bar, walks up to two tables and asks “Can I join you?”

'''