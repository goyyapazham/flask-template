from flask import Flask

nala = Flask(__name__)

@nala.route("/x")

def printx():
    return "x"

@nala.route("/y")

def printy():
    return "y"

@nala.route("/z")

def printz():
    return "z"

if __name__ == '__main__':
    nala.run()
