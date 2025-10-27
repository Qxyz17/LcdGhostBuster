import tkinter as tk
from tkinter import ttk, messagebox
import time, threading

class SetupWin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('LCD Ghost Buster – 设置时长')
        self.resizable(0, 0)
        ttk.Label(self, text='修复时长（分钟）：').grid(row=0, column=0, padx=10, pady=10)
        self.v = tk.StringVar(value='5')
        self.e = ttk.Entry(self, textvariable=self.v, width=5, justify='center')
        self.e.grid(row=0, column=1, padx=10)
        self.e.focus()
        ttk.Button(self, text='开始修复', command=self.start).grid(row=1, column=0, columnspan=2, pady=10)
        self.bind('<Return>', lambda e: self.start())

    def start(self):
        try:
            minutes = float(self.v.get())
            if not (0.1 <= minutes <= 120):
                raise ValueError
        except ValueError:
            messagebox.showerror('错误', '请输入 0.1~120 之间的数字')
            return
        self.destroy()
        FlashWin(minutes).mainloop()
