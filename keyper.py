import random, csv
from tkinter import ttk
from tkinter import *
import pyperclip as pc
from tkinter.messagebox import askyesno, askquestion

loginFields = ['Service', 'Username', 'Password']
loginList = 'data/passwords.csv'
loginData = []
content = u'\N{COPYRIGHT SIGN}'.encode('utf-8')
text = content.decode('utf-8')

class Login:
	def __init__(self, service, username, password):
		self.service = service
		self.username = username
		self.password = password
	
	def generateRandomPassword():
		firstChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
		'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
		'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
		'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
		'W', 'X', 'Y', 'Z']
		allChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
		'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
		'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
		'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
		'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9',
		'0','!', '@', '#', '$', '%', '^', '&', '*', '(', 
		')', '{', '}', '[', ']', ':', ';', '/', '=', '+', '-', '_']
		newPasswordChars = []
		newPassword = ""
		firstCharacter = random.choice(firstChars)		
		for i in range(16):
			j = 0
			newPasswordChars.append(random.choice(allChars))
			j += 1
		newPasswordChars[0] = firstCharacter
		for i in newPasswordChars:
			newPassword += i
		
		return newPassword
	
	def setService():
		thisService = input("Service: ")
		return thisService
		setUsername()
	
	def setUsername():
		thisUsername = input("Username: ")
		return thisUsername
		
			
	def displayLogin(self):
		print(f"Your new login information for {self.service} is:\nUsername: {self.username}\nPassword: {self.password}")


def initializeLoginSheet():
	confirmation = askyesno(title='Confirmation',
				message ="This will clear out all your data from the spreadsheet. Do you wish to proceed?")
	
	if confirmation:
		
		with open(loginList, 'w', newline="") as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerow(loginFields)

def addLoginToLoginSheet(service, username, password):
	loginData.delete()
	itemData = [service, username, password]
	loginData.append(itemData)
	with open(loginList, 'a', newline="") as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerows(loginData)

class App:
	def mainApp():
		app = Tk()
		app.geometry("500x500")
		app.title("Keyper by MathiesenWare.com")
		
		appFrame = Frame(app, bg="black")
		appFrame.config(width=500, height=500)
		appFrame.pack()
		
		appHeaderFrame = Frame(appFrame, bg="black")
		appHeaderFrame.place(x=0, y=0, anchor=NW)
		appHeaderFrame.config(width=500, height=100)
		
		appHeader = Label(appHeaderFrame, text="Keyper\nBy MathiesenWare.com", bg="black", fg="white")
		appHeader.place(relx=0.5, x=0, y=0, anchor=N)
		
		appFooterFrame = Frame(appFrame, bg="black")
		appFooterFrame.config(width=500, height=55)
		appFooterFrame.place(relx=0.5, rely=0.9, x=0, y=0, anchor=N)
		
		appFooter = Label(appFooterFrame, text=f"Copyright: {text} 2022 - Joseph T. Mathiesen @ www.mathiesenware.com", bg="black", fg="white")
		appFooter.place(relx=0.5, rely=0.5, x=0, y=10, anchor=S)
		
		def viewMenu():
			
			def goToMainMenu():
				with open(loginList, 'r', newline="") as csvfile:
					csvreader = csv.reader(csvfile)
					for row in csvreader:
						loginData.clear()
				viewFrame.destroy()
				passwordTable.destroy()
				mainMenu()
			
			def clearSpreadsheet():
				confirmation = askyesno(title='Confirmation',
				message ="This will clear out all your data from the spreadsheet. Do you wish to proceed?")
				
				if confirmation:
					with open(loginList, 'w', newline="") as csvfile:
						csvwriter = csv.writer(csvfile)
					passwordDataFrame.destroy()
					initializeLoginSheet()
					with open(loginList, 'r', newline="") as csvfile:
						csvreader= csv.reader(csvfile)
						for row in csvreader:
							loginData.clear()
					viewMenu()
			
			def copyPassword():
				selected = passwordTable.focus()
				selectedItems = passwordTable.item(selected)
				password = f"{selectedItems['values'][2]}"
				copiedPassword = str(password)
			
				pc.copy(copiedPassword)
										
			with open(loginList, 'r', newline="") as csvfile:
				csvreader = csv.reader(csvfile)
				loginFields = next(csvreader)
				for row in csvreader:
					loginData.append(row)
			
			viewFrame = Frame(appFrame, bg="#000000")
			viewFrame.config(width=500,height=350)
			viewFrame.place(x=0, y=270, anchor=W)
			
			passwordDataFrame = Frame(viewFrame, relief="raised", bg="black")
			passwordDataFrame.config(width=480, height=400)
			passwordDataFrame.place(relx=0.5, rely=0.5, x=0, y=0, anchor=CENTER)
			
			passwordTable = ttk.Treeview(passwordDataFrame)
			
			passwordTable['columns'] = ['Service', 'Username', 'Password']
			
			passwordTable.column("#0", width=0, stretch=NO)
			passwordTable.column("Service", anchor=CENTER, width=155)
			passwordTable.column("Username", anchor=CENTER, width=155)
			passwordTable.column("Password", anchor=CENTER, width=155)
			
			passwordTable.heading("#0", text="", anchor=CENTER)
			passwordTable.heading("Service", text="Service", anchor=CENTER)
			passwordTable.heading("Username", text="Username", anchor=CENTER)
			passwordTable.heading("Password", text="Password", anchor=CENTER)
			
			for i in range(len(loginData)):
				passwordTable.insert(parent='', index='end', iid=i,text='',values=(loginData[i]))
			
			passwordTable.place(relx=0.5, rely=0.35, x=0, y=0, anchor=CENTER)
			
			clearButton = Button(viewFrame, text="Clear Login Data", bg="#90EE90", fg="black", command=clearSpreadsheet)
			clearButton.place(relx=0.2, rely=0.9, anchor=CENTER)
			
			mainMenuButton = Button(viewFrame, text="Main Menu", bg="#90EE90", fg="black", command=goToMainMenu)
			mainMenuButton.place(relx=0.5, rely=0.9, anchor=CENTER)
			
			copyButton = Button(viewFrame, text="Copy Password", bg="#90EE90", fg="black", command=copyPassword)
			copyButton.place(relx=0.8, rely=0.9, anchor=CENTER)
		
		def addMenu():
			
			def goToMainMenu():
				addFrame.destroy()
				while len(loginData) > 0:
					loginData.clear()
				mainMenu()
			
			def showNewLogin():
				def addNewLoginToLoginSheet(service, username, password):
					itemData = [service, username, password]
					with open(loginList, 'r', newline="") as csvfile:
						csvreader = csv.reader(csvfile)
					loginData.clear()	
					loginData.append(itemData)
					serviceEntry.delete(0, END)
					usernameEntry.delete(0, END)
					with open(loginList, 'a', newline="") as csvfile:
						csvwriter = csv.writer(csvfile)
						csvwriter.writerows(loginData)
					newLoginFrame.destroy()
						
				newLoginFrame = Frame(addFrame, bg="black")
				newLoginFrame.place(x=0, y=290, anchor=W)
				newLoginFrame.config(width=500, height=100)
				
				newLoginServiceHidden = Label(newLoginFrame, text=f"{serviceEntry.get()}")
				newLoginService = Label(newLoginFrame, text=f"Service: {newLoginServiceHidden.cget('text')}", bg="black", fg="white")
				newLoginService.place(rely=0.5, anchor=SW)
				
				newLoginUsernameHidden = Label(newLoginFrame, text=f"{usernameEntry.get()}")
				newLoginUsername = Label(newLoginFrame, text=f"Username: {newLoginUsernameHidden.cget('text')}", bg="black", fg="white")
				newLoginUsername.place(rely=0.65, anchor=SW)
				
				newLoginPasswordHidden = Label(newLoginFrame, text=f"{Login.generateRandomPassword()}")
				newLoginPassword = Label(newLoginFrame, text=f"Password: {newLoginPasswordHidden.cget('text')}", bg="black", fg="white")
				newLoginPassword.place(rely=0.8, anchor=SW)
				
				addLoginButton = Button(newLoginFrame, text="Add Login", bg="#90EE90", fg="black", command=lambda: addNewLoginToLoginSheet(str(newLoginServiceHidden.cget('text')), str(newLoginUsernameHidden.cget('text')), str(newLoginPasswordHidden.cget("text"))))
				addLoginButton.place(relx=0.8, rely=0.8, anchor=SW)
			
			addFrame = Frame(appFrame, bg="#000000")
			addFrame.config(width=500,height=350)
			addFrame.place(x=0, y=270, anchor=W)
			
			addFormFrame = Frame(addFrame, bg="black")
			addFormFrame.place(x=0, y=0, anchor=NW)
			addFormFrame.config(width=500, height=350)
			
			addFormHeader = Label(addFormFrame, text="Please fill out the form", bg="black", fg="white")
			addFormHeader.place(relx=0.5, x=0, y=25, anchor=N)
			
			#Form
			
			#Service Field
			serviceEntryLabel = Label(addFormFrame, text="Service", bg="black", fg="white")
			serviceEntryLabel.place(relx=0.1, rely=0.25, anchor=CENTER) 
			
			serviceEntry = Entry(addFormFrame, width=25)
			serviceEntry.place(relx=0.5, rely=0.25, anchor=W)
			
			#Username Field
			usernameEntryLabel = Label(addFormFrame, text="Username", bg="black", fg="white")
			usernameEntryLabel.place(relx=0.1, rely=0.40, anchor=CENTER)
			
			usernameEntry = Entry(addFormFrame, width=25)
			usernameEntry.place(relx=0.5, rely=0.40, anchor=W)
			
			#Show New Login
			submitButton = Button(addFormFrame, text="Create Login", bg="#90EE90", fg="black", command=showNewLogin)
			submitButton.place(relx=0.8, rely=0.55, anchor=CENTER)
			
			mainMenuButton = Button(addFormFrame, text="Main Menu", bg="#90EE90", fg="black", command=goToMainMenu)
			mainMenuButton.place(relx=0.3, rely=0.55, anchor=CENTER)
		
		def mainMenu():
			
			def goToViewMenu():
				mainFrame.destroy()
				viewMenu()
			
			def goToAddMenu():
				mainFrame.destroy()
				addMenu()
				
			mainFrame = Frame(appFrame, bg="#fbfbfb")
			mainFrame.config(width=500,height=350)
			mainFrame.place(x=0, y=270, anchor=W)
			
			mainOptionsFrame = Frame(mainFrame, bg="black")
			mainOptionsFrame.place(x=0, y=0, anchor=NW)
			mainOptionsFrame.config(width=500, height=350)
			
			mainOptionsHeader = Label(mainOptionsFrame, text="Please select an option", bg="black", fg="white")
			mainOptionsHeader.place(relx=0.5, x=0, y=25, anchor=N)
			
			#Options
			#Option 1: View Login Details
			viewLoginDetails = Button(mainOptionsFrame, text="View Login Details", bg="#90EE90", fg="black", command=goToViewMenu)
			viewLoginDetails.place(relx=0.5, x=0, rely=0.3, anchor=CENTER)
			#Option 2: Add Login Details
			addLoginDetails = Button(mainOptionsFrame, text="Add Login Details", bg="#90EE90", fg="black", command=goToAddMenu)
			addLoginDetails.place(relx=0.5, x=0, rely=0.45, anchor=CENTER)
			#Option 3: Initialize Spreadsheet
			initializeButton = Button(mainOptionsFrame, text="Initialize Data", bg="#90EE90", fg="black", command=initializeLoginSheet)
			initializeButton.place(relx=0.5, x=0, rely=0.6, anchor=CENTER)
			#Option 4: Quit Program
			quitProgram = Button(mainOptionsFrame, text="Quit Program", bg="#90EE90", fg="black", command=app.destroy)
			quitProgram.place(relx=0.5, x=0, rely=0.75, anchor=CENTER)
			
		mainMenu()
		 
		app.mainloop()

App.mainApp()		
