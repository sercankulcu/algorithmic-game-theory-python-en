"""Chapter 3 · Code Trace: eliminate()

Iteratively eliminates strictly dominated rows and columns of a 3 × 3 game and
returns the remaining row and column indices. The function is identical to the
code on the slide; the sample game is the 3 × 3 elimination example from the
slides and the notes.
"""

def eliminate(U1, U2):
    R, S = [0, 1, 2], [0, 1, 2]   # remaining
    while True:
        x = [r for r in R for k in R if
             all(U1[k][c] > U1[r][c] for c in S)]
        y = [c for c in S for d in S if
             all(U2[r][d] > U2[r][c] for r in R)]
        if x: R.remove(x[0])      # drop a row
        elif y: S.remove(y[0])    # drop a column
        else: return R, S


if __name__ == "__main__":
    # rows A, B, C; columns X, Y, Z
    U1 = [[3, 3, 1], [3, 0, 5], [2, 2, 6]]
    U2 = [[2, 3, 4], [2, 4, 3], [1, 0, 6]]
    print(eliminate(U1, U2))


# Expected output:
# ([2], [2])
