from dash import Dash, html,dash_table,Input,Output,callback,dcc
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
            #第一欄位：表頭名稱
            html.Div([
                html.Div([
                    html.H1("台北市youbike及時資料")
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'}),
            #第二欄位：搜尋框及確認按鈕
            html.Div([
                html.Div([
                    #第二欄位：搜尋框
                    html.Div([
                                dbc.Label("站點名稱"),
                                dbc.Input(id='input_value',
                                          placeholder="請輸入站點名稱", type="text"),                                
                    ])
                ],className="col"),
                    #第二欄位：確認按鈕
                    html.Div([
                        html.Button('確定', id='submit-val',className="btn btn-primary")
                    ],className="col"),
                    #第二欄位：輸出搜尋框的值到cli上
                    html.Div(children="輸入內容",
                            id="output-content",
                            className="col"),
            ],
            className="row row-cols-auto align-items-end",
            style={"paddingTop":'2rem'}),
            #第三欄位：treeview表格顯示
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
                        row_selectable="single",
                        selected_rows=[]
                    ),
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'0.5rem'}),
            #第四欄位：treeview表格單欄顯示
            html.Div([
                html.Div(children="",className="col",id='showMessage')
            ],
            className="row",
            style={"paddingTop":'2rem'})

        ])
    ],
    className="container-lg"
    )

# 註冊輸入列動作
@callback(
        Output('output-content','children'),
        Input('submit-val','n_clicks'),
        Input('input_value','value')
)
def clickBtn(n_clicks:None | int,inputValue:str):
    if n_clicks is not None:
        #一定先檢查有沒有按button
        print(inputValue)


# 註冊單選按鈕動作
@callback(
      Output('showMessage','children'),
      Input('main_table','selected_rows')  
)
def selectedRow(selected_rows:list[int]):
    #取得一個站點的series
    if len(selected_rows) !=0:
        oneSite:pd.Series= lastest_df1.iloc[selected_rows]
        oneTable=dash_table.DataTable(oneSite.to_dict('records'),[{"name": i, "id": i} for i in oneSite.columns])
        return [oneTable]
    
    return str(selected_rows)