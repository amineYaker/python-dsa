from SimpleStack import *

stack = Stack(100)

expr = input("Expression to check: ")

errors = 0

for pos, letter in enumerate(expr):
    if letter in "{[(": # look for starting delimeters
        if stack.isFull():
            raise Exception('stack overflow on expression')
        else:
            stack.push(letter)
    elif letter in "}])":
        if stack.isEmpty():
            print("Error:", letter, "at position", pos, "has no mathcing left delimeter")
            errors+=1
        else:
            left = stack.pop()
            if not(left =="{" and letter == "}" or 
                   left =="(" and letter == ")" or 
                   left=="[" and letter == "]"):
                print("Error:", letter, "at position", pos, "does not match delimeter", left)
                errors+=1

if stack.isEmpty() and errors == 0:
    print("Delimeters are balanced in expression", expr)
elif not stack.isEmpty(): # Any delimeter on the stack were not matched
    print("Expression missing right delimeter for", stack)