######################## Non Repeating Joke Telling AI ########################

import pyttsx3 # Text to Speech Module
import pyjokes # Jokes Module

engine = pyttsx3.init() # Text to Speech Object
engine.setProperty('rate', 129) # Text to Speech

# To Creat A File
jokes_file = open('jokes.txt','a') # Open File as Append Mode

while True:
    print("You wanna hear a joke ? (y/n) :")
    engine.say("You wanna hear a joke ?") # Text to Speech
    engine.runAndWait() # Text to Speech
    check = input().lower()

    jokes_file = open("jokes.txt","r") # Open File as Read Mode
    read_jokes = jokes_file.read() # Read File
    # Split The Contents Of the File Based On New Lines And Gives A List
    all_jokes = read_jokes.split("\n")
    # print(all_jokes) # File

    if check == "y":
        print("Cooking a joke for you ...")
        engine.say("Cooking a joke for you ...") # Text to Speech
        engine.runAndWait() # Text to Speech

        joke = pyjokes.get_joke() # To Get A Joke
        while True:
            # Checks If The Joke Is Present In The Jokes.txt File or Not.
            if joke not in all_jokes:
                print(joke + "\n")
                break
            else:
                joke = pyjokes.get_joke() # To Get A Joke

        engine.say(joke) # Text to Speech
        engine.runAndWait() # Text to Speech

        jokes_file = open("jokes.txt","a") # Open File as Append Mode
        jokes_file.write(joke + "\n") # Write into File

    else:
        print("You wanna clear all jokes from the library ? (y/n) :")
        engine.say("You wanna clear all jokes from the library ?") # Text to Speech
        engine.runAndWait() # Text to Speech

        library_check = input().lower()
        if library_check == "y":
            jokes_file = open('jokes.txt','w') # Open File as Write Mode

            print("All jokes are deleted from the library.")
            engine.say("All jokes are deleted from the library.") # Text to Speech
            engine.runAndWait() # Text to Speech
        else:
            print("OK.")
            engine.say("OK.") # Text to Speech
            engine.runAndWait() # Text to Speech

        print("I think your stomach is hurting !!!\nLet's take a break ...")
        engine.say("I think your stomach is hurting. Let's take a break.") # Text to Speech
        engine.runAndWait() # Text to Speech
        break


jokes_file.close() # Close File
engine.stop() # Text to Speech