"""
ID: kevin173
LANG: PYTHON3
TASK: palsquare
"""

from math import log, floor

base = 0
palindromic_squares = []
with open("palsquare.in", 'r') as fio:
  base = int(fio.readline())

def is_palindrome(string):
  if len(string) <= 1:
    return True
  if len(string) == 2:
    return string[0] == string[1]

  mid = len(string) // 2
  low = mid - 1
  high = mid + 1 if len(string) % 2 != 0 else mid
  while low >= 0 and high < len(string):
    if string[low] != string[high]:
      return False
    low -= 1
    high += 1
  return True

# takes two naturals, returns a string
def to_base(num, base):
  # The exponent of the base corresponding to the most significant digit in num
  # e.g. base = 2, num = 3 = 11 in base 2. The most significant digit is in place floor(log_2(3))
  # = floor(1.58) = 1, 2^1 = 2 and the 2's place has the most significant digit
  base_exponent = floor(log(num, base))
  converted = ""
  while base_exponent >= 0:
    place_unit = int(base ** base_exponent)
    multiplier = int((num - (num % place_unit)) / place_unit)
    if multiplier >= 10:
      converted += chr(ord("A") - 10 + multiplier)
    else:
      converted += str(multiplier)
    num %= place_unit
    base_exponent -= 1
  return converted


for k in range(1, 301):
  squared = to_base(k * k, base)
  if is_palindrome(squared):
    palindromic_squares.append((to_base(k, base), squared))

with open("palsquare.out", "w") as fio:
  for (k, square) in palindromic_squares:
    fio.write(k + " " + square + "\n")
