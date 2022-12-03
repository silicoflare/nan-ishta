import HQ
import _core as c
import os

statement = ''
os.system('cls')
print("Nan Ishta! v2.0")
print("Kaaryagatha nillisalu 'exit' type maadi")
while True: 
    statement = input(">>> ")
    # print(f"{statement}")
    if statement == 'exit':
        break

    if c.heluREGEX.search(statement) != None:
        temp = c.heluREGEX.search(statement)
        HQ.print(temp.group(1))

    elif c.inputREGEX.search(statement) != None:
        temp = c.inputREGEX.search(statement)
        HQ.takeval(temp.group(1), temp.group(2))    

    elif c.varInitREGEX.search(statement) != None:
        temp = c.varInitREGEX.search(statement)
        print(HQ.createvar(temp.group(1), temp.group(2), temp.group(3)))

    elif c.varAssignREGEX.search(statement) != None:
        temp = c.varAssignREGEX.search(statement)
        print(HQ.assignvar(temp.group(1), temp.group(2)))

    else:
        print("NiyamaDosha: tappu aadesha")
    print()
    
print("Dhanyavaadagalu!")
