import tkinter as tk

window = tk.Tk()

c = tk.Canvas(window, height=400, width=600)
c.pack()

player = c.create_rectangle(100, 50, 150, 100, fill="red")

def player_move(action):
    pass

def keypress_handler(event):
    print("Pressed", event.keysym)


window.bind("<KeyPress>", keypress_handler)

window.mainloop()
