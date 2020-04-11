from piece import Piece

test_piece = Piece(2, False, [2, 7])
test_piece2 = Piece(1, False, [5, 2])
x = "x"
o = "o"
board1 = [
    [x, 2, x, 2, x, 2, x, 2],
    [2, x, 2, x, 2, x, 2, x],
    [x, 2, x, 2, x, 2, x, 2],
    [o, x, o, x, o, x, o, x],
    [x, o, x, o, x, o, x, o],
    [1, x, 1, x, 1, x, 1, x],
    [x, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x],

]
boardt = [
    [x, 2, x, 2, x, 2, x, 2],
    [2, x, 2, x, 2, x, o, x],
    [x, 2, x, 2, x, 2, x, 2],
    [o, x, o, x, o, x, o, x],
    [x, o, x, 2, x, o, x, o],
    [1, x, 1, x, 1, x, 1, x],
    [x, o, x, 1, x, 1, x, o],
    [1, x, 1, x, 1, x, 1, x],

]
spot1 = [2, 3]
result1 = [[3, 2], [4, 5], [6, 7]]

spot2 = [5, 2]
result2 = [[4, 1], [3, 4], [1, 6]]


def valid_moves2(my_board, my_piece):
    print("MY PIECE", my_piece.position)
    if my_piece.team != 2:
        return
    answer = []
    move_l = []
    move_r = []
    path_l = []
    path_r = []
    first = my_piece.position[0] + 1
    second_r = my_piece.position[1] + 1
    second_l = my_piece.position[1] - 1

    if first < 8 and second_r < 8 and second_l >= 0:
        if my_board[first][second_l] == o:
            move_l.append([first, second_l])
        if my_board[first][second_r] == o:
            move_r.append([first, second_r])

    jd = 0
    jl = 0

    jumpd = my_piece.position[0]
    jumpl = my_piece.position[1]
    while True:
        jd += 2
        jl += -2
        if jumpd < 6 and jumpl >= 2:
            jumpd = my_piece.position[0] + jd
            jumpl = my_piece.position[1] + jl
        else:
            break
        if my_board[first][second_l] == 1 and my_board[jumpd][jumpl] == o:
            path_l.append([jumpd, jumpl])
        else:
            break

    j = 0
    jumpd = my_piece.position[0]
    jumpr = my_piece.position[1]
    while True:
        j += 2
        if jumpd < 6 and jumpr < 6:
            jumpd = my_piece.position[0] + j
            jumpr = my_piece.position[1] + j
        else:
            break
        if my_board[first][second_r] == 1 and my_board[jumpd][jumpr] == o:
            path_r.append([jumpd, jumpr])
        else:
            break
    if len(move_l) > 0:
        answer.append(move_l)
    if len(move_r) > 0:
        answer.append(move_r)
    if len(path_l) > 0:
        answer.append(path_l)
    if len(path_r) > 0:
        answer.append(path_r)
    print("AHHAHAHAHAH", answer)
    return answer


def valid_moves1(my_board, my_piece):
    if my_piece.team != 1:
        return
    answer = []
    move_l = []
    move_r = []
    path_l = []
    path_r = []
    first = my_piece.position[0] - 1
    second_r = my_piece.position[1] + 1
    second_l = my_piece.position[1] - 1

    if first >= 0 and second_r < 8 and second_l >= 0:
        if my_board[first][second_l] == o:
            move_l.append([first, second_l])
        if my_board[first][second_r] == o:
            move_r.append([first, second_r])

    j = 0

    jumpu = my_piece.position[0]
    jumpl = my_piece.position[1]
    while True:
        j -= 2

        if jumpu >= 2 and jumpl >= 2:
            jumpu = my_piece.position[0] + j
            jumpl = my_piece.position[1] + j
        else:
            break
        if my_board[first][second_l] == 2 and my_board[jumpu][jumpl] == o:
            path_l.append([jumpu, jumpl])
        else:
            break

    ju = 0
    jr = 0
    jumpu = my_piece.position[0]
    jumpr = my_piece.position[1]
    while True:
        ju += -2
        jr += 2
        if jumpu >= 2 and jumpr < 6:
            jumpu = my_piece.position[0] + ju
            jumpr = my_piece.position[1] + jr
        else:
            break
        if my_board[first][second_r] == 2 and my_board[jumpu][jumpr] == o:
            path_r.append([jumpu, jumpr])
        else:
            break

    if len(move_l) > 0:
        answer.append(move_l)
    if len(move_r) > 0:
        answer.append(move_r)
    if len(path_l) > 0:
        answer.append(path_l)
    if len(path_r) > 0:
        answer.append(path_r)
    return answer


valid_moves2(boardt, test_piece)
valid_moves1(boardt, test_piece2)
