import tkinter as tk
from tkinter import ttk
import datasource #從datasource.py抓取資料
from tkinter import messagebox
from threading import Timer


class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            datasource.update_sqlite_data()
        except Exception:
            messagebox.showerror('下載錯誤','網路狀態不正常\n將關閉視窗\n請稍候再重試')
            self.destroy()
'''
def on_closing(w:Window):
    print('結束視窗')
    t.cancel()
    w.destroy()

t=None
def update_data()->None: #設定更新資料的時間
    print('做事')
    global t #這邊是把全域變數t引進到method“update_data”內
    t=Timer(20,update_data) #每20秒執行一次
    t.start()#程式開始運作時即啟動
'''
t=None
def main():
    def on_closing(w:Window):
        print('結束視窗')
        t.cancel()
        w.destroy()
    
    def update_data()->None: #設定更新資料的時間
        print('做事')
        global t #這邊是把全域變數t引進到method“update_data”內
        t=Timer(20,update_data) #每20秒執行一次
        t.start()#程式開始運作時即啟動
    window=Window()
    window.title('台北市youbike2.0查詢') #建立視窗名稱
    window.geometry('600x300') #建立視窗大小
    window.resizable(width=False,height=False) #限定視窗大小無法變化
    update_data()
    window.protocol('WM_DELETE_WINDOW', lambda:on_closing(window))
    window.mainloop()


if __name__ =="__main__":
    main()