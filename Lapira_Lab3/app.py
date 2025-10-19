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

if __name__ == "__main__":
    app.run(debug=True)
