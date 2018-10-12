import random
import time

input("Press ENTER to roll the dice")

while True:
#1- start the dice game and roll by pressing enter or return.

    player_dice = random.randint(1, 12)

    ai_dice = random.randint(1, 12)


#2- you will see the results printed out to the screen.

    print("You rolled:", str(player_dice))

    print("The computer rolls...")
    time.sleep(3)
    print("The computer rolled a", str(ai_dice))

    if player_dice > ai_dice:
        print("You won!")
    elif ai_dice > player_dice:
        print("You lose!")
    else:
        print("Draw")

#3- you will see a prompt asking you to roll once more or quit.

    x = input("Press ENTER to roll once more and 'q' to quit.\n")

    if x == 'q':
        break



