import tkinter as tk
from tkinter import messagebox


def generate_fibonacci():
    try:
        n = int(entry.get())
        if n <= 0:
            messagebox.showwarning("Input Error", "Please enter a positive integer.")
            return

        fib = [0, 1]
        if n == 1:
            result = [0]
        elif n == 2:
            result = [0, 1]
        else:
            while len(fib) < n:
                fib.append(fib[-1] + fib[-2])
            result = fib

        result_label.config(text=f"Sequence: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")


root = tk.Tk()
root.title("Fibonacci Generator")
root.geometry("450x350")

tk.Label(root, text="Fibonacci Generator Task", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Enter number of terms:").pack()
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Generate", command=generate_fibonacci, bg="#2196F3", fg="white").pack(pady=20)
result_label = tk.Label(root, text="", wraplength=400, font=("Arial", 10))
result_label.pack(pady=10)

root.mainloop()
