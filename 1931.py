import sys
n = int(input())
start, end = [], []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    start.append(a)
    end.append(b)

def maxConf(start, end):
    conf = list(zip(start, end))
    conf.sort(key=lambda x:(x[1],x[0]))
    cur = conf[0]
    cnt = 1

    for i in range(1, n):
        if conf[i][0] >= cur[1]:
            cnt += 1
            cur = conf[i]
    return cnt

print(maxConf(start, end))
