from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask via Kong!"

@app.route("/status")
def status():
    return {"status": "ok", "service": "flask-api"}

@app.route("/info")
def info():
    return {"author": "David", "version": "1.0"}