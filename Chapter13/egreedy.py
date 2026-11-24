"""Chapter 13 · Code Trace: ε-greedy

The ε-greedy algorithm in the multi-armed bandit: with probability ε a random
arm (explore), otherwise the arm with the largest estimate (exploit). Identical
to the slide code; the example is the call
egreedy([0.3, 0.5, 0.7], 8, 0.2, random.Random(11)) from the lecture notes.
"""
import random


def egreedy(mu, T, eps, rng):
    N, Q = [0] * len(mu), [0.0] * len(mu)
    for t in range(1, T + 1):
        if rng.random() < eps:           # explore
            a = rng.randrange(len(mu))
        else:                            # exploit
            a = Q.index(max(Q))
        r = 1 if rng.random() < mu[a] else 0
        N[a] += 1
        Q[a] += (r - Q[a]) / N[a]
    return N, Q


if __name__ == "__main__":
    N, Q = egreedy([0.3, 0.5, 0.7], 8, 0.2, random.Random(11))
    print(N, [round(q, 2) for q in Q])

# Expected output:
# [3, 0, 5] [0.0, 0.0, 0.8]
