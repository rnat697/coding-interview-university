# ---- Complexity/Performance ----
# Time Complexity: 
# - **Best case complexity**: `O(1)`
# - **Average case complexity**: `O(log n)`
# - **Worst case complexity**: `O(log n)`

# Space Complexity: O(1)

# Searching algorithm for finding an element’s position in a **sorted array** 
# by **repeatedly dividing the search interval in half**. The element is always 
# searched in the middle portion of an array. The idea of binary search is to use the 
# information that the array is sorted and reduce the time complexity to O(log N).
# Binary search algorithm can be implemented in two ways
# 1. Iterative Method
# 2. Recursive Method - Follows a divide and conquer approach.
# ---- Algorithm Pseudocode ----
# 1. Divide the search space into two halves by finding the middle index “mid”. 
# 2. Compare the middle element of the search space with the key. 
# 3. If the key is found at middle element, the process is terminated.
# 4. If the key is not found at middle element, choose which half will be used as the next search space.
#   a. If the key is smaller than the middle element, then the left side is used for next search.
#   b. If the key is larger than the middle element, then the right side is used for next search.
# 5. This process is continued until the key is found or the total search space is exhausted


# It returns index of x in given array arr if present,
# else returns -1
# Uses while loop.
def binarySearchIterative(arr:list, target:int):
  highIndex = len(arr) -1
  lowIndex = 0
  midIndex = 0
  
  while lowIndex  <= highIndex :
    midIndex  = (highIndex  + lowIndex ) // 2
    
    middleValue = arr[midIndex ]
    
    if target > middleValue:
      # If the key is larger than the middle element, then the right side is used for next search.
      # increase the lowIndex by midIndex + 1
      lowIndex  = midIndex  + 1
      
    elif(target < middleValue):
      # If the key is smaller than the middle element, then the left side is used for next search.
      # increase the highIndex by midIndex + 1
      highIndex = midIndex  - 1
    
    else:
      # If the key is found at middle element, the process is terminated.
      return midIndex
  
  # if this is reached, no element with the target is present
  return -1

# Recursive Binary Search
# Space complexity O(logn)     [NOTE: Recursion creates Call Stack]
def binarySearchRecursive(arr:list, target:int, highIndex:int, lowIndex:int):
  if highIndex >= lowIndex:
    midIndex = (highIndex + lowIndex) // 2
    middleValue = arr[midIndex]
    
    if(target > middleValue):
      # increase the lowIndex by midIndex + 1
      lowIndex = midIndex + 1
      binarySearchRecursive(arr, target, highIndex, lowIndex)

    elif(target < middleValue):
      # increase the highIndex by midIndex - 1
      highIndex = midIndex - 1
      binarySearchRecursive(arr, target, highIndex, lowIndex)
    else:
      return midIndex
  
  else:
    return -1


if __name__ == "__main__":
  array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
  target = 23
  indexIterative = binarySearchIterative(array,target)
  print(f"Index found by iterative: {indexIterative}, expected: 5")
  high = len(array) - 1
  low = 0
  indexRecursive = binarySearchRecursive(array,target,high,low)
  print(f"Index found by Recursive: {indexIterative}, expected: 5")
  