'''
Tate Thomas
CS 2420
Project 2: Sorting
'''


import random
import time


def is_sorted(lyst):
    '''Takes any list and checks if it is sorted,
       along with if the elements are ints and if it is a list.'''

    if type(lyst) is not list:
        print("Not list")
        return False

    for i in range(1, len(lyst)):

        if type(lyst[i]) is not int:
            print("Not int")
            return False

        if lyst[i] < lyst[i - 1]:
            print(i - 1, lyst[i - 1], "!<=", i,  lyst[i])
            return False

    return True


def quicksort(lyst):
    '''Outputs a lower and upper list found by using a pivot'''

    if len(lyst) < 2:
        return lyst

    pivot = lyst[-1]
    bottom = []
    top = []

    for n in range(len(lyst)):

        value = lyst[n]

        if value < pivot:
            bottom.append(value)

        elif value > pivot:
            top.append(value)

        else:
            if len(bottom) <= len(top):
                bottom.append(value)
            else:
                top.append(value)

    return quicksort(bottom) + quicksort(top)


def mergesort(lyst):
    '''Outputs new sorted list by splitting list in half until there's only 1 element,
       then puts all separate lists back together sorted.'''

    length = len(lyst)

    if length == 1:
        return lyst

    if length == 2:
        middle = 1
    else:
        middle = length // 2

    bottom = mergesort(lyst[:middle])
    top = mergesort(lyst[middle:])

    i = 0
    j = 0
    new_list = []

    while ((i < len(bottom)) or (j < len(top))):

        if i == (len(bottom) - 1):
            new_list.extend(top[j:])
            break

        if j == (len(top) - 1):
            new_list.extend(bottom[i:])
            break

        if bottom[i] <= top[j]:
            new_list.append(bottom[i])
            i += 1

        else:
            new_list.append(top[j])
            j += 1

    return new_list


def selection_sort(lyst):
    '''Sorts list by finding min and max, puts those at opposite ends,
       and repeats without those values.'''

    low = 0
    high = len(lyst) - 1

    if len(lyst) <= 1:
        return lyst

    while low <= high:

        minimum = low
        maximum = high

        for n in range(low, high + 1):

            if lyst[n] < lyst[minimum]:
                minimum = n
            elif lyst[n] > lyst[maximum]:
                maximum = n

        if lyst[minimum] == lyst[maximum]:
            return lyst

        lyst[low], lyst[minimum] = lyst[minimum], lyst[low]

        if maximum == low:
            maximum = minimum

        lyst[high], lyst[maximum] = lyst[maximum], lyst[high]

        low += 1
        high -= 1

    return lyst



def insertion_sort(lyst):
    '''Sorts list by incrementing through list and swapping behind until it's sorted.'''

    if len(lyst) <= 1:
        return lyst

    for n in range(1, len(lyst)):

        i = n

        while ((lyst[i] < lyst[i - 1]) and (i >= 1)):

            lyst[i], lyst[i - 1] = lyst[i - 1], lyst[i]
            i -= 1

    return lyst


def main():
    '''Main code, makes random list, uses each sorting algorithm.'''
    unsorted = [random.randint(0,1000000) for n in range(20000)]
    #unsorted = random.sample(range(1000000), k=20000)

    my_list = unsorted.copy()
    print("Starting insertion sort...")
    start = time.perf_counter()
    result = insertion_sort(my_list)
    stop = time.perf_counter()
    total = stop - start
    #print("\tList is sorted:", is_sorted(result))
    print(f"\tTotal time: {total:.6f} seconds")

    my_list = unsorted.copy()
    print("Starting selection sort...")
    start = time.perf_counter()
    result = selection_sort(my_list)
    stop = time.perf_counter()
    total = stop - start
    #print("\tList is sorted:", is_sorted(result))
    print(f"\tTotal time: {total:.6f} seconds")

    my_list = unsorted.copy()
    print("Starting merge sort...")
    start = time.perf_counter()
    result = mergesort(my_list)
    stop = time.perf_counter()
    total = stop - start
    #print("\tList is sorted:", is_sorted(result))
    print(f"\tTotal time: {total:.6f} seconds")

    my_list = unsorted.copy()
    print("Starting quick sort...")
    start = time.perf_counter()
    result = quicksort(my_list)
    stop = time.perf_counter()
    total = stop - start
    print("\tList is sorted:", is_sorted(result))
    print(f"\tTotal time: {total:.6f} seconds")

    my_list = unsorted.copy()
    print("Starting tim sort...")
    start = time.perf_counter()
    my_list.sort()
    stop = time.perf_counter()
    total = stop - start
    #print("\tList is sorted:", is_sorted(my_list))
    print(f"\tTotal time: {total:.6f} seconds")

if __name__ == "__main__":
    main()
