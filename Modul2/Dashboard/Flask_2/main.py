from flask import Flask,render_template

# Setting / Configuration
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Ini Index </h1>'

@app.route('/about')
def about():
    return render_template('about.html' , nama = '')

if __name__ == '__main__':
    app.run(port=3000,debug=True)
