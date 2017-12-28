from tkinter import *
import random

def addCoin():
	if (userCoin.get()<3):
		userCoin.set(userCoin.get()+1)
	setCoin()
def subtractCoin():
	if (match.get()==1):	
		if (userCoin.get()>1):
			userCoin.set(userCoin.get()-1)
	else:
		if (userCoin.get()>0):
			userCoin.set(userCoin.get()-1)

	setCoin()
def setCoin():
	if(userCoin.get()==0):
		image_label.img = PhotoImage(file="user0.gif")
		image_label.config(image=image_label.img)
	elif(userCoin.get()==1):
		image_label.img = PhotoImage(file="user1.gif")
		image_label.config(image=image_label.img)
	elif(userCoin.get()==2):
		image_label.img = PhotoImage(file="user2.gif")
		image_label.config(image=image_label.img)
	elif(userCoin.get()==3):
		image_label.img = PhotoImage(file="user3.gif")
		image_label.config(image=image_label.img)
	image_label.pack()

def setStage():
	if(stage.get()==0):
		buttonDOWN.config(state=NORMAL)
		buttonUP.config(state=NORMAL)
		buttonOK.config(text="Aceptar")
		labelMatch.set("Partida {} \n {} - {}".format(match.get(),userWinnings.get(),computerWinnings.get()))
		labelStage.set("Selecciona la cantidad de monedas")
	elif(stage.get()==1 and match.get()%2==1):
		buttonDOWN.config(state=NORMAL)
		buttonUP.config(state=NORMAL)
		userChoice.set(userCoin.get())
		setComputerChoice()
		labelStage.set("Selecciona las monedas que cres que tiene Computer")
	elif(stage.get()==2 and match.get()%2==1):
		buttonDOWN.config(state=DISABLED)
		buttonUP.config(state=DISABLED)
		userPredict.set(userCoin.get()+userChoice.get())
		setComputerPredict()
		labelStage.set("Computer dice: En total hay {} monedas".format(computerPredict.get()))
	elif(stage.get()==1 and match.get()%2==0):
		buttonDOWN.config(state=DISABLED)
		buttonUP.config(state=DISABLED)
		userChoice.set(userCoin.get())
		setComputerPredict()
		labelStage.set("Computer dice: En total hay {} monedas".format(computerPredict.get()))
	elif(stage.get()==2 and match.get()%2==0):
		buttonDOWN.config(state=NORMAL)
		buttonUP.config(state=NORMAL)
		labelStage.set("Selecciona las monedas que cres que tiene Computer")
	elif(stage.get()==3):
		buttonDOWN.config(state=DISABLED)
		buttonUP.config(state=DISABLED)
		userPredict.set(userCoin.get()+userChoice.get())
		realCoin.set(userChoice.get()+computerChoice.get())
		showUserCoin()
		showComputerCoin()
		labelStage.set("Había {} monedas!".format(realCoin.get()))
	elif(stage.get()==4):
		buttonDOWN.config(state=DISABLED)
		buttonUP.config(state=DISABLED)
		setWinner()
		labelStage.set("{} ha ganado.".format(labelWinner.get()))
		image_computer.img = PhotoImage(file="hc.gif")
		image_computer.config(image=image_computer.img)
		labelMatch.set("Partida {} \n {} - {}".format(match.get(),userWinnings.get(),computerWinnings.get()))
		gameOver()
		match.set(match.get()+1)
		stage.set(-1)

def addStage():
	stage.set(stage.get()+1)
	setStage()
	buttonUP.pack()
	buttonDOWN.pack()

def setComputerChoice():
	if (match.get()==1):
		computerChoice.set(random.randrange(1,4))
	else:
		computerChoice.set(random.randrange(0,4))

def setComputerPredict():
	if (match.get()%2==1):
		if (userPredict.get()==0):
			computerPredict.set(computerChoice.get()+0)
		elif (userPredict.get()==1):
			computerPredict.set(computerChoice.get()+random.randrange(0,2))
		elif (userPredict.get()==2):
			computerPredict.set(computerChoice.get()+random.randrange(0,3))
		elif (userPredict.get()==3):
			computerPredict.set(computerChoice.get()+random.randrange(0,4))
		elif (userPredict.get()==4):
			computerPredict.set(computerChoice.get()+random.randrange(1,4))
		elif (userPredict.get()==5):
			computerPredict.set(computerChoice.get()+random.randrange(2,4))
		elif (userPredict.get()==6):
			computerPredict.set(computerChoice.get()+3)
	elif (match.get()%2==0):
		computerPredict.set(computerChoice.get()+random.randrange(0,4))

def setWinner():
	if (userPredict.get()==realCoin.get() and userPredict.get()!=computerPredict.get()):
		labelWinner.set("Usuario")
		userWinnings.set(userWinnings.get()+1)
	elif (computerPredict.get()==realCoin.get() and userPredict.get()!=computerPredict.get()):
		labelWinner.set("Computer")
		computerWinnings.set(computerWinnings.get()+1)
	else:
		labelWinner.set("Nadie")

def showComputerCoin():
	if(computerChoice.get()==0):
		image_computer.img = PhotoImage(file="user0.gif")
		image_computer.config(image=image_computer.img)
	elif(computerChoice.get()==1):
		image_computer.img = PhotoImage(file="user1.gif")
		image_computer.config(image=image_computer.img)
	elif(computerChoice.get()==2):
		image_computer.img = PhotoImage(file="user2.gif")
		image_computer.config(image=image_computer.img)
	elif(computerChoice.get()==3):
		image_computer.img = PhotoImage(file="user3.gif")
		image_computer.config(image=image_computer.img)
	image_computer.pack()

def showUserCoin():
	if(userChoice.get()==0):
		image_label.img = PhotoImage(file="user0.gif")
		image_label.config(image=image_label.img)
		userCoin.set(0)
	elif(userChoice.get()==1):
		image_label.img = PhotoImage(file="user1.gif")
		image_label.config(image=image_label.img)
		userCoin.set(1)
	elif(userChoice.get()==2):
		image_label.img = PhotoImage(file="user2.gif")
		image_label.config(image=image_label.img)
		userCoin.set(2)
	elif(userChoice.get()==3):
		image_label.img = PhotoImage(file="user3.gif")
		image_label.config(image=image_label.img)
		userCoin.set(3)
	image_label.pack()

def gameOver():
	if (userWinnings.get()==5 or computerWinnings.get()==5):
		buttonOK.config(text="Nueva Partida")
		buttonOK.pack()
		computerWinnings.set(0)
		userWinnings.set(0)
		match.set(0)

root = Tk()
userCoin = IntVar()
computerCoin = IntVar()
match = IntVar()
stage = IntVar()
userChoice = IntVar()
userPredict = IntVar()
computerChoice = IntVar()
computerPredict = IntVar()
realCoin = IntVar()
userWinnings = IntVar()
computerWinnings = IntVar()
labelStage = StringVar()
labelMatch = StringVar()
labelWinner = StringVar()
labelStage.set("Selecciona la cantidad de monedas")
userWinnings.set(0)
computerWinnings.set(0)
stage.set(0) 
match.set(1)
userCoin.set(1)
labelMatch.set("Partida {} \n {} - {}".format(match.get(),userWinnings.get(),computerWinnings.get()))
root.title("Chinchimoney")
root.resizable(0,0)
root.iconbitmap('icon.ico')
titleImage = Frame(root)
titleImage.grid(row=0,column=0,columnspan=2)
titleImage.config(width= 256, height=64)
titleImage.config(bd=5)
scoreBoard = Frame(root)
scoreBoard.grid(row=1,column=0,columnspan=2)
scoreBoard.config(width= 256, height=32)
scoreBoard.config(bd=5)
displayText = Frame(root)
displayText.grid(row=2,column=0,columnspan=2)
displayText.config(width= 256, height=32)
displayText.config(bd=3)
userUP = Frame(root)
userUP.grid(row=3,column=0)
userUP.config(width= 128, height=32)
userUP.config(bd=5)
userDisplay = Frame(root)
userDisplay.grid(row=4,column=0)
userDisplay.config(width= 128, height=192)

computerDisplay = Frame(root)
computerDisplay.grid(row=4,column=1)
computerDisplay.config(width= 128, height=192)

userDOWN = Frame(root)
userDOWN.grid(row=5,column=0)
userDOWN.config(width= 128, height=32)
userDOWN.config(bd=5)
buttonFrame = Frame(root)
buttonFrame.grid(row=6,column=0,columnspan=2)
buttonFrame.config(width= 256, height=32)
buttonUP = Button(userUP,text="Más",command=addCoin)
buttonDOWN = Button(userDOWN,text="Menos",command=subtractCoin)
buttonUP.pack()
buttonDOWN.pack()
Label(buttonFrame).pack()
buttonOK = Button(buttonFrame,text="Aceptar",command=addStage)
buttonOK.pack()
Label(buttonFrame).pack()
userImage = PhotoImage(file="user1.gif")
image_label = Label(userDisplay, image=userImage)
image_label.pack()
computerImage = PhotoImage(file="hc.gif")
image_computer = Label(computerDisplay, image=computerImage)
image_computer.pack()
header = PhotoImage(file="header.gif")
Label(titleImage, image=header).pack()
Label(displayText, textvariable=labelStage).pack()
Label(scoreBoard, textvariable=labelMatch).pack()
root.mainloop()
