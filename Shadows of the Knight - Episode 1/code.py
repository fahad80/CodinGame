import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

x_min, x_max = 0, w-1
y_min, y_max = 0, h-1
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    for _dir in bomb_dir:
        if(_dir == 'U'):
            y_max = y0 - 1
        if(_dir == 'D'):
            y_min = y0 + 1
        if(_dir == 'R'):
            x_min = x0 + 1
        if(_dir == 'L'):
            x_max = x0 - 1

    x0 = int((x_max + x_min)/2)
    y0 = int((y_max + y_min)/2)   
    
    # To debug: print("Debug messages...", file=sys.stderr)


    # the location of the next window Batman should jump to.
    print(x0,y0)
