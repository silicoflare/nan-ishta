import _core as c
import helu
import takeValue
import varAssign
import varCreate

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
    
def takeval(name, value):
    takeValue.exe(name, value)
