from math import inf
import numpy as np

mine = []
POURING_FROM = (500, 0)
RESOURCES = ["#", ".", "+", "o", "X"]
ROCK, AIR, SOURCE, SAND, VOID = 0, 1, 2, 3, 4
count = 0


def main():
    global mine
    filename = "input.txt"
    lines = read(filename)

    min_x, max_x, min_y, max_y = domain_and_range(lines)

    mine = [[RESOURCES[AIR] for i in range(min_x, max_x + 1)] for j in range(min_y, max_y + 1)]

    place_rocks(lines, min_x, max_x, min_y, max_y)
    # print_mine()
    floor()
    # print_mine()
    sand_sent = 0
    while True:
        point = send_sand(POURING_FROM)
        sand_sent += 1
        cx, cy = point
        if mine[cy][cx] == RESOURCES[SOURCE]:
            break
        mine[cy][cx] = RESOURCES[SAND]
        #print_mine()
        #print(sand_sent)
    print_mine()
    print(sand_sent)


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list


def domain_and_range(lines):
    min_x, max_x, min_y, max_y = inf, -inf, 0, -inf

    for line in lines:
        for coordinate in line.split(" -> "):
            x, y = coordinate.split(",")
            x, y = int(x), int(y)
            min_x = x if x < min_x else min_x
            max_x = x if x > max_x else max_x
            max_y = y if y > max_y else max_y

    return min_x, max_x, min_y, max_y


def place_rocks(lines, min_x, max_x, min_y, max_y):
    global POURING_FROM
    POURING_FROM = (POURING_FROM[0] - min_x, POURING_FROM[1])
    mine[POURING_FROM[1]][POURING_FROM[0]] = RESOURCES[SOURCE]

    for line in lines:
        coordinates = line.split(" -> ")
        ax, ay = coordinates[0].split(",")
        ax, ay = int(ax) - min_x, int(ay) - min_y
        ij0 = ay, ax
        for coordinate in coordinates[1:]:
            bx, by = coordinate.split(",")
            bx, by = int(bx) - min_x, int(by) - min_y
            ij1 = by, bx
            di = np.sign(ij1[0] - ij0[0])
            dj = np.sign(ij1[1] - ij0[1])
            i = ij0[0]
            j = ij0[1]
            while i != ij1[0] or j != ij1[1]:
                mine[i][j] = RESOURCES[ROCK]
                i += di
                j += dj
            mine[ij1[0]][ij1[1]] = RESOURCES[ROCK]
            ij0 = ij1


def print_mine():
    for row in mine:
        print("".join(row))
    print("\n")


def floor():
    global POURING_FROM
    original_length = len(mine[0]) * 5
    modifier = [RESOURCES[AIR] for _ in range(original_length)]
    for i, row in enumerate(mine):
        temp = modifier + row + modifier
        mine[i] = temp
    temp = [RESOURCES[AIR] for _ in range(original_length * 3)]
    mine.append(temp)
    temp = [RESOURCES[ROCK] for _ in range(original_length * 3)]
    mine.append(temp)
    POURING_FROM = (POURING_FROM[0] + original_length, POURING_FROM[1])


def send_sand(current_point):
    cx, cy = current_point
    char = mine[cy][cx]
    if mine[cy + 1][cx] in [RESOURCES[AIR]]:  # down
        return send_sand((cx, cy + 1))
    elif mine[cy + 1][cx - 1] in [RESOURCES[AIR]]:  # diagonal left
        return send_sand((cx - 1, cy + 1))
    elif mine[cy + 1][cx + 1] in [RESOURCES[AIR]]:  # diagonal right
        return send_sand((cx + 1, cy + 1))
    else:
        return cx, cy


if __name__ == "__main__":
    main()
