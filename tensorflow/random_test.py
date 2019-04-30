# Function to get random value in range [-1, 1]

import random

def getRandom():
    number = random.random()
    minus = random.random()

    print("Minus: ", minus)

    if (minus < 0.5):
        number = number * -1
    print("Random float: ", number)
    return number

getRandom()