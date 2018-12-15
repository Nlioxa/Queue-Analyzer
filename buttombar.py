import tkinter as tk
from tkinter import ttk
from math import factorial

class ButtomBar:

    def __init__(self, master):
        self.frame = tk.Frame(master, width=600, height=300, bd=2, bg="white", relief="groov")
        self.horizontalScroll = ttk.Scrollbar(self.frame, orient=tk.HORIZONTAL)
        self.verticalScroll = ttk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.output_text = tk.Text(self.frame, wrap="word", state="disabled", width=600, height=15)

        self.verticalScroll.grid(row=0, column=1, sticky="ns") 
        self.horizontalScroll.grid(row=1, column=0, sticky="ew")    
        ttk.Sizegrip(self.frame).grid(row=1, column=1, sticky="nsew")
        self.output_text.grid(row=0, column=0, sticky="nsew")

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        

        self.output_text['yscrollcommand'] = self.verticalScroll.set
        self.output_text['xscrollcommand'] = self.horizontalScroll.set

        self.verticalScroll['command'] = self.output_text.yview
        self.horizontalScroll['command'] = self.output_text.xview
        

    def widget(self):
        return self.frame

    def update(self, vars):
        self.output_text['state'] = 'normal'
        self.output_text.delete("1.0", tk.END)        
        output = ""
        # write output text here
        output += "SYSTEM CHARACTERISTICS" + "\n"
        ## Input data
        output += "• Input data:" + "\n"
        ### number of service channels
        output += "\t○ n: {0}".format(vars['n']) + "\t\t(number of service channels)" + "\n"
        ### number of places in line
        output += "\t○ m: {0}".format(vars['m']) + "\t\t(number of places in line)" + "\n"
        ### service intensity
        output += "\t○ μ: {0:.2f}".format(vars['μ']) + "\t\t(service intensity)" + "\n"
        ### flow rate
        output += "\t○ λ: {0:.2f}".format(vars['λ']) + "\t\t(flow rate)" + "\n"
        ## System states
        output += "• System states: " + "\n"
        ### states
        output += "S[0] – the system is free" + "\n"
        for i in range (1, vars['n']):
            if i is 1:
                output += "S[{0}] – {0} channel is busy, the rest are free".format(i) + "\n"
            else:
                output += "S[{0}] – {0} channels are busy, the rest are free".format(i) + "\n"
        output += "S[{0}] – all {0} channels are busy".format(vars['n']) + "\n"
        if vars['m'] > 0:
            for i in range (1, vars['m'] + 1):
                if i is 1:
                    output += "S[{0}] – all {1} channels are busy, {2} application is in the queue".format(i+vars['n'], vars['n'], i) + "\n"
                else:
                    output += "S[{0}] – all {1} channels are busy, {2} applications are in the queue".format(i+vars['n'], vars['n'], i) + "\n"
        ## The system of equations for the probabilities of states
        output += "• The system of equations for the probabilities of states:" + "\n"
        output += "\t○ dP[0] \t\t= {0}*P[1](t) - {1}*P[1](t)".format(vars['μ'], vars['λ']) + "\n"
        for i in range (1, vars['n']):
            output += "\t○ dP[{0}] \t\t= {3}*P[{1}](t) - {4}*P[{0}](t) + {5}*P[{2}](t)".format(i, i-1, i+1, vars['λ'], vars['λ']+i*vars['μ'], (i+1)*vars['μ']) + "\n"
        if vars['m'] > 0:
            output += "\t○ dP[{0}+m] \t\t= {3}*P[{1}](t) - {4}*P[{0}](t) + {5}*P[{2}](t)".format(
                vars['n'], vars['n']-1, vars['n']+1, vars['λ'], vars['λ'] + (vars['n']+vars['m'])*vars['μ'], (vars['n']+vars['m'])*vars['μ']) + "\n"
        else:
            output += "\t○ dP[{0}] \t\t= {1}*P[{2}](t) - {3}*P[{0}](t)".format(vars['n'], vars['λ'], vars['n']-1, vars['μ']*vars['n']) + "\n"
        ## The system of equations for the limit probabilities of the system
        output += "• The system of equations for the limit probabilities of the system:" + "\n"
        ### probability of service channel downtime
        p_0 = ((sum([ ( (vars['λ']/vars['μ'])**i ) / factorial(i) for i in range(0, vars['n'] + 1) ])) + (sum([ ( (vars['λ']/vars['μ'])**(i+vars['n']) ) / ( (vars['n']**i) * factorial(vars['n']) ) for i in range(1, vars['m'] + 1) ])))**(-1)
        output += "\t○ probability of service channel downtime:" + "\n"
        output += "\t\t* p[0] = {0:.12f}".format(p_0) + "\n"
        ### probability of k requirements in the system
        output += "\t○ probability of k requirements in the system:" + "\n"
        for i in range (1, vars['n'] + 1):
            output += "\t\t▪ p[{0}] \t\t= {1:.12f}".format(i, (( (vars['λ']/vars['μ'])**i ) / factorial(i))*p_0) + "\n"
        if vars['m'] > 0:
            for i in range (1, vars['m'] + 1):
                output += "\t\t▪ p[{0}+{1}] \t\t= {2:.12f}".format(i+vars['n'], i, (( (vars['λ']/vars['μ'])**(i+vars['n']) ) / ( (vars['n']**i) * factorial(vars['n']) ))*p_0) + "\n"
        ## Other system features
        output += "• Other system features:" + "\n"
        ### probability of denial of service
        p_denial = (( (vars['λ']/vars['μ'])**(vars['n']+vars['m']) ) / ( (vars['n']**vars['m']) * factorial(vars['n']) )) * p_0
        output += "\t○ p_denial = {0:.3f}".format(p_denial) + "\t\t\t(probability of denial of service)" + "\n"
        ### relative bandwidth
        q = 1 - p_denial
        output += "\t○ q = {0:.3f}".format(q) + "\t\t\t(relative bandwidth)" + "\n"
        ### absolute bandwidth
        A = vars['λ'] * q
        output += "\t○ A = {0:.3f}".format(A) + "\t\t\t(absolute bandwidth)" + "\n"
        ### average number of busy channels
        z = A / vars['μ']
        output += "\t○ z = {0:.3f}".format(z) + "\t\t\t(average number of busy channels)" + "\n"
        ### average number of applications in the queue
        r = ( ( (vars['λ']/vars['μ'])**(vars['n']+1) * p_0 ) / (vars['n'] * factorial(vars['n'])) ) * sum([ i * ( (vars['λ']/vars['μ'])/vars['n'] )**(i-1) for i in range(1, vars['m'] + 1) ])
        output += "\t○ r = {0:.3f}".format(r) + "\t\t\t(average number of applications in the queue)" + "\n"
        ### average number of applications associated with the system
        k = z + r
        output += "\t○ k = {0:.3f}".format(k) + "\t\t\t(average number of applications associated with the system)" + "\n"
        ### average waiting time
        t_waiting = r / vars['λ']
        output += "\t○ t_waiting = {0:.3f}".format(t_waiting) + "\t\t\t(average waiting time)" + "\n"
        ### average time spent in the system
        t_syst = t_waiting + q / vars['μ']
        output += "\t○ t_syst = {0:.3f}".format(t_syst) + "\t\t\t(average time spent in the system)" + "\n"
        # end of text

        # file = open("characteristics.txt", mode="w+", encoding="UTF-8")
        # file.write(output)
        # file.close()
        self.output_text.insert("1.0", output)
        self.output_text['state'] = 'disabled'