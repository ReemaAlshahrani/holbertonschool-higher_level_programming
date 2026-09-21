#!/usr/bin/node

//Calculates the factorial of a given number recursively.
function factorial (n) {
  // Base case: return 1 if n is not a valid number or less than or equal to 1
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  
  // Recursive step: multiply n by the factorial of (n - 1)
  return n * factorial(n - 1);
}

// Convert the command-line argument to a number
const arg = Number(process.argv[2]);

// Print the final result of the factorial calculation
console.log(factorial(arg));
