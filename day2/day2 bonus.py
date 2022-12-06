import re

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
    A = rock = X: need to lose
    B = paper = Y: need to draw
    C = scissors = Z: need to win
    """
    score = 0
    tool = 0

    #points for outcome
    if move[0] == 'A':
        if move[2] == 'X':
            tool += 3
            score += 0
        elif move[2] == 'Y':
            tool += 1
            score += 3
        else:
            tool += 2
            score += 6
    elif move[0] == 'B':
        if move[2] == 'X':
            tool += 1
            score += 0
        elif move[2] == 'Y':
            tool += 2
            score += 3
        else:
            tool += 3
            score += 6
    else:
        if move[2] == 'X':
            tool += 2
            score += 0
        elif move[2] == 'Y':
            tool += 3
            score += 3
        else:
            tool += 1
            score += 6

    #print(score)
    return score + tool


if __name__ == "__main__":
    main()