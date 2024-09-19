// Given an array of integers, calculate the ratios of its elements that are *positive*,
// *negative*, and *zero*. Print the decimal value of each fraction on a new line with
// places after the decimal.

// **Note:** This challenge introduces precision problems. The test cases are scaled to six decimal places,
// though answers with absolute error of up to  are acceptable.

// **Function Description**
// Complete the *plusMinus* function in the editor below.
// plusMinus has the following parameter(s):
// - *int arr[n]*: an array of integers
// **Print**
// Print the ratios of positive, negative and zero values in the array.
// Each value should be printed on a separate line with  digits after the decimal.
// The function should not return a value.

// **Input Format**
// The first line contains an integer, , the size of the array.
// The second line contains  space-separated integers that describe arr[n].

// **Output Format**
// **Print** the following 3 lines, each to 6 decimals:
// 1. proportion of positive values
// 2. proportion of negative values
// 3. proportion of zeros

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
  // Write your code here
  let count = {}; // Can also just use normal variables lol
  count["negatives"] = 0;
  count["positives"] = 0;
  count["zeros"] = 0;

  arr.forEach((element) => {
    if (element > 0) {
      count["positives"]++;
    } else if (element < 0) {
      count["negatives"]++;
    } else {
      count["zeros"]++;
    }
  });

  let posRatio = (count["positives"] / arr.length).toFixed(6);
  let negRatio = (count["negatives"] / arr.length).toFixed(6);
  let zeroRatio = (count["zeros"] / arr.length).toFixed(6);
  console.log(posRatio);
  console.log(negRatio);
  console.log(zeroRatio);
}

let arr = [-4, 3, -9, 0, 4, 1];
plusMinus(arr);
console.log("Expected: 0.500000 0.333333 0.166667 ");

let newarr = [0, 100, 35, 0, 94, 40, 42, 87, 59, 0];
plusMinus(arr);
console.log("Expected: 0.700000, 0.000000, 0.300000");
