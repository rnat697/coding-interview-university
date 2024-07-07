# ---- Complexity/Performance ----
# Time complexity: O(n log n) for average/best case, O(n^2) worst case
#  - Divide Step: Partitioning the array takes O(n) time.
#  - Conquer Step: Quicksort is recursively called on each partition.
#    In the average and best case, each level of recursion divides the array into two roughly equal parts, resulting in O(log n) levels of recursion.
#    Each level of recursion requires O(n) work to partition the array.
#
# Space complexity: O(logn) for the stack space needed for recursion

# Divide and conquer algorithm with pivot
# ---- Algorithm Pseudocode ----
# If the size of the list is 0 or 1, return.
# Otherwise, choose one of the items in the list as a pivot and
# partition the list.
# Partition moves the items in the list into two disjoint sublists:
# all elements less than the pivot are placed in the left sublist
# and all elements greater than the pivot are placed in the right
# sublist.
# Recursively process the two sublists.

# ---- Two Way Partition Techiniques --- 
# 1. Lomuto’s Partitioning: Select the **last element** as the pivot. 
#   Then traverse the array and swap elements to ensure that elements 
#   less than the pivot come before elements greater than the pivot.
#
# 2. Hoare’s Partitioning: Select the **first element** as the pivot. 
#    Then do two scans of the array: one from the left end and one 
#    from the right end, swapping elements when necessary.

def quickSortTwoWay(array, startIndex, endIndex):
  # checks if subarray contains at least two elements
  if startIndex < endIndex:
    partitionPos = partition(array, startIndex, endIndex)
    quickSortTwoWay(array, startIndex, partitionPos-1)
    quickSortTwoWay(array, partitionPos+1, endIndex)

def partition(array, leftIndex,rightIndex):
  # using Lomuto's partitioning i.e. last element as pivot
  pivot = array[rightIndex]
  
  # pointer for the greater element
  partitionIndex = leftIndex -1
  
  for j in range(leftIndex, rightIndex):
    if array[j] <= pivot:
      partitionIndex +=1
      # swap the smaller element ith the greater element pointed by partitionIndex
      (array[partitionIndex], array[j]) = (array[j], array[partitionIndex])
    # swap the pivot element with greater element specified by partitionIndex
  (array[partitionIndex + 1], array[rightIndex]) = (array[rightIndex], array[partitionIndex + 1])
  return partitionIndex + 1 
      

# ---- Three Way Partition Techiniques --- 
# Good for arrays that are nearly sorted
  
  
  

if __name__ == "__main__":
  unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
  print("Unsorted Array: ", unsortedArr)
  sortedArr = quickSortTwoWay(unsortedArr,0, len(unsortedArr)-1)
  print("Sorted array:", unsortedArr)