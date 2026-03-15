import random
from tkinter import W

def nochilling():
    whichauramcgee = random.randint(1, 6)
    match whichauramcgee:
        case 1:
            print("you chased a monkey around and you slipped on his banana peel")
            return -5, -7, 0
        case 2:
            print("you licked a toad")
            cheekybugger = random.randint(1, 5)
            if cheekybugger <= 2:
                print("youre feeling a little funny")
                return -2, -67, 1
            elif cheekybugger == 3:
                print("the animatronics get a little quirky at night")
                print("the fred is here")
                return 0, -5, 2
            else:
                print("what was the point man")
                return -10, 0, 0
        case 3:
            return 0, 0, 0
    return 0, 0, 0