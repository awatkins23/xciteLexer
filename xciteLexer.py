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
tokenEnds = "[]=,!><()}{+-/*%\n "

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
inQuotes = False

for line in data:
    #if the last line ended while still in quotes, add the built
    #token to the list of tokens and start fresh on the new line
    if inQuotes == True:
        tokens.append(currentToken)
    currentToken = ""
    inQuotes = False
    for char in line:
        #There are three steps:
        #1. if it is a quote, swap to the quote logic
        #2. if it isn't one of the tokenEnders, add it to the current token
        #3. else, it must have found a token end, so the current token is finished
        if not inQuotes:
            if (char == "\""):
                inQuotes = True
                currentToken += char
            elif (char not in tokenEnds):
                currentToken += char
            else:
                #add the current token to the list of tokens
                if currentToken != "":
                    tokens.append(currentToken)
                #add the found token ender and then clear the current token
                tokens += char
                currentToken = ""
        else:
            #building the string until we find another quotation mark
            currentToken += char
            if (char == "\""):
                inQuotes = False
                tokens.append(currentToken)
                currentToken = ""
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