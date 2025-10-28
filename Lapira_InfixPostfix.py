def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    ops = []
    output = []

    for token in expression:
        if token == ' ':
            continue  
        if token.isalnum():
            output.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                output.append(ops.pop())
            if ops and ops[-1] == '(':
                ops.pop()
            else:
                return "Mismatched parentheses, Invalid."
        elif token in '+-*/^':
            while (ops and ops[-1] != '(' and
                   ((token != '^' and precedence(ops[-1]) >= precedence(token)) or
                    (token == '^' and precedence(ops[-1]) > precedence(token)))):
                output.append(ops.pop())
            ops.append(token)
        else:
            return f"Invalid token: {token}"

    while ops:
        if ops[-1] in '()':
            return "Mismatched parentheses, Invalid."
        output.append(ops.pop())

    return ''.join(output)


def main():
    while True:
        print("::: Infix to Postfix Converter :::")
        expression = input("Enter infix expression: ")
        if not expression:
            print("No expression provided.\n")
            continue
        postfix = infix_to_postfix(expression)
        print(f"Postfix expression: {postfix}\n")


if __name__ == "__main__":
    main()


