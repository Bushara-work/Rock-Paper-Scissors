import random


pc_score = 0

my1_score = 0

my2_score = 0

dict = {

"rock": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

"paper": '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

"scissors": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}


#Choose game type until an option is selected
while True:    
    game_mode = input('''Select a game mode: 1 player or 2 player''')
    
    if str(game_mode) == "1" or str(game_mode) == "one" or str(game_mode) == "2" or str(game_mode) == "two":
        if game_mode == "1" or str(game_mode) == "one":
            print("Player vs Computer")
            break

        else:
            print("Player vs Player")
            break
    else:
        continue
  
#Input for choices player 1 until a valid selection and computer
#then do computer or player 2 based on 1 player or 2 player gaems
    
def game():
    global pc_score

    global my1_score

    global my2_score 
    
    while True:
        print("Player")
        choose1 = (input("Rock,Paper,Scissors\n"))

        if choose1.lower() == "rock" or choose1.lower() == "paper" or choose1.lower() == "scissors":
            break
        else:
            continue
    
    if game_mode == "2" or game_mode == "two":
        while True:
            print ("Player 2")
            choose2 = (input("Rock,Paper,Scissors\n"))

            if choose2.lower() == "rock" or choose2.lower() == "paper" or choose2.lower() == "scissors":
                print("Player 1 Chose: " + choose1 + "\tCurrent Score:" + str(my1_score) + dict[choose1] + "\n")
                print("Player 2 Chose: " + choose2 + "\tCurrent Score:" + str(my2_score) + dict[choose2] + "\n")
                if choose1 == choose2:
                    print("Tie!    Player 1 Score:" + str(my1_score)  +'\tPlayer 2 Score:' + str(my2_score))
                elif (choose1 == 'rock' and choose2 == "scissors") or (choose1 == 'paper' and choose2 == "rock") or (choose1 == 'scissors' and choose2 == "paper"):
                    my1_score = my1_score + 1
                    print("First player won! New Score:" + str(my1_score) + "\tSecond Player lost New Score:" + str(my2_score))
                else:
                    my2_score = my2_score + 1
                    print("First player lost New Score:" + str(my1_score) + "\tSecond Player Won! New Score:" + str(my2_score))
                break
            else:
                continue

    else:
          #computer choice with numbers
        choices = ("rock", "paper", "scissors")
        pc_choose = random.randint(0,2)
        print("You Chose: \t" + choose1 + "Current Score:" + str(my1_score) + "\n" + dict[choose1])
        print("Computer chose: " + choices[pc_choose] + "\tCurrent score" + str(pc_score) + "\n" + dict[choices[pc_choose]] )
    
        if choose1 == choices[pc_choose]:
            print("Tie!   Your New Score:" + str(my1_score)  +'\tComputer New Score:' + str(pc_score))
        elif (choose1 == 'rock' and pc_choose == 2) or (choose1 == 'paper' and pc_choose == 0) or (choose1 == 'scissors' and pc_choose == 1):
            my1_score = my1_score + 1
            print("You won! Your New Score:" + str(my1_score) + "\tComputer New Score:" + str(pc_score))
        else:
            pc_score = pc_score + 1
            print("You lost Your New Score:" + str(my1_score) + "\tComputer New Score:" + str(pc_score))
    

    while True:
        continue_game = input("Do you want to play again?")
        if continue_game.lower() == "yes":
            game()
            break
        elif continue_game.lower() == "no":
            print('Thank you for playing')
            break
        else:
            continue

game()
