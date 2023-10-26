import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


def main():
    window=Window()
    window.title('台北市youbike2.0查詢') #建立視窗名稱
    window.geometry('600x300') #建立視窗大小
    window.resizable(width=False,height=False) #限定視窗大小無法變化
    window.mainloop()


if __name__ =="__main__":
    main()