# ---- Complexity/Performance ----
# Time Complexity: O(n log n) because of while loops [O(n)] and division steps [O(logn)]
# --> Dividing the Array: Achieves O(log n) due to halving.
# --> Merging Subarrays: Achieves O(n) due to linear merging of elements.

# Space Complexity: O(n) not sure why

# Divide and Conquer algorithm
# ---- Algorithm Pseudocode ----
# If the size of the list is 0 or 1, return.
# Otherwise, separate the list into two lists of equal or nearly
# equal size and recursively sort the first and second halves
# separately.
# Finally, merge the two sorted halves into one sorted list.

def mergeSort(array):
  # if length of the array is 1 or less then just return the array
  if len(array) <= 1:
    return array
  #   Otherwise, separate the list into two lists of equal or nearly
  #   equal size and recursively sort the first and second halves
  #   separately.
  midIndex = len(array)//2 # floor division
  leftHalf = array[:midIndex] # take everything up to mid point
  rightHalf =  array[midIndex:] # take everything after mid point
  
  # sort left and right halfs
  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)
  
  # Finally, merge the two sorted halves into one sorted list 
  return merge(sortedLeft, sortedRight)
  
  
def merge(leftArray, rightArray):
  i=j = 0
  mergedArray = []
  while i < len(leftArray) and j < len(rightArray):
    # find current item in the left and right arrays
    currentLeft = leftArray[i]
    currentRight = rightArray[j]
    
    # compare elements from both subarrays
    if(currentLeft < currentRight):
      mergedArray.append(currentLeft)
      i+=1
    else:
      mergedArray.append(currentRight)
      j+=1
  
  #  append any remaining elements from the left and right arrays
  mergedArray.extend(leftArray[i:])
  mergedArray.extend(rightArray[j:])
  
  return mergedArray
      

  
if __name__ == "__main__":
  unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
  print("Unsorted Array: ", unsortedArr)
  sortedArr = mergeSort(unsortedArr)
  print("Sorted array:", sortedArr)