import os
import INTERPRETER as i


statement = ''
os.system('cls')
print("Nan Ishta! v2.0")
print("Kaaryagatha nillisalu 'exit' type maadi")
while True: 
    statement = input(">>> ")

    # print(f"{statement}")
    
    if statement == 'exit':
        break
    
    i.runCMD(statement)

print("Dhanyavaadagalu!")