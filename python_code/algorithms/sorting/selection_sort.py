# ---- Complexity/Performance ----
# Time Complexity: O(n^2) for all cases bc of two nested loops

# Space Complexity: O(1)

# Divide and Conquer algorithm
# ---- Algorithm Pseudocode ----
# selectionSort(array, size)
#   repeat (size - 1) times
#   set the first unsorted element as the minimum
#   for each of the unsorted elements
#     if element < currentMinimum
#       set element as new minimum
#   swap minimum with first unsorted position
# end selectionSort

def selectionSort(array):
  for index in range(len(array)):
    minIndex = index
    
    for j in range(index + 1, len(array)):
      currentElement = array[j]
      if currentElement < array[minIndex]:
        minIndex = j
    
    # swapping elements to sort the array
    array[index], array[minIndex] = array[minIndex], array[index]
  return array
    


  
if __name__ == "__main__":
  unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
  print("Unsorted Array: ", unsortedArr)
  sortedArr = selectionSort(unsortedArr)
  print("Sorted array:", sortedArr)