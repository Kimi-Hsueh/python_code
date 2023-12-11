from dash import Dash, html,dash_table,Input,Output,callback
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
                        id='main_table',
                        data=lastest_df1.to_dict('records'),
                        columns=[{'id':column,'name':column} for column in lastest_df1.columns],
                        page_size=20,
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        fixed_rows={'headers': True},
                        style_cell_conditional=[
                                {   'if': {'column_id': 'index'},
                                 'width': '5%'
                                },
                                {   'if': {'column_id': '站點名稱'},
                                 'width': '25%'},
                                {   'if': {'column_id': '總數'},
                                 'width': '5%'},
                                {   'if': {'column_id': '可借'},
                                 'width': '5%'},
                                {   'if': {'column_id': '可還'},
                                 'width': '5%'},
                        ],
                        row_selectable="single", #在表單內增加單選按鈕
                        selected_rows=[] #預設單選按鈕為“不選擇”
                    ),
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'}),
            html.Div([
                html.H5("這是第3列",className="col",id='showMessage') #在網頁上新增第三個顯示區塊
            ],
            className="row",
            style={"paddingTop":'2rem'})

        ])
    ],
    className="container-lg"
    )


# 註冊單選按鈕動作
@callback(
      Output('showMessage','children'),
      Input('main_table','selected_rows')  
)
def selectedRow(selected_rows):
    print(selected_rows)
    return str(selected_rows)