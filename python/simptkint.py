#!/usr/bin/env python3

#SimpTkint (Simple Tkinter)
#Note: I wrote this in 2017 when I was learning oop (so its way to complicated), but it does the job.
#I might re-write it at some point, but until then...
#Author: SecretSheppy

global version
version = "1.11"

#imports
import os
# import numpy

#default variables
global username
username = os.getlogin()

#source verification
if __name__ == "__main__":
    print("simptkint running in source environment...")

if __name__ != "__main__":
    __name__ = "__source__"

#classes

#class that has all of the code in for writing the code
class __source__write:
    
    #writing the imports that the project needs
    @staticmethod
    def imports():

        return f"""#project created by simptkint Version {version}\n#essential tkinter imports\nfrom tkinter import *\nfrom tkinter import messagebox,ttk,scrolledtext\nfrom tkinter.ttk import Progressbar\n\n#common operator imports\nimport time\nimport os\nimport math\nimport numpy\n\n"""


    #add custom imports
    @staticmethod
    def customImports(cimport):

        return f"""#custom import for {cimport} module\nimport {cimport}\n\n"""


    #creating the window (start of code)
    @staticmethod
    def createWindow(windowName, windowTitle, windowGeometry, windowColor):

        return f"""#window "{windowName}" starts here\n{windowName}=Tk()\n{windowName}.title('{windowTitle}')\n{windowName}.geometry('{windowGeometry}')\n{windowName}['background']='{windowColor}'\n\n"""


    #destroying the window (end of code)
    @staticmethod
    def destroyWindow(windowName):

        return f"""""#destory element: "{windowName}"\n{windowName}.destroy()\n\n"""


    #creating the msgbox for messagebox.askquestion()
    @staticmethod
    def createMessage_Q(msgTitle, msgContent):

        return f"""#"{msgTitle}" msg box element | Type: Question\nmsg=messagebox.askquestion('{msgTitle}','{msgContent}')\nif msg=='yes':\n   pass\nelse:\n   pass\n\n"""

    
    #creating the msgbox for messagebox.showinfo()
    @staticmethod
    def createMessage_I(msgTitle, msgContent):

        return f"""#"{msgTitle}" msg box element | Type: Information\nmessagebox.showinfo('{msgTitle}','{msgContent}')\n\n"""

    
    #creating the msgbox for messagebox.showwarning()
    @staticmethod
    def createMessage_W(msgTitle, msgContent):

        return f"""#"{msgTitle}" msg box element | Type: Warning\nmessagebox.showwarning('{msgTitle}','{msgContent}')\n\n"""


    #creating the msgbox for messagebox.showerror()
    @staticmethod
    def createMessage_E(msgTitle, msgContent):

        return f"""#"{msgTitle}" msg box element | Type: Error\nmessagebox.showerror('{msgTitle}','{msgContent}')\n\n"""


    #creating the button
    @staticmethod
    def createButton(btnName, windowName, btnText, font, fontSize, bgColor, fgColor, btnCommand, x, y):

        return f"""#"{btnName}" button element | Function: {btnCommand}\n{btnName}=Button({windowName},text="{btnText}",font=("{font}",{fontSize}),bg="{bgColor}",fg="{fgColor}",command={btnCommand})\n{btnName}.place(relx={x},rely={y})\n\n"""


    #creating a label
    @staticmethod
    def createLabel(lblName, windowName, lblText, font, fontSize, bgColor, fgColor, x, y):

        return f"""#"{lblName}" label element\n{lblName}=Label({windowName},text="{lblText}",font=("{font}",{fontSize}),bg="{bgColor}",fg="{fgColor}")\n{lblName}.place(relx={x},rely={y})\n\n"""


    #creating a resizable statement
    @staticmethod
    def setResize(windowName, width, height):

        return f"""#Resizeable element | Width={width}, Height={height}\n{windowName}.resizable(width={width},height={height})\n\n"""


    #creating a frame
    @staticmethod
    def createFrame(frameName, windowName, width, height, y, x, color):

        return f"""#"{frameName}" frame element\n{frameName}=Frame({windowName},bg="{color}")\n{frameName}.place(relwidth={width},relheight={height},rely={y},relx={x})\n\n"""


    #creating the progressbar
    @staticmethod
    def createProgressbar(barName, windowName, length, x, y, value):

        return f"""#"{barName}" progressbar element\nstyle=ttk.Style()\nstyle.theme_use('default')\nstyle.configure("green.Horizontal.TProgressbar",backgound='black')\n{barName}=Progressbar({windowName},length={length})\n{barName}.place(relx={x},rely={y})\nbar['value']={value}\n\n"""


    #creating the scrolled text
    @staticmethod
    def createInput(windowName, variableName, entryName, inputName, inputType, x, y):

        #making inputType lowercase
        inputType = inputType.lower()

        #assigning the input type
        if inputType == 'str':
            inputVal = 'StringVar()'

        elif inputType == 'int':
            inputVal = 'IntVar()'

        elif inputType == 'float':
            inputVal = 'DoubleVar()'

        elif inputType == 'bool':
            inputVal = 'BooleanVar()'

        else:
            raise TypeError(f"input: {inputType} is not a recognised format")

        return f"""#"{inputName}" input element\n{variableName}={inputVal}\n{entryName}=Entry({windowName},textvariable={variableName},width=50)\n{entryName}.place(relx={x},rely={y})\n{inputName}={variableName}.get()\n\n"""


    #creating a slider
    @staticmethod
    def createSlider(sliderName, windowName, lowerVal, upperVal, orient, defaultVal, x, y, length, width, returnVal):

        #if the user wants to get the value from the slider
        if returnVal == True:

            return f"""#"{sliderName}" slider element | Value return = True\n{sliderName}=Scale({windowName},from_={lowerVal},to={upperVal},orient='{orient}',length={length},width={width})\n{sliderName}.set({defaultVal})\n{sliderName}.place(relx={x},rely={y})\nval={sliderName}.get()\n\n"""

        #if the user doesnt want the value returned
        else:

            return f"""#"{sliderName}" slider element | Value return = False\n{sliderName}=Scale({windowName},from_={lowerVal},to={upperVal},orient='{orient}',length={length},width={width})\n{sliderName}.set({defaultVal})\n{sliderName}.place(relx={x},rely={y})\n\n"""


    #final pack for mainloop()
    @staticmethod
    def mainloop(windowName):

        return f"""#pack all data\n{windowName}.mainloop()\n\n"""



#the class that gets imported into the project
class simptkint(__source__write):

    """SimpleTkinter Version 1.11 [12/03/2021]

    Main Classes:
    - simptkint
    - skwrite
    - interact
    - prebuilt
    
    simptkint class:
    The simptkint class contains a variety of functions that can be used to build Tkinter windows: createProject, setSize, customImport, buildWindow, buildButton, buildMsg, buildFrame, buildLabel, buildSlider, buildBar, buildInput, buildDestroy, _pack_mainloop
    The simptkint class can also be used to update and install Tkinter and SimpleTkinter: _windows_installTkinter, _linux_unix_installTkinter, _windows_installSimpTkint, _linux_unix_installSimpTkint
    /!\ simptkint does not currently support mac os, and features may be unreliable or buggy if used on an apple system.

    simptkint.skwrite() class:
    The skwrite class contains a variety of functions that can be used to add utility to the project: addVariable, addFunction, _addFunction, addClass, addSleep

    simptkint.interact() class:
    This interact class contains the more advanced interactive features that can be added to the project: 

    simptkint.prebuilt() class:
    contains prebuilt example code:

    /!\ Be aware that the __source__ classes and functions do not need to be imported into your project file."""

    #this code runs when the simpkint module is called
    #it defines the two variabels that are needed to create the project
    def __init__(cls, projectName = None, windowName = None, directory = None):

        """init function must be performed initially to setup window name and base directory. To create new window, re-assign the "windowName"."""

        #if the porjectName is defined
        if projectName:
            
            #setting self.projectName to the defined name
            simptkint.projectName = projectName

        #if the projectName is not defined
        else:
            
            #setting self.projectName to myProject
            simptkint.projectName = 'myProject'

        
        #if the directory the user wants is not the desktop
        if directory:
            
            #setting self.directory to the users choice
            simptkint.directory = directory

        #if the user doesn't supply a directory
        else:
            
            #setting self.directory to the users desktop
            simptkint.directory = f'c:/Users/{username}/Desktop'

        
        #if the user defines a windowName
        if windowName:

            #setting self.windowName to the user defined windowname
            simptkint.windowName = windowName
        
        #if the user doesn't define a window name
        else:

            #setting self.window name to the default option
            simptkint.windowName = 'myWindow'


    #function for custom imports
    @classmethod
    def customImport(cls, cimport):

        """Use this function to add custom imports to the project"""
        
        #opening the file
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        #writing the imports into the program
        _file.write(super().customImports(cimport=cimport))

        #closing the file so that the rest of the code can run in append mode
        _file.close()


    #it creates the new python file and then starts the editing process
    @classmethod
    def createProject(cls):
        
        """Use this function to create the file. Initiate with <variable>.createProject(<data>)"""

        #trying to create the file
        try:

            #opening the file to create it
            _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "w")

        #if the file already exists
        except FileExistsError:

            #telling the user what the problem is
            print("simptkint error: file already exists\nchange projectName or move existing project to a different directory")
            exit()


        #this part of the code runs after the try has run succesfully

        #writing the imports into the program
        _file.write(super().imports())

        #closing the file so that the rest of the code can run in append mode
        _file.close()

    
    #function that creats the window
    @classmethod
    def buildWindow(cls, title = '<window title>', color = 'ivory', geometry = '500x500'):

        """Use this function to create the base window. Initiate with <variable>.buildWindow(<data>)"""

        #opening the file in append mode
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        #writing the window code into the file
        _file.write(super().createWindow(windowName=simptkint.windowName, windowColor=color, windowGeometry=geometry, windowTitle=title))

        #closing the file
        _file.close()


    #function that creates a button inside the window
    @classmethod
    def buildButton(cls, btnName = 'btn', btnText = '<text here>', font = 'Tisa', fontSize = 10, bgColor = 'white', fgColor = 'black', btnCommand = '<function name here (NO BRACKETS)>', x = 0, y = 0):

        """Use this function to create a button [can be positioned anywhere in the window] Initiate with <variable>.buildButton(<data>)"""

        #opening the file in append mode
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        #writing the window code into the file
        _file.write(super().createButton(windowName=simptkint.windowName, btnName=btnName, btnText=btnText, font=font, fontSize=fontSize, bgColor=bgColor, fgColor=fgColor, btnCommand=btnCommand, x=x, y=y))

        #closing the file
        _file.close()

    
    #function that creates a messagebox
    @classmethod
    def buildMsg(cls, msgTitle = '<standard msg box>', msgContent = '<content for msg box here>', Type = 'i'):

        """Use this function to create a message box. There are different types of message boxes. Initiate with <variable>.buildMsg(<data>)"""

        #opening the file in append mode
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        
        #making Type lower case
        Type = Type.lower()


        #assigning the right type of msgbox to the file
        if Type == 'q':

            #writing the window code into the file
            _file.write(super().createMessage_Q(msgContent=msgContent, msgTitle=msgTitle))

        elif Type == 'i':

            #writing the window code into the file
            _file.write(super().createMessage_I(msgContent=msgContent, msgTitle=msgTitle))
        
        elif Type == 'w':

            #writing the window code into the file
            _file.write(super().createMessage_W(msgContent=msgContent, msgTitle=msgTitle))

        elif Type == 'e':

            #writing the window code into the file
            _file.write(super().createMessage_E(msgContent=msgContent, msgTitle=msgTitle))

        else:

            #raising an error as this is not a reccognised type
            raise TypeError(f"msgbox: {Type} is an unknow type")


        #closing the file
        _file.close()


    #function that creates a frame
    @classmethod
    def buildFrame(cls, frameName, width = 0.1, height = 1, y = 0.5, x = 0.5, color = "#000000"):

        """Use this function to create a frame [can be positioned anywhere in the window] Initiate with <variable>.buildFrame(<data>)"""

        #opening the file in append mode
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        #writing the window code into the file
        _file.write(super().createFrame(windowName=simptkint.windowName, frameName=frameName, width=width, height=height, y=y, x=x, color=color))

        #closing the file
        _file.close()


    #function that creates a label
    @classmethod
    def buildLabel(cls, lblName = 'lbl', lblText = '<label text>', font = 'Tisa', fontSize = 20, bgColor = 'white', fgColor = 'black', x = 0, y = 0):

        """Use this function to create a label or text [can be positioned anywhere in the window] Initiate with <variable>.buildLabel(<data>)"""

        #opening the file in append mode
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        #writing the window code into the file
        _file.write(super().createLabel(windowName=simptkint.windowName, lblName=lblName, lblText=lblText, font=font, fontSize=fontSize, bgColor=bgColor, fgColor=fgColor, x=x, y=y))

        #closing the file
        _file.close()


    #function that creates a slider
    @classmethod
    def buildSlider(cls, sliderName = 'sldr', lowerVal = 0, upperVal = 100, orient = 'vertical', defaultVal = 0, x = 0, y = 0, length = 200, width = 20, returnVal = True):

        """Use this function to create a slider [can be positioned anywhere in the window] Initiate with <variable>.createProject(<data>)"""

        #opening the file in append mode
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        #writing the window code into the file
        _file.write(super().createSlider(windowName=simptkint.windowName, sliderName=sliderName, lowerVal=lowerVal, upperVal=upperVal, orient=orient, defaultVal=defaultVal, x=x, y=y, length=length, width=width, returnVal=returnVal))

        #closing the file
        _file.close()


    #function that sets the resizable ness of a window
    @classmethod
    def setSize(cls, width = False, height = False):

        """Use this function to set the window size. Initiate with <variable>.setSize(<data>)"""

        #opening the file in append mode
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        #writing the window code into the file
        _file.write(super().setResize(windowName=simptkint.windowName, width=width, height=height))

        #closing the file
        _file.close()


    #function that creates a progressbar
    @classmethod
    def buildBar(cls, barName = 'bar',  length = 100, x = 0, y = 0, value = 50):

        """Use this function to create a progress bar [can be positioned anywhere in the window] Initiate with <variable>.buildBar(<data>)"""

        #opening the file in append mode
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        #writing the window code into the file
        _file.write(super().createProgressbar(windowName=simptkint.windowName, barName=barName, length=length, x=x, y=y, value=value))

        #closing the file
        _file.close()


    #function that creates an input
    @classmethod
    def buildInput(cls, variableName = 'text', entryName = 'entry', inputName = 'txt', inputType = 'str', x = 0, y = 0):

        """Use this function to create a text input [can be positioned anywhere in the window] Initiate with <variable>.buildInput(<data>)"""

        #opening the file in append mode
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        #writing the window code into the file
        _file.write(super().createInput(windowName=simptkint.windowName, variableName=variableName, entryName=entryName, inputName=inputName, inputType=inputType, x=x, y=y))

        #closing the file
        _file.close()


    #function that creates a .destroy() attribute
    @classmethod
    def buildDestroy(cls):

        """Use this function to destroy anything previously created. Initiate with <variable>.buildDestroy()"""

        #opening the file in append mode
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        #writing the window code into the file
        _file.write(super().destroyWindow(windowName=simptkint.windowName))

        #closing the file
        _file.close()


    #the final pack() function to round up the code.
    #code will not compile properly if this is not run at the end of the code
    @classmethod
    def _pack_mainloop(cls):

        """This function must be performed at the end of the file. Initiate with <variable>._pack_mainloop()"""

        #opening the file in append mode
        _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

        #writing the window code into the file
        _file.write(super().mainloop(windowName=simptkint.windowName))

        #closing the file
        _file.close()


    #installing tkinter
    @staticmethod
    def _windows_installTkinter():

        """Use this function to update or install tkinter on your windows system. Initiate with <variable>._windows_installTkinter()"""

        #os command that executes the pip in the windows cmd
        os.system('cmd /c "pip install tkinter"')

    
    @staticmethod
    def _linux_unix_installTkinter():
        
        """Use this function to update or install tkinter on your linux system. Initiate with <variable>._linux_Unix_installTkinter()"""

        #os command that executes the pip in the linux cmd
        os.system("python -m pip install tkinter")


    #updating simptkint
    @staticmethod
    def _windows_installSimpTkint():

        """Use this function to update or install simptkint on your windows system. Initiate with <variable>._windows_installSimpTkint()"""

        #os command that executes the pip in the windows cmd
        os.system('cmd /c "pip install simptkint"')


    @staticmethod
    def _linux_unix_installSimpTkint():
        
        """Use this function to update or install tkinter on your linux system. Initiate with <variable>._linux_Unix_installSimptTkint()"""

        #os command that executes the pip in the linux cmd
        os.system("python -m pip install simptkint")

    #sk help
    @staticmethod
    def help():

        """Prints the basic class structure in the console."""

        #prints the basic help guide
        print("""SimpTkint Help:\n\n\nClasses:\n\nwrite[source class]\nsimptkint[main class]\nskwrite[function and pre-written code]\ninteract[interactive code]\n\n""")

    
    #skwrite class for preset code functions...
    class skwrite:

        """skwrite includes basic and common pre-written code that can be added into the project."""
        
        #function for variable creation
        @staticmethod
        def addVariable(variableType = "string", variableName = "defaultVariable", defaultVariableVal = "defaultText"):

            """Adds a standard variable into the project."""

            #opening the file in append mode
            _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

            #writing the data to the file
            _file.write(f"""#"{variableName}" {variableType} variable created below\n{variableName} = {defaultVariableVal}\n\n""")

            #closing the file
            _file.close()


        #function to add function
        @staticmethod
        def addFunction(functionName = "defaultFunction", functionDescription = "<basic function>", passedVariables = "", numberOfFunctions = 1):

            """Adds an empty function to the project"""

            #writing to the file
            _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

            #if multiple functions
            if numberOfFunctions > 1:

                #for loop for adding mutlpile functions
                #multiple function names can be .split(";")

                #try and except
                #function names t n'e
                try:
                    functionNames = functionName.split(";")
                except AttributeError:
                    functionNames = []
                    for i in range(numberOfFunctions):
                        functionNames.append(functionName)

                #function descriptions t n'e
                try:
                    functionDescriptions = functionDescription.split(";")
                except AttributeError:
                    functionDescriptions = []
                    for i in range(numberOfFunctions):
                        functionDescriptions.append(functionDescription)
                
                #passed variables t n'e
                try:
                    _passedVariables = passedVariables.split(";")
                except AttributeError:
                    _passedVariables = []
                    for i in range(numberOfFunctions):
                        _passedVariables.append("")

                for i in range(numberOfFunctions):

                    #writing to file
                    _file.write(f"""#"{functionNames[i]}" function\n#{functionDescriptions[i]}\ndef {functionNames[i]}({_passedVariables[i]}):\n    pass\n\n""")

                #closing the file
                _file.close()

            #if only one function
            else:
                
                #writing the data to the file
                _file.write(f"""#"{functionName}" function\n#{functionDescription}\ndef {functionName}({passedVariables}):\n    pass\n\n""")

                #closing the file
                _file.close()

        
        #function to add class
        @staticmethod
        def addClass(className = "defaultclass", classDescription = "<basic class>", inheritence = ""):

            """Adds an empty class to the project"""

            #writing to the file
            _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

            #writing the data to the file
            _file.write(f"""#"{className}" class\n#{classDescription}\nclass {className}({inheritence}):\n    pass\n\n""")

            #closing the file
            _file.close()


        #function to add function inside of class
        @staticmethod
        def addClassFunction(functionName = "defaultFunction", functionDescription = "<basic function>", passedVariables = ""):

            """Adds an empty function to the class"""

            #writing to the file
            _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

            #writing the data to the file
            _file.write(f"""    #"{functionName}" function\n    #{functionDescription}\n    def {functionName}({passedVariables}):\n        pass\n\n""")

            #closing the file
            _file.close()


        #function for a pause
        @staticmethod
        def addSleep(length = 0):

            """Adds a standard sleep command into the project."""

            #opening the file
            _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

            #writing the time into the class
            _file.write(f"#sleep element\ntime.sleep({length})\n\n")

            #closing the file
            _file.close()


        #function for adding getdirr
        @staticmethod
        def addGetDir():

            """Adds standard get directory code"""

            #opening the file
            _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

            #writing the time into the class
            _file.write(f"""#Function for getting directory\ndirectory_info = os.path.dirname(os.path.realpath(__file__))\ndirectory_info_split = directory_info.split("\\\\")
for i in range(len(directory_info_split)):\n    if i == 0:\n        directroy = directory_info_split[i]\n    else:\n        directory = directory + "/" + directory_info_split[i]\n\n""")

            #closing the file
            _file.close()


    # class for interactions like searchbars ...
    class interact:

        """interact includes the more complicated interactive features."""

        #top half of the class holds the correct writing data

        #initialisng the menubar
        @staticmethod
        def __source__menuBar(windowName, barName):

            #returning the correct statement
            return f"""{barName}=Menu({windowName})\n\n"""

        
        #adding a section to the menubar
        @staticmethod
        def __source__menuHeader(barName, headerName):

            #returning the code
            return f"""{headerName} = Menu({barName}, tearoff = 0, activebackground = '#00b3ff')\n\n"""


        #adding menu content
        @staticmethod
        def __source__headerContent(headerName, labels, commands):
            #should pass tuples or lists into this class (commands, labels)

            #preseting the data variable
            data = ""

            #going round the amount of labels that is passed into the function
            for i in range(len(labels)):

                #returning the values
                data += f"""{headerName}.add_command(label="{str(labels[i])}",command={str(commands[i])})\n"""

            #returning the data variable
            return data + "\n"

        
        #completeing the headerSection
        @staticmethod
        def __source__headerClose(barName, displayName, headerName):

            #returning the code
            return f"""{barName}.add_cascade(label="{displayName}",menu={headerName})\n\n"""


        #----------------------------------------------------------------------------------------------


        #do the top bar systems in this class
        @classmethod
        def createMenuBar(cls, barName = "menubar"):

            """Initialising the menubar"""

            #creaating the cls barname variable
            cls.barName = barName

            #opening the file
            _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

            #writing the data to the file
            _file.write(cls.__source__menuBar(simptkint.windowName, barName))

            #closing the file
            _file.close()

        
        #adding a header section to the menubar
        @classmethod
        def menuBarHeader(cls, headerName = "headerMenu"):

            """Adding a header section to the code"""

            #creating the meunHeader cls variable
            cls.headerName = headerName

            #opening the file
            _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

            #writing the data to the file
            _file.write(cls.__source__menuHeader(simptkint.windowName, headerName))

            #closing the file
            _file.close()

        
        #adding content to the dropdown menu created
        @classmethod
        def barHeader_addContent(cls, labels, commands):

            """Adding content to the dropdown menu of the header section"""

            #opening the file
            _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

            #writing the data to the file
            _file.write(cls.__source__headerContent(cls.headerName, labels, commands))

            #closing the file
            _file.close()

        
        #closing the header section
        @classmethod
        def barHeader_close(cls, displayName):

            """Adding the display name and closing the header section"""

            #opening the file
            _file = open(simptkint.directory + "/" + simptkint.projectName + ".py", "a")

            #writing the data to the file
            _file.write(cls.__source__headerClose(cls.barName, displayName, cls.headerName))

            #closing the file
            _file.close()


    # class for prebuilt functions
    class prebuilt:

        """The prebuilt class includes functions for predesigned templates."""

        #function to add an empty window
        @staticmethod
        def emptyWindow(directory = f"C:/Users/{username}/Desktop"):

            """Creates an empty window"""

            simptkint.__init__(0, projectName="Empty Window", windowName="window", directory=directory)
            simptkint.createProject()
            simptkint.buildWindow("Empty Window")
            simptkint._pack_mainloop()
        

        #function to add a window with buttons
        @staticmethod
        def buttonWindow(directory = f"C:/Users/{username}/Desktop", noButtons = 1):

            """Creates a window with buttons"""

            simptkint.__init__(0, projectName="Empty Window", windowName="window", directory=directory)
            simptkint.createProject()
            simptkint.buildWindow("Empty Window")

            for i in range(noButtons):
                simptkint.skwrite().addFunction(functionName=f"noCommand_{str(i)}", functionDescription=f"empty function for btn_{str(i)}")

            xpos = 0
            ypos = 0

            for i in range(noButtons):
                simptkint.buildButton(btnName=f"btn_{str(i)}", btnText=f"btn({str(i)})", btnCommand=f"noCommand_{str(i)}", x=xpos, y=ypos)
                ypos += 0.1
                if ypos == 1:
                    xpos += 0.2
                    ypos = 0
                
            simptkint._pack_mainloop()
