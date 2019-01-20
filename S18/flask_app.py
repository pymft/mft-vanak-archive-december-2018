from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("login.html")


@app.route('/login')
def login():
    return render_template("sample.html")

@app.route('/test/<int:m>/<int:n>')
def something(m, n):
    # text = "<h1> hello </h1>" * num

    return render_template("test.html", m=m, n=n)






app.run()
