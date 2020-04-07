from piece import Piece

test_piece = Piece(2, False, [2,5]) 
test_piece2 = Piece(1, False, [5,2])
x ="x"
o = "o"
board1 = [
    [x,2,x,2,x,2,x,2],
    [2,x,2,x,2,x,2,x],
    [x,2,x,2,x,2,x,2],
    [o,x,o,x,o,x,o,x],
    [x,o,x,o,x,o,x,o],
    [1,x,1,x,1,x,1,x],
    [x,1,x,1,x,1,x,1],
    [1,x,1,x,1,x,1,x],

]
boardt = [
    [x,2,x,2,x,2,x,2],
    [2,x,2,x,2,x,2,x],
    [x,2,x,2,x,1,x,2],
    [o,x,o,x,1,x,1,x],
    [x,o,x,o,x,o,x,o],
    [1,x,1,x,1,x,1,x],
    [x,o,x,1,x,1,x,1],
    [1,x,1,x,1,x,1,x],

]
spot1 = [2,5]
result1 = [[4,7], [4,3], [6,1]]

spot2 = [5,2]
result2 = [[4,1], [4,3]]


def valid_moves2(my_board, my_piece):
    answer = []
    first = my_piece.position[0] + 1
    second_r = my_piece.position[1] + 1
    second_l = my_piece.position[1] - 1

    if first < 8 and second_r < 8 and second_l >= 0:
        if my_board[first][second_l] == o:
            answer.append([first, second_l])
        if my_board[first][second_r] == o:
            answer.append([first, second_r])
   
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
            answer.append([jumpd, jumpl])
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
            answer.append([jumpd, jumpr])
        else:
            break
    print(answer)

def valid_moves1(my_board, my_piece):
    answer = []
    first = my_piece.position[0] - 1
    second_r = my_piece.position[1] + 1
    second_l = my_piece.position[1] - 1

    if first >= 0 and second_r < 8 and second_l >= 0:
        if my_board[first][second_l] == o:
            answer.append([first, second_l])
        if my_board[first][second_r] == o:
            answer.append([first, second_r])

    
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
        if my_board[first][second_l] == 1 and my_board[jumpu][jumpl] == o:
            answer.append([jumpu, jumpl])
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
        if my_board[first][second_r] == 1 and my_board[jumpu][jumpr] == o:
            answer.append([jumpu, jumpr])
        else:
            break
    print(answer)


valid_moves2(boardt, test_piece)
valid_moves1(boardt, test_piece2)


