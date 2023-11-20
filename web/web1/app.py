from flask import Flask,url_for,render_template
import random
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    name='津承舞'
    dataFrame=get_dataFrame()
    return render_template('index.html',name=name,dataFrame=dataFrame)

def get_dataFrame()->pd.DataFrame:
    data=[['路銘燕',77,88,66],
        ['王羊鳴',87,76,65],
        ['李緊技',58,68,71]]
    return pd.DataFrame(data,columns=["姓名","國文","英文","數學"])

@app.route('auth')