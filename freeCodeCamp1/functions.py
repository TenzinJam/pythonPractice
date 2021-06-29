#def is the key word for function
# if statements are constructed using literal english words such as "or" "and" "not"
def say_hi(name):
    print("Hello "+name)

say_hi("Mike")


def cube(num):
    return num*num*num

print(cube(3))

is_male = True
is_tall = True

if is_male and is_tall:
  print("You are a tall male")
elif is_male and not(is_tall):
  print("You are a short male")
elif not(is_male) and is_tall:
  print("You are just tall")
else:
  print("You are either not male or not tall or both")
