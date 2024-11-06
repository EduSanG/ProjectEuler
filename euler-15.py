grid_x = 20
grid_y = 20

def forward(pos_x, pos_y):
    x = 0
    y = 0
    print(pos_x, ' ', pos_y)
    if pos_x < grid_x:
        x = forward(pos_x+1, pos_y)
    if pos_y < grid_y:
        y = forward(pos_x, pos_y+1)
    return x+y

def main():
    return forward(0,0)