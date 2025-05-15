"""
Project Euler - Problem 017: Number Letter Counts
https://projecteuler.net/problem=17

Description:
    If the numbers 1 to 5 are written out in words:
    one, two, three, four, five, then there are
    3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand)
    inclusive were written out in words, how many
    letters would be used?

    NOTE: Do not count spaces or hyphens. For example,
    342 (three hundred and forty-two) contains 23 letters
    and 115 (one hundred and fifteen) contains 20 letters.
    The use of "and" when writing out numbers is in compliance
      with British usage.

Author: ehem. Aushilfskassierer
"""

highestNbr = 1000
 
dictNumber = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}
 
def number_to_words(n):

    if n == 1000:
        return "onethousand"

    words = ""
    hundreds = n // 100
    remainder = n % 100
 
    if hundreds:
        words += dictNumber[hundreds] + "hundred"
        if remainder:
            words += "and"
 
    if remainder:
        if remainder <= 20:
            words += dictNumber.get(remainder, "")
        else:
            tens = remainder // 10 * 10
            units = remainder % 10
            words += dictNumber.get(tens, "")
            words += dictNumber.get(units, "")
    return words
 
total = 0

for i in range(1, highestNbr + 1):
    word = number_to_words(i)
    print(f"{i}: {word} ({len(word)} letters)")
    total += len(word)
 
print(f"\nTotal letters used from 1 to {highestNbr}: {total}")