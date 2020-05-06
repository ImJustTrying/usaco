"""
ID: kevin173
LANG: PYTHON3
TASK: beads
"""

def read_left_right(string, index):
  char = 'w'
  i = index
  l = 0
  length = len(string)

  while l < length:
    if string[i] != char:
      if char == 'w':
        char = string[i]
      elif string[i] != 'w':
        break
    i = (i + 1) % length
    l += 1

  i = (index - 1) % length
  char = 'w'
  while l < length:
    if string[i] != char:
      if char == 'w':
        char = string[i]
      elif string[i] != 'w':
        break
    i = (i - 1) % length
    l += 1
  return l



try:
  fio = open("beads.in", 'r')
except OSError:
  print("Cannot open input file")
  sys.exit()

n = int(fio.readline())
beads = fio.readline().replace('\n', '')
fio.close()
max_beads = 0

for i in range(0, n):
  # We split at i
  l = read_left_right(beads, i)
  if max_beads < l:
    max_beads = l

try:
  fio = open("beads.out", 'w')
except OSError:
  print("Cannot open output file")
  sys.exit()

fio.write(str(max_beads) + '\n')
fio.close()

