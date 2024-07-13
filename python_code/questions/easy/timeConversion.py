# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: 
# - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# **Example**
# - Return '12:01:00'.
# - Return '00:01:00'.

# **Function Description**
# Complete the `*timeConversion*` function in the editor below. 
# It should return a new string representing the input time in 24 hour format.
# `timeConversion` has the following parameter(s):
# - *string s*: a time in  hour format

# **Returns**
# - *string*: the time in  hour format

# **Input Format**
# A single string  that represents a time in -hour clock format (i.e.:  or ).

# **Constraints**
# - All input times are valid

def timeConversion(s:str):
  times = s.split(":")
  hoursString = times[0]
  hours = int(times[0])
  mins = times[1]
  seconds = times[2]
  period = seconds[2:] # takes last two in the seconds string since it indicates AM/PM
  seconds = seconds[:2]
  
  if(period == "AM" and hours == 12):
    hoursString = "00"
  elif(period == "PM" and hours < 12):
    hours += 12
    hoursString = str(hours)
    
  return hoursString + ":"+ mins + ":" + seconds

# Can also do this
def timeConversionSimplier(s):
  hour = int(s[:2])
  period = s[-2:]
  if period == 'PM' and hour != 12:
    hour += 12
  elif period == 'AM' and hour == 12:
   hour = 0  
  hour = f"{hour:02}"
  return f"{hour}{s[2:8]}"
    
      
  
  
if __name__ == "__main__":
  time = "07:05:45PM"
  converted = timeConversion(time)
  print(converted)
  
  time = "12:05:45AM"
  converted = timeConversion(time)
  print(converted)
  
  time = "03:05:45AM"
  converted = timeConversion(time)
  print(converted)