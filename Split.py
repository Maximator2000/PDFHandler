from tkinter import *
from PdfsInPython import*



class SplitManager():

    def __init__(self,frame):
        self.instructLabel=Label(frame,text="write down all pages where you want to make a cut.\n"
                                            "If you write '2,4' there will be three files from page 1-2,3-4 and 5-...")
        self.instructLabel.grid(row=0,column=0)
        self.initButton=Button(frame,text="Split",command=self.split)
        self.initButton.grid(row=1,column=0)
        self.e=Entry(frame,width=100)
        self.e.grid(row=2,column=0)

    def split(self):
        splitPDF(r""+self.e.get())