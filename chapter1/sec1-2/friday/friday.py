"""
ID: kevin173
LANG: PYTHON3
TASK: friday
"""

try:
  fio = open('friday.in', 'r')
except OSError:
  print("Error opening input file")
  sys.exit()

years = int(fio.readline())
fio.close()

# sunday ... saturday
thirteenths = [0, 0, 0, 0, 0, 0, 0]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# sunday = 0, monday = 1 ... saturday = 6
day = 1

for year in range(1900, 1900 + years):
  if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    days_in_month[1] = 29
  else:
    days_in_month[1] = 28

  for month in range(0, 12):
    # assume day is the day of the week for the first of the month
    # at the beginning of each iteration
    day = (day + 13) % 7
    thirteenths[day] += 1
    day = (day + days_in_month[month] - 13) % 7

print(years, thirteenths)
try:
  fio = open('friday.out', 'w')
except OSError:
  print("Error opening output file")
  sys.exit()

# writes the list with each element seperated by spaces
fio.write(' '.join(str(e) for e in thirteenths) + '\n')
