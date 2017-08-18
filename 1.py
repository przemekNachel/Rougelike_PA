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


def print_map(map, hero_x, hero_y):
    word = map[hero_y]
    index = hero_x
    word = word[:index] + "@" + word[index + 1:]
    map[hero_y] = word
    print(chr(27) + "[2J")
    for line in map:
        print ("".join(line))

   
def moving(x_position,y_position):
    map = load_level('1lvl.txt')
    print_map(map, x_position, y_position)
    while True:
        map = load_level('1lvl.txt')
        print_map(map, x_position, y_position)
        x = getch()
        if x == "q":
            break
        if x == "a" and map[y_position][x_position-1] != "#":
            x_position -= 1
        if x == "d" and map[y_position][x_position+1] != "#":
            x_position += 1
        if x == "w" and map[y_position-1][x_position] != "#":
            y_position -= 1
        if x == "s" and map[y_position+1][x_position] != "#":
            y_position += 1


moving(2,2)