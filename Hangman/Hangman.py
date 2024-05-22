import Hangman_Art as HA
import Hangman_Words as HW
import random

print(HA.logo)

lives = len(HA.stages)-1
'''print(lives)'''
print("!!! Welcome To Hangman !!!\n\n")

word = random.choice(HW.word_list)
'''print(word)'''

# guess = input("Guess a letter : ")
# for i in word:
#     if guess is i:
#         print("Right")
#     else:
#         print("Wrong")

display = []
for i in range (len(word)):
    display.append("_")
print(display)

print(HA.stages[lives])

EOG = False
while not EOG:
    guess = input("Guess a letter : ").lower()
    if guess in word:
        for index, i in enumerate(word):
            if guess is i:
                # print("Right")
                display[index] = i
    else:
        lives = lives - 1

    print(display)
    print(HA.stages[lives])
    '''print(lives)'''

    if "_" not in display:
        print("You Win!!")
        EOG = True
    elif lives == 0:
        print("Game Over!")
        EOG = True


