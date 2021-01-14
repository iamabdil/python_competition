'''
Question 11: Write a function extract_numbers that gets a string as a parameter. It should return a list of numbers that can be both ints and floats. Split the string to words at whitespace using the split() method. Then iterate through each word, and initially try to convert to an int. If unsuccesful, then try to convert to a float. If not a number then skip the word.
Example run: print(extract_numbers("abd 123 1.2 test 13.2 -1")) will return [123, 1.2, 13.2, -1] 
'''

the_string = "abd 123 1.2 test 13.2 -1"

def extract_numbers(string):
    # splitting the string
    string = string.split()
    numbers = []

    # attempting to convert each item to an integer
    for i in string:
        num = None

        try:
            num = int(i)
        # if conversion not possible, raise a value error
        except ValueError:
            pass
        
    # attempting to convert each item to an float
        if not num:
            try:
                num = float(i)
        # if conversion not possible, raise a value error
            except ValueError:
                pass

        if num:
            numbers.append(num)

    return numbers

def main():
    print(extract_numbers(the_string))

if __name__ == "__main__":
    main()

'''

Joke of the Question:

Old age is statistically good for you – very few people die past the age of 100.

'''