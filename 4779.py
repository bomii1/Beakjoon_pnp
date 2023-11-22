import sys

def contor(dashString):
    if len(dashString) == 1:
        return dashString
    section = int(len(dashString) // 3)
    return contor(dashString[:section]) + (" " * section) + contor(dashString[section * 2:])

while True:
    try:
        N = int(sys.stdin.readline())
        dashString = "-" * 3**N
        print(contor(dashString))
    except:
        break