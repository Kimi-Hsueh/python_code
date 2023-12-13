import plotly.express as px

df = px.data.gapminder().query("country=='India'")
df.rename(columns={'lifeExp':'平均壽命'},inplace=True)
#print(df) #驗證表格格式
fig = px.line(df, 
              x="year", 
              y="平均壽命", 
              title='印度的平均壽命', #設定圖表的要顯示的名稱
              hover_data='pop' #設定滑過圖表需顯示的欄位
              )
fig.show()


