import HQ
import _core as c

def runCMD(statement, isShell = True):
    # comments
    if statement[0] == "#":
        pass
    
    # if else statement
    elif c.ifElseREGEX.search(statement) != None:
        temp = c.ifElseREGEX.search(statement)
        HQ.ifElseEXE(temp.group(1), temp.group(2), temp.group(3))

    #print
    elif c.heluREGEX.search(statement) != None:
        temp = c.heluREGEX.search(statement)
        HQ.print(temp.group(1))

    # create variable
    elif c.varInitREGEX.search(statement) != None:
        temp = c.varInitREGEX.search(statement)
        ans = HQ.createvar(temp.group(1), temp.group(2), temp.group(3))
        if isShell:
            print(ans, end="")

    # take input
    elif c.inputREGEX.search(statement) != None:
        temp = c.inputREGEX.search(statement)
        HQ.takeval(isShell, temp.group(1), temp.group(2))    

    # assign value
    elif c.varAssignREGEX.search(statement) != None:
        temp = c.varAssignREGEX.search(statement)
        ans = HQ.assignvar(temp.group(1), temp.group(2))
        if isShell:
            print(ans, end="")

    # deprecated (don't use)
    elif c.ifREGEX.search(statement) != None:
        temp = c.ifREGEX.search(statement)
        stats = []
        while True:
            code = input("...    ")
            if code != 'SAAKU BIDU':
                stats.append(code)
            else:
                break
        HQ.ifEXE(temp.group(1), stats)

    # deprecated (don't use)
    elif c.importREGEX.search(statement) != None:
        temp = c.importREGEX.search(statement)
        HQ.importit(temp.group(1))

    # execute
    elif c.executeREGEX.search(statement) != None:
        temp = c.executeREGEX.search(statement)
        HQ.execyut(temp.group(1))

    # newline
    elif statement == '' or statement == '\n':
        pass
    
    # invalid
    else:
        print("NiyamaDosha: tappu aadesha")
    print()