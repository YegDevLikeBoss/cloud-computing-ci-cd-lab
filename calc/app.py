from flask import Flask, request
from .settings import VERSION

app = Flask(__name__)

@app.route("/add")
def sum():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return {"result": sum(a, b)}, 200

@app.route("/version")
def ver():
    return {"v": VERSION}, 200

def sum(a, b):
    return a + b