'''
Qustion 4: Convert a real number between 0 and 1 to a binary string, if you can’t represent the number in at most 32 characters print “ERROR”

Args:
    x: the number to be converted

Returns:
    answer: converted binary string
    ERROR
'''

def to_Binary(x): 
    answer = "" 
    answer = answer + "."
    # checking if number is between 0 and 1
    if(x >= 1 or x <= 0): 
        return "ERROR"
    while(x > 0): 
        # returning error if length is greater than 32
        if(len(answer) >= 32): 
            return "ERROR"
        # converting to binary
        y = x * 2
        if (y >= 1): 
            answer = answer + "1"
            x = y - 1
        else: 
            answer = answer + "0"
            x = y
    return answer 

def main():
    print(to_Binary(0.75))
    
if __name__ == "__main__":
    main()

'''

Joke of the Question:

The data science motto: If at first you don’t succeed; call it version 1.0

'''