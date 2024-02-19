import sys

separators = ["==" , "<=" , ">=" , "[" , "]" , "=" , "," , "!" , ">",
              "<" , "(" , ")" , "{" , "}" , "+" , "-" , "/" , "*" , "%"]

keywords = ["PRINT","INT","BOOL", "FLOAT", "CHAR", "STRING", "ARRAY",
            "WHILE","IF", "ELSE", "TRUE", "FALSE", "NOT", "AND", "OR"]
def fileRead(pathArgs):

    for arg in pathArgs:
        try:
            file = open(arg, "r")
        except:
            print(f'File not found at \"{path}\"')
            exit()
        lex(file)


def lex(file):

    program = file.readlines()

    for line in program:

        while("'" or '"' in line):

            startIndex = line.find("'" or '"')
            endIndex = line.find(line[startIndex], startIndex + 1)

            if(endIndex is -1):
                # TAKE EVERYTHING TO THE RIGHT
            else:
                # TAKE WHATS IN THE QUOTE

        for separator in separators.keys():
            