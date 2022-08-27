"""
again = True
while again:
    print(random.randint(1,6))
    another_role = input("Want to roll again? (y/n): ")
    if another_role.lower() == "y":
        continue
    else:
        break
"""
import random
from tkinter import *

root = Tk()
root.geometry("400x400")

l1 = Label(root, font=("times", 200))
def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(number)}')
    l1.pack()


b1 = Button(root, text="Role the dice", command=roll)
b1.place(x=170, y=300)

root.mainloop()