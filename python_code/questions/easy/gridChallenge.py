# Given a square grid of characters in the range ascii[a-z], 
# rearrange elements of each row alphabetically, ascending. 
# Determine if the columns are also in ascending alphabetical order, 
# top to bottom. Return `YES` if they are or `NO` if they are not.

# Example
# grid = [’abc’, ‘ade’, ‘efg’]
# ```
# a b c
# a d e
# e f g
# ```
# The rows are already in alphabetical order. 
# The columns `a a e`, `b d f` and `c e g` are also in alphabetical order, 
# so the answer would be `YES`. Only elements within the same row can be rearranged. 
# They cannot be moved to a different row.

# **Function Description**
# Complete the *gridChallenge* function in the editor below.
# gridChallenge has the following parameter(s):
# - *string grid[n]:* an array of strings
# **Returns**
# - *string:* either `YES` or `NO`

# **Input Format**
# The first line contains t, the number of testcases.
# Each of the next t sets of lines are described as follows:
# - The first line contains n, the number of rows and columns in the grid.
# - The next n lines contains a string of length

# **Constraints**
# - 1≤ t ≤ 100
# - 1 ≤ n ≤ 100
# - *Each string consists of lowercase letters in the range ascii[a-z]*

# **Output format**
# For each test case, on a separate line print `YES` if it is possible to 
# rearrange the grid alphabetically ascending in both its rows and columns, 
# or `NO` otherwise.

# O(n * m) because of uneven for loop
def gridChallenge(grid:list):
  # sort each string alphabetically
  for i in range(0, len(grid)):
    word = grid[i]
    sortedWord = sorted(word)
    grid[i] = sortedWord
    
    
  # determine if columns are in alphabetical order
  for row in range(0, len(grid)-1):
    currentRow = grid[row]
    nextRow = grid[row + 1]
    
    for column in range(0, len(currentRow)):
      currentChar = currentRow[column]
      nextChar = nextRow[column]
      
      # if current letter is further along the alphabet than next letter, its not alphabetical then
      if(currentChar > nextChar):
        return "NO"
      
  return "YES"
        
      
  


if __name__ == "__main__":
  grid = ["abc", "ade", "efg"]
  result = gridChallenge(grid)
  print(f"Result: {result}, expected: YES")
  
  grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
  result = gridChallenge(grid)
  print(f"Result: {result}, expected: YES")
  
  grid = ['ebacd', 'fghij', 'trpqs', 'olmkn','xywuv']
  result = gridChallenge(grid)
  print(f"Result: {result}, expected: NO")
  
  