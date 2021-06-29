#pretty similar to js objects. On top, you can get the value by dictionary.get("key")

monthConversions = {
  "Jan": "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Jul": "July",

}

print(monthConversions["Mar"])
print(monthConversions.get("Apr"))
print(monthConversions.get("Hi", "Not a valid key"))
