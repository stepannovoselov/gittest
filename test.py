import tkinter as tk

window = tk.Tk()


def keypress_handler(event):
    print("Pressed", event.keysym)


window.bind("<KeyPress>", keypress_handler)

window.mainloop()
