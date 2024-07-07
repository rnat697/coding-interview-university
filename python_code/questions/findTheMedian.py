# The median of a list of numbers is essentially its middle element 
# after sorting. The same number of elements occur after it as 
# before. Given a list of numbers with an odd number of elements, 
# find the [median](https://en.wikipedia.org/wiki/Median)
# **Example**
# `arr = [5,3,1,2,4]`
# The sorted array `arr' = [1,2,3,4,5]` . The middle element and the median is 3.

# **Function Description**
# Complete the *findMedian* function in the editor below.
# findMedian has the following parameter(s):
# - int arr[n]: an unsorted array of integers

# **Returns**
# - int: the median of the array

# **Input Format**
# The first line contains the integer n, the size of arr.
# The second line contains  space-separated integers arr[i]

# **Constraints**

# - 1 ≤ n ≤ 1000001
# - n is odd
# - -10000 ≤ arr[i] ≤ 10000

def findMedian(arr):
  sortedArray = mergeSort(arr)
  medianIndex = (len(sortedArray)-1)//2
  return sortedArray[medianIndex]


#  If the size of the list is 0 or 1, return.
# Otherwise, separate the list into two lists of equal or nearly
# equal size and recursively sort the first and second halves
# separately.
# Finally, merge the two sorted halves into one sorted list.
def mergeSort(array):
  if len(array) <= 1:
    return array
  
  midIndex = len(array)//2
  leftHalf = array[:midIndex]
  rightHalf = array[midIndex:]
  
  leftSorted = mergeSort(leftHalf)
  rightSorted = mergeSort(rightHalf)
  
  return merge(leftSorted, rightSorted)

def merge(left, right):
  i=j=0
  mergedArray = []
  while i < len(left) and j < len(right):
    currentLeft = left[i]
    currentRight = right[j]
    
    if currentLeft < currentRight: 
      mergedArray.append(currentLeft)
      i+=1
    else:
      mergedArray.append(currentRight)
      j+=1
  
  mergedArray.extend(left[i:])
  mergedArray.extend(right[j:])
  return mergedArray
  
  

if __name__ == '__main__':
  array = [0,1,2,4,6,5,3]
  median = findMedian(array)
  print(median)
  