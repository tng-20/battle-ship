import tkinter as tk
import mainMenu

root = tk.Tk()
root.title("Battleship Game")
root.geometry("800x500")

mainMenu.createMenu(root)

root.mainloop()
