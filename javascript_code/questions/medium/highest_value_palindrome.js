// Palindromes are strings that read the same from the left or right,
// for example *madam* or *0110*.

// You will be given a string representation of a number and a
// maximum number of changes you can make. Alter the string, one digit at a
// time, to create the string representation of the largest number possible
// given the limit to the number of changes. The length of the string may not be
// altered, so you must consider `0`'s left of all higher digits in your tests.
// For example `01101`  is valid,  `0011` is not.

// Given a string representing the starting number, and a maximum number
// of changes allowed, create the largest palindromic string of digits possible
//  or the string '-1' if it is not possible to create a palindrome under the
// constraints.

// **Example**
// `s = '1231'`
// `k = 3`
// Make 3 replacements to get `9339`.

// `s = '12321'`
// `k = 1`
// Make 1 replacement to get `12921`.

// **Function Description**
// Complete the *highestValuePalindrome* function in the editor below.
// highestValuePalindrome has the following parameter(s):
// - *string s:* a string representation of an integer
// - *int n:* the length of the integer string
// - *int k:* the maximum number of changes allowed

// **Returns**
// - *string:* a string representation of the highest value achievable or `-1`

// **Input Format**
// The first line contains two space-separated integers, `n` and `k`, the number of digits in the number and the maximum number of changes allowed.
// The second line contains an n-digit string of numbers.

// **Constraints**
// - 0 < n ≤ 10^5
// - 0 ≤ k ≤ 10^5
// - Each character i in the number is an integer where 0≤ i ≤ 9.

/*
 * Complete the 'highestValuePalindrome' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. INTEGER n
 *  3. INTEGER k
 */
// 5 test cases failed out of 33.
function highestValuePalindrome(s, n, k) {
  // Write your code here
  let numbersArray = s.split("");
  let remainingChanges = k;
  let numDiff = 0;
  let leftHalf = [];
  let rightHalf = [];
  let middle = [];
  leftHalf = numbersArray.slice(0, n / 2);

  if (n % 2 == 0) {
    rightHalf = numbersArray.slice(n / 2, numbersArray.length);
  } else {
    rightHalf = numbersArray.slice(n / 2 + 1, numbersArray.length);
  }
  rightHalf.reverse();

  // compare the left and right halfs to find any differences
  for (let j = 0; j < leftHalf.length; j++) {
    let leftElement = leftHalf[j];
    let rightElement = rightHalf[j];
    // This is basically where i looked at the discussions to see for help
    // https://www.hackerrank.com/challenges/richie-rich/forum/comments/167977
    if (rightElement != leftElement) {
      numDiff++;
    }
  }

  // make the changes
  for (let i = 0; i < leftHalf.length; i++) {
    let leftElement = leftHalf[i];
    let rightElement = rightHalf[i];

    if (leftElement === rightElement) {
      if (leftElement === "9") {
        continue;
      } else if (remainingChanges - 2 >= numDiff) {
        leftHalf[i] = "9";
        rightHalf[i] = "9";
        remainingChanges -= 2;
      }
    } else if (leftElement != rightElement) {
      if (leftElement === "9") {
        if (remainingChanges - 1 >= numDiff - 1) {
          rightHalf[i] = "9";
          numDiff -= 1;
          remainingChanges -= 1;
        } else {
          return -1;
        }
      } else if (rightElement === "9") {
        if (remainingChanges - 1 >= numDiff - 1) {
          leftHalf[i] = "9";
          numDiff -= 1;
          remainingChanges -= 1;
        } else {
          return -1;
        }
      } else {
        if (remainingChanges - 2 >= numDiff - 1) {
          leftHalf[i] = "9";
          rightHalf[i] = "9";
          numDiff -= 1;
          remainingChanges -= 2;
        } else if (remainingChanges - 1 > numDiff - 1) {
          if (x > y) {
            rightHalf[i] = leftElement;
          } else {
            leftHalf[i] = rightElement;
          }
          numDiff -= 1;
          remainingChanges -= 1;
        } else {
          return -1;
        }
      }
    }
  }
  rightHalf.reverse();
  middle = remainingChanges > 0 ? ["9"] : [numbersArray[Math.ceil(n / 2) - 1]];

  return n % 2 == 0
    ? leftHalf.concat(rightHalf).join("")
    : leftHalf.concat(middle, rightHalf).join("");
}
let stringA = "39543";
let maxChangesA = 1;
console.log(highestValuePalindrome(stringA, stringA.length, maxChangesA));
console.log("-- Expected: 3993 --");

let stringB = "092282";
let maxChangesB = 3;
console.log(highestValuePalindrome(stringB, stringB.length, maxChangesB));
console.log("-- Expected: 992299 --");

let stringC = "0011";
let maxChangesC = 1;
console.log(highestValuePalindrome(stringC, stringC.length, maxChangesC));
console.log("-- Expected: -1 --");
