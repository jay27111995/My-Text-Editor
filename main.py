"""
last context: 
    Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/tkinter/__init__.py", line 1892, in __call__
    return self.func(*args)
  File "/Users/jay/Desktop/notes/python/text_editor/main.py", line 55, in saveButton
    currentFile = open(completeFileName, "w+")
OSError: [Errno 45] Operation not supported: '/home/ds'
jay@student-222-91 text_editor % """


import tkinter as tk 
import os


class saveWindow:
    def __init__(self, userText, currentFile):
        saveWindow = tk.Tk()
        saveWindow.title("Create and save file") 

        frame1 = tk.Frame(saveWindow)
        fileNameLabel = tk.Label(master = frame1, text = "Enter file name:") 
        self.fileNameEntry = tk.Entry(master = frame1)
        fileNameLabel.pack(side=tk.LEFT)
        self.fileNameEntry.pack(side=tk.LEFT)

        frame2 = tk.Frame(saveWindow)
        fileDirLabel = tk.Label(master = frame2, text = "Enter file directory:")
        self.fileDirEntry = tk.Entry(master = frame2)
        fileDirLabel.pack(side=tk.LEFT)
        self.fileDirEntry.pack(side=tk.LEFT)

        frame3 = tk.Frame(saveWindow)
        saveButton = tk.Button(master = frame3, text = "Save", command = self.saveButton)
        saveButton.pack()
    
        # To display errors
        self.frame4 = tk.Frame(saveWindow)
        self.dirErrorLabel = tk.Label(master = self.frame4, 
            text = "Error: Invalid directory!", fg="red") 
        self.fileErrorLabel = tk.Label(master = self.frame4, 
            text = "Error: File already exists", fg="red")

        frame1.pack()
        frame2.pack()
        frame3.pack()
        self.frame4.pack() 
           
    def saveButton(self):
        # Get directory
        fileDir = self.fileDirEntry.get() 
        if (False == os.path.isdir(fileDir)):
            self.dirErrorLabel.pack()
            return

        # Get file Name
        fileName = self.fileNameEntry.get()
        completeFileName = fileDir + fileName
        if (True == os.path.isfile(completeFileName)):
            self.fileErrorLabel.pack()
            return        

        # Create and save
        currentFile = open(completeFileName, "w+")
        currrentFile.write(userText)


class mainWindow:
    def __init__(self, master):
        self.master = master 
        self.sidebar = tk.Frame()
        self.textEditWindow = tk.Frame()
        self.textEntry = None
        self.currentTextFile = None 

        self.master.title("My Special Text Editor")

        # Create side-bar
        self.sidebarInit()
        
        # Create text editing window 
        self.textEditWindowInit() 

        # Arrange frames 
        self.sidebar.pack(side=tk.LEFT, anchor = tk.N)
        self.textEditWindow.pack(side=tk.LEFT)


    def sidebarInit(self): 
        newButton = tk.Button(text = "New", 
                master = self.sidebar, 
                command = self.sidebarNewAction)
        newButton.pack()
        
        openButton = tk.Button(text = "Open", 
                master = self.sidebar, 
                command = self.sidebarOpenAction)
        openButton.pack()

        saveButton = tk.Button(text = "Save", 
                master = self.sidebar, 
                command = self.sidebarSaveAction)
        saveButton.pack()
       
    def textEditWindowInit(self):
        self.textEntry = tk.Text(fg="blue", bg="white", 
                master = self.textEditWindow)
        self.textEntry.pack()


    # Button action functions 
    def sidebarNewAction(self):
        # Check if there are any existing text, ask user if he wants to save?
        userText = self.textEntry("1.0", "1.1")            

    def sidebarOpenAction(self):
        None

    def sidebarSaveAction(self):
        userText = self.textEntry.get("1.0", tk.END)

        # Check if file exists, if not ask user to create a new file 
        if self.currentTextFile == None:
            saveWindow(userText, self.currentTextFile) 
        else:
            self.currentTextFile.write(userText)


root = tk.Tk()
mainWindow = mainWindow(root) 
root.mainloop()
