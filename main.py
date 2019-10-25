import random
print('welcome to the game of rock paper scissors.')
print('Here you will be playing against computer. The person that plays the strongest “object” is the winner of the game.')
print('1. rock \n2. paper \n3. scissors')
print('______________')
player_choice_index = int(input('enter choice number'))
while player_choice_index not in range(1,4):
    player_choice_index = int(input('invalid choice. please enter a number between 1 and 3'))
computer_choice_index = random.randrange(1,4)
if player_choice_index == 1:
    player_choice = 'rock'
elif player_choice_index == 2:
    player_choice = 'paper'
else:
    player_choice = 'scissors'
if computer_choice_index == 1:
    computer_choice = 'rock'
elif computer_choice_index == 2:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

print('player:   {}. {}'.format(player_choice_index,player_choice))
print('computer: {}. {}'.format(computer_choice_index, computer_choice))

if (player_choice_index == 1 and computer_choice_index == 2) or (player_choice_index == 2 and computer_choice_index == 1):
    winning_choice = 'paper'
elif (player_choice_index == 1 and computer_choice_index == 3) or (player_choice_index == 3 and computer_choice_index == 1):
    winning_choice = 'rock'
elif (player_choice_index == 2 and computer_choice_index == 3) or (player_choice_index == 3 and computer_choice_index == 2):
    winning_choice = 'scissors'
elif player_choice_index == computer_choice_index:
    winning_choice = 'none'
else:
    winning_choice = 'how did i reach here'
print('______________')
if winning_choice == 'none':
    print('its a tie')
elif winning_choice == 'paper':
    print('winner = paper')
    if player_choice_index == 2:
        print('congrats player')
    else:
        print('congrats computer')
elif winning_choice == 'rock':
    print('winner = rock')
    if player_choice_index == 1:
        print('congrats player')
    else:
        print('congrats computer')
elif winning_choice == 'scissors':
    print('winner = scissors')
    if player_choice_index == 3:
        print('congrats player')
    else:
        print('congrats computer')
else:
    print(winning_choice)