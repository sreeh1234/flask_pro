from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def fun1():
    return render_template('index.html')