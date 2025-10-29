from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("357x420+0+0")
        self.master.config(bg='gray')
        self.master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(self.master, width=17, bg='white', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()