def solution(board, h, w):
    cnt = 0
    tu = [(-1, 0), (1, 0), (0,-1), (0,1)]
    color = board[h][w]
    for tup in tu:
        if h+tup[0] < 0 or h+tup[0] > len(board)-1 or w+tup[1] < 0 or w+tup[1] > len(board)-1:
            continue
        if board[h+tup[0]][w+tup[1]] == color:
            cnt += 1
    return cnt