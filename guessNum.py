###
# Välja ett tal

correctNumber = 6
numofguesses = 3

#Be om edn siffra


while (numofguesses > 0):
    print("guess a number")
    guess = int(input())
    print("you guessed")
    print(guess)

numofguesses -= 1

    #Kolla om siffran är större, mindre eller lika

    if (guess > correctNumber):
        print("You guessed too large. Try again")
    
    #, mindre eller lika

    elif(guess < correctNumber):
        print("You guessed to low. Try again")
    else:
        print("you guessed correct")

#göra tre gånger


