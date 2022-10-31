from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title("Password Generator!")

input = Entry(root)
guessedlabel = Label(root, text = "Guessed Password- ")
torf = Label(root, text = "Did your guess match?- ")
heading = Label(root, text = "Password Generator!")
label = Label(root)

array = [[["1","2","3","4","5","6","7","8","9","0"],["Heads", "Tails"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]]]

def password():
    random_number1 = random.randint(0,9)
    random_number2 = random.randint(0,1)
    random_number3 = random.randint(0,25)

    letter1 = str(array[0][0][random_number1])
    letter2 = str(array[0][0][random_number1])
    letter3 = array[0][1][random_number2]
    letter4 = array[0][2][random_number3]
    letter5 = array[0][2][random_number3]

    generatedpass = str(letter1+letter2+letter3+letter4+letter5)
    guessedpass = str(input.get)

    label["text"] = "Your Password is- "+letter1+letter2+letter3+letter4+letter5+"!"

    guessedlabel["text"] = "Guessed Password- "+input.get()

    if(generatedpass == guessedpass):
        torf["text"] = "Did your guess match?- YES!"


btn = Button(root, text = "Generate ur Password!", command = password)
btn.place(relx = 0.5, rely = 0.5, anchor=CENTER)
heading.place(relx = 0.5, rely = 0.2, anchor=CENTER)
label.place(relx = 0.5, rely = 0.6, anchor=CENTER)
input.place(relx = 0.5, rely = 0.3, anchor=CENTER)
guessedlabel.place(relx = 0.5, rely = 0.4, anchor=CENTER)
torf.place(relx = 0.5, rely = 0.7, anchor=CENTER)


root.mainloop()