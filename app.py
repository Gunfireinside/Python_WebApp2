from flask import Flask,request,render_template

app = Flask(__name__)
@app.route("/")
def inex():
    return "Response Data"

@app.route("/another")
def another():
    return "Another Response"

@app.route("/test_request")
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route("/exercise_request/<value>")
def exercise_request(value):
    return f"{value}"

@app.route("/show_html")
def show_html():
    return render_template("test.html")

@app.route("/show_html2")
def show2_html():
    return render_template("test2.html")

@app.route("/exercise")
def exercise_name():
    return f'value:{request.args.get("my_name")}'