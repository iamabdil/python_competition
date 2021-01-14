'''
Q10: Create a function called summary that gets a list of filenames as a parameter. The input files should contain a floating point number on each line of the file. Make your function read these numbers and then return a triple containing the sum, average, and standard deviation of these numbers for the file.  https://en.wikipedia.org/wiki/Standard_deviation#Sample_standard_deviation_of_metabolic_rate_of_northern_fulmars  The main function should call the function summary for each filename in the list sys.argv[1:] of command line parameters. (Skip sys.argv[0] since it contains the name of the current program.)

Summary Function:
    Args:
        filename: files containing floating point numbers
    
    Returns:
        total_sum, average, stddev
'''

import sys
import numpy as np

def summary(filename):
    # read the file
    f = open(filename, "r")
    # splitting the file content by lines
    str_numbers = f.read().splitlines()
    numbers = []
    # looping through numbers and appending them to numbers list
    for num in str_numbers:
        try:
            numbers.append(float(num))
        except:
            pass

    # calculations  
    total_sum = sum(numbers)
    average = total_sum/len(numbers)
    stddev = np.std(numbers)

    return total_sum, average, stddev

def main():
    filenames = sys.argv[1:]

    print(filenames)

    for name in filenames:
        total_sum, average, stddev = summary(name)
        print(f"File {name} Sum: {total_sum} Average: {average} Stddev: {stddev}")


if __name__ == "__main__":
    main()

'''

Joke of the Question:

Two random variables were talking in a bar. They thought they were being discrete, but I heard their chatter continuously.

'''