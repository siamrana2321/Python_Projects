import random
from Game_Data import data 
import Art
import os


print(Art.logo)

Compare_A = random.choice(data)
print(f"Compare A : {Compare_A['name']}, A {Compare_A['description']}, From {Compare_A['country']}.")
print(Art.vs)
Against_B = random.choice(data)
print(f"Against B: {Against_B['name']}, A {Against_B['description']}, From {Against_B['country']}.")
# print(f"A = {Compare_A['follower_count']}, B = {Against_B['follower_count']}") ## For Debug
point = 0

def Print():
    global point
    os.system('cls')
    print(Art.logo)
    print(f"Compare A : {Compare_A['name']}, A {Compare_A['description']}, From {Compare_A['country']}.")
    print(Art.vs)
    print(f"Against B: {Against_B['name']}, A {Against_B['description']}, From {Against_B['country']}.")
    # print(f"A = {Compare_A['follower_count']}, B = {Against_B['follower_count']}")  ## For Debug
    point+=1
    Game()

def Game():
    global Compare_A
    global Against_B
    global point
    Check = input("Who has more followers? Type 'A' or 'B': ").lower()
    if Check == "a" or Check == "b":
        if Check == "a" and Compare_A['follower_count']>Against_B['follower_count']:
            print("Your Guess Is Right!!")
            Against_B = random.choice(data)
            Print()
        elif Check == "b" and Against_B['follower_count']>Compare_A['follower_count']:
            print("Your Guess Is Right!!")
            Compare_A = Against_B
            Against_B = random.choice(data)
            Print()
        else:
            os.system('cls')
            print(Art.logo)
            print("Your Lose!!")
            print(f"Your Point Is : {point}")
            exit()
    else:
        print("Invalid Input. Try Again !!!")
        Game()



Game()