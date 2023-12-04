import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Window(tk.Tk):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("images")
        self.geometry('512x512')
        self.configure(background='#CA7853')



class MyFrame(tk.Frame):

    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.configure(background='#9E7A7A')
        self.img=Image.open('wifi.png')
        self.wifi=ImageTk.PhotoImage(self.img)
        canvas=tk.Canvas(self,
                         width=128,
                         height=128
                         )
        canvas.create_image(64,64,image=self.wifi,anchor=tk.CENTER)
        canvas.pack()
        self.pack(expand=1, fill='both')

def main():    
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()

if __name__ == "__main__":
    main()
