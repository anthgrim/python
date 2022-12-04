import random

# Get choice from player and random choice for computer
def get_choices():
  options = ['rock', 'paper', 'scissors']
  player_choice = input("Enter a choice: rock, paper, scissors: ")

  if player_choice in options:
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
  else:
    return 'Error'

# Check winner
def check_win(player, computer):
  print(f"You chose: {player}. Computer chose: {computer}")

  if player == computer:
    return "It's a tie!"
    
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors. YOU WIN!"
    else:
      return "Paper covers rock. YOU LOSE!"
      
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock. YOU WIN!"
    else:
      return "Scissors cut paper. YOU LOSE!"
      
  elif player == "scissors":
    if computer == "rock":
      return "Rock smashes scissors. YOU LOSE!"
    else:
      return "Scissors cut paper. YOU WIN"

choices = get_choices()

if choices != "Error":
  result = check_win(choices["player"], choices["computer"])
  print(result)
else:
  print(f"{choices}. Unable to determine winner.")