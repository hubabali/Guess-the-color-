import random

colors = ["R","G","B","Y","W","O"]
tries = 10

codeLength = 4 #hwo long the code will be

#make the computer create a code
def generateCode():
    code = []
    for _ in range(codeLength):
        color = random.choice(colors)
        code.append(color)

    return code

def guessCode():
    
    while True:
        guess = input("Guess: ").upper().split(" ")
        if len(guess) != codeLength:
            print(f"you must guess {codeLength} colors, try again")
            continue

        for color in guess:
            if color not in colors:
                print(f"invalid color: {color}. Try again")
                break
        else:
            break
    
    return guess
    

def checkCode(guess, realCode):
    #make a dictionary
    colorCounts = {}
    #keep track of colors in the correct and incorrect positions
    correct = 0
    incorrect = 0

    #store inside ColorCount dictionary 
    for color in realCode: 
        if color not in colorCounts:
           #add key to dictionary
            colorCounts[color] = 0
        colorCounts[color] += 1
    #zip takes the two arguments and combines them into tubles 
    for guessColor, realColor in zip(guess, realCode):
        #decrease count from dictionary to mark that the color is in the correct position
        if guessColor == realColor:
            correct += 1
            colorCounts[guessColor] -= 1

    #same thing but for if the guess is in the wrong spot
    for guessColor, realColor in zip(guess, realCode):
        if guessColor in colorCounts and colorCounts[guessColor] > 0:
            incorrect += 1
            colorCounts[guessColor] -= 1

    return correct, incorrect


def game():
    print(f"welcome to the Color Guessing Game, you have {tries} tries to guess the code")
    print("the valid colors are", *colors)



    code = generateCode()
    for attempts in range(1, tries + 1):
        guess = guessCode()
        correct, incorrect = checkCode(guess, code)
        
        if correct == codeLength:
            print(f"YOU WIN you gussed the code in {attempts} Tries")
            break
        
        
        print(f"Correct positions: {correct}. Incorrect poitions: {incorrect}. ")

    else:
        print("you ran out of tries, the code was:" *code) #prints code spaced out

if __name__ == "__main__":
    game()