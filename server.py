from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I'm {}. I'm {}.".format(os.getenv("NAME"), os.getenv("AGE"))

@app.route("/secret")
def secret():
    return "User: {}. Password: {}.".format(os.getenv("USER"), os.getenv("PASSWORD"))

@app.route("/configmap")
def configmap():
    f = open("/app/myfamily/family.txt", "r")
    return "My Family: {}.".format(f.read())

createdat = datetime.now()
@app.route("/healthz")
def healthz():
    duration = (datetime.now() - createdat).total_seconds()
    if duration < 10:
        return "Duration: {}".format(duration)
    else:
        return "OK"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")