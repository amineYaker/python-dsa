from SimpleStack import Stack
from Queue import Queue

# Define operators and their precedence
# We group single character of equal precedence in strings
# lowest precedence is on the left
# parentheses are treated as high precedence operators

## the basic idea is to use a **stack** for operators and a queue for operands

operators = ["|", "&", "+-", "*/", "^","()"]

def precedence(operator: str) -> int: # Get the precedence of an operator
    for p, ops in enumerate(operators):
        if operator in ops:
            return p + 1

def delimiter(character): # Determine if a character is a delimiter
    return precedence(character) == len(operators)

def nextToken(s):
    token = ""
    s = s.strip()
    if len(s) > 0:
        if precedence(s[0]): # check if operator
            token = s[0]
            s = s[1:]
        else:
            while len(s) > 0 and not (precedence(s[0]) or s[0].isspace() ):
                token += s[0]
                s = s[1:]
    return token, s # return the token and remaining input

def postfix_translate(formula):
    '''Translates infix notated formula into postfix. 
            it helps evaluating the expression to use the Reverse Polish Notation 
            the algorithm uses a **stack** for operators and a **queue** for operands'''

    postfix = Queue(100)
    s = Stack(100)
    token, formula = nextToken(formula)

    while token:
        prec = precedence(token) # is it operator ?
        delim = delimiter(token) # is it a delimiter ?
        if delim: # delimiter
            if token == '(':
                s.push(token)
            else: # closing parenthesis
                while not s.isEmpty():
                    top = s.pop() # popping items from the stack until we find the opening one
                    if top == '(':
                        break
                    else:  # put rest in output
                        postfix.insert(top)
        elif prec:       # it is an operator we check the precedence
            while not s.isEmpty():
                top = s.pop()
                if (top == '(' or precedence(top) < prec):
                    s.push(top)  # we push it back because it is lower operator or the opening parenthesis of the current expression
                    break
                else:      # else top is higher precedence operator
                    postfix.insert(top) # we output it
            s.push(token) # push the (op) token in the stack
        else:                       # Input token is an operand
            postfix.insert(token)   # it goies straight to output
        
        token, formula = nextToken(formula)
    
    while not s.isEmpty(): # at the end of input, pop the stack
        postfix.insert(s.pop())
    
    ans = ""
    while not postfix.isEmpty():
        if len(ans) > 0:
            ans+= " "
        ans+= postfix.remove()
    return ans


if __name__ == '__main__':
    infix_expr = input("Infix expression to translate: ")
    print("the postfix representation of", infix_expr, "is:\n", postfix_translate(infix_expr))