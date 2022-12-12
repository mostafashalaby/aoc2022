WIDTH, HEIGHT = 40, 6
crt_screen = [["." for i in range(WIDTH)] for j in range(HEIGHT)]


def main():
    filename = "input.txt"
    lines = read(filename)

    cycle = 0
    x = 1
    for line in lines:
        if line == "noop":
            draw(cycle, x)
            cycle += 1
        else:
            addx, v = line.split(" ")
            draw(cycle, x)
            cycle += 1
            draw(cycle, x)
            cycle += 1
            x += int(v)

    for row in crt_screen:
        row_string = ' '.join(row)
        print(row_string)
    exit(1)


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list


def draw(cycle, x):
    screen_cycle = cycle % 40
    screen_row = cycle // 40
    if screen_cycle in range(x-1, x+2):
        crt_screen[screen_row][screen_cycle] = "#"


if __name__ == "__main__":
    main()
