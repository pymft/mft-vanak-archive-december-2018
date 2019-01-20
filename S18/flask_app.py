from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>hello</h1>"


@app.route('/login')
def login():
    with open("./sample.html", 'r') as f:
        text = f.read()
    return text




app.run()
