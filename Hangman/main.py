
def displayProgress(wordPhraseHidden, gameStart):
    displayCorrectLetters = ""
    for i in wordPhraseHidden:
        displayCorrectLetters += i
    if gameStart == True:
        print("Here is your word or phrase to guess: " + displayCorrectLetters)
    else:
        print("Here is your progress: " + displayCorrectLetters)
    




def playGame():
    lettersGuessed = []
    incorrectGuesses = 0
    incorrectGuessesAllowed = 5
    correctLettersDispalyed = 0
    correctLettersToDisplay = 0
    wordPhraseHidden = []
    
    wordPhrase = input("Please enter a word or phrase for your oppenent to guess.\n").upper()
    for char in wordPhrase:
        if char == " ":
            wordPhraseHidden.append("   ")
        else:
            wordPhraseHidden.append("_ ")
            correctLettersToDisplay += 1
    
    displayProgress(wordPhraseHidden, True)

    while incorrectGuesses < incorrectGuessesAllowed:
        letterCount = 0
        hiddenPhrasePosition = 0
        playerGuess = input("Please guess a character. \n").upper()
        lettersGuessed.append(playerGuess)

        for char in wordPhrase:
            if playerGuess == char:
                letterCount += 1
                wordPhraseHidden[hiddenPhrasePosition] = char
                hiddenPhrasePosition +=1
            else:
                hiddenPhrasePosition +=1
        
        if letterCount == 0:
            incorrectGuesses += 1
        else:
            correctLettersDispalyed += letterCount
            print("There were {totalCount} {guess}'s \n".format(totalCount = letterCount, guess = playerGuess))
            displayProgress(wordPhraseHidden, False)
            if  correctLettersDispalyed == correctLettersToDisplay:
                print("You won!")
                playAgain = input("Do you want to play again?\n").upper()
                if playAgain == "YES":
                    playGame()
                else:
                    break



playGame()







