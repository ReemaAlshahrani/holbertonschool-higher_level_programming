#!/usr/bin/node

// Convert the first argument to an integer representing the size of the square
const size = Math.floor(Number(process.argv[2]));

// Check if the input is not a valid number
if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  // Loop through each row (height) based on the specified size
  for (let i = 0; i < size; i++) {
    let row = '';
    // Loop through each column (width) to build the row with 'X'
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    // Print the completed row
    console.log(row);
  }
}
