#

friends = ["Jim", "Carry", "Mask"]
for name in friends:
  print(name)

for index in range(10):
  print(index)

print("Break\n Break")
for index in range(2, 9):
  print(index)

print("lenghts is", len(friends))

for index in range(len(friends)):
  print(friends[index])

for index in range(5):
  if index == 0:
    print("First iteration")
  else:
    print("not first")

#in python, the syntax for power is (2**3)

def raise_to_power(base, expo):
  total = base
  for index in range(expo-1):
    total = total * base
  return total

print(raise_to_power(2,3))
