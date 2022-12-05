import _core as c
import helu
import takeValue
import varAssign
import varCreate
import ifCon
import importing
import ifElse
import execute

def print(string):
    helu.exe(string)

def createvar(datatype, name, value):
    output = varCreate.exe(datatype, name, value)
    if output != 0:
        return output
    else:
        return ''

def assignvar(name, value):
    output = varAssign.exe(name, value)
    if output != 0:
        return output
    else:
        return ''
    
def takeval(isShell, name, value):
    takeValue.exe(isShell, name, value)

def ifEXE(cond, stat):
    ifCon.exe(cond, stat)

def importit(module):
    importing.exe(module)

def ifElseEXE(cond, tru, fal):
    ifElse.exe(cond, tru, fal)

def execyut(statement):
    execute.exe(statement)
