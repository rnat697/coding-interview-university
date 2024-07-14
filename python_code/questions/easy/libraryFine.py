# Your local library needs your help! Given the expected and actual return dates for a library book, 
# create a program that calculates the fine (if any). The fee structure is as follows:
# 1. If the book is returned on or before the expected return date,
#    no fine will be charged (i.e.: `fine = 0`.)
# 2. If the book is returned after the expected return *day* but still within
#    the same calendar month and year as the expected return date, 
#    `fine = 15 Hackos * (the number of days late)`.
# 3. If the book is returned after the expected return *month* but still within the 
#    same calendar year as the expected return date, the 
#    `fine = 500 Hackos * (the number of months late)`.
# 4. If the book is returned after the calendar *year* in which it was expected, 
#    there is a fixed fine of `10000 Hackos`.
# Charges are based only on the least precise measure of lateness. For example, 
# whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, 
# that is a year late and the fine would be `10,000 Hackos`.

# **Example**
# `d1,m1,y1 = 14,7,2018`
# `d2,m2,y2 = 5,7,2018`
# The first values are the return date and the second are the due date. 
# The years are the same and the months are the same. 
# The book is `14-5=9` days late. Return `9*15 = 135`.

# **Function Description**
# Complete the *libraryFine* function in the editor below.
# libraryFine has the following parameter(s):
# - *d1, m1, y1*: returned date day, month and year, each an integer
# - *d2, m2, y2*: due date day, month and year, each an integer

# **Returns**
# - *int:* the amount of the fine or  if there is none
# **Input Format**
# The first line contains 3 space-separated integers, `d1,m1,y1` denoting the respective 
# day, month, year on which the book was returned.
# The second line contains 3 space-separated integers, `d1,m1,y1`, denoting the respective 
# day, month, and year on which the book was due to be returned.

# **Constraints**
# - 1 ≤ d1,d2 <31
# - 1 ≤ m1,m2 <12
# - 1 ≤ y1,y2 = 3000
# - It is guaranteed that the dates will be valid Gregorian calendar dates.


#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
  YEAR_FINE = 10000
  MONTH_FINE = 500
  DAY_FINE = 15
  NO_FINE = 0
  
  if(y1<y2 or (y1==y2 and m1 < m2) or (y1==y2 and m1 == m2 and d1<=d2)):
    return NO_FINE
  
  if(y1 > y2):
    return YEAR_FINE
  else:
    if(m1 > m2):
      monthsLate = m1 - m2
      return MONTH_FINE * monthsLate
    else:
      if(d1 > d2):
        daysLate = d1 - d2
        return DAY_FINE * daysLate

def libraryFineSimplier(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 == y2 and m1 > m2:
        return 500 * (m1 - m2)
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return 15 * (d1 - d2)
    else:
        return 0

if __name__ == '__main__':
  # returned 14/7/2018, due 5/7/2018
  fine = libraryFine(14,7,2018,5,7,2018)
  print(fine)
  
  # returned 9/6/2015, due 6/6/2015
  fine = libraryFine(9,6,2015,6,6,2015)
  print(fine)
  
   # returned 1/1/2018, due 31/12/2017
  fine = libraryFine(1,1,2018,31,12,2017)
  print(fine)
  
  # returned 2/7/1014, due 1/1/1015
  fine = libraryFine(2,7,1014,1,1,1015)
  print(fine)
  
    # returned 2/7/2015, due 1/2/2014
  fine = libraryFine(2,7,2015,1,2,2014)
  print(fine)
  