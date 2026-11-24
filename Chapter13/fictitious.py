"""Chapter 13 · Code Trace: fictitious()

Fictitious play in Matching Pennies: each player best-responds to the
frequencies of the opponent's past actions; returns the H/T counters
(0 = H, 1 = T). Identical to the slide code; the example is fictitious(6).
"""

def fictitious(T):
    nm, nx = [0, 0], [0, 0]   # H/T counters
    a, b = 0, 0               # round 1: both H
    for t in range(1, T + 1):
        nm[a] += 1            # matcher's history
        nx[b] += 1            # mismatcher's history
        # matcher: match the mismatcher's majority
        a = 0 if nx[0] >= nx[1] else 1
        # mismatcher: avoid the matcher's majority
        b = 1 if nm[0] > nm[1] else 0
    return nm, nx


if __name__ == "__main__":
    nm, nx = fictitious(6)
    print(nm, nx)
    print(round(nm[0] / 6, 2), round(nx[0] / 6, 2))

# Expected output:
# [3, 3] [1, 5]
# 0.5 0.17
