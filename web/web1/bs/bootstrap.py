<<<<<<< HEAD
from flask import Blueprint,render_template
import pandas as pd
from . import datasource

bp = Blueprint('bs', __name__, url_prefix='/bs')

@bp.route("/")
def index():
    return render_template("bs/index.html")

@bp.route("/test1")
def test():
    data:list[tuple] = datasource.lastest_datetime_data()
    return render_template("bs/test1.html",data=data)

@bp.route("/product")
def product():
    return render_template("bs/product.html")

@bp.route("/profile")
def profile():
    return render_template("bs/profile.html")
=======
from flask import Blueprint,render_template
from bs import datasource
import pandas as pd

bp = Blueprint('bs', __name__, url_prefix='/bs')

@bp.route("/")
def index():
    return render_template("bs/index.html")

@bp.route("/test1")
def test1():
    data:list[tuple]=datasource.lastest_datetime_data()
    dataframe=pd.DataFrame(data)
    print(dataframe)
    return render_template("bs/test1.html")

@bp.route("/product")
def product():
    return render_template('bs/product.html')

@bp.route("/profile")
def profile():
    return render_template('bs/profile.html')
>>>>>>> 1f97109faefd784e19b77469af4c741e16ad767f
