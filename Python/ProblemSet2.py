""" QUESTION 1:
Write a function between(number, low, high) that returns True if the number is in the interval [low, high] (between (or equal to) low and high), and False otherwise.

between(3, 1, 6) → True
between(2, 2, 2) → True
between(5, 2, 4) → False
"""
def between(n, low, high):
  for i in range(low,high+1):
    if i == n:
      return True
  return False


""" QUESTION 2:
Write a function justone(a, b) that returns True if exactly one (but not both) of the numbers a or b is 10, and False otherwise.

justone(5, 10) → True
justone(10, 10) → False
justone(8, 2) → False
"""
def justone(a,b):
  if a == 10 or b == 10:
    if a == 10 and b == 10:
      return False
    return True
  return False


""" QUESTION 3:
Write a function max3(a, b, c) the returns the maximum value of the parameters a, b, and c.

max3(2, 5, 3) → 5
max3(3, 3, 2) → 3
max3(10, 9, 9) → 10
"""
def max3(a,b,c):
  if a > b:
    if b > c:
      return a
    else:
      if a > c:
        return a
      else:
        return c
  else:
    if a > c:
      return b
    else:
      if c > b:
        return c
      else:
        return b


""" QUESTION 4:
Write a function sumprod(a,b) that takes 2 integer values as parameters and returns their sum if they are not equal and their product if they are.

sumprod(3, 3) → 9
sumprod(2, 5) → 7
sumprod(0, 2) → 2
"""
def sumprod(a,b):
  if a == b:
    return a*b
  else:
    return a+b


""" QUESTION 5:
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""
def pos_neg(a, b, negative):
  if negative == True:
    if a < 0 and b < 0:
      return True
    return False
  else:
    if a * b < 0:
      return True
    return False


def main():
    print(between(3, 1, 6))
    print(justone(8, 2))
    print(max3(10, 9, 9))
    print(sumprod(3, 3))
    print(pos_neg(-4, -5, True))
main()