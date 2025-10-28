from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaofTriangle', methods=['GET', 'POST'])
def area_of_triangle():
    result = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        result = 0.5 * base * height
    return render_template('areaofTriangle.html', result=result)

@app.route('/areaofCircle', methods=['GET', 'POST'])
def area_of_circle():
    result = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        result = 3.14159 * radius * radius
    return render_template('areaofCircle.html', result=result)

# infix to postfix

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

@app.route('/inpostfix', methods=['GET', 'POST'])
def inpostfix():
    result = None
    if request.method == 'POST':
        expression = request.form.get('inputString', '').strip()
        if not expression:
            result = "Please enter a valid expression."
        else:
            result = infix_to_postfix(expression)
    return render_template('inpostfix.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
