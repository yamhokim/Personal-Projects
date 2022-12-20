def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    list_of_dir = [(1, -1), (1, 1)]
    for i in range(0, 8):
        for j in range(0, 8):
            for element in list_of_dir:
                open_seq_count += detect_row(board, col, i, j, length, element[0], element[1])[0]
                semi_open_seq_count += detect_row(board, col, i, j, length, element[0], element[1])[1]

    for i in range(8):
        open_seq_count += detect_row(board, col, 0, i, length, 1, 0)[0]
        semi_open_seq_count += detect_row(board, col, 0, i, length, 1, 0)[1]

    for i in range(8):
        open_seq_count += detect_row(board, col, i, 0, length, 0, 1)[0]
        semi_open_seq_count += detect_row(board, col, i, 0, length, 0, 1)[1]

    return open_seq_count, semi_open_seq_count

def detect_row(board, col, y_start, x_start, length, d_y, d_x): # Test for Bugs etc.
    open_seq_count = 0
    semi_open_seq_count = 0
    if d_y == 1 and d_x == 0:
        empty_list = []
        if y_start == 0:
            empty_list.append(None)
        else:
            empty_list.append(board[y_start-1][x_start])

        while y_start <= 7:
            empty_list.append(board[y_start][x_start])
            y_start += 1
        if y_start == 7:
            empty_list.append(None)

    elif d_y == 0 and d_x == 1:
        empty_list = []
        if x_start == 0:
            empty_list.append(None)
        else:
            empty_list.append(board[y_start][x_start-1])

        while x_start <= 7:
            empty_list.append(board[y_start][x_start])
            x_start += 1
        if x_start == 7:
            empty_list.append(None)

    elif d_y == 1 and d_x == 1:
        empty_list = []
        if x_start == 0 or y_start == 0:
            empty_list.append(None)
        else:
            empty_list.append(board[y_start-1][x_start-1])

        while x_start <= 7 and y_start <= 7:
            empty_list.append(board[y_start][x_start])
            x_start += 1
            y_start += 1
        empty_list.append(None)

    elif d_y == 1 and d_x == -1:
        empty_list = []
        if x_start == 7 or y_start == 0:
            empty_list.append(None)
        else:
            empty_list.append(board[y_start-1][x_start+1])

        while x_start >= 0 and y_start <= 7:
            empty_list.append(board[y_start][x_start])
            x_start -= 1
            y_start += 1
        if x_start == 0 or y_start == 7:
            empty_list.append(None)

    length_counter = 0
    for n in range(len(empty_list)):
        if empty_list[n] == col:
            length_counter += 1
        else:
            length_counter = 0

        if length_counter == length:
            after = empty_list[n+1]
            before = empty_list[n-length]
            if after == " " and before == " ":
                open_seq_count += 1
            elif (after == " " and before != " ") or (after != " " and before == " "):
                semi_open_seq_count += 1
    return open_seq_count, semi_open_seq_count

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

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

if __name__ == "__main__":
    test_detect_rows()