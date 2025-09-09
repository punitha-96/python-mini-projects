import random

choices = ['rock','paper','scissors']
user_score = 0
computer_score = 0

while True:
  user = input('Choose Rock, Paper, Scissors or type quit to stop :  ').lower()

  if user == 'quit':
    break
  if user not in choices:
    print('Invalid choice. Please choose Rock, Paper, or Scissors.')
    continue

  computer = random.choice(choices)
  print(f'You chose {user}, computer chose {computer}') # Added for clarity
  if user == computer:
    print('Its a tie')
  elif (user == 'rock' and computer == 'scissors') or \
       (user == 'paper' and computer == 'rock') or \
       (user == 'scissors' and computer == 'paper'):
    print('You win!')
    user_score = user_score + 1
  else:
    print('You lose!')
    computer_score = computer_score + 1

print(f'User score is : {user_score} and computer_score is : {computer_score}')
