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
import functools

n = 0
intervals = []
with open("milk2.in", 'r') as fio:
  n = int(fio.readline())
  for i in range(0, n):
    intervals.append(fio.readline().split(' '))
    intervals[i] = (int(intervals[i][0]), int(intervals[i][1]))

def length(interval):
  return interval[1] - interval[0]

def intervals_interlap(i1, i2):
  return i2[0] <= i1[1] and i2[0] >= i1[0] or i1[0] <= i2[1] and i1[0] >= i2[0]

# assumes intervals is nonempty
# will find the longest continuous intervals starting at the first farmers starting time.
# each interval is seperated by some amount of time -- i.e. none of the intervals overlap.
def generate_longest_intervals(intervals):
  longest_intervals = []
  current_longest = intervals[0]
  for i in range(1, len(intervals)):
    if not intervals_interlap(intervals[i], current_longest):
      longest_intervals.append(current_longest)
      current_longest = intervals[i]
    elif intervals_interlap(intervals[i], current_longest):
      current_longest = (current_longest[0], max(current_longest[1], intervals[i][1]))

  longest_intervals.append(current_longest)
  return longest_intervals


# sort the intervals by the start time for each farmer in ascending order
intervals.sort(key=lambda a: a[0])
longest_milking_intervals = generate_longest_intervals(intervals)
longest_non_milking_intervals = [
(longest_milking_intervals[i][1], longest_milking_intervals[i+1][0])
for i in range(0, len(longest_milking_intervals) - 1)
]

max_milking_interval_length = functools.reduce(
  lambda a,b: a if a>b else b, map(length, longest_milking_intervals))

if n == 1:
  max_non_milking_interval_length = 0
else:
  max_non_milking_interval_length = functools.reduce(
    lambda a,b: a if a>b else b, map(length, longest_non_milking_intervals), 0)

"""
print(intervals)
print(sorted)
print(longest_milking_intervals)
print(max_milking_interval_length)
print(max_non_milking_interval_length)
"""
with open("milk2.out", "w") as fio:
  fio.write(str(max_milking_interval_length) + " " + str(max_non_milking_interval_length) + "\n")
