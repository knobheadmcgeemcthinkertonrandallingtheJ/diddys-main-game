import random

def GoSomewhere():
    x = random.randint(1, 3)
    print("Go somewhere")
    match x: 
        case 1:
            print("You go to the waterfall")
        case 2:
            print("You go to the cave")
        case 3:
            print("You go to the ancient temple")
    return x 


