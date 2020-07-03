"""
ID: kevin173
LANG: PYTHON3
TASK: milk
"""


milk_demand = 0
num_farmers = 0
cost_and_supply = [] # List of tuples
total_cost = 0
total_milk = 0
with open("milk.in", "r") as fio:
  t = fio.readline().split()
  milk_demand = int(t[0])
  num_farmers = int(t[1])
  for i in range(num_farmers):
    t = fio.readline().split()
    # Price is first, then supply
    cost_and_supply.append((int(t[0]), int(t[1])))

# Sort by price in ascending order
cost_and_supply.sort(key=lambda x : x[0])

print("N = {}, M = {}, (P, A) = {}".format(milk_demand, num_farmers, cost_and_supply))
for i in range(len(cost_and_supply)):
  if total_milk >= milk_demand:
    break
  else:
    remaining_demand = milk_demand - total_milk
    if cost_and_supply[i][1] <= remaining_demand:
      total_milk += cost_and_supply[i][1]
      total_cost += cost_and_supply[i][0] * cost_and_supply[i][1]
    else:
      total_milk += remaining_demand
      total_cost += cost_and_supply[i][0] * remaining_demand

with open("milk.out", "w") as fio:
  fio.write(str(total_cost) + "\n")
