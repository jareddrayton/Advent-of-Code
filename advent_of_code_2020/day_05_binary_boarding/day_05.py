from operator import itemgetter

with open("input.txt", 'r') as f:
    boarding_passses = f.readlines()

boarding_passses = [board_pass.strip() for board_pass in boarding_passses]
boarding_passses = [[board_pass[0:7], board_pass[7:]] for board_pass in boarding_passses]

def row_con(row_num):
    row_num = row_num.replace('F', '0')
    row_num = row_num.replace('B', '1')
    row_num = int(row_num, 2)
    return row_num

def col_con(col_num):
    col_num = col_num.replace('L', '0')
    col_num = col_num.replace('R', '1')
    col_num = int(col_num, 2)
    return col_num

def convert(board_list):
    con_board_list = []
    for row, col in board_list:
        con_board_list.append( (row_con(row), col_con(col), row_con(row) * 8  + col_con(col) ))
    return con_board_list

print("Part 1", max(convert(boarding_passses), key=itemgetter(2)))

a = sorted(convert(boarding_passses), key=itemgetter(2))

for i in range(len(a)):
    if a[i+1][2] - a[i][2] == 2:
        print("Part 2", a[i][2]+1)
        break
