def do_operation(operand1, operand2, operator):
    # Convert operands to integers first
    num1 = int(operand1)
    num2 = int(operand2)
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 // num2
    else:
        raise ValueError("Unknown operator")

def postfix_evaluate1digit(expression):
    operands = []
    operators ="*/-+"

    for ch in expression:
        if ch.isdigit():
            operands.append(ch)
        elif ch in operators:
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = do_operation(operand1, operand2, ch)
            operands.append(str(result))

    result = operands.pop()
    return result

def postfix_evaluate_multidigit(expression):
    operands = []
    operators =["*","/","-","+"]

    expression_list = expression.split(",")

    for item in expression_list:
        if item in operators:
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = do_operation(operand1, operand2, item)
            operands.append(str(result))
        else:
            operands.append(item)            

    result = operands.pop()
    return result

if __name__ == "__main__":
    assert postfix_evaluate1digit("132*+") == "7" , "Wrong!!! ERROR ‼️ It should give  7"
    assert postfix_evaluate1digit("13+2*") == "8" , "Wrong!!! ERROR ‼️ It should give  8"
    assert postfix_evaluate1digit("13+24+*") == "24" , "Wrong!!! ERROR ‼️ It should give  24"
    assert postfix_evaluate1digit("132*+4+") == "11" , "Wrong!!! ERROR ‼️ It should give  11"
    assert postfix_evaluate1digit("13+2-") == "2" , "Wrong!!! ERROR ‼️ It should give  2"
    assert postfix_evaluate_multidigit("20,30,+,2,*,10,*,4,/") == "250" , "Wrong!!! ERROR ‼️ It should give  250"