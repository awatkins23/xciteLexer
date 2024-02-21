import time

keywordSeparators = ["<=" , ">=" , "==" , "[" , "]" , "=" , "," , "!" , ">",
              "<" , "(" , ")" , "{" , "}" , "+" , "-" , "/" , "*" , "%",
              "PRINT","INT","BOOL", "FLOAT", "CHAR", "STRING", "ARRAY",
            "WHILE","IF", "ELSE", "TRUE", "FALSE", "NOT", "AND", "OR"]

subStrings = []
currentProgram = ""
start_time = 0


def readArgs(pathArgs):
    global currentProgram
    global start_time

    for x in range(1, len(pathArgs)):
        try:
            file = open(pathArgs[x], "r")
            currentProgram = pathArgs[x]
        except:
            print(f'File not found at \"{pathArgs[x]}\"')
            exit()
        start_time = time.time()
        lex(file)

def divideStringsFromToken(subStringIndex, startOfToken, endOfToken):

    leftSubString = subStrings[subStringIndex][1][0:startOfToken].strip()
    rightSubString = subStrings[subStringIndex][1][endOfToken:len(subStrings[subStringIndex][1])].strip()
    tokenSubString = subStrings[subStringIndex][1][startOfToken:endOfToken].strip()

    if(leftSubString != ""):
        del subStrings[subStringIndex]
        subStrings.insert(subStringIndex, (False, leftSubString))
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

    if(endOfToken == -1):
        divideStringsFromToken(subStringIndex, startOfToken, -1)

    else:
        divideStringsFromToken(subStringIndex, startOfToken, endOfToken + 1)

        if(subStringIndex + 2 < len(subStrings)):
            quoteParser(subStrings[subStringIndex + 2][1])

def keywordSeperatorParser():
    for token in keywordSeparators:
        subStringsLength = len(subStrings) - 1

        for currentIndex in range(0,subStringsLength + 1):
            subStringsLength = len(subStrings)

            if subStrings[currentIndex][0] != True:
                startOfToken = subStrings[currentIndex][1].find(token)

                if(startOfToken != -1):
                    endOfToken = startOfToken + len(token)
                    divideStringsFromToken(currentIndex, startOfToken, endOfToken)

def indentifierParser():
    subStringsLength = len(subStrings)
    subStringsLength = len(subStrings)
    currentIndex = 0

    while (currentIndex < subStringsLength):
        if subStrings[currentIndex][0] != True:
            startOfToken = subStrings[currentIndex][1].find("@")

            if (startOfToken == -1):
                currentIndex += 1
                continue

            subString = subStrings[currentIndex][1]
            
            if (startOfToken == len(subString) - 1):
                divideStringsFromToken(currentIndex, startOfToken, startOfToken + 1)
                currentIndex += 1
            else:
                x = startOfToken + 1
                while (((subString[x] == "_") or (subString[x].islower()))):
                        if(subString[x] == "@"):
                            divideStringsFromToken(currentIndex, startOfToken, x - 1)
                            break
                        if(x == len(subString) - 1):
                            x+=1
                            break
                        x+=1

                endOfToken = x

                divideStringsFromToken(currentIndex, startOfToken, endOfToken)
                currentIndex += 1
        else:
            currentIndex += 1
        subStringsLength = len(subStrings)

def lex(file):

    global subStrings

    subStrings.clear()
    program = file.readlines()

    for line in program:
        
        line = line.strip()

        if(line == ""):
            continue


        subStrings.append((False, line))
        quoteParser(line)

        # MUST DEAL WITH COMMENTS RIGHT AFTER QUOTE

        keywordSeperatorParser()
        indentifierParser()

    end_time = time.time()
    print(f'     TOKENIZATION FOR "{currentProgram}" TOOK {end_time - start_time}\n')
    for string in subStrings:
        print(f"{string[0]} : {string[1]}")
    
