def main():
    filename = "input.txt"
    lines = read(filename)
    hill_matrix, possible_starts, end = populate(lines)
    answers = bfs(hill_matrix, end)

    possible_starts_steps = []
    for coordinate in answers:
        if coordinate in possible_starts:
            possible_starts_steps.append(answers[coordinate])
    print(min(possible_starts_steps))


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list


def populate(lines):
    hill_matrix = [["-" for i in range(len(lines[0]))] for j in range(len(lines))]
    possible_starts = []
    end = (0, 0)

    for i in range(len(lines)):
        hill_matrix[i] = []
        for j, char in enumerate(lines[i]):
            if char == "S" or char == "a":
                possible_starts.append((i, j))
            if char == "E":
                end = (i, j)
            hill_matrix[i].extend(char)

    return hill_matrix, possible_starts, end


def bfs(hill_matrix, end):
    """Returns a dictionary of coordinate keys, with the value of each being the number of steps from end to it"""
    frontier = [end]
    level = dict()
    level[end] = 0

    while frontier:
        current = frontier.pop(0)
        for neighbor in neighbors(hill_matrix, current):
            if neighbor not in level:
                level[neighbor] = level[current] + 1
                frontier.append(neighbor)
    return level


def neighbors(hill_matrix, current):
    incline = list("SabcdefghijklmnopqrstuvwxyzE")
    incline.reverse() #because we are hiking down from the end to the start, think of this as decline
    neighbors = []
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for direction in directions:
        step = (current[0] + direction[0], current[1] + direction[1])

        # Make sure within range
        if step[0] > (len(hill_matrix) - 1) or step[0] < 0 or step[1] > (
                len(hill_matrix[len(hill_matrix) - 1]) - 1) or step[1] < 0:
            continue

        # Make sure hikable terrain
        if not hikable(incline, hill_matrix, current, step):
            continue
        neighbors.append(step)
    return neighbors


def hikable(incline, hill_matrix, current, step):
    cur_value = hill_matrix[current[0]][current[1]]
    step_value = hill_matrix[step[0]][step[1]]

    cur_incline = incline.index(cur_value)
    step_incline = incline.index(step_value)

    return step_incline - cur_incline <= 1


if __name__ == "__main__":
    main()