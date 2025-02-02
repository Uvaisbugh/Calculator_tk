import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            screen_var.set("")
    elif text == "C":
        screen_var.set("")
    elif text == "Backspace":
        current_text = screen_var.get()
        screen_var.set(current_text[:-1])  # Remove the last character
    else:
        screen_var.set(screen_var.get() + text)

# Initialize main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry Field
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20 bold", bd=10, relief=tk.SUNKEN, justify="right")
screen.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

# Button Layout
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["Backspace"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack()
    for char in row:
        btn = tk.Button(frame, text=char, font="Arial 15", width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

# Run the application
root.mainloop()
