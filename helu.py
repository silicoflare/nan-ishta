import expression_exec as ex
import stringExp as sxp

def exe(string):
    if string[0]=="'":
        stuff = sxp.makeStr(string)
    else:
        stuff = ex.makeExp(string)
    
    # print(f"stuff: '{stuff}'")

    exec(f"print('{stuff}', end='')")