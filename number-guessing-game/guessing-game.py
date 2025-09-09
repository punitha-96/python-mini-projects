import random

secret_number = random.randint(1,10)
guess = None
attempts = 0

while secret_number!=guess:
  guess = int(input('Guess a number between 1 to 10 '))
  attempts = attempts + 1
  if guess < secret_number:
    print('Too low! Try Again!')
  elif guess >secret_number:
    print('Too high! Try Again!')
  else:
    print(f'Congrats! You guessed it in {attempts} attempts!')

