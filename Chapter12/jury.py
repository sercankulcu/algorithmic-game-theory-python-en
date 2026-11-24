"""Chapter 12 · Code Trace: jury()

Condorcet jury theorem: computes, with a binomial sum, the probability that the
majority is right among n independent voters who are each right with
probability p. Identical to the slide code.
"""

from math import comb
def jury(n, p):
    total = 0
    for k in range(n // 2 + 1, n + 1):
        term = comb(n, k) * p**k * (1 - p)**(n - k)
        total += term
    return total
print(round(jury(5, 0.6), 4))

# Expected output:
# 0.6826
