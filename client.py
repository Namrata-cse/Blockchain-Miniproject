from tkinter import *
from tkinter import ttk
import json

class Form:
	counter=0
	def __init__(self, window, master):
		window.title("Feedback Form")
		window.geometry('400x400')
		cc_text = Label(window ,text = "Course Code").grid(row = 0,column = 0)
		sess_text = Label(window ,text = "Session").grid(row = 1,column = 0)
		ins_text = Label(window ,text = "Instructor Name").grid(row = 2,column = 0)
		feedback_text = Label(window ,text = "Feedback").grid(row = 3,column = 0)

		cc=StringVar()
		sess=StringVar()
		ins=StringVar()
		fb=StringVar()

		cc_entry = Entry(window, textvariable=cc).grid(row = 0,column = 1)
		sess_entry = Entry(window, textvariable=sess).grid(row = 1,column = 1)
		ins_entry = Entry(window, textvariable=ins).grid(row = 2,column = 1)
		fb_entry = Entry(window, textvariable=fb).grid(row = 3,column = 1)

		self.cc=cc
		self.sess=sess
		self.ins=ins
		self.fb=fb

		btn1 = ttk.Button(window ,text="Submit", command = lambda:self.save_info(window, master)).grid(row=4,column=0)
		btn2 = ttk.Button(window ,text="Exit", command = lambda:self.exit(window, master)).grid(row=4,column=1)

	def save_info(self, window, master):
		cc_info=self.cc.get()
		sess_info=self.sess.get()
		ins_info=self.ins.get()
		fb_info=self.fb.get()
		Form.counter+=1
		file = open("results.txt", "a+")
		file.write("Transaction No: "+str(Form.counter)+", ")
		file.write("Course Code: " + cc_info + ", ")
		file.write("Session: "+ sess_info + ", ")
		file.write("Instructor Name: " + ins_info + ", ")
		file.write("Feedback: " + fb_info + "\n")
		file.close()
		print("SUBMITTED")
		window.withdraw()
		self.cc.set('')
		self.sess.set('')
		self.ins.set('')
		self.fb.set('')
		# master.deiconify()
		choose=Toplevel(window)
		choose.title("Choose")
		choose.geometry('350x100')
		l = Label(choose, text = "Thank you for submitting.")
		btn1 = ttk.Button(choose ,text="Submit another feedback", width=50, command=lambda:self.option(1, choose, window, master)).grid(row=0,column=0, pady=10, padx=10)
		btn2 = ttk.Button(choose ,text="Go back to login page", width=50, command=lambda:self.option(2, choose, window,master)).grid(row=1,column=0)

	def option(self, btn, choose, master, root):
		choose.destroy()
		if(btn==1):
			master.deiconify()
		if(btn==2):
			master.destroy()
			root.deiconify()

	def exit(self, window, master):
		window.destroy()
		master.deiconify()


