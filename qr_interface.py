import tkinter as tk

root = tk.Tk()
root.title("QR Code Scanner")

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=20)

def update_label(status):
    label.config(text=status)
