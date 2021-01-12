
'''
# Q8: Schedule Tasks to minimise the waiting time. Given a list of service time for tasks, find the best scheduling to minimise the waiting time. For example given service time [2, 5, 1, 3], if we schedule them in the given order the waiting time = 0 + (2) + (2 +5) + (2 +5 +1) = 17, if we schedule them in order of decreasing service, the waiting time = 0 + (5) + (5+3) + (5+3 +2) = 23. The best scheduling in this case is [1, 2, 3, 5]

Args:
    times: a list of service times for tasks

Returns:
    sorted times: the times sorted in ascending order

'''

service_times = [2, 5, 1, 3]
def shortestTime(times):
    # sorting service times
    return sorted(times)

def main():
    print(shortestTime(service_times))
    
if __name__ == "__main__":
    main()

'''

Joke of the Question:

Data is like people – interrogate it hard enough and it will tell you whatever you want to hear

'''