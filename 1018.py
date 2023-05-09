def sol(rowIndex, columnIndex, chessBoard):
    filter = ["BWBWBWBW", "WBWBWBWB"]
    count1, count2 = 0,0

    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if filter[0][j] != chessBoard[rowIndex+i][columnIndex+j]:
                    count1 += 1
            else:
                if filter[1][j] != chessBoard[rowIndex+i][columnIndex+j]:
                    count1 += 1

        for j in range(8):
            if i % 2 == 0:
                if filter[1][j] != chessBoard[rowIndex+i][columnIndex+j]:
                    count2 += 1
            else:
                if filter[0][j] != chessBoard[rowIndex+i][columnIndex+j]:
                    count2 += 1
    return min(count1, count2)

# 입력
row, column = map(int, input().split())
chessBoard = []
for i in range(row):
    chessBoard.append(list(input()))

# count 값을 담을 리스트
minimum = []
# 출력
for i in range(row-7):
    for j in range(column-7):
        minimum.append(sol(i, j, chessBoard))
print(min(minimum))
