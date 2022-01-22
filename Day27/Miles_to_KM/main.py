import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        
    def __calculate(self):
        self.result_km.config(text=round(float(self.input_field.get()) * 1.609, 2))
        
    def create_widgets(self):
        self.input_field = tk.Entry(width=10)
        self.input_field.grid(row=0, column=1)
        
        self.mile_label = tk.Label(text="Miles")
        self.mile_label.grid(row=0, column=2)
        
        self.equal_label = tk.Label(text="is equal to")
        self.equal_label.grid(row=1, column=0)
        
        self.result_km = tk.Label()
        self.result_km.grid(row=1, column=1)
        
        self.km_label = tk.Label(text="KM")
        self.km_label.grid(row=1, column=2)
        
        self.calc_btn = tk.Button(text="Calculate", command=self.__calculate)
        self.calc_btn.grid(row=2, column=1)
        
app = App()
app.master.title("Mile to KM")
app.master.config(padx=50, pady=50)
app.mainloop()
