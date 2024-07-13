# You are in charge of the cake for a child's birthday. You have decided the cake will have one 
# candle for each year of their total age. They will only be able to blow out the tallest of the 
# candles. Count how many candles are tallest.

# **Example**
# `candles = [4,4,1,3]`
# The maximum height candles are 4 units high. There are 2 of them, so return 2.

# **Function Description**
# Complete the function `birthdayCakeCandles` in the editor below.
# birthdayCakeCandles has the following parameter(s):
# - *int candles[n]*: the candle heights

# **Returns**
# - *int*: the number of candles that are tallest

# **Input Format**
# The first line contains a single integer, n, the size of candles[].
# The second line contains n space-separated integers, where each integer i describes the height of candles[i].

# **Constraints**
# - 1 ≤ n < 10^5
# - 1 ≤ candles[i] ≤ 10^7
import math

# My implementation
def birthdayCakeCandles(candles):
  # find maximum height of cancdles and find the frequency of said candles
  maxHeight = 0
  for i in range(0, len(candles)):
    candleHeight = candles[i]
    if candleHeight > maxHeight:
      maxHeight = candleHeight
  
  # Python's lists have a builtin function called count so I don't need a frequency hashmap
  return candles.count(maxHeight)

# Other ppl's
def birthdayCakeCandlesReversed(candles):
  # To get maxHeight can also do candles.sort(reverse=True) and take candles[0] as max
  candles.sort(reverse=True)
  maxHeight = candles[0]
  return candles.count(maxHeight)
  
if __name__ == "__main__":
  arr = [3,2,1,3]
  max = birthdayCakeCandles(arr)
  print(max)
  print(birthdayCakeCandlesReversed(arr))