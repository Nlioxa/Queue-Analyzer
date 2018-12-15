import tkinter as tk
from tkinter import ttk

vars = {
    'λ': 0,
    'μ': 0,
    'n': 0,
    'm': 0
}

class SideBar:

    def __init__(self, master):
        # variables
        self.λ_var = tk.StringVar()
        self.μ_var = tk.StringVar()
        self.n_var = tk.StringVar()
        self.m_var = tk.StringVar()

        # widgets
        self.frame = tk.Frame(master, width=200, height=400, bd=2, bg="#e5e5e5", relief="groov")

        self.label = tk.Label(self.frame, text="INPUT", bg="#e5e5e5", relief="groov")

        self.ubutton = tk.Button(self.frame, text="Calculate", relief="groov")

        self.λ_entry = tk.Entry(self.frame, textvariable=self.λ_var, width=10)
        self.λ_label = tk.Label(self.frame, text="λ = ", width=5, bg="#e5e5e5")

        self.μ_entry = tk.Entry(self.frame, textvariable=self.μ_var, width=10)
        self.μ_label = tk.Label(self.frame, text="μ = ", width=5, bg="#e5e5e5")

        self.n_entry = tk.Entry(self.frame, textvariable=self.n_var, width=10)
        self.n_label = tk.Label(self.frame, text="n = ", width=5, bg="#e5e5e5")

        self.m_entry = tk.Entry(self.frame, textvariable=self.m_var, width=10)
        self.m_label = tk.Label(self.frame, text="m = ", width=5, bg="#e5e5e5")

        # pack
        self.label.grid     (row=0, column=0, columnspan=2, sticky="nsew")
        self.λ_label.grid   (row=1, column=0)
        self.λ_entry.grid   (row=1, column=1)
        self.μ_entry.grid   (row=2, column=1)
        self.μ_label.grid   (row=2, column=0)
        self.n_entry.grid   (row=3, column=1)
        self.n_label.grid   (row=3, column=0)
        self.m_entry.grid   (row=4, column=1)
        self.m_label.grid   (row=4, column=0)

        self.ubutton.grid   (row=5, column=0, columnspan=2)
        # self.ubutton.bind('<Button-1>', self.update_vars)
        self.λ_entry.bind('<Return>', self.update_vars)
        self.μ_entry.bind('<Return>', self.update_vars)
        self.n_entry.bind('<Return>', self.update_vars)
        self.m_entry.bind('<Return>', self.update_vars)

        self.frame.rowconfigure     (0, weight=0)
        self.frame.columnconfigure  (0, weight=1)

    def widget(self):
        return self.frame

    def button(self):
        return self.ubutton

    def update_vars(self, event):
        global vars
        try:
            vars['λ'] = float(self.λ_entry.get())
            vars['μ'] = float(self.μ_entry.get())
            vars['n'] = int(self.n_entry.get())
            vars['m'] = int(self.m_entry.get())
        except ValueError:
            pass