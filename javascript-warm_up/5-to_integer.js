#!/usr/bin/node

// Convert the first command-line argument to a number and floor it
const num = Math.floor(Number(process.argv[2]));

// Check if the resulting value is NaN (Not a Number)
if (isNaN(num)) {
  console.log('Not a number');
} else {
  // If it is a valid number, print it with the required format
  console.log('My number: ' + num);
}
