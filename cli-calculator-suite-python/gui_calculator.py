import tkinter as tk

def click(event):
    current = str(entry.get())
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current.replace('^', '**'))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("GUI Calculator")

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["%", "^"]
]

for row in buttons:
    frame = tk.Frame(root)
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18", width=4, height=2)
        b.pack(side=tk.LEFT, expand=True, fill="both")
        b.bind("<Button-1>", click)
    frame.pack(expand=True, fill="both")

root.mainloop()
