#!/usr/bin/node

// Convert the command line argument to an integer representing the number of occurrences
const x = Math.floor(Number(process.argv[2]));

// Check if the input is not a valid number
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  // Loop 'x' times and print the message in each iteration
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
