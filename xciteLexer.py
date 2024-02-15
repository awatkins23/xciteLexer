import sys
import re

def validateToken(token):
    if re.search("\".*\"", token):
        return "string literal"
    if re.search("\'.\'", token):
        return "char literal"
    elif re.search("[0-9]+[.][0-9]+", token):
        return "float literal"
    elif re.search("[0-9]+", token):
        return "int literal"
    elif re.search("@[a-zA-Z_]+", token):
        return "identifier"
    else:
        try:
            return language[token]
        except:
            return "error"

language = {
    "INT": "INT keyword",
    "BOOL": "BOOL keyword", 
    "FLOAT": "FLOAT keyword", 
    "CHAR": "CHAR keyword", 
    "STRING": "STRING keyword",
    "ARRAY": "ARRAY keyword",
    "WHILE": "WHILE keyword", 
    "IF": "IF keyword", 
    "ELSE": "ELSE keyword", 
    "TRUE": "TRUE keyword", 
    "FALSE": "FALSE keyword", 
    "NOT": "NOT keyword", 
    "AND": "AND keyword", 
    "OR": "OR keyword",
    "PRINT": "PRINT keyword",
    "[": "open square bracket",
    "]": "close square bracket",
    "=": "assignment",
    ",": "comma",
    "!": "exclamation",
    ">": "greater than",
    "<": "less than",
    ">=": "greater than or equal to",
    "<=": "less than or equal to",
    "==": "is equal to",
    "(": "open parenthesis",
    ")": "close parenthesis",
    "{": "open curly brace",
    "}": "close curly brace",
    "+": "addition",
    "-": "subtraction",
    "/": "division",
    "*": "multiplication",
    "%": "modulus"
}
tokens = []
separators = "[]=,!><()\{\}+-/*%\n "

try:
    path = sys.argv[1]
except:
    print('Please provide a path')
    sys.exit()

try:
    file = open(path, "r")
except:
    print(f'Unable to find file at \"{path}\"')
    sys.exit()

data = file.readlines()
read = True

for line in data:
    if read == False:
        tokens.append(tmp)
    tmp = ""
    read = True
    for char in line:
        if read:
            if (char == "\""):
                read = False
                tmp += char
            elif (char not in separators):
                tmp += char
            else:
                if tmp != "":
                    tokens.append(tmp)
                tokens += char
                tmp = ""
        else:
            tmp += char
            if (char == "\""):
                read = True
                tokens.append(tmp)
                tmp = ""
try:
    while True:
        tokens.remove(' ')
except:
    print("")
try:
    while True:
        tokens.remove('\n')
except:
    print("")

print(tokens)

for token in tokens:
    print(token + ": " + validateToken(token))