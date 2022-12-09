rope = [[(0, 0)] for _ in range(10)]


def main():
    filename = "input.txt"
    lines = read(filename)

    for line in lines:
        direction, magnitude = line.split(" ")
        for _ in range(int(magnitude)):
            populate(direction)
    print(len(set(rope[-1])))


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list


def populate(direction):
    head = rope[0].pop()
    rope[0].append(head)
    move_head(head, direction)

    for i in range(1, len(rope)):
        t1 = rope[i-1].pop()
        rope[i-1].append(t1)
        t2 = rope[i].pop()
        rope[i].append(t2)
        move_tails(t1, t2, i)


def move_head(head, direction):
    hx, hy = head[0], head[1]
    hx += 1 if direction == 'R' else -1 if direction == 'L' else 0
    hy += 1 if direction == 'D' else -1 if direction == 'U' else 0
    head = (hx, hy)
    rope[0].append(head)


def move_tails(t1, t2, knot_num):
    t1x, t1y = t1[0], t1[1]
    t2x, t2y = t2[0], t2[1]
    xdelta = t1x - t2x
    ydelta = t1y - t2y
    if abs(xdelta) > 1 or abs(ydelta) > 1:
        t2x += sign(xdelta)
        t2y += sign(ydelta)
    t2 = (t2x, t2y)
    rope[knot_num].append(t2)


def sign(x):
    return (x > 0) - (x < 0) # True = 1, False = 0


if __name__ == "__main__":
    main()
