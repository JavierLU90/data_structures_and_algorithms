def quick_sort(nums, low, high):
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle - 1)
        quick_sort(nums, middle + 1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

'''
QUICK SORT

Quick sort is an efficient sorting algorithm that's widely used in production sorting implementations. Like merge sort, quick sort is a recursive divide and conquer algorithm.

Divide:

Select a pivot element that will preferably end up close to the center of the sorted pack
Move everything onto the "greater than" or "less than" side of the pivot
The pivot is now in its final position
Recursively repeat the operation on both sides of the pivot

Conquer:

The array is sorted after all elements have been through the pivot operation


Pseudocode:

Select a "pivot" element - We'll arbitrarily choose the last element in the list
Move through all the elements in the list and swap them around until all the numbers less than the pivot are on the left, and the numbers greater than the pivot are on the right
Move the pivot between the two sections where it belongs
Recursively repeat for both sections


Assignment:

We now have two sorting algorithms on our LockedIn backend! It is a bit annoying to maintain both in the codebase. Quicksort is fast on large datasets just like merge sort, but is also lighter on memory usage. Let's use quick sort for both follower count and influencer revenue sorting!

Complete the quick_sort and partition functions according to the given algorithms.

The process is started with quick_sort(A, 0, len(A)-1).


quick_sort(nums, low, high):

If low is less than high:
    Partition the input list using the partition function and store the returned "middle" index
    Recursively call quick_sort on the left side of the partition
    Recursively call quick_sort on the right side of the partition

partition(nums, low, high):

Set pivot to the element at index high
Set i to the index below low
For each index (j) from low to high:
    If the element at index j is less than the pivot:
        Increment i by 1
        Swap the element at index i with the element at index j
Swap the element to the right of i with the pivot element
Return the new index of the pivot element (the item in the "middle" of the partition)
'''