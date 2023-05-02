def sol(A, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return 0
    if target == A[mid]:
        return 1
    elif target < A[mid]:
        return sol(A, target, start, mid-1)
    elif target > A[mid]:
        return sol(A, target, mid+1, end)

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
Ms = list(map(int, input().split()))

for i in range(M):
    print(sol(A, Ms[i], 0, N-1))
