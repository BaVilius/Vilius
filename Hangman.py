def split(word) :
    return list(word)
def IsUsed(guessedLetter, usedLetters):
    for x in usedLetters:
        if guessedLetter == x:
            print("You have used this letter already")
            return True
    usedLetters.append(guessedLetter)
    return False
   

lives = 5

usedLetters = []
CorrectLetters = []

#input & handling

mWord = input("Type in your word : ")

for i in range(15):
    print("*******************************************************")
print("OK. Thanks and goodluck!")


mWList = split(mWord)

for x in mWList:
    CorrectLetters.append("_,")
          
while lives >= 1:
    i = 0
    RightGuess = False
    Used = False
    
    guessedLetter = input("Guess a letter: ")
    
    if IsUsed(guessedLetter, usedLetters):
        print(usedLetters)
        Used = True
    else:
        Used = False
        for x in mWList:
            if guessedLetter == x:
                CorrectLetters[i] = x
                RightGuess = True;
            i = i + 1
    if not RightGuess and not Used:
        print("You are wrong! : ", CorrectLetters)
     
        lives = lives - 1
    if RightGuess:
        
        print("Correct! : ", CorrectLetters)


    if CorrectLetters == mWList:
        print("Good Job!")
        print("( ͡° ͜ʖ ͡°)")
        break

    print("*******************************************************")
    print("*******************************************************")
    print("*******************************************************")
    print("*******************************************************")


    
   

