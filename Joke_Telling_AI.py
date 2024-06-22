######################## Joke Telling AI - (Joke Can Repeat) ########################

import pyttsx3 # Text to Speech Module
import pyjokes # Jokes Module

engine = pyttsx3.init() # Text to Speech Object
engine.setProperty('rate', 129) # Text to Speech


while True:
    print("You wanna hear a joke ? (y/n) :")
    engine.say("You wanna hear a joke?") # Text to Speech
    engine.runAndWait() # Text to Speech
    check = input().lower()

    if check == "y":
        print("Cooking a joke for you ...")
        engine.say("Cooking a joke for you ...") # Text to Speech
        engine.runAndWait() # Text to Speech

        joke = pyjokes.get_joke() # To Get A Joke
        print(joke + "\n")
        engine.say(joke) # Text to Speech
        engine.runAndWait() # Text to Speech

    else:
        print("I think your stomach is hurting !!!\nLet's take a break ...")
        engine.say("I think your stomach is hurting. Let's take a break.") # Text to Speech
        engine.runAndWait() # Text to Speech
        break
    engine.stop() # Text to Speech