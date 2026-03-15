from donotchillonhim import nochilling

health, cheekigan = 100, 67

def main():
    global health, cheekigan
    while True:
        print("You are a big egghead in the jugnle")
        print("Option 1: Go chase the animals or something")
        print("Option 2: Go somewhere")
        print("Option 3: Do something else")
        match input():
            case "1":
                healthigan, cheekiganigan, WhatsHappening = nochilling()
                health += cheekiganigan
                cheekigan += cheekiganigan
                if healthigan != 0:
                    print("you " + (healthigan < 0 and "lost " or "gained ") + str(abs(healthigan)) + " health")
            case "2":
                place = 1
            case "3":
                pass
            case _:
                print("Invalid option")
main()