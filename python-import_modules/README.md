# Python - Import & Modules

This project explores the concepts of modules, importing functions, handling command-line arguments, and understanding Python bytecode within the Ubuntu 22.04 LTS environment.

## Learning Objectives
* How to import functions from another file.
* How to use and create modules.
* How to use the built-in function `dir()`.
* How to prevent code from being executed when imported (`if __name__ == "__main__":`).
* How to handle command-line arguments using `sys.argv`.

---

## Tasks Overview

| Task Number | File Name | Description |
| :--- | :--- | :--- |
| **0. Import a simple function** | `0-add.py` | Imports a basic addition function from `add_0.py` and prints the result using string formatting. |
| **1. My first toolbox!** | `1-calculation.py` | Imports mathematical functions (`add`, `sub`, `mul`, `div`) from `calculator_1.py` and performs operations. |
| **2. How to make a script dynamic!** | `2-args.py` | Prints the number of and the list of its command-line arguments. |
| **3. Infinite addition** | `3-infinite_add.py` | Computes and prints the sum of all numerical arguments passed via the command line. |
| **4. Who are you?** | `4-hidden_discovery.py` | Uses `dir()` to find and print all non-private names defined in a compiled module (`hidden_4.pyc`). |
| **5. Everything can be imported** | `5-variable_load.py` | Demonstrates that variables can be imported from other files just like functions. |
| **6. Build my own calculator!** | `100-my_calculator.py` | An advanced task creating a fully functional CLI calculator that handles dynamic input and exits properly. |
| **7. Easy print** | `101-easy_print.py` | An advanced brainteaser that prints `#pythoniscool` without using `print`, `eval`, or `open`. |
| **8. ByteCode -> Python #3** | `102-magic_calculation.py` | An advanced task reconstructing a Python function from its raw Bytecode instructions. |
| **9. Fast alphabet** | `103-fast_alphabet.py` | Prints the uppercase alphabet in exactly 3 lines without loops or string literals. |

---

## Requirements
* **Environment:** Ubuntu 22.04 LTS
* **Python Version:** Python 3.10
* **Style Guide:** Code compliant with `pycodestyle` (version 2.7.*)
