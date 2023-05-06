#hello seb i made a change to the code 
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
                e = str(input("You run at him and he is caught of guard. You tackle him to the floor and he is knocked unconcious"))
