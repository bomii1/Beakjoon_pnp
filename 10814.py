import sys

num = int(input())
member = []
for i in range(num):
    age, name = map(str, sys.stdin.readline().split())
    member.append([int(age), name])
    member[i].append(i)
# 정렬
member.sort(key=lambda x:(x[0],x[2]))

for i in range(num):
    print(int(member[i][0]), member[i][1])
