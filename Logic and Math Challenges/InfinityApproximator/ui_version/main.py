# main.py - UI version
# A GUI interface using Tkinter for the Infinity Approximator

import tkinter as tk
from tkinter import ttk, messagebox
from modules import series_approximations

def compute():
    try:
        function = function_var.get()
        terms = int(terms_entry.get())

        if function == "e":
            result = series_approximations.e_approx(terms)
        elif function == "π":
            result = series_approximations.pi_approx(terms)
        elif function == "sin(x)":
            x = float(extra_entry.get())
            result = series_approximations.sin_approx(x, terms)
        elif function == "ln(1 + x)":
            x = float(extra_entry.get())
            result = series_approximations.ln1p_approx(x, terms)
        else:
            result = "Invalid function"

        result_label.config(text=f"Result: {result}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Infinity Approximator")

function_var = tk.StringVar()
function_dropdown = ttk.Combobox(root, textvariable=function_var)
function_dropdown['values'] = ("e", "π", "sin(x)", "ln(1 + x)")
function_dropdown.grid(row=0, column=1)
ttk.Label(root, text="Function:").grid(row=0, column=0)

terms_entry = ttk.Entry(root)
terms_entry.grid(row=1, column=1)
ttk.Label(root, text="Number of Terms:").grid(row=1, column=0)

extra_entry = ttk.Entry(root)
extra_entry.grid(row=2, column=1)
ttk.Label(root, text="x value (if needed):").grid(row=2, column=0)

ttk.Button(root, text="Compute", command=compute).grid(row=3, column=0, columnspan=2)

result_label = ttk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
