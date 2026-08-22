# Python - Everything is Object

This directory contains advanced Python programming exercises focusing on how CPython handles objects, memory management, variable references, mutability, caching (`NSMALLPOSINTS`, `NSMALLNEGINTS`), and internal data structures.

## Comprehensive Tasks & Answers Summary

| File Name | Task / Question Concept | Answer / Result | Brief Explanation |
| :--- | :--- | :--- | :--- |
| `0-answer.txt` | Print the type of an object | `type` | The built-in function used to get an object's type. |
| `1-answer.txt` | Get variable identifier (memory address) | `id` | The built-in function that returns the CPython memory address. |
| `2-answer.txt` | `a = 89`, `b = 100` (Same object?) | `No` | They are two different integer objects in memory. |
| `3-answer.txt` | `a = 89`, `b = 89` (Same object?) | `Yes` | Small integers like 89 are pre-allocated/cached by CPython (`NSMALLPOSINTS`). |
| `4-answer.txt` | `a = 89`, `b = a` (Same object?) | `Yes` | `b` points to the exact same object reference as `a`. |
| `5-answer.txt` | `a = 89`, `b = a + 1` (Same object?) | `No` | Evaluating `a + 1` creates a new integer object (90). |
| `6-answer.txt` | `s1 == s2` for equal string values | `True` | Compares the values of strings; both are equal. |
| `7-answer.txt` | `s1 is s2` where `s2 = s1` | `True` | Compares object identities; both variables point to the same object. |
| `8-answer.txt` | `s1 == s2` for literal string values | `True` | Compares values; both strings have identical content. |
| `9-answer.txt` | `s1 is s2` for independent literal strings | `True` | String interning in CPython reuses identical literal strings within the same code block. |
| `10-answer.txt` | `l1 == l2` for identical lists | `True` | Compares list values (elements are equal). |
| `11-answer.txt` | `l1 is l2` for separate lists | `False` | They are two distinct list objects created separately in memory. |
| `12-answer.txt` | `l2 = l1`, `l1 == l2` | `True` | Lists have equal values. |
| `13-answer.txt` | `l2 = l1`, `l1 is l2` | `True` | Both reference the exact same list object. |
| `14-answer.txt` | `l1.append(4)`, print `l2` | `[1, 2, 3, 4]` | Modifying the list through one reference reflects in both because they share the same object. |
| `15-answer.txt` | `l1 = l1 + [4]`, print `l2` | `[1, 2, 3]` | Using `+` operator creates a **new** list object for `l1`, leaving `l2` unchanged. |
| `16-answer.txt` | Integer increment inside function | `1` | Integers are immutable; passing `a` to a function passes its value, and local modification does not change the outer variable. |
| `17-answer.txt` | List append inside function | `[1, 2, 3, 4]` | Lists are mutable; modifying the list object in-place affects the original list outside. |
| `18-answer.txt` | List reassignment inside function | `[1, 2, 3]` | Reassigning the local variable `n = v` inside the function does not change the original reference `l1` outside. |
| `19-copy_list.py` | Function to copy a list | Custom Code | Returns a shallow copy of a list using slicing `a_list[:]`. |
| `20-answer.txt` | `a = ()` (Is a a tuple?) | `Yes` | Empty parentheses denote an empty tuple. |
| `21-answer.txt` | `a = (1, 2)` (Is a a tuple?) | `Yes` | Comma-separated items inside parentheses form a tuple. |
| `22-answer.txt` | `a = (1)` (Is a a tuple?) | `No` | Parentheses around a single value without a comma evaluate to an integer, not a tuple. |
| `23-answer.txt` | `a = (1, )` (Is a a tuple?) | `Yes` | Adding a trailing comma forces it to be recognized as a tuple. |
| `24-answer.txt` | `a = (1)`, `b = (1)`, `a is b` | `True` | Both are evaluated as integers (cached small integers), so they share the same memory ID. |
| `25-answer.txt` | `a = (1, 2)`, `b = (1, 2)`, `a is b` | `False` | Tuples are distinct immutable objects created separately. |
| `26-answer.txt` | `a = ()`, `b = ()`, `a is b` | `True` | Empty tuples are cached/singletons in CPython. |
| `27-answer.txt` | `a = a + [5]` (Same ID?) | `No` | Using `+` creates a new list object, changing the memory address (`id`). |
| `28-answer.txt` | `a += [4]` (Same ID?) | `Yes` | Using `+=` on a list performs an in-place modification (`__iadd__`), keeping the same object ID. |
| `100-magic_string.py` | Magic string counter function | Custom Code | Uses a default function argument to keep track of iterations and print "BestSchool" repetitively. |
| `101-locked_class.py` | Locked class attribute restriction | Custom Code | Uses `__slots__ = ("first_name",)` to restrict dynamic attribute creation. |
| `103-line1.txt` | `a = 1` | `1` | Creates a small integer object (cached). |
| `103-line2.txt` | `b = 1` | `0` | Reuses the pre-existing cached small integer object. |
| `104-line1.txt` | `a = 1024` | `1` | Creates a new large integer object (outside small int range). |
| `104-line2.txt` | `b = 1024` | `1` | Creates another independent large integer object for `b`. |
| `104-line3.txt` | After `del a`, is `a`'s int deleted? | `Yes` | Reference count drops to zero, destroying the object. |
| `104-line4.txt` | After `del b`, is `b`'s int deleted? | `Yes` | Reference count drops to zero, destroying the object. |
| `104-line5.txt` | `c = 1024` | `1` | Creates a new integer object for `c`. |
| `105-line1.txt` | Small int objects in memory before line 2 | `262` | CPython pre-allocates small integers from `-5` to `256` (`NSMALLNEGINTS` & `NSMALLPOSINTS`). |
| `106-line1.txt` | `a = "SCHL"` | `1` | Creates a new string object in memory. |
| `106-line2.txt` | `b = "SCHL"` | `0` | Reuses the existing string object via string interning within the code block. |
| `106-line3.txt` | After `del a`, is string deleted? | `No` | The string object is still referenced by `b`. |
| `106-line4.txt` | After `del b`, is string deleted? | `Yes` | Last reference removed, so the string object is deleted from memory. |
| `106-line5.txt` | `c = "SCHL"` | `1` | Creates a new string object during the final assignment. |

---

