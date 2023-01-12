import tkinter as tk

window = tk.Tk()

c = tk.Canvas(window, height=400, width=600)
c.pack()

player = c.create_rectangle(100, 50, 150, 100, fill="red")


def player_move(action):
    global player

    x, y, x1, y1 = c.coords(player)

    if action == "top":
        c.move(player, 0, -10)

    elif action == "down":
        c.move(player, 0, 10)

    elif action == "right":
        c.move(player, 10, 0)

    elif action == "left":
        c.move(player, -10, 0)


def keypress_handler(event):
    # print("Pressed", event.keysym)
    if event.char == 'w': #
        player_move('top')
    if event.char == 's':
        player_move('down')
    if event.char == 'd':
        player_move('right')
    if event.char == 'a':
        player_move('left')

window.bind("<KeyPress>", keypress_handler)

window.mainloop()
