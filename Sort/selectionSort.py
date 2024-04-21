# Selection Sort
# Select minimum in the array, then push to the first index
# Select minimum in the rest array, then push to the second index
# Select minimum in the rest array, then push to the third index
# N*(N+1)/2
# O(N^2)
# Not efficient for big data...
# Couldn't pass all test cases in Leetcode due to the time limit (exceeded).
def selection_sort(array):
    for x in range(len(array)):
        min = array[x]
        requireSwap = False
        for y in range(x+1,len(array)):
            if min > array[y]:
                min = array[y]
                index = y
                requireSwap = True
        if requireSwap:
            temp = array[x]
            array[x] = array[index]
            array[index] = temp
    print(array)

# test data
arr = [5,2,3,1]
# arr = [-9, -2, 45, 0, 3, 11, 88, 200]
selection_sort(arr)

