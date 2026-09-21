#!/usr/bin/node

// Check if there are fewer than two numbers provided as arguments
if (process.argv.length <= 3) {
  console.log(0);
} else {
  // Extract arguments from index 2 onwards and convert them to numbers
  const args = process.argv.slice(2).map(Number);

  // Sort the array in descending order (largest to smallest)
  args.sort((a, b) => b - a);

  // Print the second element, which is the second biggest integer
  console.log(args[1]);
}
