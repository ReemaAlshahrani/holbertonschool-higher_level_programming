#!/usr/bin/node

// Function to add two command-line arguments converted to integers
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
