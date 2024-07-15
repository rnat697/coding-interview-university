# Two friends like to pool their money and go to the ice cream parlor. 
# They always choose two distinct flavors and they spend all of their money.
# Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

# **Example**. `m = 6 cost = [1, 3,  4, 5, 6]`
# The two flavors that cost 1 and 5 meet the criteria. Using 1-based indexing, they are at indices 1 and 4.

# **Function Description**
# Complete the *icecreamParlor* function in the editor below.
# icecreamParlor has the following parameter(s):
# - *int m:* the amount of money they have to spend
# - *int cost[n]:* the cost of each flavor of ice cream
# **Returns**
# - *int[2]:* the indices of the prices of the two flavors they buy, sorted ascending

# **Input Format**
# The first line contains an integer, t, the number of trips to the ice cream parlor. 
# The next t sets of lines each describe a visit.
# Each trip is described as follows:
# 1. The integer m, the amount of money they have pooled.
# 2. The integer n, the number of flavors offered at the time.
# 3. n space-separated integers denoting the cost of each flavor: `cost[cost[1], cost[2],…,cost[n]]`.
# **Note**: The index within the cost array represents the flavor of the ice cream purchased.

# **Constraints**
# - 1 ≤ t ≤ 50
# - 2 ≤ m < 10^4
# - 2 ≤ n ≤ 10^4
# - 1≤ cost[i] ≤ 10^4, ∀ i e [1,n]
# - There will always be a unique solution.

# O(n) time complexity
def icecreamParlor(m:int, arr:list):
  cost_indexes = {}  # Dictionary to store the indices of the costs
  
  for i in range(0, len(arr)):
    # calculate the complement of the cost e.g if m = 6, and arr[0] = 1, 6-1 = 5
    complement = m - arr[i]
    
    # check if complement is already in the dictionary, if it is, return the index values
    if complement in cost_indexes:
      return [cost_indexes[complement]+1, i+1]

    # otherwise continue to add to dictionary
    cost_indexes[arr[i]] = i
    
  
def icecreamParlorMine(m, arr):
  # assumes array is already sorted... but like its not sorted at all...
  # even if we had another array to store the sorted version it would take O(n log n) coz sorting algorithms
    # take the min value
  minValue = arr[0]
  # compare all others with that value
  for i in range(1, len(arr)):
    combineCost = minValue + arr[i]
    if(combineCost == m):
      
      return [1,i+1]
   
  
  
if __name__ == "__main__":
  money = 6
  costs = [1,3,4,5,6]
  indexes = icecreamParlor(money,costs)
  print(f"Indexes: {indexes}, expected: [1, 4]")
  
  costs = [1, 4, 5, 3, 2]
  money = 4
  indexes = icecreamParlor(money,costs)
  print(f"Indexes: {indexes}, expected: [1, 4]")
  
  costs = [2, 2,4, 3]
  money = 4
  indexes = icecreamParlor(money,costs)
  print(f"Indexes: {indexes}, expected: [1, 2]")