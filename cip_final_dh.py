import random
from itertools import zip_longest

def main():
    print(introduction)
    print(scuba)
    print(welcome)
    print(f"Select:\n1 - Rules\n2 - Play")
    start = input("What do you want to do?")
    while True:
        if start == "1":
            print(rules)
            print(f"Select:\n1 - Rules\n2 - Play")
            start = input("What do you want to do?")
        else:
            start = input("Are you ready to start? Press Enter.")
            play()
            break

    #make the a dictionary of the treasures with the values
def play():
    treasures_dict = make_treasure_dictionary() #create the dictionary
    #starting values
    treasures = 0
    movement = 0
    score = 0
    round_tracker = 20
    direction = "2"
    #create an empty dictionary to save the treasures that you pick up
    loot = {}
    loot_map = {
        0:triangle0,
        1:triangle1,
        2:triangle2,
        3:triangle3,
        4:square4,
        5:square5,
        6:square6,
        7:square7,
        8:diamond8,
        9:diamond9,
        10:diamond10,
        11:diamond11,
        12:hexagon12,
        13:hexagon13,
        14:hexagon14,
        15:hexagon15
    }
    #Play continues while true
    #Play continues while true
    while movement < 19 or movement >= 0:   
        #what to do if you're going down
        if direction  == "2":
            #roll 2 dice and save the numbers
            dice1_roll, dice2_roll = roll_dice()
            print("\nYour roll:")
            #print the ASCII dice
            display_dice(dice1_roll, dice2_roll)
            #save the value the spaces moved
            summed_roll = determine_movement(treasures, dice1_roll, dice2_roll)
            #provide some information about progress 
            print_statements(summed_roll, treasures, round_tracker)
            #change the movement based on the spaces moved
            movement += summed_roll
            #as long as the movement is not at the end
            if movement < 19: 
                if movement in treasures_dict:
                    shape = get_shape(treasures_dict, movement)
                    print("You feel around in dark and you find:")
                    print_shape(shape)
                    print(f"You are on space {movement}")
                    print("\nSelect:\n1 - Yes\n2 - No")
                    choice = input("Do you want to take it?")
                    if choice == "1" and movement in treasures_dict:
                        treasures += 1
                        score += treasures_dict[movement]['value']
                        loot.update(treasure_chest(movement, treasures_dict))
                        round_tracker -=treasures
                else:
                    print("There is no treasure here. Keep searching!")
                    round_tracker -= treasures
                #if you have gone down and taken a lot of treasures and run out of air on the way down
                if round_tracker < 0:
                    print(dead)
                    print("You don't have enough oxygen!\nYou didn't make it and your treasures sank back to the bottom of the ocean.")
                    break
                print("Select:\n1 - Up\n2 - Down")
                direction = input("What direction do you want to go?")
            #if you reach the end exactly
            elif movement == 19:
                if movement in treasures_dict: #in case the last move was taking the last treasure
                    shape = get_shape(treasures_dict, movement)
                    print("You feel around in dark and you find:")
                    print_shape(shape)
                    print(f"You are on space {movement}")
                    print("\nSelect:\n1 - Yes\n2 - No")
                    choice = input("Do you want to take it?")
                    if choice == "1" and movement in treasures_dict:
                        treasures += 1
                        score += treasures_dict[movement]['value']
                        loot.update(treasure_chest(movement, treasures_dict))
                        round_tracker -=treasures
                else:
                    print("There is no treasure here. Keep searching!")
                    user_input = input("It's too dark down here.\nYou must go back up. Press Enter.")
                    direction = "1"
                    round_tracker -=treasures
            #if the movement exceeds the length of the treasure trail
            else:
                movement = 19
                if movement in treasures_dict: #in case the last move was taking the last treasure
                    shape = get_shape(treasures_dict, movement)
                    print("You feel around in dark and you find:")
                    print_shape(shape)
                    print(f"You are on space {movement}")
                    print("\nSelect:\n1 - Yes\n2 - No")
                    choice = input("Do you want to take it?")
                    if choice == "1" and movement in treasures_dict:
                        treasures += 1
                        score += treasures_dict[movement]['value']
                        loot.update(treasure_chest(movement, treasures_dict))
                        round_tracker -=treasures
                else:
                    print("There is no treasure here. Keep searching!")
                    round_tracker -= treasures
                user_input = input("It's too dark down here.\nYou must go back up. Press Enter.")
                direction = "1"
        #what to do if heading up, either by choice or because you reached the end
        if direction == "1":
            dice1_roll, dice2_roll = roll_dice()
            print("Your roll:")
            display_dice(dice1_roll, dice2_roll)
            summed_roll = determine_movement(treasures, dice1_roll, dice2_roll) 
            print_statements(summed_roll, treasures, round_tracker)
            movement -= summed_roll
            if movement >= 0 and movement in treasures_dict:
                shape = get_shape(treasures_dict, movement)
                print("You feel around in dark and you find:")
                print_shape(shape)
                print(f"You are on space {movement}.")
                print("Select:\n1 - Yes\n2 - No")
                choice = input("Do you want to take it?")
                if choice == "1":
                    treasures += 1
                    score += treasures_dict[movement]['value']
                    loot.update(treasure_chest(movement, treasures_dict))
            #if you hit a spot that has already had treasure taken on the way down
            elif movement >0 and movement not in treasures_dict and round_tracker > 0:
                print("There is no treasure here. Keep searching!")
            #losing condition
            if movement > 0 and round_tracker <= 0:
                print(dead)
                print("You don't have enough oxygen!\nYou didn't make it and your treasures sank back to the bottom of the ocean.")
                break
            #win condition
            if movement <= 0 and round_tracker >= 0:
                print("Congrats, you made it! Your score is", score)
                print("Here are your treasures:")
                draw_loot(loot, loot_map)
                break
            user_input  = input("You must go back up. Press Enter.")
            round_tracker -= treasures  

#randomly generate dice values
def roll_dice():
    dice1_roll = random.randint(1,3)
    dice2_roll = random.randint(1,3)
    return dice1_roll, dice2_roll
#show the ASCII dice
def display_dice(dice1_roll, dice2_roll):
    if dice1_roll == 1:
        lines1 = [line.rstrip() for line in one_pip.strip('\n').split('\n')]
    elif dice1_roll == 2:
        lines1 = [line.rstrip() for line in two_pip.strip('\n').split('\n')]
    else:
        lines1 = [line.rstrip() for line in three_pip.strip('\n').split('\n')]
    if dice2_roll == 1:
        lines2 = [line.rstrip() for line in one_pip.strip('\n').split('\n')]
    elif dice2_roll == 2:
        lines2 = [line.rstrip() for line in two_pip.strip('\n').split('\n')]
    else:
        lines2 = [line.rstrip() for line in three_pip.strip('\n').split('\n')]

    max_width1 = max(len(line) for line in lines1)
    max_width2 = max(len(line) for line in lines2)
    for line1, line2 in zip_longest(lines1, lines2, fillvalue=''):
        print(f"{line1.ljust(max_width1)} {line2.ljust(max_width2)}")
#Calculate how many places to move by adding up the dice and subtracting the number of treasures
def determine_movement(treasures, dice1_roll, dice2_roll):
    summed_roll = dice1_roll+dice2_roll - treasures
    if summed_roll < 0:
        summed_roll = 0
    return summed_roll 
#Create the list of shapes and the number of each shapes
def constrained_sum_sample_pos(n, total, low, high):
    """Return a randomly chosen list of n positive integers summing to total,
    with each integer in the range [low, high]. Each such list is equally likely to occur."""
    
    # Initialize an empty list to store the result
    result = []
    
    # Distribute the total into n parts
    for _ in range(n - 1):
        # Generate a random number between low and high (inclusive)
        number = random.randint(low, min(high, total - sum(result) - (n - len(result) - 1) * low))
        result.append(number)
    
    # The last number is determined to make the sum exactly total
    result.append(total - sum(result))
    
    # Shuffle the result to make it random
    random.shuffle(result)
    
    return result

#creates values for the shapes based on options
def triangle_value_choices(n):
    triangle_list = [0, 1, 2, 3]
    return(random.choices(triangle_list, k=n))
def square_value_choices(n):
    square_list = [4, 5, 6, 7]
    return(random.choices(square_list, k=n))
def dia_value_choices(n):
    dia_list = [8, 9, 10, 11]
    return(random.choices(dia_list, k=n))
def hex_value_choices(n):
    hex_list = [12, 13, 14, 15]
    return(random.choices(hex_list, k=n))
#create the treasure path
def create_shape_count():
    shape_count = constrained_sum_sample_pos(4, 20, 3, 6) #use function to generate 4 number that add up to 20 with a minimum of 3
    return shape_count
#create the dictionary that will store the treasure shapes and values
def make_treasure_dictionary():
    shape_count = create_shape_count()
    
    point_list = []
    point_list.append(triangle_value_choices(shape_count[0]))
    point_list.append(square_value_choices(shape_count[1]))
    point_list.append(dia_value_choices(shape_count[2]))
    point_list.append(hex_value_choices(shape_count[3]))
    point_list = sum(point_list, []) #point_list is in a nested list, so this line turns it into a flat list

    shape_list = []
    for i in range(4):
        if i == 0:
            for shape in range(shape_count[i]):
                shape_list.append("triangle")
        if i == 1:
            for shape in range(shape_count[i]):
                shape_list.append("square")
        if i == 2:
            for shape in range(shape_count[i]):
                shape_list.append("diamond")
        if i == 3:
            for shape in range(shape_count[i]):
                shape_list.append("hexagon")
    treasure_dict ={}
    treasure_dict = {i: {"shape": shape_list[i], "value": point_list[i]} for i in range(1,20)}
    return(treasure_dict)

#print statements 
def print_statements(summed_roll, treasures, round_tracker):   
    print(f"\nYou moved: {summed_roll} spaces.")
    if treasures == 1:
        print(f"You have {treasures} treasure.")
        if round_tracker >= 0:
            print(f"Your oxygen level is {round_tracker}.")
        else: #correction when round tracker is negative
            print("Your oxygen level is 0.")
    else:
        print(f"You have {treasures} treasures.")
        if round_tracker >= 0:
            print(f"Your oxygen level is {round_tracker}.")
        else: #correction for when round tracker is negative
            print("Your oxygen level is 0.")
#pull out the shape names from the dictionary
def get_shape(treasure_dict, movement):
    shape = treasure_dict[movement]['shape']
    return shape
#call the ASCII shape
def print_shape(shape):
    if shape == 'triangle':
        print(triangle)
    elif shape == 'square':
        print(square)
    elif shape == 'diamond':
        print(diamond)
    else:
        print(hexagon)
#create a dictionary with the shape that have been gathered
def treasure_chest(treasure_id, treasures_dict):
    treasure_chest = {}
    if treasure_id in treasures_dict:
        treasure_chest[treasure_id] = treasures_dict.pop(treasure_id)
    return treasure_chest
#Draw the treasures that have been gathered
def draw_loot(loot, loot_map):
    for key, item in loot.items():
        if item['shape'] == 'triangle' and item['value'] in loot_map:
            print(loot_map[item['value']])
        elif item['shape'] == 'square' and item['value'] in loot_map:
            print(loot_map[item['value']])
        elif item['shape'] == 'diamond' and item['value'] in loot_map:
            print(loot_map[item['value']])
        else:
            print(loot_map[item['value']])

#Instructions and welcome text
introduction = r"""
   ===       DEEP SEA ADVENTURE     ===
  ===   A GAME BY DELANIE H.      ===
 ===  CODE IN PLACE 2024       ===
"""
welcome = r"""
    Welcome to Deep Sea Adventure, inspired by the tabletop game created by Jun Sasaki and Goro Sasaki*
    In this game, you are an adventurer searching the depths of the sea for treasure. 
    Going down is easy, but as you gather more treasure, it will be harder and harder 
    to move - treasure is heavy!
    Will you be able to gather your riches and make it back to the top before your air runs out?
    *This game is not affiliated with the game makers or its producers.
    ASCII art was created by me, or from https://asciiart.website/index.php
    """
rules = r"""
    How to play: Each round will start with a roll of two dice. The sum of the dice is how
    many spaces you can move. Watch out! These dice only go up to three, so the highest movement is 6.
    There are four types of treasures: triangle, squares, diamonds, and hexagons. Each treasure has a value,
    but you won't know how much until you get back to the surface! The treasure will be more valuable
    the deeper you go. 
    After you move, you will have the option to take the treasure or leave it. Taking the treasure 
    means you have points BUT you're now holding more weight! Your movement will be reduced by 1 for each
    treasure you are carrying. You will also be using more oxygen, and you have a limited supply. You don't 
    consume any oxygen while you don't have treasures, but the time starts ticking once you pick up your
    first treasure.
    You have the choice to go up or down, but once you decide to go up, there's no turning back. You can 
    only move up, but you can pick up treasure along the way.
    Good luck, adventurer!
"""

# ASCII art
scuba = r"""
             o
        o  o
        o o o
      o
     o    ______          ______
     _ *o(_||___)________/___
   O(_)(       o  ______/    \
  > ^  `/------o-'            \
    ___/
"""
one_pip = r"""
     ______
    |      |
    |  O   |
    |______|
"""
two_pip = r"""
     ______
    | O    |
    |      |
    |_____O|
"""
three_pip = r"""
     ______
    |     O|
    |  O   |
    |O_____|
"""
triangle = r"""
   / \
  /   \
 /_____\
"""
triangle0 = r"""
   / \
  / 0 \
 /_____\
"""
triangle1 = r"""
   / \
  / 1 \
 /_____\
"""
triangle2 = r"""
   / \
  / 2 \
 /_____\
"""
triangle3 = r"""
  / \
 / 3 \
/_____\
"""
square = r"""
 ______
|      |
|      |
|______|
"""
square4 = r"""
 ______
|      |
|   4  |
|______|
"""
square5 = r"""
 ______
|      |
|   5  |
|______|
"""
square6 = r"""
 ______
|      |
|   6  |
|______|
"""
square7 = r"""
 ______
|      |
|   7  |
|______|
"""
diamond = r"""
    /\
   /  \
  /    \
  \    /
   \  /
    \/
"""
diamond8 = r"""
    /\
   /  \
  / 8  \
  \    /
   \  /
    \/
"""
diamond9 = r"""
    /\
   /  \
  / 9  \
  \    /
   \  /
    \/
"""
diamond10 = r"""
    /\
   /  \
  / 10 \
  \    /
   \  /
    \/
"""
diamond11 = r"""
    /\
   /  \
  / 11 \
  \    /
   \  /
    \/
"""
hexagon = r"""
   ____
 /      \
/        \
\        /
 \______/
"""
hexagon12 = r"""
   ____
 /      \
/   12   \
\        /
 \______/
"""
hexagon13 = r"""
   ____
 /      \
/   13   \
\        /
 \______/
"""
hexagon14 = r"""
   ____
 /      \
/   14   \
\        /
 \______/
"""
hexagon15 = r"""
   ____
 /      \
/   15   \
\        /
 \______/
"""
confetti = r"""
                                   .''.
       .''.      .        *''*    :_\/_:     .
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.'_\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =- /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.  ' 
      *            *..*         :      
        *                      
        *      
"""
dead = r"""
  .---.
 /     \
( () () )
 \  M  / 
  |HHH|
  `---'
"""

main()
