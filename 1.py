def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def load_level(file):
    map = []
    with open(file) as inputfile:
        for line in inputfile:
            map.append(line.strip())
    return map

map = load_level('1lvl.txt')

def print_map(map, x, y):

    word = map[y]
    index = x
    word = word[:index] + "@" + word[index + 1:]
    map[y] = word

    print(chr(27) + "[2J")
    for line in map:
        print ("".join(line))

print_map(map,0,0)
x_position = 0
y_position = 0
while True:
    print_map(map,x_position,y_position)
    x = getch()
    if x == "q":
        break
    if x == "a":
        x_position -= 1
    if x == "d":
        x_position += 1
    if x == "w":
        y_position -= 1
    if x == "s":
        y_position += 1
