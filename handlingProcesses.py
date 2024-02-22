#CSC 415 Assignment 3 Cody Dearth & Alec Watkins

import re

class Lexer:
    def __init__(self,file):
        try:
            self.file = open(file, "r")
            self.parseFile()
        except Exception as error:
            print(error)
            exit()

    keywordSeparators = ["<=" , ">=" , "==" , "[" , "]" , "=" , "," , "!" , ">",
                "<" , "(" , ")" , "{" , "}" , "+" , "-" , "/" , "*" , "%",
                "PRINT","INT","BOOL", "FLOAT", "CHAR", "STRING", "ARRAY",
                "WHILE","IF", "ELSE", "TRUE", "FALSE", "NOT", "AND", "OR"]

    language = {
        "INT": "INT Keyword",
        "BOOL": "BOOL Keyword", 
        "FLOAT": "FLOAT Keyword", 
        "CHAR": "CHAR Keyword", 
        "STRING": "STRING Keyword",
        "ARRAY": "ARRAY Keyword",
        "WHILE": "WHILE Keyword", 
        "IF": "IF Keyword", 
        "ELSE": "ELSE Keyword", 
        "TRUE": "TRUE Keyword", 
        "FALSE": "FALSE Keyword", 
        "NOT": "NOT Keyword", 
        "AND": "AND Keyword", 
        "OR": "OR Keyword",
        "PRINT": "PRINT Keyword",
        "[": "Open Square Bracket",
        "]": "Close Square Bracket",
        "=": "Assignment",
        ",": "Comma",
        "!": "Exclamation",
        ">": "Greater Than",
        "<": "Less Than",
        ">=": "Greater Than or Equal To",
        "<=": "Less Than or Equal To",
        "==": "Is Equal To",
        "(": "Open Parenthesis",
        ")": "Close Parenthesis",
        "{": "Open Curly Brace",
        "}": "Close Curly Brace",
        "+": "Addition",
        "-": "Subtraction",
        "/": "Division",
        "*": "Multiplication",
        "%": "Modulus"
    }

    subStrings = []
    lexTable = []
    currentProgram = ""

    def divideStringsFromToken(self,subStringIndex, startOfToken, endOfToken):

        leftSubString = self.subStrings[subStringIndex][1][0:startOfToken].strip()
        rightSubString = self.subStrings[subStringIndex][1][endOfToken:len(self.subStrings[subStringIndex][1])].strip()
        tokenSubString = self.subStrings[subStringIndex][1][startOfToken:endOfToken].strip()

        if(leftSubString != ""):
            del self.subStrings[subStringIndex]
            self.subStrings.insert(subStringIndex, (False, leftSubString))
            self.subStrings.insert(subStringIndex + 1, (True, tokenSubString))
            if(rightSubString != ""):
                self.subStrings.insert(subStringIndex + 2, (False, rightSubString))
        else:
            del self.subStrings[subStringIndex]
            self.subStrings.insert(subStringIndex, (True, tokenSubString))
            if(rightSubString != ""):
                self.subStrings.insert(subStringIndex + 1, (False, rightSubString))

    def quoteParser(self,line):

        subStringIndex = self.subStrings.index((False, line))
        subString = self.subStrings[subStringIndex][1]
        comment_index = line.find("$")
        double_index = line.find("\"")
        single_index = line.find("\'")

        if (comment_index == 0):
            del self.subStrings[subStringIndex]
            return

        if ((double_index & single_index & comment_index) == -1):
            return
        
        elif ((double_index | single_index) != -1):
            startOfToken = min(double_index, single_index)
            endOfToken = subString.find(subString[startOfToken], startOfToken + 1)

        else:
            startOfToken = max(double_index, single_index)
            endOfToken = subString.find(subString[startOfToken], startOfToken + 1)

        if(endOfToken != -1):
            if((comment_index < startOfToken)):
                self.divideStringsFromToken(subStringIndex, comment_index, len(subString))
                if(self.subStrings[subStringIndex + 1] == False):
                    print(f"YEET: {self.subStrings[subStringIndex + 1]}")
                    del self.subStrings[subStringIndex + 1]
            else:
                self.divideStringsFromToken(subStringIndex, startOfToken, endOfToken + 1)


    def keywordSeperatorParser(self):
        for token in self.keywordSeparators:
            subStringsLength = len(self.subStrings)
            currentIndex = 0

            while (currentIndex < subStringsLength):

                if self.subStrings[currentIndex][0] != True:
                    startOfToken = self.subStrings[currentIndex][1].find(token)
                    if(startOfToken != -1):
                        endOfToken = startOfToken + len(token)
                        self.divideStringsFromToken(currentIndex, startOfToken, endOfToken)
                        subStringsLength = len(self.subStrings)
                    currentIndex += 1
                else:
                    currentIndex += 1

    def indentifierParser(self):
        subStringsLength = len(self.subStrings)
        currentIndex = 0

        while (currentIndex < subStringsLength):
            if self.subStrings[currentIndex][0] != True:
                startOfToken = self.subStrings[currentIndex][1].find("@")

                if (startOfToken == -1):
                    currentIndex += 1
                    continue

                subString = self.subStrings[currentIndex][1]
                
                if (startOfToken == len(subString) - 1):
                    self.divideStringsFromToken(currentIndex, startOfToken, startOfToken + 1)
                    currentIndex += 1
                else:
                    x = startOfToken + 1
                    while (((subString[x] == "_") or (subString[x].islower()))):
                            if(subString[x] == "@"):
                                self.divideStringsFromToken(currentIndex, startOfToken, x - 1)
                                break
                            if(x == len(subString) - 1):
                                x+=1
                                break
                            x+=1

                    endOfToken = x

                    self.divideStringsFromToken(currentIndex, startOfToken, endOfToken)
                    currentIndex += 1
            else:
                currentIndex += 1
            subStringsLength = len(self.subStrings)

    def integerFloatParser(self):
        subStringsLength = len(self.subStrings)
        currentIndex = 0

        while (currentIndex < subStringsLength):

            if self.subStrings[currentIndex][0] != True:
                subString = self.subStrings[currentIndex][1]

                if(subString.isdigit()):
                    self.divideStringsFromToken(currentIndex, 0, len(subString))
                    currentIndex += 1

                else:
                    float = re.findall("[-]?[0-9]+[.][0-9]+", subString)
                    integer = re.findall("[-]?[0-9]+[.]?[.0-9]*", subString)
                    if ((float != [])):
                        startOfToken = subString.find(float[0])
                        endOfToken = startOfToken + len(float[0])
                        self.divideStringsFromToken(currentIndex, startOfToken, endOfToken)
                        currentIndex +=1

                    elif (integer != []):
                        startOfToken = subString.find(integer[0])
                        endOfToken = startOfToken + len(integer[0])
                        self.divideStringsFromToken(currentIndex, startOfToken, endOfToken)
                        currentIndex += 1

                    else:
                        currentIndex += 1
            else:
                currentIndex += 1
            subStringsLength = len(self.subStrings)

    def defineTokensWithOutput(self):
        for string in self.subStrings:
            if(string[1][0] == "$"):
                continue
            if re.search("^\".*\"", string[1]):
                self.lexTable.append((string[1],"String Literal"))
            elif re.search("^\'.\'", string[1]):
                self.lexTable.append((string[1],"Char Literal"))
            elif re.search("^[-]?(0[.]|[1-9][0-9][.])[0-9]*", string[1]):
                self.lexTable.append((string[1],"Float Literal"))
            elif re.search("^[-]?[1-9][0-9]*", string[1]):
                self.lexTable.append((string[1],"Int Literal"))
            elif re.search("^@[a-zA-Z_]+", string[1]):
                self.lexTable.append((string[1],"Identifier"))
            else:
                try:
                    self.lexTable.append((string[1],self.language[string[1]]))
                except:
                    self.lexTable.append((string[1],"Error"))

    def parseFile(self):
        
        program = self.file.readlines()
        for line in program:
            line = line.strip()

            if(line == ""):
                continue
            self.subStrings.append((False, line))
            self.quoteParser(line)
            self.integerFloatParser()
            self.keywordSeperatorParser()
            self.indentifierParser()
        self.defineTokensWithOutput()

    def lex(self):

        if (self.lexTable != []):
            return self.lexTable.pop(0)
        else:
            return None
