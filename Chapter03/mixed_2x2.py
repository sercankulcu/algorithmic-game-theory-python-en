"""Chapter 3 · Code Trace: mixed_2x2()

Computes the interior mixed Nash equilibrium of a 2 × 2 game with the
indifference principle in exact fractions: the row probability p, the column
probability q and the row player's payoff. The function is identical to the code
on the slide; the examples are from the lecture notes.
"""

from fractions import Fraction as F
def mixed_2x2(A, B):
    da = A[0][0] - A[0][1] - A[1][0] + A[1][1]
    if da == 0: return None     # degenerate
    q = F(A[1][1] - A[0][1], da)  # row indifferent
    db = B[0][0] - B[0][1] - B[1][0] + B[1][1]
    if db == 0: return None
    p = F(B[1][1] - B[1][0], db)  # column indifferent
    if not (0 < p < 1 and 0 < q < 1):
        return None               # no interior eq.
    u1 = A[0][0] * q + A[0][1] * (1 - q)
    return p, q, u1


if __name__ == "__main__":
    # Battle of the Sexes: 0 = Opera, 1 = Football
    p, q, u1 = mixed_2x2([[3, 0], [0, 2]], [[2, 0], [0, 3]])
    print(p, q, u1)
    # Free Money: no interior equilibrium
    print(mixed_2x2([[1, 0], [0, 0]], [[1, 0], [0, 0]]))
    # Prisoner's Dilemma: da = 0
    print(mixed_2x2([[-1, -3], [0, -2]], [[-1, 0], [-3, -2]]))


# Expected output:
# 3/5 2/5 6/5
# None
# None
