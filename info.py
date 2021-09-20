from tkinter import *
from PdfsInPython import*
import os



class InfoManager():

    def __init__(self,frameList):
        self.infotext=StringVar(frameList[0])
        self.infotext.set("No information")
        self.e=Entry(frameList[0],width=100)
        self.e.grid(row=0,column=1)
        self.toDoLabel=Label(frameList[0],text="Enter the directory of your PDF at the rigth")
        self.toDoLabel.grid(row=0,column=0)
        self.infoButton=Button(frameList[0],text="Click here for more information",command=self.getInfo)
        self.infoButton.grid(row=1,column=0)
        self.openButton=Button(frameList[0],text="View file",command=self.open)
        self.openButton.grid(row=2,column=0)
        self.infoLabel=Label(frameList[0],text=self.infotext.get(),wraplength=400)
        self.infoLabel.grid(row=1,column=1)

    def getInfo(self):
        if not self.e.get()=="":
            self.infotext.set(get_meta(r""+self.e.get()))
            self.infoLabel.config(text=self.infotext.get())
    def open(self):
        if not self.e.get()=="":
            try :
                os.system(r""+self.e.get())
            except :
                self.infotext.set("Could not find path")
                self.infoLabel.config(text=self.infotext.get())


