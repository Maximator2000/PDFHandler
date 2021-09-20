from tkinter import *
from tkinter import ttk
from info import InfoManager
from Split import SplitManager
from PdfsInPython import *
root=Tk()
root.geometry("900x400")

mainNotebook=ttk.Notebook(root)
mainNotebook.pack()

frameList=[
    Frame(mainNotebook,width=900, height=400),
    Frame(mainNotebook,width=900, height=400),
    Frame(mainNotebook,width=900, height=400)
]
name=["info","split","merge"]
for i in range(len(frameList)):
    frameList[i].pack(fill="both",expand=1)
    mainNotebook.add(frameList[i],text=name[i])

infoM=InfoManager(frameList)
splitM=SplitManager(frameList[1])






root.mainloop()