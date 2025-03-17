import tkinter as tk
import tkUtil as util
import os
from game import game

def newGame(frame, oldFrame = ""):
    util.clear(oldFrame)

    gameFrame = tk.Frame(frame)
    util.pack(gameFrame)

    titleFrame = tk.Frame(gameFrame)
    util.pack(titleFrame)

    title = tk.Label(titleFrame, text = "New game", font = (60))
    util.pack(title)

    nameFrame = tk.Frame(gameFrame)
    util.pack(nameFrame)

    t1 = tk.Label(nameFrame, text = "Enter name for save: ")
    util.grid(t1, 0, 0)

    saveName = tk.StringVar()
    nameEntry = tk.Entry(nameFrame, textvariable = saveName)
    util.grid(nameEntry, 0, 1)

    buttonFrame = tk.Frame(gameFrame)
    util.pack(buttonFrame)

    b1 = tk.Button(buttonFrame, text = "Return", command = lambda: createMenu(frame, gameFrame))
    util.grid(b1, 0, 0)

    b2 = tk.Button(buttonFrame, text = "Start game", command = lambda: game(True, saveName, frame, gameFrame))
    util.grid(b2, 0, 1)

def resumeGames(frame, oldFrame = ""):
    util.clear(oldFrame)

    savesFrame = tk.Frame(frame)
    util.pack(savesFrame)

    titleFrame = tk.Frame(savesFrame)
    util.pack(titleFrame)

    title = tk.Label(titleFrame, text = "Game saves", font = (60))
    util.pack(title)

    scrollFrame = tk.Frame(savesFrame)
    util.pack(scrollFrame)

    scrollBar = tk.Scrollbar(scrollFrame)
    scrollBar.pack(side = "right", fill = "y")

    saveList = tk.Listbox(scrollFrame, yscrollcommand = scrollBar.set)

    saves = os.listdir(os.getcwd() + "/saves")
    saves = sorted(saves)

    for i in saves:
        saveList.insert("end", i)
    
    saveList.pack(side = "left", fill = "both")
    scrollBar.config(command = saveList.yview)

    buttonFrame = tk.Frame(savesFrame)
    util.pack(buttonFrame)

    button = tk.Button(buttonFrame, text = "Return", command = lambda: createMenu(frame, savesFrame))
    util.pack(button)

def instructions(frame, oldFrame = ""):
    util.clear(oldFrame)

    instructionFrame = tk.Frame(frame)
    util.pack(instructionFrame)

    titleFrame = tk.Frame(instructionFrame)
    util.pack(titleFrame)

    title = tk.Label(titleFrame, text = "How to play battlehips", font = (60))
    util.pack(title)

    textFrame = tk.Frame(instructionFrame)
    util.pack(textFrame)

    text = tk.Label(textFrame, text = "something will be here")
    util.pack(text)

    buttonFrame = tk.Frame(instructionFrame)
    util.pack(buttonFrame)

    button = tk.Button(buttonFrame, text = "Return", command = lambda: createMenu(frame, instructionFrame))
    util.pack(button)

def createMenu(frame, oldFrame = ""):
    if oldFrame != "":
        util.clear(oldFrame)

    menuFrame = tk.Frame(frame)
    util.pack(menuFrame)

    titleFrame = tk.Frame(menuFrame)
    util.pack(titleFrame)

    title = tk.Label(titleFrame, text = "Battleships", font = (60))
    util.pack(title)

    buttonFrame = tk.Frame(menuFrame)
    util.pack(buttonFrame)

    button1 = tk.Button(buttonFrame, text = "New game", command = lambda: newGame(frame, menuFrame))
    button2 = tk.Button(buttonFrame, text = "Resume game", command = lambda: resumeGames(frame, menuFrame), state = "disabled")
    button3 = tk.Button(buttonFrame, text = "How to play?", command = lambda: instructions(frame, menuFrame))
    button4 = tk.Button(buttonFrame, text = "Quit", command = lambda: quit())

    util.pack(button1)
    util.pack(button2)
    util.pack(button3)
    util.pack(button4)




