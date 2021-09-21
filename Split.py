from tkinter import *
from PdfsInPython import*



class SplitManager():

    def __init__(self,frame):
        self.instructLabel=Label(frame,text="write down all pages where you want to make a cut.\n"
                                            "If you write '2,4' there will be three files from page 1-2,3-4 and 5-...")
        self.instructLabel.grid(row=0,column=0)
        self.initButton=Button(frame,text="Split",command=self.split)
        self.initButton.grid(row=1,column=0)
        self.inputInfo=Label(frame,text="Write the direction to the pdf on the rigth and your outputfile beneath it")
        self.inputInfo.grid(row=2,column=0)
        self.e=Entry(frame,width=100)
        self.e.grid(row=2,column=1)
        self.o=Entry(frame,width=100)
        self.o.grid(row=3,column=1)
        self.pages=Entry(frame,width=100)
        self.pages.grid(row=0,column=1)


    def split(self):
        splitByPages(r""+self.e.get(),r""+self.o.get(),"test_v1",self.getPages())

    def getPages(self):
        listOfP=[]
        input=self.pages.get()
        list=input.split(',')
        for elem in list:
            if '-' in elem:
                numbers=elem.split('-')
                for i in range(int(numbers[0]),int(numbers[1])+1):
                    listOfP.append(i)
                    print(i)
            else:
                listOfP.append(int(elem))
                print(int(elem))
        return listOfP
