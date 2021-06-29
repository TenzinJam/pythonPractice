#

i = 1
while i <= 10:
  print(i)
  i += 1

print("Done with the loop")

secret_word = "elephant"
guess = ""
count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
  if count < guess_limit:
    guess = input("Enter your guess: ")
    count += 1
    
  else:
    out_of_guesses = True


if out_of_guesses:
  print("Out of guesses, you lose")
else:
  print("correct!!")
