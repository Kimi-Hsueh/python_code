import csv
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('台積電')
        self.frame=Frame(self) #套用class Frame的所有實體

class Frame(ttk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.pack()

        self.scroll = tk.Scrollbar(self)
        self.scroll.pack(side='right', fill='y')
        self.tree=ttk.Treeview(self,columns=['1','2','3','4','5','6','7'],show='headings')
        self.scroll.configure(command=self.tree.yview)
        self.tree.heading(1,text='交易日')
        self.tree.heading(2,text='開盤價')
        self.tree.heading(3,text='最高價')
        self.tree.heading(4,text='最低價')
        self.tree.heading(5,text='收盤價')
        self.tree.heading(6,text='調整後收盤價')
        self.tree.heading(7,text='成交量')
        self.tree.pack()

        stock=self.price_list()
        for row in stock:
            self.tree.insert('', tk.END, values=row)

        self.tree.bind('<<TreeviewSelect>>',self.item_select)
        
        
        
    def price_list(self):
        stacklist=list()
        with open('./台積電.csv','r',encoding='utf-8') as file:
            reader=csv.reader(file)
            next=(file)
            for row in reader:
                stacklist.append(row)
        return stacklist
    
    def item_select(self,event):
        print(self.tree.selection())

def main():
    window=Window()
    window.mainloop()

if __name__ == '__main__':
    main()