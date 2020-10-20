# from tkinter import *        
  
# # Following will import tkinter.ttk module and  
# # automatically override all the widgets 
# # which are present in tkinter module. 
# from tkinter.ttk import * 
# root = Tk()   
  
# # Initialize tkinter window with dimensions 100x100               
# root.geometry('100x100')     
  
# btn = Button(root, text = 'Click me !', 
#                 command = root.destroy) 
  
# # Set the position of button on the top of window 
# btn.pack(side = 'top')       
  
# root.mainloop()

# import tkinter as tk
# from tkinter import filedialog

# def UploadAction(event=None):
#     filename = filedialog.askopenfilename()
#     print('Selected:', filename)


# root = tk.Tk()
# button = tk.Button(root, text='Open', command=UploadAction)
# button.pack()

# root.mainloop()

from tkinter import *
import tkinter.messagebox
import urllib.request
import turtle
from tkinter import filedialog
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


# def main():
#     counts = analyzeFile(url.get())
#     drawHistogram(counts)

def UploadAction(event=None):
    		filename = filedialog.askopenfilename()
    		# if filename is not None: 
    			
    			# print(s)
    		with open(filename, "r") as f:
    			s=f.read()
    			print(s)
    			Label(frame2, text=f.read()).pack()
    		
    		analyzeFile(filename)
    		
    		# counts = countLetters(text.lower())
    		print('Selected:', filename)

def analyzeFile(filename):
    try:
    	

# root = tk.Tk()
		# button = tk.Button(root, text='Open', command=UploadAction)
        # infile = urllib.request.urlopen(url)
        # s = str(infile.read().decode()) # Read the content as string from the URL
        # s=UploadAction()
        # s=filename.read()
       
        counts = countLetters(filename)

        # infile.close() # Close file
    except ValueError:
        tkinter.messagebox.showwarning("file"," does not exist")

def countLetters(filename):
    counts = [] # Create and initialize counts
    with open(filename,'r') as file:
    	for line in file: 
        # reading each word         
        	for word in line.split():
        		counts.append(word)
    drawHistogram(counts)

def drawHistogram(list):

    # WIDTH = 400
    # HEIGHT = 300

    # raw_turtle.penup()
    # raw_turtle.goto(-WIDTH / 2, -HEIGHT / 2)
    # raw_turtle.pendown()
    # raw_turtle.forward(WIDTH)

    # widthOfBar = WIDTH / len(list)

    # for i in range(len(list)):
    #     height = list[i] * HEIGHT / max(list)
    #     drawABar(-WIDTH / 2 + i * widthOfBar,
    #         -HEIGHT / 2, widthOfBar, height, letter_number=i)

    # raw_turtle.hideturtle()


	counts = Counter(word_list)

	labels, values = zip(*counts.items())

	# sort your values in descending order
	indSort = np.argsort(values)[::-1]

	# rearrange your data
	labels = np.array(labels)[indSort]
	values = np.array(values)[indSort]

	indexes = np.arange(len(labels))

	bar_width = 0.35

	plt.bar(indexes, values)

	# add labels
	plt.xticks(indexes + bar_width, labels)
	plt.show()

def drawABar(i, j, widthOfBar, height, letter_number):
    alf='abcdefghijklmnopqrstuvwxyz'
    raw_turtle.penup()
    raw_turtle.goto(i+2, j-20)

    #sign letter on histogram
    raw_turtle.write(alf[letter_number])
    raw_turtle.goto(i, j)

    raw_turtle.setheading(90)
    raw_turtle.pendown()


    raw_turtle.forward(height)
    raw_turtle.right(90)
    raw_turtle.forward(widthOfBar)
    raw_turtle.right(90)
    raw_turtle.forward(height)

window = Tk()
window.title("Occurrence of Letters in a Histogram from URL")

frame1 = Frame(window)
frame1.pack()

scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = Y)

canvas = tkinter.Canvas(frame1, width=450, height=450)
raw_turtle = turtle.RawTurtle(canvas)

scrollbar.config(command = canvas.yview)
canvas.config( yscrollcommand=scrollbar.set)
canvas.pack()

frame2 = Frame(window)
frame2.pack()

frame3 = Frame(window)
frame3.pack()

# Label(frame2, text = "Enter a URL: ").pack(side = LEFT)
# url = StringVar()
# Entry(frame2, width = 50, textvariable = url).pack(side = LEFT)
button=Button(frame2, text = "Open", command=UploadAction).pack(side = LEFT)
# button = window.Button(text='Open', command=UploadAction)
window.mainloop()
