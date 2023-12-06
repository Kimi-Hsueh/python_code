from dash import Dash, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

#-----指定網頁路徑的名稱及套用dash_bootstrap_components設定-----#
dash2 = Dash(requests_pathname_prefix="/dash/app2/",external_stylesheets=[dbc.themes.BOOTSTRAP])

dash2.layout =html.Div(
    [html.H1('全台灣最混的網站上線嚕'),
     html.P('24小時無聊男子不在線'),
     html.P('這是用dash-bootstrap做的')],
     style={'backgroundColor':'aqua'},
     className="container-lg"
)