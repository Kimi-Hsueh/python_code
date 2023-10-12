import dataSource #匯入已建立download method的py檔案
import tkinter as Tk #匯入視窗化tkinter模組
from tkinter import ttk

def main():
    window = Tk.Tk() #inital 視窗化tkinter模組
    window.title('這是py-tkinter視窗') #使用tk模組命名視窗名稱
    label=Tk.Label(window,text="我是kimi，不是mikey",font=('Helvetica', '30')) #設定視窗內文字內容及文字格式
    label.pack(padx=200,pady=100) #設定視窗大小，x是寬度，y是高度
    window.mainloop() #讓視窗一直保持運行，一直到按下“x”按鈕關閉它

if __name__ == '__main__':
    main()