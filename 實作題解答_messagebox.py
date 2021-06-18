"""
Created on Tue Dec 31 09:49:42 2019

@author: ShawnHou
"""
import tkinter as tk
import tkinter.messagebox

def clickMe():
    content=entry.get()
    tkinter.messagebox.showinfo(title='提示', message=content)

window = tk.Tk()
window.title('我的tk')
window.geometry('300x300')
label = tk.Label(window,text='我的GUI')

label.pack()

entry = tk.Entry(window, width = 20)
entry.pack()

button = tk.Button(window, text = '按鈕',command = clickMe)
button.pack()

window.mainloop()
