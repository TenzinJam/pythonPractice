#grid and nested loop is similar to js as well.
# "in" is the syntax equivalent to .includes in js.


number_grid = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [0]
]

print(number_grid[0][0])

for row in number_grid:
  for column in row:
    print(column)

def translate(phrase):
  translated = ""
  for letter in phrase:
    if letter in "aeiouAEIOU":
      translated = translated + "g"
    else:
      translated = translated + letter
  return translated


print(translate(input("Enter a phrase: ")))
