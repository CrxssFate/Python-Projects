import random


def get_choices():
  player_choice = input('enter a choice (rock, paper, scissors): ')
  options = ['paper', 'rock', 'scissors']
  computer_choice = random.choice(options)
  choices = {'player': player_choice, 'computer': computer_choice}
  return choices


def check_win(player, computer):
  print('You chose ' + player + ', computer chose ' + computer)
  if player == computer:
    return 'its a tie!'
  elif player == 'rock' and computer == 'scissors':
      return 'rock smashes scissors, you win!'
  elif player == 'paper' and computer == 'rock':
      return 'paper covers rock, you win!'
  elif player == 'scissors' and computer == 'paper':
      return 'scissors cut paper, you win!'
  else:
      return 'you lose!'

choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)