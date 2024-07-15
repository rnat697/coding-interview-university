# Given the time in numerals we may convert it into words, as shown below:
# ```
# 5:00 --> five o' clock
# 5:01 --> one minute past five
# 5:10 --> ten minutes past five
# 5:15 --> quarter past five
# 5:28 --> twenty eight minutes past five
# 5:30 --> half past five
# 5:40 --> twenty minutes to six
# 5:45 --> quarter to six
# 5:47 --> thirteen minutes to six
# ```
# At `minutes = 0`, use *o' clock*. For `1 ≤ minutes ≤ 30`, use *past*, 
# and for `30 < minutes` use *to*. Note the space between the apostrophe 
# and *clock* in *o' clock*. Write a program which prints the time in words 
# for the input given in the format described.

# **Function Description**
# Complete the *timeInWords* function in the editor below.
# timeInWords has the following parameter(s):
# - *int h:* the hour of the day
# - *int m:* the minutes after the hour
# **Returns**
# - *string:* a time string as described
# **Input Format**
# The first line contains h, the hours portion The second line contains m, the minutes portion

# **Constraints**
# - 1 ≤ h ≤ 12
# - 0 ≤ m < 60

# O(1) since we're just accessing the element
# why is this medium level question, its ez just tedious
def timeInWords(h, m):
  timeWords = ["o' clock","one","two","three","four", "five", "six", "seven",
             "eight","nine", "ten", "eleven", "twelve","thirdteen", "fourteen",
             "quarter","sixteen", "seventeen", "eighteen", "nineteen", "twenty",
             "twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
             "twenty six", "twenty seven", "twenty eight","twenty nine", "half" ]
  timeSentence = ""
  upcomingMin = 0
  
  if m == 0:
    timeSentence = timeWords[h] + " " + timeWords[0]
  
  elif m >= 1 and m <= 30:
    timeSentence = timeWords[m] + " minutes past " + timeWords[h]
  else:
    upcomingMin = 60 - m
    timeSentence = timeWords[upcomingMin] + " minutes to " + timeWords[h+1]

  # Remove minutes from the string if its quarter past / quarter to
  if m == 15 or upcomingMin == 15 or m == 30:
    timeSentence = timeSentence.replace("minutes ", "")
  
  # Replace minutes with minute from the minute is 1
  if m == 1 or upcomingMin == 1:
    timeSentence = timeSentence.replace("minutes", "minute")
  
  return timeSentence



if __name__ == "__main__":
  hour = 5
  minute = 47
  time = timeInWords(hour,minute)
  print(f"Time: {time}, Expected: thirteen minutes to six")
  
  hour = 1
  minute = 1
  time = timeInWords(hour,minute)
  print(f"Time: {time}, Expected: one minute past one")
  
  hour = 5
  minute = 30
  time = timeInWords(hour,minute)
  print(f"Time: {time}, Expected: half past five")
  
  hour = 3
  minute = 00
  time = timeInWords(hour,minute)
  print(f"Time: {time}, Expected: three o' clock")
  
  hour = 7
  minute = 15
  time = timeInWords(hour,minute)
  print(f"Time: {time}, Expected: quarter past seven")