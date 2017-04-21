import sys

# argv: a list of integers that are >= 0 and less than a certain limit k.
def main(list, k):

    # Parse input 'list ' to turn it into a list of integers.

    
    counting_array = []
    sorted_array = []
    i = 0
    # Create a list of size (k+1) with all 0's.
    while (i <= k):
        counting_array.append(0)
        i += 1
    # For each element from input list, update our counting_array.
    for element in list:
        counting_array[int(element)] += 1
    j = 0
    while (j <= k):
        l = 0
        num = counting_array[j]
        while (l < num):
            sorted_array.append(j)
            l+=1
        j+=1
    print(sorted_array)

if __name__ == "__main__":
    # argv: countingSort.py - a list of integers - an upper limit k
    if (len(sys.argv) != 3):
        print("Wrong number of arguments: Please include your path of the file.")
        exit(1)
    main(sys.argv[1], int(sys.argv[2]))