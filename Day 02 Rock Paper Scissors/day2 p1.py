def main():
    filename = "input.txt"
    list_moves = read(filename)
    print(list_moves)

    total_score = 0
    for move in list_moves:
        total_score += give_score(move)

    print(total_score)
    return exit(1)



def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list

def give_score(move):
    """
    A = rock = X
    B = paper = Y
    C = scissors = Z
    """
    score = 0

    #points for tool chosen
    if move[2] == 'X':
        score += 1
    elif move[2] == 'Y':
        score += 2
    else:
        score += 3

    #points for outcome
    if move[0] == 'A':
        if move[2] == 'X':
            score += 3
        elif move[2] == 'Y':
            score += 6
        else:
            score += 0
    elif move[0] == 'B':
        if move[2] == 'X':
            score += 0
        elif move[2] == 'Y':
            score += 3
        else:
            score += 6
    else:
        if move[2] == 'X':
            score += 6
        elif move[2] == 'Y':
            score += 0
        else:
            score += 3

    #print(score)
    return score


if __name__ == "__main__":
    main()