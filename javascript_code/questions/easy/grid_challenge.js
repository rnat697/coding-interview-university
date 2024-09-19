// Given a grid of characters in the range ascii[a-z], (PS: ITS NOT ACTUALLY A SQUARE GRID -.-)
// rearrange elements of each row alphabetically, ascending.
// Determine if the columns are also in ascending alphabetical order,
// top to bottom. Return `YES` if they are or `NO` if they are not.

// Example
// grid = [’abc’, ‘ade’, ‘efg’]
// ```
// a b c
// a d e
// e f g
// ```
// The rows are already in alphabetical order.
// The columns `a a e`, `b d f` and `c e g` are also in alphabetical order,
// so the answer would be `YES`. Only elements within the same row can be rearranged.
// They cannot be moved to a different row.

// **Function Description**
// Complete the *gridChallenge* function in the editor below.
// gridChallenge has the following parameter(s):
// - *string grid[n]:* an array of strings
// **Returns**
// - *string:* either `YES` or `NO`

// **Input Format**
// The first line contains t, the number of testcases.
// Each of the next t sets of lines are described as follows:
// - The first line contains n, the number of rows and columns in the grid.
// - The next n lines contains a string of length

// **Constraints**
// - 1≤ t ≤ 100
// - 1 ≤ n ≤ 100
// - *Each string consists of lowercase letters in the range ascii[a-z]*

// **Output format**
// For each test case, on a separate line print `YES` if it is possible to
// rearrange the grid alphabetically ascending in both its rows and columns,
// or `NO` otherwise.

/*
 * Complete the 'gridChallenge' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING_ARRAY grid as parameter.
 */

// O(n * m) nested loops + uneven for loop.
function gridChallenge(grid) {
  // Write your code here

  // Rearrange each element in the row to alphabetical order
  grid = grid.map((element) => element.split("").sort());

  // compare each column.
  // i = number of columns/x direction, j = rows/y direction
  for (let i = 0; i < grid[0].length; i++) {
    for (let j = 0; j < grid.length - 1; j++) {
      let currentCol = grid[j][i];
      let nextCol = grid[j + 1][i];
      // is current letter larger than next --> out of order.
      if (currentCol.localeCompare(nextCol) > 0) {
        return "NO";
      }
    }
  }
  return "YES";
}

let grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"];
let result = gridChallenge(grid);
console.log(result);
console.log("EXPECTED: YES");

let simpleGrid = ["abc", "tyu", "efg"];
let resultnegative = gridChallenge(simpleGrid);
console.log(resultnegative);
console.log("EXPECTED: NO");

let grida = ["abc", "lmp", "qrt"];
let resulta = gridChallenge(grida);
console.log(resulta);
console.log("EXPECTED: YES");

let gridb = ["mpxz", "abcd", "wlmf"];
let resultb = gridChallenge(gridb);
console.log(resultb);
console.log("EXPECTED: NO");

let gridc = ["abc", "hjk", "mpq", "rtv"];
let resultc = gridChallenge(gridc);
console.log(resultc);
console.log("EXPECTED: YES");
