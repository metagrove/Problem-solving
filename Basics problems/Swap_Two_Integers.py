"""
1.Given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a. 
Just write the code to swap values of a and b at the specified place.

Examples

Input: a = 1, b = 2
Output: 2 1
Explanation: Initially a = 1 and b = 2, now a = 2 and b = 1.

Input: a = 6, b = 7  
Output: 7 6 
Explanation: Initially a = 6 and b = 7, now a = 7 and b = 6.

Approach: Swap Two Integers

goal:
You have two variables a and b.
After swapping, a should have b’s value, and b should have a’s value.

Decide a swapping method:
Temp variable: Safe and clear.
Math trick: Avoids extra variable but less readable.
Python tuple unpacking: Clean and Pythonic.

Steps using temp variable:
Store a in a temporary variable temp.
Assign b to a.
Assign temp to b.

Steps using Python unpacking:

a, b = b, a  #to swap in a single line
""" 

# Write your code below 

a = int(input())
b = int(input())
c = 0 

# Write Code to Swap

c = a
a = b 
b = c
     #or
a,b = b,a #without tempory variable

print(a, b)

