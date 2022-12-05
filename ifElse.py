import _core as c
import expression_exec as ex
import INTERPRETER as i

def exe(condition, trueStat, falseStat):
    try:
        value = eval(ex.makeExp(condition))
        if value:
            i.runCMD(trueStat)
        else:
            i.runCMD(falseStat)
    except KeyError as ke:
        print(f"AstitvaDosha: {ke} hesurina astitva illa.")
        return 0
