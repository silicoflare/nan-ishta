import _core as c
import expression_exec as ex
import INTERPRETER as i

def exe(condition, statements):
    try:
        value = eval(ex.makeExp(condition))
        if value:
            for x in statements:
                # print(x)
                i.runCMD(x)
        else:
            return 0
    except KeyError as ke:
        print(f"AstitvaDosha: {ke} hesurina astitva illa.")
        return 0
