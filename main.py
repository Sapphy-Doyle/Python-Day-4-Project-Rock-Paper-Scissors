import random

rock = '''
Rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def game_loop():

  print("Welcome to rock, paper, scissors!")
  user_choice = int(input("Please input 1 for rock, 2 for paper, or 3 scissors:\n")) - 1
  
  computer_choice = random.randint(0, 2)
  
  if user_choice >= 3 or user_choice < 0:
    print("You didn't make a vaild selection. Looks like you lose!")
    game_loop()
  else:
  
    game_list = [rock, paper, scissors]
  
    print("You chose:")
    print(game_list[user_choice])
    print("The computer chose:")
    print(game_list[computer_choice])
  
    if user_choice == 0 and computer_choice == 2:
      print("You win!\n")
      game_loop()
    elif computer_choice > user_choice:
      print("You lose!\n")
      game_loop()
    elif user_choice > computer_choice:
      print("You win!\n")
      game_loop()
    elif user_choice == computer_choice:
      print("It's a draw!\n")
      game_loop()
    elif computer_choice == 0 and user_choice == 2:
      print("You lose!\n")
      game_loop()

game_loop()
