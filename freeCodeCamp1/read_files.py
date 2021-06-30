
# read, write, append, and read and write
# readable does not seem to be working. Error says: "file objext has no attributed 'readable'"


employee_file = open("employees.txt", "r")
print(employee_file.read())
print(employee_file.readlines())

print(employee_file.readline())

employee_file.close()

open("employee.txt", "w")
open("employee.txt", "a")
open("employee.txt", "r+")
