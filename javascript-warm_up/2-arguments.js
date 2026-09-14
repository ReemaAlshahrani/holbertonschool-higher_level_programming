#!/usr/bin/node

// Calculate the number of actual arguments by subtracting Node.js and script paths
const args = process.argv.length - 2;

// Check if no arguments were passed
if (args === 0) {
  console.log('No argument');
} 
// Check if exactly one argument was passed
else if (args === 1) {
  console.log('Argument found');
} 
// Handle the case when multiple arguments were passed
else {
  console.log('Arguments found');
}
