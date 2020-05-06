"""
ID: kevin173
LANG: PYTHON3
TASK: ride
"""

fin = open('ride.in', 'r')
# ord will return the ascii value as an int of a character
comet = [ord(x) for x in fin.readline()]
group = [ord(x) for x in fin.readline()]
fin.close()
# Remove the newline from the strings
del comet[-1]
del group[-1]


comet_sum = 1
group_sum = 1
for char in comet:
  comet_sum *= char - 64
for char in group:
  group_sum *= char - 64
comet_sum %= 47
group_sum %= 47

fout = open('ride.out', 'w')
if comet_sum == group_sum:
  fout.write("GO\n")
else:
  fout.write("STAY\n")
fout.close()
