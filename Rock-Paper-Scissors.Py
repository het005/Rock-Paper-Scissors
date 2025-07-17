import random as rd

def Game():
        choices=["rock","paper","scissors"]
        user_choise=input("choose Rock , Paper, or Scissors:-").lower()
        computer_choise=rd.choice(choices)
        if user_choise==computer_choise:
            return("Match Tie")
        elif (
        (user_choise == 'rock' and computer_choise == 'scissors') or
        (user_choise == 'paper' and computer_choise == 'rock') or
        (user_choise == 'scissors' and computer_choise == 'paper')
    ):
               print("You Win!")
        else:
              print(f"You Lose computer cohoose {computer_choise}")

Game()
