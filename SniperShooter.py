from tkinter import*
import random,time,playsound,tkinter as tk
class SniperGame:
    def shot(self,person):
        time.sleep(1)
        playsound.playsound('gunfireSound.wav')
        self.root.destroy()
        if person == "Hostage":
            print("Negative, you shot a Hostage!"),time.sleep(1)
        elif person == "Fugitive":
            print("Suspect Down..Good Job Officer!!")

    def ExitSniping(self):
        tk.messagebox.askquestion()

    def __init__(self):
        print("###Sniper Shooting###\n\nShoot the Fugitive and  not the Hostages"), time.sleep(2)
        print("Shoot on command."),time.sleep(1),print("I repeat, Shoot on Command"),time.sleep(2),print("SHOOT!\n\n")

        self.root = Tk()
        self.root.geometry('1741x622')
        self.root.config(bg='black')
      #  root.configure(cursor="scopeCursor.png")
        photo = PhotoImage(file="scene2.png")
        label = Label(self.root, image=photo).place(x=0,y=0)

        NumOfHostages = 7
        for i in range(0, NumOfHostages):
            i=random.randint(50,1650)
            j=random.randint(50,500)
            photo = PhotoImage(file="hostage.png")
            label = Label(self.root, image=photo)
            label.place(x=i-75, y=j)
            Button(self.root,text="H",height=1,width=1,bg='black',fg='white',command=lambda:self.shot("Hostage")).place(x=i,y=j)

        i=random.randint(50,1550)
        j=random.randint(50,500)
        photo = PhotoImage(file="fugitive.png")
        label = Label(self.root, image=photo)
        label.place(x=i-75, y=j)
        Button(self.root,text="F",height=1,width=1,bg='black',fg='white',command=lambda:self.shot("Fugitive")).place(x=i,y=j)

        self.root.mainloop()
s = SniperGame()

"""
        image = pyglet.image.load('scopeCursor.png')
        cursor = pyglet.window.ImageMouseCursor(image, 16, 8)
        self.root.set _mouse_cursor(cursor)
"""
