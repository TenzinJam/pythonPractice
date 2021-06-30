#try-except block
# it's pretty similar to try catch in javascript
# this can also help with some mathematical operations that's not valid. such as 10/3. It will go through the except code and print invalid input. The input was valid because it was a number, but mathematically it was not possible to compute that number. Except will catch that as well.

# we can except specific kind of error in this try except block. In the example below we are using built in keywords such as ZeroDivisionError and ValueError. Depending on what kind of error it is, it will display the message accordingly.

# you can also name the error and print that error, like we did in the case of ZeroDivisionError, where we named it as "err" and then print it out. This err message returned in "integer division or modulo by zero" as specified by python, and not by the developer.

# therefore, it is not a good practice to do an umbrella except.

try:
  number = int(input("Enter a number:" ))
  print(number)
except ZeroDivisionError as err:
  print(err)
except ValueError:
  print("Invalid input")

