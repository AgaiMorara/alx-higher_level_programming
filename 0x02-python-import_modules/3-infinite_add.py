#!/usr/bin/python3

def infinitesum(argv):
    ans = 0
    n = len(argv) - 1
    for i in range(1, n + 1):
        ans = ans + int(argv[i])
    return (ans)


if __name__ == "__main__":
    import sys
    print(infinitesum(sys.argv))
