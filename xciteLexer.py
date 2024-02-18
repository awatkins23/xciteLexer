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
inSingleQuotes = False

for line in data:
    currentToken = ""
    inQuotes = False
    inSingleQuotes = False
    for char in line:
        #There are four steps:
        #1. if it is a quote, swap to the quote logic
        #2. if it is a single quote, swap to the single quote logic
        #3. if it isn't one of the tokenEnders, add it to the current token
        #4. else, it must have found a token end, so the current token is finished
        if inQuotes:
            #building the string until we find another quotation mark
            currentToken += char
            if (char == "\""):
                inQuotes = False
                tokens.append(currentToken)
                currentToken = ""
        elif inSingleQuotes:
            #building the string until we find another quotation mark
            currentToken += char
            if (char == "\'"):
                inSingleQuotes = False
                tokens.append(currentToken)
                currentToken = ""
        else:
            if (char == "\""):
                inQuotes = True
                currentToken += char
            elif (char == "\'"):
                inSingleQuotes = True
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
    #if the last line ended while still in quotes, add the built
    #token to the list of tokens and start fresh on the new line
    if inQuotes == True or currentToken != "":
        tokens.append(currentToken)



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

for i in range(0, len(tokens) - 1):
    if ((tokens[i] == '>' or tokens[i] == '<' or tokens[i] == '=') and i != len(tokens) - 1 and tokens[i+1] == '='):
        tokens[i] = tokens[i] + tokens[i+1]
        del tokens[i+1]

print(tokens)

for token in tokens:
    print(token + ": " + validateToken(token))