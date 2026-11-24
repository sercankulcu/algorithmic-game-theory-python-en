"""Chapter 14 · Code Trace: sandwich()

Sandwich attack on an xy = k automated market maker: the attacker front-runs
the user's trade and sells right after it; if the user's slippage limit
(min_out) is violated the trade reverts. Prints the attacker's profit.
Identical to the slide code.
"""

swap = lambda x, y, dx: y - x * y / (x + dx)  # xy=k
def sandwich(x, y, a, u, min_out):
    b1 = swap(x, y, a)           # front-run: sell a A
    x, y = x + a, y - b1
    b2 = swap(x, y, u)           # user: sell u A
    if b2 < min_out:
        return None              # tx reverted
    x, y = x + u, y - b2
    a2 = swap(y, x, b1)          # back-run: sell b1 B
    return round(a2 - a, 2)
for a in [20, 50, 80]:
    print(a, sandwich(1000, 1000, a, 100, 82))

# Expected output:
# 20 4.07
# 50 9.71
# 80 None
