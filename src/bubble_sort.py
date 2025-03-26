def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True
        end -= 1
    return nums

'''
BUBBLE SORTS

Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order. It continues to loop over the slice until the whole list is completely sorted. Here's the pseudocode:

Set swapping to True
Set end to the length of the input list
While swapping is True:
    Set swapping to False
    For i from the 2nd element to end:
        If the (i-1)th element of the input list is greater than the ith element:
            Swap the (i-1)th element and the ith element
            Set swapping to True
    Decrement end by one
Return the sorted list

Assignment:
While our avocado toast influencers were happy with our search functionality, now they want to be able to sort all their followers by follower count. Bubble sort is a straightforward sorting algorithm that we can implement quickly, so let's do that!

Complete the bubble_sort function according to the described algorithm above.
'''