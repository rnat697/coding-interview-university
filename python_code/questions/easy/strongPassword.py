# Louise joined a social networking site to stay in touch with her friends. 
# The signup page required her to input a *name* and a *password*. However, the password must be *strong*. 
# The website considers a password to be *strong* if it satisfies the following criteria:
# - Its length is at least 6.
# - It contains at least one digit.
# - It contains at least one lowercase English character.
# - It contains at least one uppercase English character.
# - It contains at least one special character. The special characters are: `!@#$%^&*()-+`
# She typed a random string of length n in the password field but wasn't sure if it was strong. 
# Given the string she typed, can you find the minimum number of characters she must add to make her password strong?
# *Note*: Here's the set of types of characters in a form you can paste in your solution:

# ```
# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"
# ```

# **Example**
# `password = '2bbbb'` 
# This password is 5 characters long and is missing an uppercase and a special character. 
# The minimum number of characters to add is 2.

# `password = '2bb#A'`
# This password is 5 characters long and has at least one of each character type. 
# The minimum number of characters to add is 1.

# **Function Description**
# Complete the *minimumNumber* function in the editor below.
# *minimumNumber* has the following parameters:
# - *int n:* the length of the password
# - *string password:* the password to test

# **Returns**
# - *int:* the minimum number of characters to add

# **Input Format**
# The first line contains an integer n, the length of the password.
# The second line contains the password string. Each character is either 
# a lowercase/uppercase English alphabet, a digit, or a special character.

# **Constraints**
# - 1 ≤ n ≤ 100
# - All characters in `password` are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+ ].
def minimumNumber(n:int, password:str):
  missingChars = 0
  numbers = "0123456789"
  lowercase = "abcdefghijklmnopqrstuvwxyz"
  uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  specialChar = "!@#$%^&*()-+"
  
  hasNumber = hasLower = hasUpper = hasSpecial = False
  
  for char in password:
    if char in numbers:
      hasNumber = True
    elif char in lowercase:
      hasLower = True
    elif char in uppercase:
      hasUpper = True
    elif char in specialChar:
      hasSpecial = True
    
  # calculate number of missing charaacters
  if not hasNumber:
    missingChars += 1
  if not hasLower:
    missingChars += 1
  if not hasUpper:
    missingChars += 1
  if not hasSpecial:
    missingChars += 1
  
  # Use max to ensure the password meets both length and character type requirements.
  # - missingChars: The number of additional characters needed to include all required character types.
  # - 6 - n: The number of characters needed to reach the minimum length of 6.
  # We take the maximum of these two values to cover both requirements.
  # if n is already 6 then we just use the missingChars. but if n is like really small, the length requirement takes presidence etc
  return max(missingChars, 6 - n)
  
  
  


if __name__ == "__main__":
  password = '2bbbb'
  length = 5
  minNum = minimumNumber(5, password)
  print(f"Minimum number: {minNum}, expected: 2")
  
  password = '2bb#A'
  length = 5
  minNum = minimumNumber(5, password)
  print(f"Minimum number: {minNum}, expected: 1")
  
  password = 'Ab1'
  length = 3
  minNum = minimumNumber(3, password)
  print(f"Minimum number: {minNum}, expected: 3")
  
  password = '#HackerRank'
  length = 11
  minNum = minimumNumber(11, password)
  print(f"Minimum number: {minNum}, expected: 1")