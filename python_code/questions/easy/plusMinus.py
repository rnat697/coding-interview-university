# Given an array of integers, calculate the ratios of its elements that are *positive*, 
# *negative*, and *zero*. Print the decimal value of each fraction on a new line with  
# places after the decimal.

# **Note:** This challenge introduces precision problems. The test cases are scaled to six decimal places, 
# though answers with absolute error of up to  are acceptable.

# **Function Description**
# Complete the *plusMinus* function in the editor below.
# plusMinus has the following parameter(s):
# - *int arr[n]*: an array of integers
# **Print**
# Print the ratios of positive, negative and zero values in the array. 
# Each value should be printed on a separate line with  digits after the decimal. 
# The function should not return a value.

# **Input Format**
# The first line contains an integer, , the size of the array.
# The second line contains  space-separated integers that describe arr[n].

# **Output Format**
# **Print** the following 3 lines, each to 6 decimals:
# 1. proportion of positive values
# 2. proportion of negative values
# 3. proportion of zeros

import math

def plusMinus(arr):
  positives = 0
  negatives = 0 
  zeros = 0
  for i in range(0,len(arr)):
    number = arr[i]
    
    if(number == 0):
      zeros += 1
    elif(number > 0):
      positives += 1
    else:
      negatives += 1
  
  positiveRatio = format(positives/len(arr), ".6f")
  negativesRatio = format(negatives/len(arr), ".6f")
  zerosRatio = format(zeros/len(arr), ".6f")
  
  print(positiveRatio)
  print(negativesRatio)
  print(zerosRatio)
  
if __name__ == "__main__":
  array = [-4, 3, -9, 0, 4, 1]
  plusMinus(array)