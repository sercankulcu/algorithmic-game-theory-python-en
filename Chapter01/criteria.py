"""Chapter 1 · Code Trace: Uncertainty Criteria

For a decision table with unknown probabilities, returns the indices of the
actions chosen by the maximin, maximax, Laplace and Savage (minimax regret)
criteria. The function is identical to the code on the slide; the investment
table below is from the lecture notes.
"""

def criteria(U):
    A, m = range(len(U)), len(U[0])
    mm = max(A, key=lambda i: min(U[i]))      # maximin
    mx = max(A, key=lambda i: max(U[i]))      # maximax
    lp = max(A, key=lambda i: sum(U[i]) / m)  # Laplace
    best = [max(r[j] for r in U) for j in range(m)]
    reg = [max(best[j] - r[j] for j in range(m))
           for r in U]            # max regret
    sv = reg.index(min(reg))                  # Savage
    return mm, mx, lp, sv


if __name__ == "__main__":
    # rows: 0 Large investment, 1 Small investment, 2 No investment
    # columns: Good, Fair, Bad
    U = [[200, 50, -120],
         [90, 40, -20],
         [0, 0, 0]]
    print(criteria(U))


# Expected output:
# (2, 0, 0, 1)
