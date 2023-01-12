import tkinter as tk

window = tk.Tk()

c = tk.Canvas(window, height=400, width=600)
c.pack()

player = c.create_rectangle(100, 50, 150, 100, fill="red")


def player_move(action):
    global player

    x, y, *other = c.coords(player)

    if action == "top":
        c.move(player, x, y + 10)

    elif action == "down":
        c.move(player, x, y - 10)

    elif action == "right":
        c.move(player, x + 10, y)

    elif action == "left":
        c.move(player, x - 10, y)


def keypress_handler(event):
    print("Pressed", event.keysym)


window.bind("<KeyPress>", keypress_handler)

window.mainloop()
