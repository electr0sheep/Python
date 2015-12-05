import sys

__author__ = 'michaeldegraw'

index = 0
input = ""


###==========================================================================###
###  DFA from Project 1                                                      ###
###==========================================================================###

# Preconditions - none
# Postconditions - index will equal the position in "string" where the token ended
#                - will return a token represented as a string

def state1(string):
    global index
    if index == len(string):
        return ""
    elif string[index] == " " or string[index] == "\t" or string[index] == "\n":
        index += 1
        return state1(string)
    elif string[index] == '/':
        index += 1
        return state2(string)
    elif string[index] == '(':
        index += 1
        return state6(string)
    elif string[index] == ')':
        index += 1
        return state7(string)
    elif string[index] == '+':
        index += 1
        return state8(string)
    elif string[index] == '-':
        index += 1
        return state9(string)
    elif string[index] == '*':
        index += 1
        return state10(string)
    elif string[index] == ':':
        index += 1
        return state11(string)
    elif string[index] == '.':
        index += 1
        return state13(string)
    elif string[index].isdigit():
        index += 1
        return state14(string)
    elif string[index].isalpha() and string[index] != 'r' and string[index] != 'w':
        index += 1
        return state16(string)
    elif string[index] == 'r':
        index += 1
        return state17(string)
    elif string[index] == 'w':
        index += 1
        return state21(string)
    else:
        return "error"


def state2(string):
    global index
    if index == len(string):
        return "div"
    elif string[index] == '/':
        index += 1
        return state3(string)
    elif string[index] == '*':
        index += 1
        return state4(string)
    else:
        return "div"


def state3(string):
    global index
    if index == len(string):
        return ""
    elif string[index] == '\n':
        index += 1
        return state1(string)
    else:
        index += 1
        return state3(string)


def state4(string):
    global index
    if index == len(string):
        return "error"
    elif string[index] == '*':
        index += 1
        return state5(string)
    else:
        index += 1
        return state4(string)


def state5(string):
    global index
    if index == len(string):
        return "error"
    elif string[index] == '/':
        index += 1
        return state1(string)
    elif string[index] == '*':
        index += 1
        return state5(string)
    else:
        index += 1
        return state4(string)


def state6(string):
    return "lparen"


def state7(string):
    return "rparen"


def state8(string):
    return "plus"


def state9(string):
    return "minus"


def state10(string):
    return "times"


def state11(string):
    global index
    if index == len(string):
        return "error"
    elif string[index] == '=':
        index += 1
        return state12(string)
    else:
        return "error"


def state12(string):
    return "assign"


def state13(string):
    global index
    if index == len(string):
        return "error"
    elif string[index].isdigit():
        index += 1
        return state15(string)
    else:
        return "error"


def state14(string):
    global index
    if index == len(string):
        return "number"
    elif string[index] == '.':
        index += 1
        return state15(string)
    elif string[index].isdigit():
        index += 1
        return state14(string)
    else:
        return "number"


def state15(string):
    global index
    if index == len(string):
        return "number"
    elif string[index].isdigit():
        index += 1
        return state15(string)
    else:
        return "number"


def state16(string):
    global index
    if index == len(string):
        return "id"
    elif string[index].isalpha() or string[index].isdigit():
        index += 1
        return state16(string)
    else:
        return "id"


def state17(string):
    global index
    if index == len(string):
        return "id"
    elif string[index] == 'e':
        index += 1
        return state18(string)
    elif string[index].isalpha() or string[index].isdigit():
        index += 1
        return state16(string)
    else:
        return "id"


def state18(string):
    global index
    if index == len(string):
        return "id"
    elif string[index] == 'a':
        index += 1
        return state19(string)
    elif string[index].isalpha() or string[index].isdigit():
        index += 1
        return state16(string)
    else:
        return "id"


def state19(string):
    global index
    if index == len(string):
        return "id"
    elif string[index] == 'd':
        index += 1
        return state20(string)
    elif string[index].isalpha() or string[index].isdigit():
        index += 1
        return state16(string)
    else:
        return "id"


def state20(string):
    global index
    if index == len(string):
        return "read"
    elif string[index].isalpha() or string[index].isdigit():
        index += 1
        return state16(string)
    else:
        return "read"


def state21(string):
    global index
    if index == len(string):
        return "id"
    elif string[index] == 'r':
        index += 1
        return state22(string)
    elif string[index].isalpha() or string[index].isdigit():
        index += 1
        return state16(string)
    else:
        return "id"


def state22(string):
    global index
    if index == len(string):
        return "id"
    elif string[index] == 'i':
        index += 1
        return state23(string)
    elif string[index].isalpha() or string[index].isdigit():
        index += 1
        return state16(string)
    else:
        return "id"


def state23(string):
    global index
    if index == len(string):
        return "id"
    elif string[index] == 't':
        index += 1
        return state24(string)
    elif string[index].isalpha() or string[index].isdigit():
        index += 1
        return state16(string)
    else:
        return "id"


def state24(string):
    global index
    if index == len(string):
        return "id"
    elif string[index] == 'e':
        index += 1
        return state25(string)
    elif string[index].isalpha() or string[index].isdigit():
        index += 1
        return state16(string)
    else:
        return "id"


def state25(string):
    global index
    if index == len(string):
        return "write"
    elif string[index].isalpha() or string[index].isdigit():
        index += 1
        return state16(string)
    else:
        return "write"


###==========================================================================###
###  End of DFA                                                              ###
###==========================================================================###


###==========================================================================###
###  CFG from Project 2                                                      ###
###==========================================================================###

# Preconditions - global variable "input" is a valid non-empty string
# Postconditions - none

def program():
    outputString = "<Program>\n"
    outputString = stmt_list(outputString, 2)
    if outputString == "error":
        return "error"
    outputString += "</Program>\n"
    return outputString


def stmt_list(outputString, indentLevel):
    global input
    outputString += format("stmt_list", indentLevel)
    if input:
        outputString = stmt(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
        outputString = stmt_list(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
    outputString += format("/stmt_list", indentLevel)
    return outputString


def stmt(outputString, indentLevel):
    global input
    outputString += format("stmt", indentLevel)
    if scan() == "id":
        outputString = id(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
        outputString = assign(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
        outputString = expr(outputString, indentLevel + 2)
    elif scan() == "read":
        outputString = read(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
        outputString = id(outputString, indentLevel + 2)
    elif scan() == "write":
        outputString = write(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
        outputString = expr(outputString, indentLevel + 2)
    else:
        return "error"
    if outputString == "error":
        return "error"
    outputString += format("/stmt", indentLevel)
    return outputString


def expr(outputString, indentLevel):
    outputString += format("epxr", indentLevel)
    outputString = term(outputString, indentLevel + 2)
    if outputString == "error":
        return "error"
    outputString = term_tail(outputString, indentLevel + 2)
    if outputString == "error":
        return "error"
    outputString += format("/expr", indentLevel)
    return outputString


def term_tail(outputString, indentLevel):
    global input
    outputString += format("term_tail", indentLevel)
    if scan() == "plus" or scan() == "minus":
        outputString = add_op(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
        outputString = term(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
        outputString = term_tail(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
    outputString += format("/term_tail", indentLevel)
    return outputString


def term(outputString, indentLevel):
    outputString += format("term", indentLevel)
    outputString = factor(outputString, indentLevel + 2)
    if outputString == "error":
        return "error"
    outputString = fact_tail(outputString, indentLevel + 2)
    if outputString == "error":
        return "error"
    outputString += format("/term", indentLevel)
    return outputString


def fact_tail(outputString, indentLevel):
    global input
    outputString += format("fact_tail", indentLevel)
    if scan() == "times" or scan() == "div":
        outputString = mult_op(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
        outputString = factor(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
        outputString = fact_tail(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
    outputString += format("/fact_tail", indentLevel)
    return outputString


def factor(outputString, indentLevel):
    global input
    outputString += format("factor", indentLevel)
    if scan() == "lparen":
        outputString = lparen(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
        outputString = expr(outputString, indentLevel + 2)
        if outputString == "error":
            return "error"
        outputString = rparen(outputString, indentLevel + 2)
    elif scan() == "id":
        outputString = id(outputString, indentLevel + 2)
    elif scan() == "number":
        outputString = number(outputString, indentLevel + 2)
        outputString = outputString
    else:
        return "error"
    if outputString == "error":
        return "error"
    outputString += format("/factor", indentLevel)
    return outputString


def add_op(outputString, indentLevel):
    global input
    outputString += format("add_op", indentLevel)
    if scan() == "plus":
        outputString = plus(outputString, indentLevel + 2)
    elif scan() == "minus":
        outputString = minus(outputString, indentLevel + 2)
    else:
        return "error"
    if outputString == "error":
        return "error"
    outputString += format("/add_op", indentLevel)
    return outputString


def mult_op(outputString, indentLevel):
    global input
    outputString += format("mult_op", indentLevel)
    if scan() == "times":
        outputString = times(outputString, indentLevel + 2)
    elif scan() == "div":
        outputString = div(outputString, indentLevel + 2)
    else:
        return "error"
    if outputString == "error":
        return "error"
    outputString += format("/mult_op", indentLevel)
    return outputString


def id(outputString, indentLevel):
    global input
    if scan() == "id":
        outputString += format("id", indentLevel)
        outputString += indentString(indentLevel + 2)
        outputString += printSymbol() + "\n"
        outputString += format("/id", indentLevel)
        consume()
        return outputString
    else:
        return "error"


def assign(outputString, indentLevel):
    global input
    if scan() == "assign":
        outputString += format("assign", indentLevel)
        outputString += indentString(indentLevel + 2)
        outputString += ":=\n"
        outputString += format("/assign", indentLevel)
        consume()
        return outputString
    else:
        return "error"


def read(outputString, indentLevel):
    global input
    if scan() == "read":
        outputString += format("read", indentLevel)
        outputString += indentString(indentLevel + 2)
        outputString += "read\n"
        outputString += format("/read", indentLevel)
        consume()
        return outputString
    else:
        return "error"


def write(outputString, indentLevel):
    global input
    if scan() == "write":
        outputString += format("write", indentLevel)
        outputString += indentString(indentLevel + 2)
        outputString += "write\n"
        outputString += format("/write", indentLevel)
        consume()
        return outputString
    else:
        return "error"


def lparen(outputString, indentLevel):
    global input
    if scan() == "lparen":
        outputString += format("lparen", indentLevel)
        outputString += indentString(indentLevel + 2)
        outputString += "(\n"
        outputString += format("/lparen", indentLevel)
        consume()
        return outputString
    else:
        return "error"


def rparen(outputString, indentLevel):
    global input
    if scan() == "rparen":
        outputString += format("rparen", indentLevel)
        outputString += indentString(indentLevel + 2)
        outputString += ")\n"
        outputString += format("/rparen", indentLevel)
        consume()
        return outputString
    else:
        return "error"


def number(outputString, indentLevel):
    global input
    if scan() == "number":
        outputString += format("number", indentLevel)
        outputString += indentString(indentLevel + 2)
        outputString += printSymbol() + "\n"
        outputString += format("/number", indentLevel)
        consume()
        return outputString
    else:
        return "error"


def plus(outputString, indentLevel):
    global input
    if scan() == "plus":
        outputString += format("plus", indentLevel)
        outputString += indentString(indentLevel + 2)
        outputString += "+\n"
        outputString += format("/plus", indentLevel)
        consume()
        return outputString
    else:
        return "error"


def minus(outputString, indentLevel):
    global input
    if scan() == "minus":
        outputString += format("minus", indentLevel)
        outputString += indentString(indentLevel + 2)
        outputString += "-\n"
        outputString += format("/minus", indentLevel)
        consume()
        return outputString
    else:
        return "error"


def times(outputString, indentLevel):
    global input
    if scan() == "times":
        outputString += format("times", indentLevel)
        outputString += indentString(indentLevel + 2)
        outputString += "*\n"
        outputString += format("/times", indentLevel)
        consume()
        return outputString
    else:
        return "error"


def div(outputString, indentLevel):
    global input
    if scan() == "div":
        outputString += format("div", indentLevel)
        outputString += indentString(indentLevel + 2)
        outputString += "/\n"
        outputString += format("/div", indentLevel)
        consume()
        return outputString
    else:
        return "error"


###==========================================================================###
###  End of CFG                                                              ###
###==========================================================================###

###==========================================================================###
###  General purpose functions                                               ###
###==========================================================================###

## returns a string puts angle brackets around "string", as well as a newline
def format(string, indentLevel):
    returnString = indentString(indentLevel)
    returnString += "<" + string + ">\n"
    return returnString


## returns a string containing indentLevel spaces
def indentString(indentLevel):
    outputString = ""
    for x in range(0, indentLevel):
        outputString += " "
    return outputString


## get a token type from input string (id, number, write)
def scan():
    global index
    global input
    tempIndex = index
    tempString = state1(input)
    index = tempIndex
    return tempString


## print the value of the current token in the token string (X, 123)
def printSymbol():
    global index
    global input
    state1(input)
    tempIndex = index
    index = 0
    return input[:tempIndex]


## removes a token from the input string
def consume():
    global index
    global input
    state1(input)
    text = input
    input = input[index:]
    text = input
    # if input string is not empty, trim any spaces and newline characters
    #  that occur before the next token
    while input and (input[0] == " " or input[0] == "\n"):
        input = input[1:]
        text = input
    index = 0


## primer function sets global variable input and runs begins our CFG
def buildParseTree(inputString):
    global input
    input = inputString
    print(program())


###==========================================================================###
###  End of general purpose functions                                        ###
###==========================================================================###

## "main" function
# make sure an input file was given as a parameter
if len(sys.argv) > 1:
    try:
        # if an input file was given, try to open it
        with open(sys.argv[1], 'r') as file:
            s = file.read()
    except:
        print("ERROR: The file \"" + sys.argv[1] + "\" does not exist!\n")
        print("Please make sure your text file is in the same\nworking directory as the python file")

    # if the given input file is empty, we can't do anything
    if len(s) == 0:
        print("ERROR: There isn't anything in \"" + sys.argv[1] + "\"")
    else:
        # trim possible trailing new line characters
        if s[len(s) - 1] == "\n":
            s = s[:len(s) - 1]
        # AND NOW RUN THE PROGRAM
        buildParseTree(s)
else:
    print("ERROR: No input file given")
