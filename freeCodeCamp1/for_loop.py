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
