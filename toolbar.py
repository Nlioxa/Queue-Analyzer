import tkinter as tk
from tkinter import ttk

class ToolBar:

    def __init__(self, master):
        self.frame = tk.Frame(master, width=800, height= 25, bd=2, bg="white", relief="groov")

    def widget(self):
        return self.frame