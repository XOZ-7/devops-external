from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('/', methods=['POST'])
def register():
    name = request.form['name']
    year = request.form['year']
    return render_template('register.html', name=name, year=year, methods=['POST'])

def __name__ == '__main__':
    app.run(debug=True)