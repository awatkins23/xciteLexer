# xciteLexer
CSC 415 Lexer Assignment

Keywords: INT, BOOL, FLOAT, CHAR, STRING, ARRAY, WHILE, IF, ELSE, TRUE, FALSE, NOT, AND, OR, PRINT

String Literals: String literals are surrounded by a pair of double quotes. Any character except a double quote or line break can be contained inside a string literal. (A quote isn't allowed inside a string, because a quote is what we use to close the string.) Empty strings are allowed.

Character Literals: Character literals are surrounded by a pair of single quotes. Any character except a single quote can be contained inside a character literal. Empty characters are not allowed. Exacly one character must be enclosed in the quotes.

Integer Literals: Integer literals consist of numeric digits (0-9) with an optional negative sign in front. Leading zeros are not allowed, except for the number 0 itself. Negative zero is not allowed.

Floating-point Literals: Float literals consist of numeric digits (0-9) with a single decimal point and an optional negative sign in front. There must be at least one digit before and after the decimal point. A leading zero is only allowed when the zero is the only digit in front of the decimal.

Identifiers: Identifiers must start with the @ symbol. After the @ symbol, they can consist only of lowercase letters and underscores. There must be at least one character after the @ symbol.

Comments: Start with dollar sign symbol...
```
Operators & Separator Symbols:
Lexeme 	Token Description
[ 	open square bracket
] 	close square bracket
= 	assignment
, 	comma
! 	exclamation
> 	greater than
< 	less than
>= 	greater than or equal to
<= 	less than or equal to
== 	is equal to
( 	open parenthesis
) 	close parenthesis
{ 	open curly brace
} 	close curly brace
+ 	addition
- 	subtraction
/ 	division
* 	multiplication
% 	modulus
```