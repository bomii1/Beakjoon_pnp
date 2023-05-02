def sol(n, m, namu):
    low, high = 0, max(namu)
    subH = lambda x:x-H if x >= H else 0

    while True:
        H = int((low + high) / 2)
        SUM = sum(subH(x) for x in namu)

        if high - low == 1: # 적어도 m개 -> m보다 크거나 같다
            break
        elif SUM > m:
            low = H
        elif SUM < m:
            high = H
        else: # 같을 때
            break
    return H

n, m = map(int, input().split())
namu = list(map(int, input().split()))
answer = sol(n,m,namu)
print(answer)

