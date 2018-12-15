import tkinter as tk
from tkinter import ttk
# include components
# from frames.menu import *
from toolbar import *
from sidebar import *
from mainframe import *
from buttombar import ButtomBar

import win32gui, win32con
The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)

def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

# Init master
root        = tk.Tk()
content     = tk.Frame(root, bg="white")

# Menu
# menu = Menu(root)

# Slaves
toolbar     = ToolBar(content)
sidebar     = SideBar(content)
buttombar   = ButtomBar(content)
main        = MainFrame(content)

# Layout
content.grid    (column=0, row=0, sticky="nsew")
## subFrames
# toolbar.widget().grid      (column=0, row=0, columnspan=3, sticky="nsew")
sidebar.widget().grid      (column=0, row=1, rowspan=2, sticky="ns")
main.widget().grid         (column=1, row=1, sticky="nsew")
buttombar.widget().grid    (column=1, row=2, sticky="nsew")
## Weight
root.columnconfigure    (0, weight=1)
root.rowconfigure       (0, weight=1)
content.columnconfigure (0, weight=0)
content.columnconfigure (1, weight=1)
content.rowconfigure    (0, weight=0)
content.rowconfigure    (1, weight=4)
content.rowconfigure    (2, weight=0)

# Root config
root.title("Queue Analyzer - by Illia Korzun IK-61 KPI")
# root.iconbitmap(r'C:/Users/NLIOXA/Desktop/PyApp/Sources/images/icon.ico')
# root.config(menu=menu.widget())
root.geometry("800x600")
center(root)


# Events
def update_canvas(event):          
     sidebar.update_vars(event)
     if any(vars.values()) > 0 and vars['n'] + vars['m'] <= 116:
          main.update(vars)
     if vars['n'] > 0:
          buttombar.update(vars)
## update canvas
sidebar.button().bind('<Button-1>', update_canvas)

# Loop
root.mainloop()
