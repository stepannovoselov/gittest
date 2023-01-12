#CE6ZP672
import random
def make_choice(x,y,field):
    w = len(field)
    h = len(field[0])
    for i in range(x + 1, w):
        if field[i][y] == 1:
            return "go_right"
        if field[i][y] == -1:
            break
    for i in range(y + 1, h):
        if field[x][i] == 1:
            return "go_down"
        if field[x][i] == -1:
            break
    for i in range(x - 1, -w):
        if field[i][y] == 1:
            return "go_left"
        if field[i][y] == -1:
            break
    for i in range(y - 1, -h):
        if field[x][i] == 1:
            return "go_up"
        if field[x][i] == -1:
            break
    for i in range(x + 1, w):
        if field[i][y] != -1:
            return "go_right"
        if field[i][y] == -1:
            break
    for i in range(y + 1, h):
        if field[x][i] != -1:
            return "go_down"
        if field[x][i] == -1:
            break
    for i in range(x - 1, -w):
        if field[i][y] != -1:
            return "go_left"
        if field[i][y] == -1:
            break
    for i in range(y - 1, -h):
        if field[x][i] != -1:
            return "go_up"
        if field[x][i] == -1:
            break