import sys
import re
from tkinter import *
from tkinter import filedialog

current_cmd = ""         # current_cmd -> currentCommand
current_cmd_Cntr = 0     # current_cmd_Cntr -> currentcommandCounter
programIn = []

#tkinter native library is used to open a file navigation dialog to select the desired Prog.asm file
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/", title = "Select .asm file", filetypes = (("asm files","*.asm"),("all files","*.*")))

with open(root.filename, 'r') as file:
    programIn = file.read().splitlines()
    file.close()

#Are there more commands to process?
def hasMoreCommands():
    if (current_cmd_Cntr) != len(programIn):
        return True
    else:
        return False

#Reads the next command. Removes whitespace and comments
def advance():
    global current_cmd_Cntr
    global current_cmd
    current_cmd = programIn[current_cmd_Cntr].replace(" ", "").split("//")[0]
    current_cmd_Cntr += 1

#Returns the command type, A, L or C
def commandType():
    global current_cmd
    if current_cmd.startswith("@"):
        return "A_COMMAND"
    elif current_cmd.startswith("("):
        return "L_COMMAND"
    elif not current_cmd:
        return ""
    else:
        return "C_COMMAND"

#Returns Xxx from @Xxx or (Xxx)
def symbol():
    global current_cmd
    if current_cmd.startswith("@"):
        return current_cmd.strip("@")
    else:
        return re.search(r'\((.*?)\)', current_cmd).group(1)

#Returns the computation insctructions of a C command
def comp():
    global current_cmd
    if "=" in current_cmd:
        if ";" in current_cmd:
            return current_cmd.split("=")[1].split(";")[0]
        else:
            return current_cmd.split("=")[1]
    elif ";" in current_cmd:
        return current_cmd.split(";")[0]

#Returns the jump conditions of a C command
def jump():
    global current_cmd
    if ";" in current_cmd:
        return current_cmd.split(";")[1]

#Returns the destination registers of a C command
def dest():
    global current_cmd
    if "=" in current_cmd:
        return current_cmd.split("=")[0]