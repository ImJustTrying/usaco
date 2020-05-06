"""
ID: kevin173
LANG: PYTHON3
TASK: gift1
"""

fio = open('gift1.in', 'r')
np = int(fio.readline())
names = []
balances = []
for i in range(0, np):
  names.append(fio.readline())
  balances.append(0)

print(np, names)
for i in range(0, np):
  gifter_index = names.index(fio.readline())
  # will be the list [initial balance, num of friends to share with]
  numbers = [int(num) for num in fio.readline().split()]
  if numbers[1] != 0:
    gift = numbers[0] // numbers[1]
    balances[gifter_index] -= numbers[0]
    balances[gifter_index] += numbers[0] - gift * numbers[1]
  for j in range(0, numbers[1]):
    receiver_index = names.index(fio.readline())
    balances[receiver_index] += gift

fio.close()
fio = open('gift1.out', 'w')
for i in range(0, np):
  fio.write(names[i].replace('\n', '') + ' ' + str(balances[i]) + '\n')
fio.close()
