from dash import Dash, html,dash_table
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from .assets import datasource
import pandas as pd


#-----指定網頁路徑的名稱及套用dash_bootstrap_components設定-----#
dash2 = Dash(requests_pathname_prefix="/dash/app2/",external_stylesheets=[dbc.themes.BOOTSTRAP])

#-----頁籤的命名-----#   
dash2.title='DASH的示範網頁'

#-----導入資料來源-----#
lastest_data = datasource.lastest_datetime_data()
lastest_df = pd.DataFrame(lastest_data,columns=['站點名稱','更新時間','行政區','地址','總數','可借','可還'])
lastest_df1 = lastest_df.reset_index()
lastest_df1['站點名稱'] = lastest_df1['站點名稱'].map(lambda name:name[11:])


dash2.layout = html.Div(
    [
        dbc.Container([
            html.Div([
                html.Div([
                    html.H1("台北市youbike及時資料")
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'}),
            html.Div([
                html.Div([
                    dash_table.DataTable(
                        data=lastest_df1.to_dict('records'),
                        columns=[{'id':column,'name':column} for column in lastest_df.columns],
                        page_size=20,
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        fixed_rows={'headers': True}
                    ),
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'}),
        ])
    ],
    className="container-lg"
    )