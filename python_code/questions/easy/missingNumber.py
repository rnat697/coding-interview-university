# Given two arrays of integers, find which elements in the second array are missing from the first array.
# **Example**
# `arr = [7,2,5,3,5,3]` 
# `brr = [7,2,5,4,6,3,5,3]`
# The `brr` array is the original list. The numbers missing are `[4,6]`.

# **Notes**
# - If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. 
#   If that is not the case, then it is also a missing number.
# - Return the missing numbers sorted ascending.
# - Only include a missing number once, even if it is missing multiple times.
# - The difference between the maximum and minimum numbers in the original list is less than or equal to 100.

# **Function Description**
# Complete the *missingNumbers* function in the editor below. It should return a sorted array of missing numbers.
# missingNumbers has the following parameter(s):
# - *int arr[n]:* the array with missing numbers
# - *int brr[m]:* the original array of numbers
# **Returns**
# - *int[]:* an array of integers

# **Constraints**
# - 1 ≤ n, m ≤ 2x10^5
# - n ≤ m
# - 1 ≤ `brr[i]` ≤ 10^4
# - max(brr) - min(brr) ≤ 100

# My implementation - Total complexity O(m * n) because of the loop is comparing between two different array lengths 
# (counts elements in 'arr' for each unique element in 'brr'.) - also because .count is another for loop
#  but also O(n log n) because of sorting - negligble compared to O(m *n)
def missingNumbers(arr:list, brr:list):
  freqOriginal = {} # frequency of numbers in brr array
  missing = []
  
  # store frequency of numbers of the original brr array
  for i in range(0, len(brr)):
    elementB = brr[i]
    if elementB in freqOriginal:
      freqOriginal[elementB] += 1
    else:
      freqOriginal[elementB]  = 1
  
  for number, originFreq in freqOriginal.items():
    otherFreq = arr.count(number) # NOTE: this is another for loop
    # if arr's freqyency is smaller than brr's frequency then we found a missing number
    if originFreq > otherFreq:
      missing.append(number)
  
  missing.sort()
  return missing

# more optimal way: O(m + n) - bruh this was the first way i was thinking but i was like nah thats not optimal right??
# but nooooooooooo its optimal
def missingNumbersOptimal(arr:list, brr:list):
  freqOriginal = {} # frequency of numbers in brr array
  freqSecond = {}
  missing = []
  
  # store frequency of numbers of the original brr array
  for i in range(0, len(brr)): # O(m)
    elementB = brr[i]
    if elementB in freqOriginal:
      freqOriginal[elementB] += 1
    else:
      freqOriginal[elementB]  = 1
  
  # store frequency of numbers of the arr array
  for i in range(0, len(arr)): # O(n)
    elementA = arr[i]
    if elementA in freqSecond:
      freqSecond[elementA] += 1
    else:
      freqSecond[elementA]  = 1
  
  for number, originFreq in freqOriginal.items(): # # O(m)
    # We find missing number by checking if number is not in the second freq array OR 
    # the frequency of that number in the second array is less than the original
    if number not in freqSecond or freqSecond[number] < originFreq:
      missing.append(number)
  
  missing.sort() # O (n log n)
  return missing
  # O(m) + O(n) + O(m) + O(n log n)
  # O(2m) + O(n) + O(n log n) 
  # O(m + n) + O(n log n) < -- drop the 2 since we don't care about constants
  # O(m + n) < -- drop O(n log n) since its lesser than O(m + n) and we care about worst case execution
  
  

if __name__ == "__main__":
  arr = [7,2,5,3,5,3]
  brr = [7,2,5,4,6,3,5,3]
  missingNums = missingNumbers(arr, brr)
  print(f"missing numbers: {missingNums}, expected: [4,6]")