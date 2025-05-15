"""
Project Euler - Problem 020: Factorial Digit Sum
https://projecteuler.net/problem=20

Description:
    n! means n * (n-1) * ... * 2 * 1.

    For example, 10! = 10*9*...*2*1=3628800,
    and the sum of the digits in the number 10!
    is 3+6+2+8+8+0+0=27.
    
    Find the sum of the digits in the number 100!.

Author: ehem. Aushilfskassierer
"""
x = 100
 
showCalc = True
 
def factorial(n):
    assert isinstance(n, int) and n >= 0,\
        "n has to be an int and >= 0 (0! = 1)"
 
    res = n
    while n > 1:
        res *= (n-1)
        n -= 1
 
    return res
 
facto = factorial(x)
crossSum = 0
 
 
for digit in str(facto):
    crossSum += int(digit)
 
if showCalc:
    print(" + ".join(str(facto)) + " = ")
 
print(crossSum)