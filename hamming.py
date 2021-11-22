
def hamming_diff(s1, s2):
    c = 0
    if len(s1) != len(s2):
        return -1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            c += 1
    return c

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(hamming_diff(s1, s2))
