# ---- Complexity/Performance ----
# Time Complexity: best case = O(n) when array is already sorted, 
# worst-case & average = O(n^2)

# Space Complexity: O(1)

# Similar to sorting cards on our hand. Assume first card is already sorted
# ---- Algorithm Pseudocode ----
# function INSERTIONSORT(list a[0 ··· n - 1])
#   for i=1 to n - 1 do
#   j=i - 1
#   while a[j] > a[j + 1] and j >= 0 do
#     SWAP(a, j, j + 1)
#     j=j - 1
#   return a
def insertionSortUOA(array):
  # assume first element is sorted already so we start at 1
  for i in range(1, len(array)):
    # Initialize j to the index of the element just before the current element i
    j = i-1
    while j >= 0 and array[j] > array[j+1]:
      # swap array[j] and array[j+1]
      array[j],array[j+1] = array[j+1],array[j]
      j = j-1
  return array

# PROGRAMIZ PSEUDOCODE
#insertionSort(array)
#   mark first element as sorted
#   for each unsorted element X
#     'extract' the element X
#     for j <- lastSortedIndex down to 0
#       if current element j > X
#         move sorted element to the right by 1
#     break loop and insert X here
# end insertionSort
def insertionSortProgramiz(array):
  for step in range(1, len(array)):
    key = array[step]
    j = step - 1
    
    # Compare key with each element on the left of it until an element smaller than it is found
    while j >= 0 and key < array[j]:
      array[j + 1] = array[j]  # Shift larger elements one position to the right
      j = j - 1
    
    # Place key after the element just smaller than it
    array[j + 1] = key


if __name__ == "__main__":
  print("---UOA Leccy version---")
  unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
  print("Unsorted Array: ", unsortedArr)
  sortedArray = insertionSortUOA(unsortedArr)
  print("Sorted array:", sortedArray)
  
  print("---Programiz version---")
  unsorted = [9, 5, 1, 4, 3]
  print("Unsorted Array: ", unsorted)
  insertionSortProgramiz(unsorted)
  print("Sorted array:", unsorted)