head_list = [(0, 0)]
tail_list = [(0, 0)]


def main():
    filename = "input.txt"
    lines = read(filename)

    for line in lines:
        direction, magnitude = line.split(" ")
        populate(direction, int(magnitude))

    print(head_list)
    print(tail_list)
    print(len(set(tail_list)))


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list


def populate(direction, magnitude):
    for i in range(magnitude):
        head = head_list.pop()
        head_list.append(head)
        hx, hy = head[0], head[1]

        tail = tail_list.pop()
        tail_list.append(tail)
        tx, ty = tail[0], tail[1]

        if direction == "R":
            if hx == tx:
                hx += 1
            elif hx - tx == 1:
                if hy == ty:
                    hx += 1
                    tx += 1
                else:
                    hx += 1
                    tx = hx - 1
                    ty = hy
            elif hx - tx == -1:
                hx += 1
        elif direction == "L":
            if hx == tx:
                hx -= 1
            elif hx - tx == 1:
                hx -= 1
            elif hx - tx == -1:
                if hy == ty:
                    hx -= 1
                    tx -= 1
                else:
                    hx -= 1
                    tx = hx + 1
                    ty = hy
        elif direction == "U":
            if hy == ty:
                hy += 1
            elif hy - ty == 1:
                if hx == tx:
                    hy += 1
                    ty += 1
                else:
                    hy += 1
                    ty = hy - 1
                    tx = hx
            elif hy - ty == -1:
                hy += 1
        elif direction == "D":
            if hy == ty:
                hy -= 1
            elif hy - ty == 1:
                hy -= 1
            elif hy - ty == -1:
                if hx == tx:
                    hy -= 1
                    ty -= 1
                else:
                    hy -= 1
                    ty = hy + 1
                    tx = hx
        new_head = (hx, hy)
        new_tail = (tx, ty)
        head_list.append(new_head)
        tail_list.append(new_tail)


if __name__ == "__main__":
    main()
