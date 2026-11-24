"""Chapter 14 · Code Trace: compare()

Trigger strategy in algorithmic collusion: compares, through discounted sums,
the cooperation path that earns 50 every period with the deviation path that
undercuts the price in period s, earns 100 and then earns 0. Identical to the
slide code.
"""

def compare(delta, s, T):
    coop, dev = 0.0, 0.0         # cooperate / deviate
    for t in range(T):
        coop += delta**t * 50
        if t < s:
            dev += delta**t * 50
        elif t == s:
            dev += delta**t * 100  # A undercuts
        # t > s: trigger fired, profit 0
    return round(coop, 2), round(dev, 2)
print(compare(0.6, 2, 6))
print(compare(0.4, 2, 6))

# Expected output:
# (119.17, 116.0)
# (82.99, 86.0)
