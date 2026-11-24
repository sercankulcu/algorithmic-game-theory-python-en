"""Chapter 14 · Code Trace: revenue()

Automated mechanism design for a single buyer with two types (L has value 1, H
has value 3): computes the seller's expected revenue as a function of the
probability xL of selling to L, with the IR and IC constraints binding.
Identical to the slide code.
"""

def revenue(xL, qL, vL=1, vH=3):
    pL = xL * vL                 # L's IR binds
    pH = pL + vH * (1 - xL)      # H's IC binds
    return qL * pL + (1 - qL) * pH
for qL in [0.5, 0.75]:
    G = [revenue(x, qL) for x in [0, 0.5, 1]]
    print(qL, G)

# Expected output:
# 0.5 [1.5, 1.25, 1.0]
# 0.75 [0.75, 0.875, 1.0]
