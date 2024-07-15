# Lauren has a chart of distinct projected prices for a house over the next several years.
# She must buy the house in one year and sell it in another, and she must do so at a loss. 
# She wants to minimize her financial loss.

# **Example**
# `price = [20,15,8,2,12]`
# Her minimum loss is incurred by purchasing in year `2` at `price[1] = 15` and 
# reselling in year `5` at `price[4] = 12`. Return `15 - 12 = 3`.

# **Function Description**
# Complete the *minimumLoss* function in the editor below.
# minimumLoss has the following parameter(s):
# - *int price[n]:* home prices at each year
# **Returns**
# - *int:* the minimum loss possible

# **Input Format**
# The first line contains an integer n, the number of years of house data.
# The second line contains n space-separated long integers that describe each `price[i]` .

# **Constraints**
# - 2 ≤ n ≤ 2x10^8
# - 1 ≤ price[i] ≤ 10^16
# - All the prices are distinct.
# - A valid answer exists.

# **Subtasks**
# - 2≤ n≤ 1000 for 50% of the maximum score.

# My Implementation - Using brute force - O(n^2) complexity but times out for larger arrays
# 11 tests/ 16 passed
def minimumLoss(price:list):
  minLoss = 99999999999999999
  
  for i in range(0, len(price)):
    buyingCost = price[i]
    
    for j in range(i+1, len(price)):
      sellingCost = price[j]
      currentLoss = buyingCost - sellingCost
      # print(f"price i: {buyingCost}, price j: {sellingCost}, current Loss: {currentLoss}")
      # assume negatives mean profits and we don't count profit since we're looking for losses
      # also asumes 0 is a profit
      if currentLoss > 0 and currentLoss < minLoss:
        minLoss = currentLoss
  
  return minLoss


# ------- Optimal solution from a user in discussions -----
# Compelxity: O(n log n) because sorting algorithm
# Approach:
# - Sort the prices in descending order along with their original indices to keep track of the order of years.
# - Iterate through the sorted list and compare each price with the next one to find valid buy-sell pairs.
# - Calculate the loss when a valid pair (buying year < selling year) is found and update the minimum loss.
# - Return the minimum loss found.

# Explanation:
# - Sorting the prices in descending order helps in identifying the maximum possible selling price 
#   that comes after a given buying price, ensuring a valid transaction.
# - We iterate through the sorted list and compare each price with the next one to check if it's a valid 
#   buy-sell pair (buying year < selling year).
# - By keeping track of the original indices, we ensure that we only consider transactions where buying 
#   happens before selling, as required.
# - Using the min() function helps to efficiently find the smallest loss among all valid transactions.

def minimumLossOptimal(price:list):
  minLoss = 10**16
  # Creating a list of indicies in sorted descending order 
  # i.e: price = [5,10,3] --> indices = [0,1,2] --> sortedIndicies = [1,0,2]
  # range(len(prices)) creates a list of indices [0, 1, 2, ..., len(prices)-1].
  # key=lambda x: prices[x] specifies that sorting should be based on the values in prices at each index x.
  sortedIndices = sorted(range(len(price)), key=lambda x: price[x], reverse=True)

  # Iterate through sorted indices to find minimum loss
  for i in range(len(sortedIndices)-1):
    currentSortedIndex = sortedIndices[i]
    nextSortedIndex = sortedIndices[i+1]
    
    # i.e: sortedIndicies = [1,0,2] --> current = 1, next = 0 --> skip
    # next iteration --> current = 0, next = 2 --> go in if
    if currentSortedIndex < nextSortedIndex:
      # Get original value from orignal array using the indicies we found
      buyingPrice = price[currentSortedIndex]
      sellingPrice = price[nextSortedIndex]
      
      # Calculate loss
      loss = buyingPrice - sellingPrice
      
      # Update min_loss if current loss is smaller
      minLoss = min(minLoss, loss)
  
  return minLoss
      


if __name__ == "__main__":
  # price = [20,15,8,2,12]
  # loss = minimumLoss(price)
  # print(f"loss: {loss}, expected: 3")
  
  # price = [5,10,3]
  # loss = minimumLoss(price)
  # print(f"loss: {loss}, expected: 2")
  
  # price = [20,7,8,2,5]
  # loss = minimumLoss(price)
  # print(f"loss: {loss}, expected: 2")
  
  price = [20,15,8,2,12]
  loss = minimumLossOptimal(price)
  print(f"loss: {loss}, expected: 3")
  
  price = [5,10,3]
  loss = minimumLossOptimal(price)
  print(f"loss: {loss}, expected: 2")
  
  price = [20,7,8,2,5]
  loss = minimumLossOptimal(price)
  print(f"loss: {loss}, expected: 2")
  