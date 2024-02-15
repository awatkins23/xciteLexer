import sys
import re

def validateToken(token):
    if re.search("\".*\"", token):
        return "string literal"
    else:
        try:
            return language[token]
        except:
            return "error"

language = {
    "INT": "INT keyword",
    "=": "assignment",
    "!": "exclamation",
    "PRINT": "PRINT keyword",
    "(": "open parenthesis",
    ")": "close parenthesis",
    "!": "exclamation"
}
tokens = []
separators = " !(),\n"

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