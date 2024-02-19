import sys

separators = ["==" , "<=" , ">=" , "[" , "]" , "=" , "," , "!" , ">",
              "<" , "(" , ")" , "{" , "}" , "+" , "-" , "/" , "*" , "%"]

keywords = ["PRINT","INT","BOOL", "FLOAT", "CHAR", "STRING", "ARRAY",
            "WHILE","IF", "ELSE", "TRUE", "FALSE", "NOT", "AND", "OR"]

subStrings = []
currentStartIndex = 0


def readArgs(pathArgs):

    for arg in pathArgs:
        try:
            file = open(arg, "r")
        except:
            print(f'File not found at \"{arg}\"')
            exit()
        lex(file)

def divideStringsFromToken(subStringIndex, startOfToken, endOfToken):

    leftSubString = subStrings[subStringIndex][1][0:startOfToken]
    rightSubString = subStrings[subStringIndex][1][endOfToken:-1]
    tokenSubString = subStrings[subStringIndex][1][startOfToken:endOfToken]

    if(leftSubString != ""):
        subStrings.insert(subStringIndex, (False, leftSubString))
        del subStrings[subStringIndex]
        subStrings.insert(subStringIndex + 1, (True, tokenSubString))
        if(rightSubString != ""):
            subStrings.insert(subStringIndex + 2, (False, rightSubString))
    else:
        del subStrings[subStringIndex]
        subStrings.insert(subStringIndex, (True, tokenSubString))
        if(rightSubString != ""):
            subStrings.insert(subStringIndex + 1, (False, rightSubString))

def quoteParser(line):

    subStringIndex = subStrings.index((False, line))
    subString = subStrings[subStringIndex][1]

    double_index = line.find("\"")
    single_index = line.find("\'")

    if ((double_index & single_index) == -1):
        return
    elif ((double_index | single_index) != -1):
        startOfToken = min(double_index, single_index)
        endOfToken = subString.find(subString[startOfToken], startOfToken + 1)
    else:
        startOfToken = max(double_index, single_index)
        endOfToken = subString.find(subString[startOfToken], startOfToken + 1)

    print(f"start: {startOfToken} end: {endOfToken} subString = {subString}" )

    if(endOfToken == -1):
        divideStringsFromToken(subStringIndex, startOfToken, -1)
    else:
        divideStringsFromToken(subStringIndex, startOfToken, endOfToken)
        # RECURSE THE RIGHT SIDE
        if(subStringIndex <= len(subStrings)):
            quoteParser(subStrings[subStringIndex + 1])

def lex(file):

    global currentStartIndex
    global subStrings

    currentStartIndex = 0
    subStrings.clear()
    program = file.readlines()

    for line in program:
        
        subStrings.append((False, line))

        quoteParser(line)
    print(subStrings)
