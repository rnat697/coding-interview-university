# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity.
# If the amount spent by a client on a particular day is *greater than or equal to* 2x the client's median
# spending for a trailing number of days, they send the client a notification about potential fraud. 
# The bank doesn't send the client any notifications until they have at least that trailing number of 
# prior days' transaction data.
# Given the number of trailing days d and a client's total daily expenditures for a period of n days, 
# determine the number of times the client will receive a notification over all n days.

# **Example**
# expenditure = [10,20,30,40,50]
# d = 3
# On the first three days, they just collect spending data. At day **4**, trailing expenditures are 
# [10,20,30]. The median is 20 and the days expenditure is 40. Because 40 >= 2 x 20, there will be a notice.
# The next day, trailing expenditures are [20,30,40] and the expenditures are 50. This is less than 2 x 30 so no 
# notice will be sent. Over the period, there was one notice sent.

# Note: The median of a list of numbers can be found by first sorting the numbers ascending. If there is an odd number 
# of values, the middle one is picked. If there is an even number of values, the median is then defined to be the 
# average of the two values.

# **Function Description**
# Complete the function *activityNotifications* in the editor below.
# activityNotifications has the following parameter(s):
# - *int expenditure[n]:* daily expenditures
# - *int d*: the lookback days for median spending

# **Returns**
# - *int:* the number of notices sent

# **Input Format**
# The first line contains two space-separated integers n and d, the number of days of transaction data, 
# and the number of trailing days' data used to calculate median spending respectively.
# The second line contains n space-separated non-negative integers where each integer i denotes expenditure[i].

# **Constraints**
# - 1≤ n≤ 2*10^5
# - 1 ≤ d ≤ n
# - 0 ≤ expenditure[i] ≤200

# My non-optimal implementation - too frequent sorting, 
# Sorting the list for each day where a notification check is required results in a time complexity of O(d log d) where 
# d is the length of the trailing days. Since this sorting happens for each day after the initial 
# d days, it leads to a total complexity of O((n-d) . d log d)
def activityNotifications(expenditure:list, d:int):
  numNotifs = 0
  trailingExpediture = []
 
  for i in range(0, len(expenditure)):
     # Collect trailing expenses
    if i < d:
      trailingExpediture.append(expenditure[i])
    elif i > d:
      trailingExpediture.pop(0)
      trailingExpediture.append(expenditure[i-1])
    
    # sort trailing expenses and find median only after trailing period
    if(i >=d):
      medianCost = findMedian(trailingExpediture)
      
      # calculate if there is a notice or not
      currentCost = expenditure[i]
      print(f"median cost: {medianCost}, current cost: {currentCost}, >=: {2*medianCost}")
      if(currentCost >= (2*medianCost)):
        numNotifs += 1
    
  return numNotifs
    
  
def findMedian(array:list):
  sortedTrailing = array.copy()
  sortedTrailing.sort()
  print(sortedTrailing)
  
  length = len(sortedTrailing)
  medianIndex = round((length/2))-1
  # if even then find average of two median values
  if(length % 2 == 0):
    median1 = sortedTrailing[medianIndex]
    median2 = sortedTrailing[medianIndex+1]
    return (median1 + median2)/2
  else:
    return sortedTrailing[medianIndex]
    
# ---- Implementation from discussions using frequency table. -------
# Complexity of O(n)
def activityNotificationsOptimal(expenditure, d):
  freq = {}
  notify = 0
  
  def findMedian(middleIndex):
    freqTotal = 0 # keeps track of total occurances of expenditures (ie how many times each cost has been seen)
    # Goes through the entire range from 0 to 200 based from the constraints
    for expendiatureValue in range(201): 
      if expendiatureValue in freq:
        # if the value exists in the frequency table, increase the occurance total by its value in the freq table
        freqTotal = freqTotal + freq[expendiatureValue]
        # print(f"Frequency Total: {freqTotal}, middle Index: {middleIndex}, expenditure: {expendiatureValue}")
        
        # Check if the cumulative occurrence count meets or exceeds the target index.
        # If true, return the current expenditure value as it represents the median.
        if freqTotal >= middleIndex:
          return expendiatureValue
            
            
  for i in range(len(expenditure)-1):
    cost = expenditure[i]
    # Populate frequency table with trailing expenditures
    if cost in freq:
      freq[cost]+=1
    else:
      freq[cost]=1
    # print(f"i: {i},val: {cost}, freq: {freq}")
    
    # when trailing period has finished, start calculating median and find notifications
    if i >= d - 1:
      
      # calculating median
      if d % 2 == 0:
        firstIndex = d//2
        secondIndex = d//2+1
        # When length of array is even take the average of two medians
        median = (findMedian(firstIndex)+findMedian(secondIndex))/2
      else:
        index = d/2
        median = findMedian(index)
      # print("median: ",median)
      
      # Check if current day's expenditure triggers a notification
      currentExpenditure = expenditure[i+1]
      if currentExpenditure >= (median*2) :
        notify += 1
        # print("notify: ",notify)
      
      # remove the head element from dictionary
      headIndex = i - d + 1
      head = expenditure[headIndex]
      freq[head]-=1

  return notify 
  
  
  
  
  

if __name__ == "__main__":
  expenditure = [10,20,30,40,50]
  days = 3
  notices = activityNotifications(expenditure, days)
  print(f"Number of notifications: {notices}, Expected: 1")
  
  expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
  days = 5
  notices = activityNotifications(expenditure, days)
  print(f"Number of notifications: {notices}, Expected: 2")
  
  expenditure = [1, 2, 3, 4, 4]
  days = 4
  notices = activityNotifications(expenditure, days)
  print(f"Number of notifications: {notices}, Expected: 0")
  