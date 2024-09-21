// Reduce a string of lowercase characters in range `ascii[‘a’..’z’]`by doing a series of operations.
// In each operation, select a pair of adjacent letters that match, and delete them.
// Delete as many characters as possible using this method and return the resulting string.
// If the final string is empty, return `Empty String`

// **Example**.
// `s = 'aab'`
// `aab` shortens to `b` in one operation: remove the adjacent `a` characters.
// `s = 'abba'`
// Remove the two 'b' characters leaving 'aa'. Remove the two 'a' characters to leave ''. Return 'Empty String'.

// **Function Description**
// Complete the *superReducedString* function in the editor below.
// superReducedString has the following parameter(s):
// - *string s:* a string to reduce

// **Returns**
// - *string:* the reduced string or `Empty String`

// **Input Format**
// A single string, s.

// **Constraints**
// - 1 ≤ length of s ≤ 100

/*
 * Complete the 'superReducedString' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function superReducedString(s) {
  // Write your code here
  let charArray = s.split("");
  let reducedChars = [];
  charArray.forEach((character) => {
    if (reducedChars && reducedChars[reducedChars.length - 1] == character) {
      reducedChars.pop();
    } else {
      reducedChars.push(character);
    }
  });

  if (reducedChars.length === 0) {
    return "Empty String";
  } else {
    return reducedChars.join("");
  }
}

// Recursion from discussions
function superReducedStringRecursion(s) {
  let charArray = s.split("");
  if (charArray.length === 0) {
    return "Emptry String";
  }

  for (let i = 0; i < charArray.length; i++) {
    if (charArray[i] === charArray[i + 1]) {
      charArray.splice(i, 2);
      return superReducedStringRecursion(charArray.join(""));
    } else if (i == charArray.length - 1) {
      return charArray.join("");
    }
  }
}

let strA = "aab";
console.log(superReducedString(strA));
console.log("EXPECTED: b");

let strB = "abba";
console.log(superReducedString(strB));
console.log("EXPECTED: Empty String");

let strC = "aaabccddd";
console.log(superReducedString(strC));
console.log("EXPECTED: abd");

console.log(superReducedStringRecursion(strC));
console.log("EXPECTED: abd");
