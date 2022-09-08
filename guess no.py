print("this is a game of guessiing where user enter a no  between 1 to 100 to play tha game of guess.....")
winning = 70
g = 1
KO = False
print("there are only 5 attempts \n")

while g <= 5:

    n = int(input("guess the no:-   "))
    if n > winning:
        print("u guess very high number  please input lower no...\n")
    elif n < winning:
        print("u guess the lower no please input higher no...\n")
    else:
        print("congratulations u have guess the correct no")
        print("u guess the correct no in ", g, "attempts")
        break
    print("the attempts left are", 5 - g)
    g = g + 1

if g > 5:
    print("you lose .. game over")