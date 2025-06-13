import tkinter as tk
from math import *

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#e6f2ff")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, bg="#e6f2ff")
        input_frame.pack(pady=10)

        input_field = tk.Entry(input_frame, font=('arial', 20, 'bold'), textvariable=self.input_text,
                               width=25, bd=5, relief='ridge', justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Button layout
        button_frame = tk.Frame(self.root, bg="#cce6ff")
        button_frame.pack()

        # Buttons
        buttons = [
            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', 'log'],
            ['1', '2', '3', '-', 'x^y'],
            ['0', '.', '(', ')', '+'],
            ['sin', 'cos', 'tan', '!', 'C'],
            ['=']
        ]

        for row_index, row in enumerate(buttons):
            for col_index, button in enumerate(row):
                if button == '=':
                    tk.Button(button_frame, text=button, width=40, height=2, fg='white', bg='#004080',
                              font=('arial', 12, 'bold'),
                              command=self.calculate).grid(row=row_index, column=col_index, columnspan=5, pady=5)
                else:
                    tk.Button(button_frame, text=button, width=7, height=2, bg='#99ccff', fg='black',
                              font=('arial', 12, 'bold'),
                              command=lambda b=button: self.on_button_click(b)).grid(row=row_index, column=col_index, pady=5, padx=2)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == 'sqrt':
            self.expression += "sqrt("
        elif char == 'log':
            self.expression += "log10("
        elif char == 'sin':
            self.expression += "sin(radians("
        elif char == 'cos':
            self.expression += "cos(radians("
        elif char == 'tan':
            self.expression += "tan(radians("
        elif char == 'x^y':
            self.expression += "**"
        elif char == '!':
            self.expression += "factorial("
        else:
            self.expression += str(char)
        self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression + (")" * self.expression.count("("))))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
