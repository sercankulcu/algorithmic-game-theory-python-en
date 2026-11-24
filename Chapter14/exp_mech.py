"""Chapter 14 · Code Trace: exp_mech()

The exponential mechanism in differential privacy: each candidate price is
chosen with weight exp(ε·R/2), proportional to its empirical revenue score;
shows how much the probabilities change when one buyer is removed. Identical
to the slide code.
"""

import math
def exp_mech(v, prices, eps):
    R = [p * sum(x >= p for x in v) for p in prices]
    w = [math.exp(eps * r / 2) for r in R]   # Δ = 1
    W = sum(w)
    return [x / W for x in w]
v = [0.62, 0.15, 0.91, 0.47, 0.33, 0.78, 0.55, 0.08]
P = [0.2, 0.4, 0.6, 0.8]
q = exp_mech(v, P, 2)
print([round(x, 3) for x in q])
q = exp_mech(v[1:], P, 2)       # 0.62 removed
print([round(x, 3) for x in q])

# Expected output:
# [0.175, 0.389, 0.319, 0.117]
# [0.206, 0.375, 0.251, 0.168]
