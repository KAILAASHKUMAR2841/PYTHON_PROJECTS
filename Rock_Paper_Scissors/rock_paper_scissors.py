import random

def play():
  user = input("'rock', 'paper', 'scissor':  ").lower()
  cpu = random.choice(['rock', 'paper', 'scissor'])
  print(f"Opponent: {cpu}")
  if user == cpu:
    return "TIED ::"

  if is_win(user, cpu):
    return 'You WON! :)'
  
  return 'YOU LOSE! :('

def is_win(player, opponent):
  if (player == 'rock' and opponent == 'scissor') or (player == 'scissor' and opponent == 'paper')\
     or (player == 'paper' and opponent == 'rock'):
    return True

print(play())