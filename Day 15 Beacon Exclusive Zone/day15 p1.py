import re
from math import inf

mine = []
sensors = []
beacons = []
POURING_FROM = (500, 0)
RESOURCES = [".", "S", "B", "#"]
VOID, S, B, BEACONLESS = 0, 1, 2, 3

def main():
    global mine
    filename = "input.txt"
    lines = read(filename)

    min_x, max_x, min_y, max_y = domain_and_range(lines)
    #print(min_x, max_x, min_y, max_y)
    #print(sensors)
    #print(beacons)

    #mine = [[RESOURCES[VOID] for i in range(min_x, max_x + 1)] for j in range(min_y, max_y + 1)]
    #print_mine(min_x, max_x, min_y, max_y)
    place_s_b(min_x, min_y)
    #print_mine(min_x, max_x, min_y, max_y)

    y = 2000000
    cnt = confirm_beaconless(y - min_y)
    print(cnt)



def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list

def print_mine(min_x, max_x, min_y, max_y):
    x_list = range(min_x, max_x + 1)
    y_list = range(min_y, max_y + 1)
    for i in range(len(mine)):
        print("{:02d} {}".format((y_list[i]), "".join(mine[i])))

    print("\n")


def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)


def domain_and_range(lines):
    min_x, max_x, min_y, max_y = inf, -inf, inf, -inf

    for line in lines:
        x_and_y = [int(item) for item in re.findall(r'(-?\d+)', line)]
        for x, y in (grouped(x_and_y, 2)):
            sensors.append((x, y)) if len(sensors) == len(beacons) else beacons.append((x, y))
            min_x = x if x < min_x else min_x
            max_x = x if x > max_x else max_x
            min_y = y if y < min_y else min_y
            max_y = y if y > max_y else max_y


    return min_x, max_x, min_y, max_y

def place_s_b(min_x, min_y):
    global sensors, beacons
    transform_coordinates = lambda x, y: (x - min_x , y - min_y)
    for i in range(len(sensors)):
        sx, sy = transform_coordinates(sensors[i][0], sensors[i][1])
        bx, by = transform_coordinates(beacons[i][0], beacons[i][1])
        #mine[sy][sx] = RESOURCES[S]
        #mine[by][bx] = RESOURCES[B]
        sensors[i] = (sx, sy)  # update new coordinates
        beacons[i] = (bx, by)
        #print_mine(min_x, max_x, min_y, max_y)


def confirm_beaconless(y):
    intervals = []
    for i, sensor in enumerate(sensors):
        manhattan_distance = abs(beacons[i][1] - sensor[1]) + abs(beacons[i][0] - sensor[0])
        dx = manhattan_distance - abs(sensor[1] - y)
        intervals.append((sensor[0] - dx, sensor[0] + dx))

    beacon_there = []
    for bx, by in beacons:
        if by == y:
            beacon_there.append(bx)

    min_x = min([i[0] for i in intervals])
    max_x = max([i[1] for i in intervals])

    cnt = 0
    for x in range(min_x, max_x + 1):
        if x in beacon_there:
            continue

        for left, right in intervals:
            if left <= x <= right:
                cnt += 1
                break

    return cnt


if __name__ == "__main__":
    main()