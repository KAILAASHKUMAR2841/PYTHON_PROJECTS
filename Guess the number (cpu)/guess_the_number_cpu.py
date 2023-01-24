import random
def guessing(x):
  random_number = random.randint(1, x)
  guess = 0
  while guess != random_number:
    guess = int(input("Guess the number: "))
    if (guess > random_number):
      print("Too High. Try again! :(")
    elif (guess < random_number):
      print("Too Low. Try Again! :(")
  print(f"Hurray! You guessed the Correct_Number :) '{guess}'")

x = int(input("Enter the range of number to be guessed: "))
guessing(x)
