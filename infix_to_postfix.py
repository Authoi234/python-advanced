def infix_to_postfix(expression):
    precedence = {}
    precedence["/"] = 2
    precedence["*"] = 2
    precedence["-"] = 1
    precedence["+"] = 1

    operators = Stack()    
