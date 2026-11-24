"""Chapter 2 · Code Trace: Level-k Guess

In the Guess 2/3 of the Average game, computes the guesses of level-k players,
finds the target for a population that mixes levels 0-1-2, and prints each
level's distance from the target. Identical to the code on the slide.
"""

def guess(k, L0=45):     # level-k
    g = L0
    for _ in range(k):
        g = g * 2 / 3
    return g
share = {0: 0.3, 1: 0.4, 2: 0.3}   # belief
avg = sum(p * guess(k) for k, p in share.items())
target = avg * 2 / 3
for k in range(5):
    print(k, round(guess(k), 1),
          round(abs(guess(k) - target), 1))


# Expected output:
# 0 45 24.0
# 1 30.0 9.0
# 2 20.0 1.0
# 3 13.3 7.7
# 4 8.9 12.1
