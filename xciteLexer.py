import sys
import re

keywords = {
    "PRINT": "PRINT keyword",
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
    "OR": "OR keyword"
}

separators = {
    "==":"is equal to",
    "<=":"less than or equal to",
    ">=":"greater than or equal to",
    "[": "open square bracket",
    "]": "close square bracket",
    "=": "assignment",
    ",": "comma",
    "!": "exclamation",
    ">": "greater than",
    "<": "less than",
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

lexed_dict = []
space = " "
start_index = 0

# ACCOUNT FOR COMMENTS
#####
for line in data:

    temp_index = 0
    
    # QUOTATION LEXER
    while (temp_index != -1):

        # NEED TO ENSURE THAT QUOTES ARE HANDLED IN ORDER OF WHICH COMES FIRST
        double_index = line.find("\"")
        single_index = line.find("\'")

        if ((double_index & single_index) == -1):
            break
        elif ((double_index | single_index) != -1):
            temp_index = min(double_index, single_index)
        else:
            temp_index = max(double_index, single_index)
            
    

        currentQuoteType = line[temp_index]
        temp_indexEnd = line.find(currentQuoteType, temp_index + 1)

        if (temp_indexEnd == -1):
            lexed_dict.update({line[temp_index:len(line) - 1]: [start_index + temp_index, "error"]})
            line = line.replace(line[temp_index:len(line) - 1], space * (temp_indexEnd - temp_index + 1))
            print(line)##
            break
        else:
            Literal = line[temp_index:temp_indexEnd + 1]
            line = line.replace(Literal, space * (temp_indexEnd - temp_index + 1))

            if (currentQuoteType == "\""): lexed_dict.update({Literal: [start_index + temp_index, "string literal"]})
            elif (len(Literal) == 3): lexed_dict.update({Literal: [start_index + temp_index, "character literal"]})
            else: lexed_dict.update({Literal: [start_index + temp_index, "error"]})
            print(line)##

    # SEPARATOR LEXER
    for separator in separators.keys():

        temp_index = line.find(separator)

        while (temp_index != -1):
            lexed_dict.update({separator: [start_index + temp_index, separators[separator]]})
            line = line.replace(separator, space * len(separator), 1)
            temp_index = line.find(separator)
            print(line)##

    # IDENTIFIER LEXER
            # TO BE DONE

    # KEYWORD LEXER
    for keyword in keywords.keys():

        temp_index = line.find(keyword)

        while (temp_index != -1):
            lexed_dict.update({keyword: [start_index + temp_index, keywords[keyword]]})
            line = line.replace(keyword, space * len(keyword), 1)
            temp_index = line.find(keyword)
            print(line)##
            
    start_index += len(line)
            
        
lexed_dict = sorted((lexed_dict.keys(), value) for (key,value) in lexed_dict.values())
for x in range(len(lexed_dict)):
    print(lexed_dict[x])