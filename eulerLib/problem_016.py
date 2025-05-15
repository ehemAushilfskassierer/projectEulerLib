"""
Project Euler - Problem 016: Power Digit Sum
https://projecteuler.net/problem=16

Description:
    2^15 = 32768 and the sum of its digits is
    3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number
    2^1000?

Author: ehem. Aushilfskassierer
"""

base = 2
exponent = 1000
showSubtotal = False

num = base ** exponent
res = 0

for i in str(num):
    res += int(i)

if showSubtotal:
    print(" + ".join(str(num)) + " = ")
print(res)