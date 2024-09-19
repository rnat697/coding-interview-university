// Louise joined a social networking site to stay in touch with her friends.
// The signup page required her to input a *name* and a *password*. However, the password must be *strong*.
// The website considers a password to be *strong* if it satisfies the following criteria:
// - Its length is at least 6.
// - It contains at least one digit.
// - It contains at least one lowercase English character.
// - It contains at least one uppercase English character.
// - It contains at least one special character. The special characters are: `!@#$%^&*()-+`
// She typed a random string of length n in the password field but wasn't sure if it was strong.
// Given the string she typed, can you find the minimum number of characters she must add to make her password strong?
// *Note*: Here's the set of types of characters in a form you can paste in your solution:

// ```
// numbers = "0123456789"
// lower_case = "abcdefghijklmnopqrstuvwxyz"
// upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
// special_characters = "!@#$%^&*()-+"
// ```

// **Example**
// `password = '2bbbb'`
// This password is 5 characters long and is missing an uppercase and a special character.
// The minimum number of characters to add is 2.

// `password = '2bb#A'`
// This password is 5 characters long and has at least one of each character type.
// The minimum number of characters to add is 1.

// **Function Description**
// Complete the *minimumNumber* function in the editor below.
// *minimumNumber* has the following parameters:
// - *int n:* the length of the password
// - *string password:* the password to test

// **Returns**
// - *int:* the minimum number of characters to add

// **Input Format**
// The first line contains an integer n, the length of the password.
// The second line contains the password string. Each character is either
// a lowercase/uppercase English alphabet, a digit, or a special character.

// **Constraints**
// - 1 ≤ n ≤ 100
// - All characters in `password` are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+ ].

/*
 * Complete the 'minimumNumber' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. STRING password
 */

// O(n)
function minimumNumber(n, password) {
  // Return the minimum number of characters to make the password strong

  const numbers = "0123456789";
  const lower_case = "abcdefghijklmnopqrstuvwxyz";
  const upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const special_characters = "!@#$%^&*()-+";

  let hasDigit,
    hasLower,
    hasUpper,
    hasSpecial = false;

  let additions = 0;
  // [...variable] --> spread function turns it into array basically a split() when used for strings, when used with arrays just shallow copy
  [...password].forEach((char) => {
    if (numbers.includes(char)) {
      hasDigit = true;
    } else if (lower_case.includes(char)) {
      hasLower = true;
    } else if (upper_case.includes(char)) {
      hasUpper = true;
    } else if (special_characters.includes(char)) {
      hasSpecial = true;
    }
  });

  if (!hasDigit) additions++;
  if (!hasLower) additions++;
  if (!hasUpper) additions++;
  if (!hasSpecial) additions++;

  return Math.max(additions, 6 - n);
}
// regex version
function minimumNumberRegex(n, password) {
  // Define regex patterns for required character types
  const hasDigit = password.match(/[0-9]/);
  const hasLower = password.match(/[a-z]/);
  const hasUpper = password.match(/[A-Z]/);
  const hasSpecial = password.match(/[!@#$%^&*()\-+]/);

  let additions = 0;

  // Check if each type is missing
  if (!hasDigit) additions++;
  if (!hasLower) additions++;
  if (!hasUpper) additions++;
  if (!hasSpecial) additions++;

  // Return the maximum of additions needed or the difference from 6
  return Math.max(additions, 6 - n);
}

let password1 = "2bbbb";
let result1 = minimumNumber(password1.length, password1);
console.log(result1);
console.log("EXPECTED: 2");

let password2 = "2bb#A";
let result2 = minimumNumber(password2.length, password2);
console.log(result2);
console.log("EXPECTED: 1");
