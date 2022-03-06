import random as rand
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(320, 50, window=entry1)

entry2 = tk.Entry (root)
canvas1.create_window(320, 80, window=entry2)

label1 = tk.Label(root, text = "Bottom of the range, number is included:")
canvas1.create_window(130, 50, window=label1)

label2 = tk.Label(root, text = "Top of the range, number is NOT included:")
canvas1.create_window(130, 80, window=label2)

def getRandomNumber ():
    num1 = entry1.get()
    num2 = entry2.get()
    number = rand.randrange(int(num1), int(num2))
    label3 = tk.Label(root, text=number)
    canvas1.create_window(200, 220, window=label3)

button1 = tk.Button(text="Get your number", command=getRandomNumber)
canvas1.create_window(200, 180, window=button1)

root.mainloop()