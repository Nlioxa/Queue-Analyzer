import tkinter as tk
from tkinter import ttk

# menu

class Menu:

    def __init__(self, master):
        self.menu = tk.Menu(master)
        self.file_menu   = self.menu.add_cascade(menu=tk.Menu(self.menu), label="File")
        self.schema_menu = self.menu.add_cascade(menu=tk.Menu(self.menu), label="Schema")
        self.view_menu   = self.menu.add_cascade(menu=tk.Menu(self.menu), label="View")
        self.action_menu = self.menu.add_cascade(menu=tk.Menu(self.menu), label="Action")
        self.help_menu   = self.menu.add_cascade(menu=tk.Menu(self.menu), label="Help")

    def widget(self):
        return self.menu