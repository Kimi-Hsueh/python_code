import dataSource #匯入已建立download method的py檔案
import tkinter as Tk #匯入視窗化tkinter模組
from tkinter import ttk

class Winodwset(Tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('111年度人口統計') #使用tk模組命名視窗名稱
        self.configure(background='red') #設定視窗內的背景色

        topFrame=Tk.Frame(self,background='#86C166') #設定視窗上部欄位底色
        label=Tk.Label(topFrame,text="111年度人口統計",font=('Helvetica', '30')) #設定視窗內文字內容及文字格式
        label.pack(padx=200,pady=100) #設定視窗大小，x是寬度，y是高度
        topFrame.pack()

        bottomFrame=Tk.Frame(self,background='#8B81C3') #設定視窗下部欄位
        choies = dataSource.cityNames() #去dataSource呼叫cityNames()method
        choiesvar=Tk.StringVar(value=choies) #設定選單變數“choiesvar”
        listbox=Tk.Listbox(bottomFrame,listvariable=choiesvar,width=12) #設定下拉選單變數“listbox”在視窗的下部欄位，選單內容以“choiesvar”為內容，選單寬度為12px
        listbox.pack()
        bottomFrame.pack(expand=True,fill='x')
        
        

def main():
    window = Winodwset() #inital 視窗化tkinter模組
    window.mainloop() #讓視窗一直保持運行，一直到按下“x”按鈕關閉它
    
if __name__ == '__main__':
    main()