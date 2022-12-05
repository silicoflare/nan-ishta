import INTERPRETER as i
import _core as c

cmds = [
    "'Hello World!' ANTHA HELU",
    "SANKHYE a ANDRE 10",
    "'a={a}' ANTHA HELU"
]

# cmds = [
#     "'Hello World!' ANTHA HELU",
#     "'Hello World!' ANTHA HELU",
#     "'Hello World!' ANTHA HELU"
# ]

for x in cmds:
    i.runCMD(x, isShell = False)