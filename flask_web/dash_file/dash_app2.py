from dash import Dash, html
import plotly.express as px
import pandas as pd

dash2 = Dash(requests_pathname_prefix="/dash/app2/")

dash2.layout =html.Div([
    html.H1('DASH H1'),
    html.P('台灣最混的網頁上線嚕'),
    html.P('無聊男子24小時不在線')
])