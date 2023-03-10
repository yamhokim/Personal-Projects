                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          """Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 30, 2021
"""

def is_empty(board):
    for i in board:
        for j in i:
            if j != " ":
                return False
    return True

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

import copy

def search_max(board): # Update me
    board_copy = copy.deepcopy(board)
    list_of_points = []
    for row in range(8):
        for space in range(8):
            if board_copy[row][space] == " ":
                board_copy[row][space] = "b"
                coords = (row, space)
                points = score(board_copy)
                pair = [coords, points]
                list_of_points.append(pair)
                board_copy = copy.deepcopy(board)

    while len(list_of_points) > 1:
        if list_of_points[0][1] < list_of_points[1][1]:
            del list_of_points[0]
        elif list_of_points[0][1] > list_of_points[1][1]:
            del list_of_points[1]
        elif list_of_points[0][1] == list_of_points[1][1]:
            del list_of_points[1]
    print(list_of_points) # Remove me later
    move_y = list_of_points[0][0][0]
    move_x = list_of_points[0][0][1]

    return (move_y, move_x)

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    #check if full:
    row = 0
    while True:
        for column in range (8):
            if board[column][row] == " ":
                break
            while board[column][row]!=" ":
                row += 1
                pass

            print("DRAW")
            return
        break

    for j in range (4):
        for i in range (4):
            for d_y, d_x in [(0, 1), (1, 0), (1, 1)]:

                if board[j][i]==board[j+d_y][i+d_x]==board[j+d_y*2][i+d_x*2]==board[j+d_y*3][i+d_x*3]==board[j+d_y*4][i+d_x*4] and board[j][i] != " ":
                    print(board[j][i], "WINS")
                    return

            for d_y, d_x in [(0, 1)]:
                if board[j*2][i]==board[j*2+d_y][i+d_x]==board[j*2+d_y*2][i+d_x*2]==board[j*2+d_y*3][i+d_x*3]==board[j*2+d_y*4][i+d_x*4] and board[j*2][i] != " ":
                    print(board[j][i], "WINS")
                    return

            for d_y, d_x in [(1,0), (1, -1)]:
                if board[j][i*2]==board[j+d_y][i*2+d_x]==board[j+d_y*2][i*2+d_x*2]==board[j+d_y*3][i*2+d_x*3]==board[j+d_y*4][i*2+d_x*4] and board[j][i*2] != " ":
                    print(board[j][i*2], "WINS")
                    return

    print ("CONTINUE PLAYING")
    return


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


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

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


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == "__main__":
    test_is_bounded()

