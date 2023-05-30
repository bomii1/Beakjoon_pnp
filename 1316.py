import sys

def wordChecker(word):
    group = [word[0]]
    for i in range(1, len(word)):
        if word[i-1] != word[i]:
            if word[i] in group:
                return False
            else:
                group.append(word[i])
        else:
            pass
    return True

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for i in range(n)]

count = 0
for word in words:
    if wordChecker(word):
        count += 1
print(count)