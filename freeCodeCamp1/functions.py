#def is the key word for function

def say_hi(name):
    print("Hello "+name)

say_hi("Mike")

def cube(num):
    return num*num*num

print(cube(3))

# if statements are constructed using literal english words such as "or" "and" "not"
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

#comparison in python. Same as js, but in python we use double equals.

def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  return num3

print(max_num(2,4,5))

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num3 = float(input("Enter second number: "))

if op == "+":
  print(num1+num3)
elif op == "-":
  print(num1-num3)
elif op == "/":
  print(num1/num3)
elif op == "*":
  print(num1*num3)
else:
  print("Invalid Operator")
