def is_bounded(board, y_end, x_end, length, d_y, d_x):
    if d_y == 1 and d_x == 0:
        if board[y_end+1][x_end] == " " and board[y_end-length][x_end] == " ":
            return "OPEN"
        elif (board[y_end+1][x_end] == "b" and board[y_end-length][x_end] == "b") or (board[y_end+1][x_end] == "w" and board[y_end-length][x_end] == "w"):
            return "CLOSED"
        else:
            return "SEMI-OPEN"

    elif d_y == 1 and d_x == 1:
        sub_list = []
        sub_list.append(board[y_end+1][x_end+1])
        len = 0
        cur_y = y_end
        cur_x = x_end
        while board[cur_y][cur_x] != None and len <= length:
            sub_list.append(board[cur_y][cur_x])
            len += 1
            cur_y -= 1
            cur_x -= 1
        if sub_list[-1] == " " and sub_list[0] == " ":
            return "OPEN"
        elif (sub_list[-1] == "b" and sub_list[0] == "b") or (sub_list[-1] == "w" and sub_list[0] == "w"):
            return "CLOSED"
        else:
            return "SEMIOPEN"

    elif d_y == 1 and d_x == -1:
        sub_list = []
        sub_list.append(board[y_end-1][x_end-1])
        len = 0
        cur_y = y_end
        cur_x = x_end
        while board[cur_y][cur_x] != None and len <= length:
            sub_list.append(board[cur_y][cur_x])
            len += 1
            cur_y += 1
            cur_x += 1

        if sub_list[-1] == " " and sub_list[0] == " ":
            return "OPEN"
        elif (sub_list[-1] == "b" and sub_list[0] == "b") or (sub_list[-1] == "w" and sub_list[0] == "b"):
            return "CLOSED"
        else:
            return "SEMIOPEN"

    elif d_y == 0 and d_x == 1:
        row = board[y_end]
        if row[x_end+1] == " " and row[x_end-length-1] == " ":
            return "OPEN"
        elif (row[x_end+1] == "b" and row[x_end-length-1] == "b") or (row[x_end+1] == "w" and row[x_end-length-1] == "w"):
            return "CLOSED"
        else:
            return "SEMIOPEN"


def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))



def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x

if __name__ == "__main__":
    test_is_bounded()

