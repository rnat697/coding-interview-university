//---- Complexity/Performance ----
// Time Complexity:
// - **Best case complexity**: `O(1)`
// - **Average case complexity**: `O(log n)`
// - **Worst case complexity**: `O(log n)`

// Space Complexity: O(1)

// Searching algorithm for finding an element’s position in a **sorted array**
// by **repeatedly dividing the search interval in half**. The element is always
// searched in the middle portion of an array. The idea of binary search is to use the
// information that the array is sorted and reduce the time complexity to O(log N).
// Binary search algorithm can be implemented in two ways
// 1. Iterative Method
// 2. Recursive Method - Follows a divide and conquer approach.
// ---- Algorithm Pseudocode ----
// 1. Divide the search space into two halves by finding the middle index “mid”.
// 2. Compare the middle element of the search space with the key.
// 3. If the key is found at middle element, the process is terminated.
// 4. If the key is not found at middle element, choose which half will be used as the next search space.
//   a. If the key is smaller than the middle element, then the left side is used for next search.
//   b. If the key is larger than the middle element, then the right side is used for next search.
// 5. This process is continued until the key is found or the total search space is exhausted

// It returns index of x in given array arr if present,
// else returns -1
// Uses while loop.

function binarySearchIterative(arr, target) {
  let highIndex = arr.length - 1;
  let midIndex = 0;
  let lowIndex = 0;

  while (lowIndex <= highIndex) {
    midIndex = Math.floor((highIndex + lowIndex) / 2);
    let midValue = arr[midIndex];

    if (target < midValue) {
      // If the key is smaller than the middle element, then the left side is used for next search.
      // increase the highIndex by midIndex + 1
      highIndex = midIndex + 1;
    } else if (target > midValue) {
      // If the key is larger than the middle element, then the right side is used for next search.
      // low index is midIndex - 1
      lowIndex = midIndex - 1;
    } else {
      return midValue;
    }
  }
  return -1;
}

function binarySearchRecursive(arr, target, start, end) {
  if (start > end) return -1;
  let mid = Math.floor((start + end) / 2);
  let midValue = arr[mid];
  if (target < midValue) {
    // If the key is smaller than the middle element, then the left side is used for next search.
    return binarySearchRecursive(arr, target, start, mid + 1);
  } else if (target > midValue) {
    // if the key is larger than the middle element, then the right side is used for next search.
    return binarySearchRecursive(arr, target, mid - 1, end);
  } else {
    return midValue;
  }
}

const array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91];
const target = 23;
let iterative = binarySearchIterative(array, target);
console.log(iterative);
let recursive = binarySearchRecursive(array, target, 0, array.length);
console.log(recursive);
