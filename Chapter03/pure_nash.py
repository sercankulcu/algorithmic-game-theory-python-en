"""Chapter 3 · Code Trace: pure_nash()

Finds all pure Nash equilibria of a two-player matrix game by checking, in each
cell, whether both players are at a best response. The function is identical to
the code on the slide; the sample 3 × 3 game is from the lecture notes.
"""

def pure_nash(U1, U2):
    m, n, eq = len(U1), len(U1[0]), []
    for i in range(m):
        for j in range(n):
            br1 = max(U1[k][j] for k in range(m))
            br2 = max(U2[i][l] for l in range(n))
            if U1[i][j] == br1 and U2[i][j] == br2:
                eq.append((i, j))
    return eq


if __name__ == "__main__":
    # rows A, B, C; columns X, Y, Z
    U1 = [[4, 0, 1], [2, 3, 0], [1, 2, 3]]
    U2 = [[3, 2, 1], [1, 3, 2], [4, 0, 2]]
    print(pure_nash(U1, U2))


# Expected output:
# [(0, 0), (1, 1)]
