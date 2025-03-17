import tkinter as tk

def clear(frame):
    if frame != "":
        frame.destroy()

def pack(item):
    item.pack(padx = 10, pady = 10)

def grid(item, row, column):
    item.grid(row = row, column = column, padx = 10, pady = 10)