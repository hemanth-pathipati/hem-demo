import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Replace with your actual ExchangeRate API key
API_KEY = "dbe4c6ba2cdd33bcc3709371"
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Currency Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.create_widgets()
        self.get_currency_list()

    def create_widgets(self):
        # Amount
        tk.Label(self.root, text="Amount:", font=("Arial", 12)).pack(pady=5)
        self.amount_entry = tk.Entry(self.root, font=("Arial", 12))
        self.amount_entry.pack()

        # From Currency
        tk.Label(self.root, text="From Currency:", font=("Arial", 12)).pack(pady=5)
        self.from_currency = ttk.Combobox(self.root, state="readonly", font=("Arial", 11))
        self.from_currency.pack()

        # To Currency
        tk.Label(self.root, text="To Currency:", font=("Arial", 12)).pack(pady=5)
        self.to_currency = ttk.Combobox(self.root, state="readonly", font=("Arial", 11))
        self.to_currency.pack()

        # Convert Button
        convert_btn = tk.Button(self.root, text="Convert", command=self.convert, bg="#007ACC", fg="white",
                                font=("Arial", 12, "bold"))
        convert_btn.pack(pady=10)

        # Result
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), fg="green")
        self.result_label.pack()

    def get_currency_list(self):
        try:
            response = requests.get(API_URL + "USD")
            data = response.json()
            currencies = sorted(data["conversion_rates"].keys())
            self.from_currency['values'] = currencies
            self.to_currency['values'] = currencies
            self.from_currency.set("USD")
            self.to_currency.set("EUR")
        except:
            messagebox.showerror("Error", "Could not fetch currency list. Check your API key or internet connection.")

    def convert(self):
        amount_str = self.amount_entry.get()
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()

        try:
            amount = float(amount_str)
            if amount < 0:
                raise ValueError("Amount must be positive")

            url = API_URL + from_curr
            response = requests.get(url)
            data = response.json()

            rate = data["conversion_rates"][to_curr]
            converted_amount = amount * rate

            self.result_label.config(
                text=f"{amount:.2f} {from_curr} = {converted_amount:.2f} {to_curr}"
            )
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid amount.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
