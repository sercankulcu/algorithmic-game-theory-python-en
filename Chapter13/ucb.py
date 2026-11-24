"""Chapter 13 · Code Trace: UCB

UCB1 in the multi-armed bandit: each round the arm with the largest score
Q + √(2 ln t / N) is pulled; the score of an arm that has never been pulled is
infinite. Identical to the slide code; the `import math` line, which is not
visible on the slide, is added. The example is the call
ucb([0.3, 0.5, 0.7], 8, random.Random(3)) from the lecture notes.
"""
import math     # not on the slide; added so the code runs
import random


def ucb(mu, T, rng):
    K = len(mu)
    N, Q = [0] * K, [0.0] * K
    for t in range(1, T + 1):
        b = [math.inf if n == 0 else
             math.sqrt(2*math.log(t)/n) for n in N]
        a = max(range(K), key=lambda i: Q[i] + b[i])
        r = 1 if rng.random() < mu[a] else 0
        N[a] += 1
        Q[a] += (r - Q[a]) / N[a]
    return N, Q


if __name__ == "__main__":
    N, Q = ucb([0.3, 0.5, 0.7], 8, random.Random(3))
    print(N, [round(q, 2) for q in Q])

# Expected output:
# [2, 2, 4] [0.5, 0.0, 1.0]
