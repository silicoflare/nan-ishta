import re

_variables = {}

keywords = [
    "SANKHYE", 
    "DASHAMANSHA", 
    "SHABDA", 
    "TARKA", 
    "ANDRE"
]

heluREGEX = re.compile(r"^(('[^']*')|(.+)) ANTHA HELU$")
varInitREGEX = re.compile(r"^(SANKHYE|TARKA|DASHAMANSHA|SHABDA) ([a-zA-Z_\$]+) ANDRE (.+)$")
varAssignREGEX = re.compile(r"^([a-zA-Z_\$]+) ANDRE (.+)$")
inputREGEX = re.compile(r"^([a-zA-Z_\$]+) ANDRE ('[^']*') ANTHA KELU$")