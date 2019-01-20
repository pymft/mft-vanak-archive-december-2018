from flask import Flask, render_template, request, redirect
import pygal


app = Flask(__name__)

@app.route('/chart/<int:myvalue>')
def chart(myvalue):
    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage in February 2012 (in %)'
    pie_chart.add('IE', 19.5)
    pie_chart.add('Firefox', 36.6)
    pie_chart.add('Chrome', 36.3)
    pie_chart.add('Safari', 4.5)
    pie_chart.add('Opera', 2.3)

    pie_chart.add('My Value', myvalue)
    return render_template('charts.html', chart=pie_chart.render_data_uri())

@app.route('/')
def hello():
    return render_template("login.html")

@app.route('/login', methods=["GET", "POST"])
@app.route('/login/<color>', methods=["GET", "POST"])
def login(color="008888"):
    if request.method == 'GET':
        color = "#" + color
        return render_template("enroll.html", color=color)
    if request.method == 'POST':
        return redirect("/test")

@app.route('/test')
@app.route('/test/<int:m>/<int:n>')
def something(m=10, n=10):
    # text = "<h1> hello </h1>" * num

    return render_template("test.html", m=m, n=n)






app.run(host="0.0.0.0", port=8000)
