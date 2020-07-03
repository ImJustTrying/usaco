"""
ID: kevin173
LANG: PYTHON3
TASK: namenum
"""

digits = ""
names = []
keypad_mappings = {
  "2": {"A","B","C"},
  "3": {"D","E","F"},
  "4": {"G","H","I"},
  "5": {"J","K","L"},
  "6": {"M","N","O"},
  "7": {"P","R","S"},
  "8": {"T","U","V"},
  "9": {"W","X","Y"}
}

with open("namenum.in", "r") as fio:
  digits = fio.readline()
# remove the newline at the end
digits = digits[0 : len(digits) - 1]

with open("dict.txt", "r") as fio:
  for line in fio:
    names.append(line[0 : len(line) - 1])

# filter for names that are the same length as the digit combination
names = filter(lambda name: len(name) == len(digits), names)

for i in range(0, len(digits)):
  try:
    possible_characters = keypad_mappings[digits[i]]
    #print(possible_characters)
    names = [name for name in names if name[i] in possible_characters]
  except KeyError:
    #print("keyerror")
    names = []
    break

with open("namenum.out", "w") as fio:
  num_names = 0
  for name in names:
    fio.write(name + "\n")
    num_names += 1
  if num_names == 0:
    fio.write("NONE\n")
