## Guess the Word python application made by Michael Lian Gau
## This mini project is one of the project suggestion from r/beginnerprojects

import csv
import os
import random
import tkinter

os.getcwd()
wordsList = []
wordArr = []
wordLen = 0
wordFind = []
playerLives = 3

def startGame():
    letEntry.delete(0)
    stLbl.config(text = "Guess the Word")
    with open('words.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = '\n')
        for row in csv_reader:
            wordsList.append(row[0])

    global wordLen
    global playerLives
    playerLives = 3
    randomizeWord = random.randint(0, (len(wordsList)-1)) #Randomize word to use

    deWord = wordsList[randomizeWord]
    #print(deWord)
    #print(len(deWord))
    
    wordLen = len(deWord)

    for letter in range(len(deWord)):
        wordArr.append(deWord[letter])
        wordFind.append("_")

    #print(wordArr)
    #print(wordFind)
    print("Guess the word!")

    wordLbl.config(text = wordFind)
    startBtn.grid_forget()
    loserBtn.grid(row = 3, column = 0, padx = 5, pady = 5)
    livesLbl.grid(row = 2, column = 0)
    livesLbl.config(text = "Tries: " + str(playerLives))
    letEntry.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nswe')
    letEntry.focus()

def checkLetter(event = None):
    letterInput = letEntry.get()
    global wordLen
    global playerLives
    
    for letter in range(len(wordArr)):
        if letterInput in wordArr[letter]:
            if letterInput in wordFind[letter]:
                print("\nYou have already input that!")
            else:
                wordFind[letter] = letterInput
                wordLen -= 1
                print(wordFind)
                wordLbl.config(text = wordFind)
                
    if letterInput not in wordArr:
        playerLives -= 1
        livesLbl.config(text = "Tries: " + str(playerLives))
    
    if (playerLives == 0):
        giveUp()
    
    if (wordLen == 0):
        stLbl.config(text = "You have WON!")
        loserBtn.grid_forget()
        letEntry.grid_forget()
        livesLbl.grid_forget()
        startBtn.grid(row = 2, column = 0, padx = 5, pady = 5)
        startBtn.config(text = "Restart?")
        wordFind.clear()
        wordArr.clear()

def giveUp():
    stLbl.config(text = "LOOOOOOSERRRRR!!!!\n the word is:")
    loserBtn.grid_forget()
    letEntry.grid_forget()
    livesLbl.grid_forget()
    startBtn.grid(row = 2, column = 0, padx = 5, pady = 5)
    startBtn.config(text = "Restart?")
    wordLbl.config(text = wordArr)
    wordFind.clear()
    wordArr.clear()
    

mw = tkinter.Tk()
mw.title("Guess the Word!")
f1 = tkinter.Frame(mw)
f1.grid(row = 0)

f2 = tkinter.Frame(mw)
f2.grid(row = 1)

stLbl = tkinter.Label(f1, text = "Guess the word!", font = ("Courier", 20))
stLbl.grid(row = 0, column = 0, columnspan = 3, sticky = 'nswe', padx = 10, pady = 5)

wordLbl = tkinter.Label(f2, font = ("Courier", 15))
wordLbl.grid()

letEntry = tkinter.Entry(f2, width = 5, font = ("Courier", 15))

startBtn = tkinter.Button(f2, text = "Start", font = ("Courier", 15), command = startGame)
startBtn.grid(row = 2, column = 0, padx = 5, pady = 5)

loserBtn = tkinter.Button(f2, text = "Give Up?",  font = ("Courier", 15), command = giveUp)

livesLbl = tkinter.Label(f2, text = "Tries: 3", font = ("Courier", 13))

mw.bind("<Return>", checkLetter)

mw.mainloop()