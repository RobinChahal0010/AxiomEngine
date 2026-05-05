import tkinter as tk
from sympy import sympify
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from math_engine import *
from scientific_calc import *

# ---------- SAFE EXEC ----------

def safe_exec(func):
    try:
        return func()
    except Exception:
        return "Error: Invalid Input"

# ---------- FUNCTIONS ----------

history_list = []

def update_history(exp, res):
    history_list.append(f"{exp} = {res}")
    history_var.set("\n".join(history_list[-5:]))

def sci_calc():
    exp = entry.get()
    res = safe_exec(lambda: calculate(exp))
    result.set(res)
    update_history(exp, res)

def derivative_btn():
    exp = entry.get()
    res = safe_exec(lambda: derivative(exp))
    result.set(res)
    update_history(exp, res)

def integral_btn():
    exp = entry.get()
    res = safe_exec(lambda: integral(exp))
    result.set(res)
    update_history(exp, res)

def simplify_btn():
    exp = entry.get()
    res = safe_exec(lambda: simplify_expr(exp))
    result.set(res)
    update_history(exp, res)

def solve_eq():
    exp = entry.get()
    res = safe_exec(lambda: solve_equation(exp))
    result.set(res)
    update_history(exp, res)

def system_solver():
    equations = text_box.get("1.0", tk.END).split("\n")
    res = safe_exec(lambda: solve_system(equations))
    result.set(res)

def clear_all():
    entry.delete(0, tk.END)
    result.set("")

# ---------- GRAPH EMBED ----------

def plot_graph():
    try:
        expr = sympify(entry.get())
        fig = plt.figure()
        x = list(range(-10, 10))
        y = [expr.subs('x', val) for val in x]

        plt.plot(x, y)
        plt.title("Graph")

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except:
        result.set("Error in graph")

# ---------- WINDOW ----------

root = tk.Tk()
root.title("Ultimate Math Solver PRO")
root.geometry("600x700")
root.configure(bg="#1e1e1e")

# ---------- ENTRY WITH PLACEHOLDER ----------

def on_click(event):
    if entry.get() == "Enter expression...":
        entry.delete(0, tk.END)

entry = tk.Entry(root, width=40, font=("Segoe UI", 12))
entry.insert(0, "Enter expression...")
entry.bind("<FocusIn>", on_click)
entry.pack(pady=10)

# ---------- BUTTONS ----------

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

tk.Button(frame, text="Scientific", command=sci_calc).grid(row=0, column=0)
tk.Button(frame, text="Derivative", command=derivative_btn).grid(row=0, column=1)
tk.Button(frame, text="Integral", command=integral_btn).grid(row=1, column=0)
tk.Button(frame, text="Simplify", command=simplify_btn).grid(row=1, column=1)
tk.Button(frame, text="Solve Eq", command=solve_eq).grid(row=2, column=0)
tk.Button(frame, text="Plot", command=plot_graph).grid(row=2, column=1)

tk.Button(root, text="Clear", command=clear_all, bg="red").pack(pady=5)

# ---------- SYSTEM SOLVER (N EQUATIONS) ----------

tk.Label(root, text="Enter multiple equations (one per line)").pack()

text_box = tk.Text(root, height=5, width=50)
text_box.pack()

tk.Button(root, text="Solve System", command=system_solver).pack(pady=10)

# ---------- RESULT ----------

result = tk.StringVar()
tk.Label(root, textvariable=result, fg="green").pack(pady=10)

# ---------- HISTORY ----------

history_var = tk.StringVar()
tk.Label(root, text="History", fg="white", bg="#1e1e1e").pack()
tk.Label(root, textvariable=history_var, fg="cyan", bg="#1e1e1e").pack()

root.mainloop()