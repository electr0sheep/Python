import sys

__author__ = 'michaeldegraw'

index = 0
output = ""


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


def scan(string):
    global output
    while index < len(s):
        temp = state1(s)
        if temp == "error":
            output = "error"
            return
        else:
            output += temp
            output += ", "


# "main" function
if len(sys.argv) > 1:
    try:
        with open(sys.argv[1], 'r') as file:
            s = file.read()

        scan(s)
        output = output[:-2]
        if len(output) == 0:
            print("ERROR: There isn't anything in \"" + sys.argv[1] + "\"")
        else:
            print(output)
    except:
        print("ERROR: The file \"" + sys.argv[1] + "\" does not exist!\n")
        print("Please make sure your text file is in the same\nworking directory as the python file")

else:
    print("ERROR: No input file given")
