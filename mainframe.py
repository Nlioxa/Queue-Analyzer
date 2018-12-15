import tkinter as tk
from tkinter import ttk


class MainFrame:

    def __init__(self, master):
        self.frame = tk.Frame(master, width=600, height=400, bd=2, bg="white", relief="groov")
        
        self.length_var = tk.StringVar(value=6)
        self.length_entry = tk.Entry(self.frame, textvariable=self.length_var, bg="white", relief="groov", width=50)
        self.label = tk.Label(self.frame, text="STATES SCHEMA", bg="white", relief="groov")
        self.length_label = tk.Label(self.frame, text="Count of states in a single row = ", bg="white", relief="groov", anchor='w')

        self.horizontalScroll = ttk.Scrollbar(self.frame, orient=tk.HORIZONTAL)
        self.verticalScroll = ttk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.canvas = tk.Canvas(self.frame, bg="white", scrollregion=(0, 0, 1000, 1000), 
            yscrollcommand=self.verticalScroll.set, xscrollcommand=self.horizontalScroll.set)
        
        self.horizontalScroll['command']    = self.canvas.xview
        self.verticalScroll['command']      = self.canvas.yview

        ttk.Sizegrip(self.frame).grid(column=3, row=2, sticky="se")
        self.horizontalScroll.grid  (row=2, column=0, columnspan=3, sticky="ew")
        self.verticalScroll.grid    (row=0, column=3, rowspan=2, sticky="ns")        
        self.canvas.grid            (row=1, column=0, columnspan=3, sticky="nsew")

        self.label.grid             (row=0, column=0, sticky="ew")
        self.length_entry.grid      (row=0, column=2, sticky="ew")
        self.length_label.grid      (row=0, column=1, sticky="we")

        # self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1) 

        self.row_length = 6

        # self.length_entry.bind('<Return>', self.update)

    def widget(self):
        return self.frame

    # drawing schema
    def update(self, vars):
        canvas = self.canvas
        canvas.delete('all')
        # algorithm
        for i in range(vars['n']+vars['m']+1):
            if i is 0:
                color = "lightgreen"
            elif i > 0 and i < vars['n']:
                color = "lightblue"
            elif i is vars['n']:
                color = "red"
            elif i > vars['n']:
                color = "yellow"    

            try:
                if int(self.length_entry.get()) > 13 or int(self.length_entry.get()) < 5:
                    raise ValueError
                self.row_length = int(self.length_entry.get())
            except ValueError:
                pass
            row_length = self.row_length
            a = 50
            abs_y = 100*((i+1)//row_length+1)
            if (i+1)%row_length is 0 and i is not 0: abs_y -= 100
            # if i//4 > 1 and i%4 > 0: abs_y -= 100
            delta_x = 100 + a*(i%row_length)        
            m0_rect = {
                'x': a * (i%row_length) - 50,
                'y': abs_y - 50
            }
            m1_rect = {
                'x': m0_rect['x'] + a,
                'y': m0_rect['y'] + a
            }
            canvas.create_rectangle(delta_x+m0_rect['x'], m0_rect['y'], delta_x+m1_rect['x'], m1_rect['y'], fill=color)
            # if i <= vars['n']+vars['m']:
            m0_line = {
                'x': m1_rect['x'],
                'y': m0_rect['y'] + a/2
            }
            m1_line = {
                'x': m0_line['x'] + a,
                'y': m0_line['y']
            }
            if i < vars['n']+vars['m']:
                canvas.create_line(delta_x+m0_line['x'], m0_line['y']-a/4, delta_x+m1_line['x'], m1_line['y']-a/4, arrow=tk.LAST)
                canvas.create_line(delta_x+m0_line['x'], m0_line['y']+a/4, delta_x+m1_line['x'], m1_line['y']+a/4, arrow=tk.FIRST)
                canvas.create_text(a/2+delta_x+m0_line['x'], m0_line['y']-a/2, text='λ={0:.3f}'.format(vars['λ']))
                if i < vars['n']: 
                    μ_i = (i+1)*vars['μ']
                else: 
                    μ_i = vars['n']*vars['μ']
                canvas.create_text(a/2+delta_x+m0_line['x'], m0_line['y']+a/2, text='μ={0:.3f}'.format(μ_i))
            
            canvas.create_text(delta_x+m0_line['x']-a/2, m0_line['y'], text="S[{0}]".format(i))