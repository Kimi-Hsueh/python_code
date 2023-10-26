import tkinter as tk
from tkinter import ttk
import datasource #從datasource.py抓取資料
from tkinter import messagebox


class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            datasource.update_sqlite_data()
        except Exception:
            messagebox.showerror('下載錯誤','網路狀態不正常\n將關閉視窗\n請稍候再重試')
            self.destroy()

        #for item in data:
            #print(item)


def main():
    window=Window()
    window.title('台北市youbike2.0查詢') #建立視窗名稱
    window.geometry('600x300') #建立視窗大小
    window.resizable(width=False,height=False) #限定視窗大小無法變化
    window.mainloop()


if __name__ =="__main__":
    main()