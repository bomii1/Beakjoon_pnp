def sol(rowIndex, columnIndex, chessBoard):
    filter = ["BWBWBWBW", "WBWBWBWB"]
    count1, count2 = 0,0

    start = chessBoard[rowIndex][columnIndex]
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

row, column = map(int, input().split())
chessBoard = []
for w in range(row):
    chessBoard.append(list(input()))

minimum = []

for a in range(row-7):
    for b in range(column-7):
        minimum.append(sol(a, b, chessBoard))
print(min(minimum))
