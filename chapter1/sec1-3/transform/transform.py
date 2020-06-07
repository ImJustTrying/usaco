"""
ID: kevin173
LANG: PYTHON3
TASK: transform
"""

size = 0
before = []
after = []
transformation = ""
with open("transform.in", "r") as fio:
  size = int(fio.readline())
  for i in range(size):
    row = []
    for j in range(size):
      row.append(fio.read(1))
    fio.read(1)
    before.append(row)

  for i in range(size):
    row = []
    for j in range(size):
      row.append(fio.read(1))
    fio.read(1)
    after.append(row)


# return a new pattern that results from rotating the passed in pattern 90 degrees clockwise
def rotate90(pattern, rotations):
  for n in range(rotations):
    rotated = []
    for i in range(size):
      row = []
      for j in range(size):
        row.append(pattern[j][i])
      row.reverse()
      rotated.append(row)
    pattern = rotated
  return pattern

# return a new pattern that is reflected horizontally -- i.e. reflected over a vertical line
# through the center of the pattern
def reflect(pattern):
  reflected = []
  for i in range(size):
    row = []
    for j in reversed(range(size)):
      row.append(pattern[i][j])
    reflected.append(row)
  return reflected


print("size = {}\nbefore = {}\nafter = {}".format(size, before, after))
print("rotated 90: {}".format(rotate90(before, 1)))
print("relfected: {}".format(reflect(before)))


# First we will check if one of the simpler transformations applies -- i.e. 1-4 and 6
# 6 -- no change
if after == rotate90(before, 1):
  transformation = "1"
elif after == rotate90(before, 2):
  transformation = "2"
elif after == rotate90(before, 3):
  transformation = "3"
elif after == reflect(before):
  transformation = "4"
elif after == rotate90(reflect(before), 1) or after == rotate90(reflect(before), 2) or \
  after == rotate90(reflect(before), 3):
  transformation = "5"
elif before == after:
  transformation = "6"
else:
  transformation = "7"

print(transformation)
with open("transform.out", "w") as fio:
  fio.write(transformation + "\n")
