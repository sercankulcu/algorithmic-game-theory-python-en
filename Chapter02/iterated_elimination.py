"""Chapter 2 · Iterated Elimination Step by Step

Follows the iterated elimination of dominated strategies in the Guess 2/3 of the
Average game: each round the largest meaningful guess is multiplied by 2/3.
Identical to the code on the slide.
"""

hi = 90                # largest possible guess
for t in range(1, 7):
    # avg ≤ hi  ⇒  target ≤ (2/3)·hi
    hi = hi * 2 / 3
    print(t, round(hi, 1))
# hi = 90·(2/3)^k → 0 : unique equilibrium, all 0


# Expected output:
# 1 60.0
# 2 40.0
# 3 26.7
# 4 17.8
# 5 11.9
# 6 7.9
