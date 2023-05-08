print ("HUNGER GAMES")
a = str(input("You've been put with the forest behind you, weapons infront, a big guy to your right and a child to your left. Will you go forward, backwards, left or right?"))
if a == "forward" or a == "Forward":
    b = str(input("You've managed to grab a bow and 2 arrows. The big guy is running at you. Do you try to shoot or run?"))
    if b == "shoot" or b == "Shoot":
        print ("You miss..... the big guys gets to you and snaps your neck.")
    elif b == "run" or b == "Run":
        c = str(input("You've escaped to the forest and it's already getting dark. You can either find wood for a fire or try to find shelter. "))
        if c == "find wood" or c == "wood" or c == "Wood" or c == "Find Wood":
            d = str(input("You go out to search for wood. You've collected a big pile, but you see someone. They have a similar build to you and have a small pocket knife. Do you run with your wood, drop your wood and run or fight?"))
            if d == "fight" or d == "Fight":
                #This whole section for the next 45 lines is the fight made by SEBASTIAN
                import random
                data = True
                #health is the opponents health
                health = 200
                #helth2 is your health
                health2 = 200
                while data:
                    d = [ random.randint(1, 2) for _ in range(1) ]
                    a = str(input("Fight!    Punch:50 (50%)    Kick:75 (33%)"))
                    print ("Opponents health:",health)
                    if health <= 0:
                        data = False
                        z = str(input("You run away with the loot you have gathered from the body."))
                        #This is where the story carries on if you win the fight
                    elif a == "Punch" or a == "punch":
                       b = [ random.randint(1, 2) for _ in range(1) ]
                    if b == [1]:
                        health = health - 50
                    elif b == [2]:
                           health = health
                    elif a == "Kick" or a == "kick":
                        c = [ random.randint(1, 3) for _ in range(1) ]
                    if c == [1]:
                        health = health - 75
                    elif c == [2]:
                        health = health
                    if health2 <= 0:
                        data = False
                        e = print("You lost the battle. You have lost the hunger games.")
                        #This is when you die
                    elif d == [1]:
                        health2 = health2 - 50
                        print("You were punched! Your health is now:",health2)
                    elif d == [2]:
                        health2 = health2
