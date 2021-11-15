
def levenstein_diff(s1, s2):
    n = len(s1)
    m = len(s2)
    D = [[None] * (m + 1) for i in range(n + 1)]

    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            t = 1 if s1[i - 1] != s2[j - 1] else 0
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + t)
    for x in D:
        print(x)
    return D[n][m]

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(levenstein_diff(s1, s2))
