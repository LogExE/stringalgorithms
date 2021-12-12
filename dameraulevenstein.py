
def dameraulevenstein(s1, s2):
    n = len(s1)
    m = len(s2)
    D = [[None] * (m + 1) for i in range(n + 1)]

    lastIndex = {c: 0 for c in s1 + s2}
    
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        last = 0
        for j in range(1, m + 1):
            inds = lastIndex[s2[j - 1]]
            indf = last
            if s1[i - 1] == s2[j - 1]:
                last = j
            t = 1 if s1[i - 1] != s2[j - 1] else 0

            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + t)
            if indf != 0 and inds != 0:
                D[i][j] = min(D[i][j], D[inds - 1][indf - 1] + (i - inds - 1) + 1 + (j - indf - 1))
        lastIndex[s1[i - 1]] = i

    return D[n][m]

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(dameraulevenstein(s1, s2))
