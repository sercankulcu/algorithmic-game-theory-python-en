"""Chapter 12 · Code Trace: punish()

Computes the payoffs in the public goods game with punishment, given the
contributions and the punishment points (whoever gives a point pays 1, the
punished player loses 3). Identical to the slide code; the examples are the
three punishment regimes in the lecture notes (Table 12.13): nobody punishes,
P2–P4 give P1 2 points each, only P2 and P3 give.
"""

def punish(c, p):        # p[i][j]: i's points to j
    n = len(c)
    share = 1.6 * sum(c) / n
    u = [10 - c[i] + share for i in range(n)]
    for i in range(n):
        for j in range(n):
            u[i] -= p[i][j]       # costs 1 per point
            u[j] -= 3 * p[i][j]   # target loses 3
    return u


if __name__ == "__main__":
    c = [0, 10, 10, 10]
    for givers in [[], [1, 2, 3], [1, 2]]:
        p = [[0] * 4 for _ in range(4)]
        for i in givers:
            p[i][0] = 2
        print(givers, punish(c, p))

# Expected output:
# [] [22.0, 12.0, 12.0, 12.0]
# [1, 2, 3] [4.0, 10.0, 10.0, 10.0]
# [1, 2] [10.0, 10.0, 10.0, 12.0]
