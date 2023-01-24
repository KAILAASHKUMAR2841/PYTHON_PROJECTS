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

guessing(10)
'''def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  while feedback != 'c':
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low
    feedback = input(f"Is {guess} too High(H), too Low(L), or Correct(C)").lower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1
  print(f"Yay! computer guessed the number correctly")
computer_guess(10)'''