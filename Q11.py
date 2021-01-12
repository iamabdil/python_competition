'''
Question 11: Write a function extract_numbers that gets a string as a parameter. It should return a list of numbers that can be both ints and floats. Split the string to words at whitespace using the split() method. Then iterate through each word, and initially try to convert to an int. If unsuccesful, then try to convert to a float. If not a number then skip the word.
Example run: print(extract_numbers("abd 123 1.2 test 13.2 -1")) will return [123, 1.2, 13.2, -1] 


Args:

Returns:

'''

the_string = "abd 123 1.2 test 13.2 -1"

def extract_numbers(string):
    string = string.split()
    numbers = []

    for i in string:
        num = None

        try:
            num = int(i)
        except ValueError:
            pass

        if not num:
            try:
                num = float(i)
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