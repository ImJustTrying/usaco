"""
ID: kevin173
LANG: PYTHON3
TASK: milk2
"""

"""
4
100 200
201 301
302 402
405 503
"""

n = 0
farmers = []
with open("milk2.in", 'r') as fio:
  n = int(fio.readline())
  for i in range(0, n):
    farmers.append(fio.readline().split(' '))
    farmers[i] = (int(farmers[i][0]), int(farmers[i][1]))

