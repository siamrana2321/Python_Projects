import random
import os
from Art import logo 

print(logo)
def Blackjack():
    user_cards = []
    com_cards = []
    game_check = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game_check == "y":
        os.system('cls') # for Clearing The Terminal After One Input.
        print(logo)
        for i in range(2):
            user_cards.append(random.randint(2,11))
            com_cards.append(random.randint(2,11))
        

        user_card_sum = sum(user_cards)
        if user_card_sum == 21:
            print(f"Your cards: {user_cards}, current score: {user_card_sum}")
            print("!!! BlackJack !!!")
            print("!!! You Win !!!")
            Blackjack()
        if user_card_sum > 21 :
            user_cards[0]=1
            user_cards[1]=1
            user_card_sum = sum(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_card_sum}")
        else:
            print(f"Your cards: {user_cards}, current score: {user_card_sum}")
        # print(f"Your cards: {user_cards}, current score: {user_card_sum}")
        com_card_sum = sum(com_cards)
        print(f"Computer's first card: {com_cards[0]}")
        
        user_check = True
        while user_check:
            hit_stand = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if hit_stand == "y":
                user_cards.append(random.randint(2,11))
                user_card_sum = sum(user_cards)
                if user_card_sum>21:
                    if 11 in user_cards:
                        for index, card in enumerate(user_cards):
                            if card==11:
                                user_cards[index]=1
                                user_card_sum = sum(user_cards)
                    else:
                        print(f"Your cards: {user_cards}, current score: {user_card_sum}")
                        print("!!! You Lose !!!")
                        Blackjack()
                print(f"Your cards: {user_cards}, current score: {user_card_sum}")
                    
            else:
                print(f"Your final hand: {user_cards}, final score: {user_card_sum}")
                user_check = False

        com_check = True
        while com_check:
            if com_card_sum<17:
                com_cards.append(random.randint(2,11))
                com_card_sum = sum(com_cards)
            elif com_card_sum>21:
                print(f"Computer's final hand: {com_cards}, final score: {com_card_sum}")
                print("!!! You Win !!!")
                Blackjack()
            else:
                print(f"Computer's final hand: {com_cards}, final score: {com_card_sum}")
                com_check = False

        if com_card_sum == user_card_sum:
            print("!!! Match Draw !!!")
        elif com_card_sum > user_card_sum:
            print("!!! You Lose !!!")
        else:
            print("!!! You Win !!!")
        Blackjack()
    else:
        print("\n!!! Thanks For Playing Our Game !!!")
        exit()

Blackjack()







