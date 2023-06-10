import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm

import LogisticRegression as LR
import KNN as RF
import SVMLinearKernel as SVMLK
import SVMGaussianKernel as SVMGK
import pred as pr
from tkinter import *

bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"


def Home():
        global window
        def clear():
            print("Clear1")
            txt.delete(0, 'end')    
            txt1.delete(0, 'end')
            txt2.delete(0, 'end')
            txt3.delete(0, 'end')
  



        window = tk.Tk()
        window.title("Fruit adulteration Detection")

 
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        bg = ImageTk.PhotoImage(file ="bg.png")
        # Show image using label
        label1 = Label( window, image = bg)
        label1.place(x = 0, y = 0)
        

        message1 = tk.Label(window, text="Fruit Adulteration Detection" ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
        message1.place(x=100, y=20)

        lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=100, y=200)
        
        txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=400, y=215)

        lbl1 = tk.Label(window, text="Enter the PPM Value",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl1.place(x=100, y=400)
        
        txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt1.place(x=400, y=415)

        lbl2 = tk.Label(window, text="Result",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl2.place(x=100, y=500)
        
        txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt3.place(x=400, y=515)

        


        def browse():
                path=filedialog.askopenfilename()
                print(path)
                txt.delete(0, 'end')
                txt.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select DataSet Folder")     

        
        

        def LRprocess():
                sym=txt.get()
                if sym != "":
                        LR.process(sym)
                        tm.showinfo("Input", "Logistic Regression Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        def KNNprocess():
                sym=txt.get()
                if sym != "":
                        RF.process(sym)
                        tm.showinfo("Input", "Random Forest Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        def SVMLKprocess():
                sym=txt.get()
                if sym != "":
                        SVMLK.process(sym)
                        tm.showinfo("Input", "SVM Linear Kernel Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        def SVMGKprocess():
                sym=txt.get()
                if sym != "":
                        SVMGK.process(sym)
                        tm.showinfo("Input", "SVM Gaussian Kernel Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")
                
        def predict():
                sym=txt1.get()
                txt3.delete(0, 'end')
                
                if sym != "":
                        res=pr.process(sym)
                        txt3.insert('end',"Predicted as :"+str(res))                        
                        tm.showinfo("Output", "Predicted as"+str(res))
                else:
                        tm.showinfo("Input error", "Enter the PPM Value")
                

        

        browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.place(x=650, y=200)

        

        clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=950, y=200)
         
        
        

        LRbutton = tk.Button(window, text="LogisticRegression", command=LRprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        LRbutton.place(x=10, y=600)


        RFbutton = tk.Button(window, text="KNN", command=KNNprocess  ,fg=fgcolor   ,bg=bgcolor1 ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        RFbutton.place(x=180, y=600)

        SVMbutton = tk.Button(window, text="SVMLinearKernel", command=SVMLKprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=16  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        SVMbutton.place(x=355, y=600)

        SVM1button = tk.Button(window, text="SVMGaussianKernel", command=SVMGKprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        SVM1button.place(x=540, y=600)
        
        SVM2button = tk.Button(window, text="Predict", command=predict  ,fg=fgcolor   ,bg=bgcolor1   ,width=16  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        SVM2button.place(x=745, y=600)

        

        quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=900, y=600)

        window.mainloop()
Home()