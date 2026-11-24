"""Chapter 13 · Code Trace: hedge()

The Hedge (multiplicative weights) algorithm: the weight of each action is
multiplied by e^(η·gain), actions are chosen with probability proportional to
their weights; returns the total expected gain. Identical to the slide code;
the example is the five-round sequence with three experts from the lecture
notes (η = 0.5).
"""

import math
def hedge(G, eta):
    w = [1.0] * len(G[0])
    total = 0.0
    for g in G:                       # each round
        W = sum(w)
        p = [x / W for x in w]
        total += sum(pi * gi for pi, gi in zip(p, g))
        w = [x*math.exp(eta*gi) for x, gi in zip(w, g)]
    return total


if __name__ == "__main__":
    G = [[1, 0, 0.5]] * 2 + [[0, 1, 0.5]] * 3
    total = hedge(G, 0.5)
    print(round(total, 2))
    print("regret:", round(3 - total, 2))

# Expected output:
# 2.34
# regret: 0.66
