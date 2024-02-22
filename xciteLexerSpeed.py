#CSC 415 Assignment 3 Cody Dearth & Alec Watkins

from handlingProcesses import Lexer
import sys

if (len(sys.argv) >= 2):
    lex = Lexer(sys.argv[1])
    current = lex.lex()
    while(current!=None):
        print(f"{current[0]}  {current[1]}")
        current = lex.lex()
else:
    print("Please provide a file path as an arguement")
