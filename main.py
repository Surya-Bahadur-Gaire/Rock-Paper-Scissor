from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint


#main window
root=Tk()
root.title("Rock Paper Scissors")
#root.geometry("1550X800")
root.configure(bg="brown")
#img background
#root.ImageTk.PhotoImage(file="images\img1")

#inserting image for rock paper scissors 
#for user
rock_img=ImageTk.PhotoImage(Image.open("rock3.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper2.png"))
scissor_img=ImageTk.PhotoImage(Image.open("scissor3.png"))
#for computer
Com_rock_img=ImageTk.PhotoImage(Image.open("rock3.png"))
Com_paper_img=ImageTk.PhotoImage(Image.open("paper2.png"))
Com_scissorimg=ImageTk.PhotoImage(Image.open("scissor3.png"))

#placing picture
user_label=Label(root,image=rock_img,bg="brown",bd=5)
user_label.grid(row=1,column=4)
com_label=Label(root,image=rock_img,bg="brown",bd=5)
com_label.grid(row=1,column=0)


#scores
playerscore=Label(root,text=0,font=100,bg="brown",fg="white")
playerscore.grid(row=1,column=3)
computerscore=Label(root,text=0,font=100,bg="brown",fg="white")
computerscore.grid(row=1,column=1)

#placing button for user
rock_btn=Button(root,text="ROCK",command=lambda:updateChoice("rock_btn"),bd=10,width=15,height=2,bg="green",fg="white",font=("times new roman",20,"bold"))
rock_btn.grid(row=2,column=1)
paper_btn=Button(root,text="PAPER",command=lambda:updateChoice("paper_btn"),bd=10,width=15,height=2,bg="orange",fg="white",font=("times new roman",20,"bold"))
paper_btn.grid(row=2,column=2)
scissor_btn=Button(root,text="SCISSOR",command=lambda:updateChoice("scissor_btn"),bd=10,width=15,height=2,bg="blue",fg="white",font=("times new roman",20,"bold"))
scissor_btn.grid(row=2,column=3)

#indicators
user_indicator=Label(root,text="PLAYER",font=("times New Roman",40),bg="brown",fg="white")
user_indicator.grid(row=0,column=3)
com_indicator=Label(root,text="COMPUTER",font=("times New Roman",40,),bg="brown",fg="white")
com_indicator.grid(row=0,column=1)

#messages
msg=Label(root,font=("times new roman",16,"bold"),bg="brown",fg="white")
msg.grid(row=3,column=2)

choices=["rock_btn","paper_btn","scissor_btn"]

#updating picture or functional part
def updateChoice(x):
    #computer
    com_Choices=choices[randint(0,2)]
    if com_Choices=="rock_btn":
        com_label.configure(image=rock_img)
    elif com_Choices=="paper_btn":
        com_label.configure(image=paper_img)
    else:
        com_label.configure(image=scissor_img)


    #for user
    if x=="rock_btn":
        user_label.configure(image=rock_img)
    elif x=="paper_btn":
         user_label.configure(image=paper_img)
    else:
         user_label.configure(image=scissor_img)

    winnerScore(x,com_Choices)

#updating message
def updateMessage(x):
    msg['text']=x

#update user score
def updateUserScore():
    score=int(playerscore["text"])
    score +=1
    playerscore["text"]=str(score)

#update computer score
def updateComputerScore():
    score=int(computerscore["text"])
    score +=1
    computerscore["text"]=str(score)

#check winner score
def winnerScore(player,computer):
    if player==computer:
        updateMessage("It is a Tie")
    elif player=="rock_btn":
        if computer=="paper_btn":
            updateMessage("COMPUTER WIN. player lose.")
            updateComputerScore()
        else:
            updateMessage("PLAYER WIN. computer lose")
            updateUserScore()
    elif player=="paper_btn":
        if computer=="scissor_btn":
            updateMessage("COMPUTER WIN. player lose.")
            updateComputerScore()
        else:
            updateMessage("PLAYER WIN. computer lose")
            updateUserScore()
    elif player=="scissor_btn":
        if computer=="rock_btn":
            updateMessage("COMPUTER WIN. player lose.")
            updateComputerScore()
        else:
            updateMessage("PLAYER WIN. computer lose")
            updateUserScore()
    else:
        pass
#declearing winner


root.mainloop()