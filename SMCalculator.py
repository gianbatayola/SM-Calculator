import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        font_tuple_1 = ("Times New Roman", 15, "bold")
        font_tuple_2 = ("Times New Roman", 10)

        style = ttk.Style()
        style.configure('W.TButton', font=font_tuple_2)

        self.title_label = tk.Label(self, text='{}'.format('SafeMoon Profitability'),
                                    font=font_tuple_1)
        self.title_label.pack()

        self.invest_label = tk.Label(self, text='Quantity to Invest (USD) :',
                                     font=font_tuple_2)
        self.invest_label.pack()
        self.invest_entry = tk.Entry(self)
        self.invest_entry.pack()

        self.asset_label = tk.Label(self, text='Asset Price (USD) :',
                                    font=font_tuple_2)
        self.asset_label.pack()
        self.asset_entry = tk.Entry(self)
        self.asset_entry.pack()

        self.profit_label = tk.Label(self, text='Final Value (USD) :',
                                     font=font_tuple_2)
        self.profit_label.pack()
        self.profit_entry = tk.Entry(self)
        self.profit_entry.pack()

        self.calc_button = ttk.Button(self, text='Calculate', style='W.TButton',
                                      command=self.calculate)
        self.calc_button.pack()

    def calculate(self):
        if self.invest_entry.get() and self.asset_entry.get() and self.profit_entry.get():
            real_value = float(self.invest_entry.get()) * 0.9
            current_price = float(self.asset_entry.get())
            final = float(self.profit_entry.get())
            appreciation_factor = final / real_value
            value = current_price * appreciation_factor
            tk.messagebox.showinfo('Attention', 'Sell at ${:.10f}'.format(value))
        else:
            tk.messagebox.showinfo('Attention', 'One or more invalid inputs')


app = App()
app.mainloop()
