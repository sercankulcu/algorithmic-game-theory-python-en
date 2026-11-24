"""Chapter 3 · Code Trace: maximin()

In a 2 × n zero-sum game, finds the row player's maximin mixed strategy in exact
fractions by taking the intersection points of the lines as candidates. The
function is identical to the code on the slide; the sample matrix is from the
lecture notes.
"""

from fractions import Fraction as F
def maximin(A):                   # A: 2 x n
    n, cand = len(A[0]), [F(0), F(1)]
    for j in range(n):
        for k in range(j + 1, n):
            d = A[0][j] - A[1][j] - A[0][k] + A[1][k]
            if d != 0:
                cand.append(F(A[1][k] - A[1][j], d))
    g = lambda p: min(p*a+(1-p)*b for a, b in zip(*A))
    p = max((c for c in cand if 0 <= c <= 1), key=g)
    return p, g(p)


if __name__ == "__main__":
    # columns X, Y, Z
    A = [[4, 1, 3], [0, 3, 2]]
    p, v = maximin(A)
    print(p, v)


# Expected output:
# 1/2 2
