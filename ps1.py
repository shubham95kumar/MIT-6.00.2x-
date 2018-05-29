###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows
    
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    sortedCows = sorted(cows, key = lambda x: cows[x], reverse =True)
    allTripList = []
    while len(sortedCows)>0:
        newLimit  = limit
        count  = 0
        tripList = []
        #looping over sortedCows to add to the tripList until limit is exceeded
        for i in sortedCows:
            if cows[i] <= newLimit:
                tripList.append(i)
                newLimit -= cows[i]#updated value of limit after each loop
            elif cows[i] > newLimit:
                count  += 1
        #statement to break out of while loop
        if count == len(sortedCows):
            break
        
        [sortedCows.remove(each) for each in tripList]
        
        allTripList.append(tripList)
    return allTripList
    
# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    Cows = list(cows.keys())
    def value(lst):
        load = 0
        for each in lst:
            load += cows[each]
        return load   
    
    listOfCow = []
    [listOfCow.append(partition) for partition in get_partitions(Cows)]
    listOfCows = sorted(listOfCow, key =len)#list of partition sets is sorted as per the length of each subset
    for i in listOfCows:
        for each in i:
            if value(each) <= limit:
                continue
            else:
                break
        else:
            return i#if any partition set within listOfCows has all the elements <= limit,
        #then that particular set is the the one with minimum trips
        #since the list is sorted in increasing number of elements within a partition set or inc no of trips.
        continue
    
#    Cows = list(cows.keys())
#    listOfCows = []#A [list of cows] where each list is <= limit 
#    def value(lst):
#        load = 0
#        for each in lst:
#            load = load + cows[each]
#        return load   
#    
#    [listOfCows.append(partition) for partition in get_partitions(Cows)]
#        
#    def bruteforce(setPartitions, limit, noOfTrips = 0, least = 0):
#        if setPartitions == []:
#            return temp
#        else:
#            nextItem=setPartitions[0]
#            for each in nextItem:
#                if value(each)<=limit:
#                    noOfTrips += 1
#                else:
#                    bruteforce(setPartitions[1:], limit, 0, least)
#            if noOfTrips<least or least == 0:
#                least = noOfTrips
#                temp = nextItem
#                bruteforce(setPartitions[1:], limit, 0, least)
#        return temp
#    setPartitions = listOfCows
#    limit = limit
#    return bruteforce(setPartitions, limit, noOfTrips = 0, least = 0)

# Problem 3
import time
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows ={'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
    limit=10
    start1 = time.time()
    print(greedy_cow_transport(cows,limit), end = " ")
    end1 = time.time()
    
    print("greedy time:", end1-start1, end1, start1)
    print()
    start2 = time.time()
    print(brute_force_cow_transport(cows,limit), end = " ")
    end2 = time.time()
    print("bruteforce time:", end2-start2, end2, start2)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""
compare_cow_transport_algorithms()


