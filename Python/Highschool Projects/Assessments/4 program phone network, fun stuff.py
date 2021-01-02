# Tell the user That this program will check his phone network.
# Ask the user to Enter his 10-digit phone number.
# Check the length of the phone number to be 10, not less, not more.
# If he phone number does not equal 10, kick him all.
# If the 0:3 indices is "059" tell the user that he is in the zain network.
# If the 0:3 indices is "056" tell the user that he is in the mobily network.
# If the 0:3 indices is "053" tell the user that he is in the STC network.
# If the 0:3 indices is non of the above, then kick him out.

print("This program will check your phone network")
while True:
    phone_number = input("Enter your 10-digit phone number here: ")
    if len(phone_number) != 10:
        print("Error! That is not a phone number.")
    elif phone_number[0:3] == "059":
        print("You're on the Zain network.")
        while True:
            fun_stuff = input("Welcome, anything I can do for you (commands are: cook (name of food), tell me a joke, talk to me, Play with me, Tickle): ")
            if fun_stuff[0:4] == "cook" or fun_stuff[0:4] == "Cook":
                print("cooking" + fun_stuff[4:])
            elif fun_stuff == "tell me a joke" or fun_stuff == "Tell me a joke":
                print("A man walked into the bar.... I forgot the rest")
            elif fun_stuff == "Talk to me" or fun_stuff == "talk to me":
                print("Hi, I am just like siri")
            elif fun_stuff == "Play with me" or fun_stuff == "play with me":
                print("I am a computer, I cant play.")
            elif fun_stuff == "Tickle" or fun_stuff == "tickle":
                print("hahahahahahahaha!!! Please stop")
            else:
                print("no command found.")
    elif phone_number[0:3] == "056":
        print("You're in the Mobily network")
        while True:
            fun_stuff = input("Welcome, anything I can do for you (commands are: cook (name of food), tell me a joke, talk to me, Play with me, Tickle): ")
            if fun_stuff[0:4] == "cook" or fun_stuff[0:4] == "Cook":
                print("cooking" + fun_stuff[4:])
            elif fun_stuff == "tell me a joke" or fun_stuff == "Tell me a joke":
                print("A man walked into the bar.... I forgot the rest")
            elif fun_stuff == "Talk to me" or fun_stuff == "talk to me":
                print("Hi, I am just like siri")
            elif fun_stuff == "Play with me" or fun_stuff == "play with me":
                print("I am a computer, I cant play.")
            elif fun_stuff == "Tickle" or fun_stuff == "tickle":
                print("hahahahahahahaha!!! Please stop")
            else:
                print("no command found.")
    elif phone_number[0:3] == "053":
        print("You're in the STC network")
        while True:
            fun_stuff = input("Welcome, anything I can do for you (commands are: cook (name of food), tell me a joke, talk to me, Play with me, Tickle): ")
            if fun_stuff[0:4] == "cook" or fun_stuff[0:4] == "Cook":
                print("cooking" + fun_stuff[4:])
            elif fun_stuff == "tell me a joke" or fun_stuff == "Tell me a joke":
                print("A man walked into the bar.... I forgot the rest")
            elif fun_stuff == "Talk to me" or fun_stuff == "talk to me":
                print("Hi, I am just like siri")
            elif fun_stuff == "Play with me" or fun_stuff == "play with me":
                print("I am a computer, I cant play.")
            elif fun_stuff == "Tickle" or fun_stuff == "tickle":
                print("hahahahahahahaha!!! Please stop")
            else:
                print("no command found.")
    else:
        print("Error! No network found")
        
