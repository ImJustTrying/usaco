"""
ID: kevin173
LANG: PYTHON3
TASK: palsquare
"""

base = 0
with open("palsquare.in", 'r') as fio:
  base = int(fio.readline())

def log_base(n, b):
  return log(n) / log(b)

def num_digits_in_base(n, b):
  return (n % b == 0) ? log_base(n, b) : log_base(n, b) + 1

def is_palindromic_in_base(n, b):
  length = num_digits(n)
