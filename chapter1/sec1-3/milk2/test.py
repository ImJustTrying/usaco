"""
ID: kevin173
LANG: PYTHON3
TASK: milk2
"""

n = 0
farmers = []
with open("milk2.in", 'r') as fio:
  n = int(fio.readline())
  for i in range(0, n):
    farmers.append(fio.readline().split(' '))
    farmers[i] = (int(farmers[i][0]), int(farmers[i][1]))


def sort_list_by_index(l, index):
  for length in range(2, len(l) + 1):
    for i in reversed(range(1, length)):
      if l[i][index] < l[i - 1][index]:
        temp = l[i]
        l[i] = l[i - 1]
        l[i - 1] = temp
      else:
        break
  return l


# Finds other ranges in l that intersect r
def find_intersecting_ranges(l, t):
  new_list = []
  for ran in l:
    if ran[0] <= t and ran[1] >= t:
      new_list.append(ran)
  return new_list


def f(x):
"""
1) Solve for two intervals, combine results 
