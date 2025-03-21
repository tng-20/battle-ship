import tkinter as tk
import tkUtil as util
import os
from random import randint
from time import sleep

class user:
    def __init__(self, name: str, ships, attacks = []):
        self.name = name
        self.ships = ships  # Stores ship positions
        self.attacks = [] if attacks == [] else attacks  # Tracks attacked positions

    def placeShips(self, positions):
        if len(positions) == 5:
            self.ships = positions

    def attack(self, x, y, opponent):
        if (x, y) in self.attacks:
            return "aa"
        self.attacks.append((x, y))
        return "hit" if (x, y) in opponent.ships else "miss"

    def allSunk(self, opponent):
            return all(pos in opponent.attacks for pos in self.ships)

class grid:
    def __init__(self, sizeX: int , sizeY: int):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = [["empty"] * self.sizeX for i in range(self.sizeY)]
        self.buttonGrid = []
        self.labelGrid = []

    def getPos(self, pos):
        return self.grid.index(pos)

    def place(self, posX: int, posY: int, item: str):
        self.grid[posX][posY] = item

    def buttonAction(self, state, x, y):
        self.buttonGrid[x][y]["state"] = state

    def buttonActionAll(self, state):
        for i in self.buttonGrid:
            for x in i:
                x["state"] = state
    
    def getPosI(self, x, y):
        return self.grid[x][y]
        
    def createButtonGrid(self, frame, clickHandler):
        letters = [chr(i + 65) for i in range(self.sizeX)]
        numbers = [i + 1 for i in range(self.sizeX)]
        buttonFrame = tk.Frame(frame)
        for x, row in enumerate(self.grid):
            tempRow = []
            for y, column in enumerate(row):
                button = tk.Button(buttonFrame, text = str(x) + "," + str(y), bg = "grey", command = lambda y = y, x = x: clickHandler(x, y))
                button.grid(row = x, column = y)
                self.place(x, y, letters[x] + str(numbers[-y - 1]))
                tempRow.append(button)
            self.buttonGrid.append(tempRow)
        return buttonFrame
    
    def createLabelGrid(self, frame):
        labelFrame = tk.Frame(frame)
        for x, row in enumerate(self.grid):
            tempRow = []
            for y, column in enumerate(row):
                label = tk.Label(labelFrame, text = "   ", bg = "grey")
                label.grid(row = x, column = y)
                tempRow.append(label)
            self.labelGrid.append(tempRow)
        return labelFrame
    
    def updateLabel(self, x, y, result = "", colour = ""):
        if result != "":
            if result == "hit":
                self.labelGrid[x][y]["bg"] = "red"
            else:
                self.labelGrid[x][y]["bg"] = "black"
        elif colour != "":
            self.labelGrid[x][y]["bg"] = colour

    def updateButton(self, x, y, result):
        if result == "hit":
            self.buttonGrid[x][y]["bg"] = "red"
        else:
            self.buttonGrid[x][y]["bg"] = "black"





####################### ---MAIN--- ###########################




def game(newGame: bool, saveName, frame, oldFrame = ""):
    def save():
        saveFile = open(os.getcwd() + "/saves/" + saveName + ".txt", "w")
        playerItems = [player.ships, player.attacks]
        computerItems = [computer.ships, computer.attacks]
        splitPI = ",".join(x for i in playerItems for x in i)
        splitCI = ",".join(x for i in computerItems for x in i)
        saveFile.write(splitPI + "\n")
        saveFile.write(splitCI)
        saveFile.close()
    
    def load():
        saveFile = open(os.getcwd() + "/saves/" + saveName + ".txt", "r")
        playerItem = saveFile.readline().strip()
        computerItem = saveFile.readline().strip()
        saveFile.close()
        playerItems = playerItem.split(",")
        computerItems = computerItem.split(",")
        playerShips = playerItems[0: 5]
        computerShips = computerItems[0: 5]
        playerAttacks = playerItems[6:]
        computerAttacks = computerItems[6:]
        
        return playerShips, playerAttacks, computerShips, computerAttacks

    def confirm():
        if len(selectedPositions) < 5:
            message.set("Not enougth boats")
        else:
            util.clear(selectionFrame)
            util.clear(confirmFrame)
            player.ships = selectedPositions
            gameScreen()

    def selectPosition(x, y):
        if len(selectedPositions) < 5 and (x, y) not in selectedPositions:
            selectedPositions.append((x, y))
            playerGrid.buttonGrid[x][y]["bg"] = "blue"
        elif len(selectedPositions) >= 5 and (x, y) not in selectedPositions:
            selectedPositions.append((x, y))
            oldX, oldY = selectedPositions[0]
            playerGrid.buttonGrid[oldX][oldY]["bg"] = "grey"
            playerGrid.buttonGrid[x][y]["bg"] = "blue"
            selectedPositions.pop(0)

    def gameScreen():
        gridFrames = tk.Frame(gameFrame)

        tG = targetGrid.createButtonGrid(gridFrames, playerTurn)
        tG.grid(row = 0, column = 0, padx = 10, pady = 10)

        #fG = playerGrid.createLabelGrid(gridFrames)
        #fG.grid(row = 0, column = 1, padx = 10, pady = 10)

        util.grid(tG, 0, 0)

        #util.grid(fG, 0, 1)

        util.pack(gridFrames)

        print(player.ships)

        for i in pA:
            x, y = targetGrid.getPos(i)
            targetGrid.updateButton(x, y, player.attack(x, y, computer))

        infoFrame = tk.Frame(gameFrame)
        util.pack(infoFrame)

        boatList = tk.Listbox(infoFrame)
        util.pack(boatList)

        for x, y in player.ships:
            boatList.insert("end", targetGrid.getPosI(x, y))

    def playerTurn(x, y):
        result = "aa"
        while result == "aa":
            result = player.attack(x, y, computer)
        targetGrid.updateButton(x, y, result)
        #save()
        if computer.allSunk(player):
            winScreen()
        else:
            computerTurn()

    def computerTurn():
        targetGrid.buttonActionAll("disabled")
        posObtain = False
        while not(posObtain):
            cx = randint(0, 9)
            cy = randint(0, 9)
            if (cx, cy) not in computer.attacks:
                posObtain = True
        computer.attack(cx, cy, player)
        #save()
        if player.allSunk(computer):
            winScreen()
        else:
            targetGrid.buttonActionAll("normal")
            for ax, ay in player.attacks:
                targetGrid.buttonAction("disabled", ax, ay)

    def winScreen():
        from mainMenu import createMenu      
        util.clear(gameFrame)

        winFrame = tk.Frame(frame)
        util.pack(winFrame)

        if computer.allSunk(player):
            text = tk.Label(winFrame, text = "You have won")
        elif player.allSunk(computer):
            text = tk.Label(winFrame, text = "You have lost")

        button = tk.Button(winFrame, text = "Return to menu", command = lambda: createMenu(frame, winFrame))

        util.pack(text)
        util.pack(button)

    util.clear(oldFrame)

    gameFrame = tk.Frame(frame)
    util.pack(gameFrame)

    pS, pA, cS, cA = [], [], [], []

    if newGame:
        playerGrid = grid(10, 10)
        selectedPositions = []

        selectionFrame = tk.Frame(gameFrame)
        util.pack(selectionFrame)
        util.pack(playerGrid.createButtonGrid(selectionFrame, selectPosition))

        confirmFrame = tk.Frame(gameFrame)
        util.pack(confirmFrame)

        message = tk.StringVar()
        errorMessage = tk.Label(confirmFrame, textvariable = message)
        util.pack(errorMessage)

        b1 = tk.Button(confirmFrame, text = "confirm", command = confirm)
        util.pack(b1)
        player = user("user", selectedPositions)
        computerSP = []
        while len(computerSP) < 5:
            pos = (randint(0, 9), randint(0, 9))
            if pos not in computerSP and pos not in selectedPositions:
                computerSP.append(pos)
        print(computerSP)
        temp = []
        for x, y in computerSP:
            temp.append(playerGrid.getPosI(x, y))
        print(temp)
        computer = user("computer", computerSP)       
    else:
        pS, pA, cS, cA = load()
        player = user("user", pS, pA)
        computer = user("computer", cS, cA)
        gameScreen()

    targetGrid = grid(10, 10)    

root = tk.Tk()
root.resizable(True, True)

game(True, "test", root)

root.mainloop()
