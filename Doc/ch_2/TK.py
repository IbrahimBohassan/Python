import tkinter as tk

root = tk.Tk()
root.title("My First Tk Window")
root.geometry("300x150")

def on_button_click():
    label.config(text="Hello From Ibrahim!")

label = tk.Label(root, text="Click the button below:")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=5)

root.mainloop()