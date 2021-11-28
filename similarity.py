
def similarity(s1, s2, s = (lambda c1, c2: c1 == c2)):
    n = len(s1)
    m = len(s2)
    V = [[None] * (m + 1) for i in range(n + 1)]

    V[0][0] = 0
    
    for i in range(1, n + 1):
        V[i][0] = V[i - 1][0] + s(s1[i - 1], " ")
    for j in range(1, m + 1):
        V[0][j] = V[0][j - 1] + s(" ", s2[j - 1])
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            V[i][j] = max(V[i - 1][j - 1] + s(s1[i - 1], s2[j - 1]),
                          V[i - 1][j] + s(s1[i - 1], " "),
                          V[i][j - 1] + s(" ", s2[j - 1]))

    return V[n][m]

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(similarity(s1, s2))
