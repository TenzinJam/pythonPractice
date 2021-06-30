

employee_file = open("employees.txt", "a")
employee_file.write("\nHello villages")

employee_file.close()

# if you use a "w" then it will rewrite the file, rather than adding data.
# employee_file = open("employees.txt", "w")
# you can also use this to create a file
# html syntax can also be added using this write function. But make sure when you use "w" and when "r"
