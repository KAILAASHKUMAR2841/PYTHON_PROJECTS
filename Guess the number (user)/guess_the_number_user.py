import random
def computer_guessing(x):
  low = 1
  high = x
  feedback = ''
  while feedback != 'c':
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low
    feedback = input(f"Is {guess} too High(H), too Low(L),\
 or Correct(C)").lower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1
  print("Yay! The made the cpu guess correctly.")

computer_guessing(10)