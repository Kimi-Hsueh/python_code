from flask import Flask,render_template,url_for
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from dash_file import app

app = Flask(__name__)
application = DispatcherMiddleware(
    app,
    {"/app1": app1.server, "/app2": app2.server},
)


@app.route("/")
def index():
    return render_template("index.html")