"""
ID: kevin173
LANG: PYTHON3
TASK: namenum
"""
from math import ceil, log10

serial = 0
with open("namenum.in", 'r') as fio:
  serial = int(fio.readline())


def get_digits(number):
  digits = []
  num_digits = int(ceil(log10(number))) + 1
  if log10(number) == ceil(log10(number)):
    num_digits += 1

  # [10^n, 10^n-1, ... 10^1] for n = num_digits
  for place in reversed([10**x for x in range(1, num_digits)]):
    prev_place = place // 10
    digit = (number % place - number % prev_place) // prev_place
    digits.append(digit)
  return digits

def generate_permutations(number):
  digits = get_digits(number)
  num_digits = len(digits)
  permutations = []
  indices = [0 for x in range(0, num_digits)]
  # 2 = ABC, 3 = DEF ... 9 = WXY, Q and Z are excluded
  keypad_map = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'],
    ['M', 'N', 'O'], ['P', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y']]

  """
  Think of indices as a 4 digit number in base 3 (digits only having the value 0, 1, or 2).
  iterating through all the numbers between 0 and 10000 (in base 3) will give us all the
  possible permutations. In our case, we use each digit as an index to the keypad_map array.
  """
  # Maxed means indices is all twos (i.e. [2, 2, 2, ... 2]), prev_maxed let's us execute the loop
  # when the list is maxed and stop immediately after that.
  prev_maxed = False
  maxed = False
  while not maxed:
    maxed = prev_maxed
    print(indices)
    name = []

    for i in range(0, num_digits):
      name.append(keypad_map[digits[i] - 2][indices[i]])
    permutations.append("".join(name))

    # Increment the number represented by indices
    overflow = True
    i = num_digits - 1
    while i >= 0 and overflow:
      indices[i] = (indices[i] + 1) % 3
      print(indices[i] == 0)
      oveflow = indices[i] == 0
      print(overflow)
      i -= 1
      # print(overflow, 1 == 0, indices[i + 1] == 0)
    prev_maxed = list(filter(lambda a : a != 2, indices)) == []

  return permutations


digits = get_digits(serial)
permutations = generate_permutations(serial)
print(digits, permutations)
