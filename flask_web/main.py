from flask import Flask,render_template,url_for
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from dash_file.dash_app1 import dash1
from werkzeug.serving import run_simple

app = Flask(__name__)
application = DispatcherMiddleware(
    app,
    {"/app1": dash1.server},
) #中繼app，我要產生一個中繼的app
#
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    run_simple("localhost", 8080, application,use_debugger=True,use_reloader=True)