import turtle
import random

screen = turtle.Screen()
screen.setup(width=500,height=400)
turtle.title("Turtle Game")

def Turtle_Race():
    isGameOn = True
    color = ["red","green","blue","orange","yellow","purple"]

    turtles = []
    y_ex = -125
    for i in range(1,7):
        new_turl = turtle.Turtle(shape="turtle")
        new_turl.color(color[i-1])
        new_turl.penup()
        new_turl.goto(x=-240,y=y_ex)
        turtles.append(new_turl)
        y_ex+=50

    bet_color = turtle.textinput(title="Your Bet.",prompt='''Colors : "red","green","blue","orange","yellow","purple") \nEnter The Color :''')
    while bet_color not in color:
        bet_color = turtle.textinput(title="Your Bet.",prompt='''Color Does Not Exist.\nColors : "red","green","blue","orange","yellow","purple") \nEnter A Valid Color : ''')

    while isGameOn:
        for tur in turtles:
            if tur.xcor()>220:
                isGameOn = False
                win_color = tur.pencolor()
                if win_color == bet_color:
                    print(f"You Win !! {win_color} Is The Winner!!!")
                else:
                    print(f"You Lose !! {win_color} Is The Winner!!!")
            rnd = random.randint(0,10)
            tur.forward(rnd)
    check = turtle.textinput(title="Check",prompt="Do You Want To Play Again? ('y'/'n').")
    if check == "y":
        screen.clear()
        Turtle_Race()
    else:
        exit()

Turtle_Race()





screen.exitonclick()