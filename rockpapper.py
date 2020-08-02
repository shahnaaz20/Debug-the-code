from random import randint
import random
def win():
    return ('You win!')
def lose():
    return ('You lose!')
def rock_paper():
        player_choice = input('What do you pick? (rock, paper, scissors)')   
        random_move = randint(0, 2)
        player_choice.strip()
        moves = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(moves)
        while True:
            if player_choice == computer_choice  :
                return ('Draw!')
            elif player_choice == 'rock' and computer_choice == 'scissors':
                return (win())
            elif player_choice == 'paper' and computer_choice == 'scissors':
                return (lose())
            elif  player_choice  == 'scissors' and computer_choice == 'paper':
                return (win())
            elif player_choice  == 'scissors' and computer_choice == 'rock':
                return(lose())
            elif player_choice == 'paper' and computer_choice == 'rock':
                return (win())
            elif player_choice  == 'rock' and computer_choice == 'paper':
                return (lose())
print(rock_paper())
again = input('Do you want to play again? (y or n)').strip()
if again == 'y':
    print(rock_paper())
else:
    print("Thank you playing")

        
    
    


