
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tenzin"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends[1] = "Daniel"
print(friends[1])


# append, extend, insert, remove, clear, pop, count, index, sort
lucky_number = [4, 8, 15, 16, 23, 42]
friends.append("Tashi")
friends.insert(1, "Lhamo")
friends2 = friends.copy()
print("new list", friends2)
name_sorted = friends.sort()
print("sorted", name_sorted)
print(friends.index("Tashi"))
print(friends.count("Lhamo"))
friends.remove("Jim")
friends.clear()
friends.extend(lucky_number)
friends.pop()
number_sorted = lucky_number.sort()
print(lucky_number.reverse())
print(number_sorted)
print(friends)

