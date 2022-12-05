import re
import math
import random


_variables = {}

_temp_ = ''

keywords = [
    "SANKHYE", 
    "DASHAMANSHA", 
    "SHABDA", 
    "TARKA", 
    "ANDRE",
    "_temp_"
]

heluREGEX = re.compile(r"^(('[^']*')|(.+)) ANTHA HELU$")
varInitREGEX = re.compile(r"^(SANKHYE|TARKA|DASHAMANSHA|SHABDA) ([a-zA-Z_\$]+) ANDRE (.+)$")
varAssignREGEX = re.compile(r"^([a-zA-Z_\$]+) ANDRE (.+)$")
inputREGEX = re.compile(r"^([a-zA-Z_\$]+) ANDRE ('[^']*') ANTHA KELU$")
ifREGEX = re.compile(r"^(.+) IDDARE->$")
importREGEX = re.compile(r"^([a-zA-Z]+) SERISU$")
ifElseREGEX = re.compile(r"^(.+) IDDARE (.+) -ILLA- (.+)")
executeREGEX = re.compile(r"^(.+) CHALISU$")