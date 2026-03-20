# you explore the temple and step on a booby trap, you fall into a pit and are impaled by spikes. You die.

# you notice the traps and avoid them, you find a chest. you open it and a tripwire behind is triggered, you are hit by an arrow and die.

#  avoids traps and doesnt open chest and notices tripwire behind it and leaves alive.

import random

def templlp():
    mason = random.randint(1,3)
    match mason:
        case 1:
            print("You enter the ancient temple and see a chest in the middle of the room.")
            print("Option 1: Open the chest")
            print("Option 2: Avoid the chest and look around")
            choice = input()
            if choice == "1":
                print("You open the chest and a tripwire behind it is triggered. You are hit by an arrow and die.")
            elif choice == "2":
                print("You avoid the chest and look around. You notice traps and avoid them, you find a chest. You open it and a tripwire behind is triggered, but you notice it and avoid it. You leave alive.")
            else:
                print("Invalid choice choose 1 or 2 you egg")
        case 2:
            print("youre dilly dallying around the temple and step on a booby trap, you fall into a pit and are impaled by spikes. You die.")
        case 3:
            pass