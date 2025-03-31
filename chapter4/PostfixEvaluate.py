from PostfixTranslate import *
from SimpleStack import *

def postfix_evaluate(formula):
    '''Evaluates a postfix notated expression using a stack.'''

    postfix = postfix_translate(formula)
    s= Stack(100)

    token, postfix = nextToken(postfix)

    while token:
        prec = precedence(token)

        if prec:
            right = s.pop()
            left = s.pop()
            
            match token:
                case '|':
                    s.push(left | right)
                case '&':
                    s.push(left & right)
                case '+':
                    s.push(left + right)
                case '-':
                    s.push(left - right)
                case '*':
                    s.push(left * right)
                case '/':
                    s.push(left / right)
                case '%':
                    s.push(left % right)
                case '^':
                    s.push(left ^ right)
        else:
            s.push(int(token))

        print("after processing", token, "stack holds:", s)

        token, postfix = nextToken(postfix)

    print('Final result =', s.pop())

if __name__ == '__main__':
    infix_expr = input("Infix expression to translate: ")
    print("the postfix representation of", infix_expr, "is:\n", postfix_translate(infix_expr))
    postfix_evaluate(infix_expr)


        