"""Chapter 14 · Code Trace: greedy()

Greedy winner determination in a combinatorial auction: bids are sorted by a
key and the bundles that do not overlap are accepted in that order. Two
orderings are compared: by value and by value per item. Identical to the slide
code.
"""

def greedy(bids, key):
    ranked = sorted(bids, key=key, reverse=True)
    total, used = 0, set()
    for S, v in ranked:
        if not (S & used):        # no overlap
            total += v
            used |= S
    return total
T = [({'a','b','c'}, 10), ({'a'}, 4), ({'b'}, 4), ({'c'}, 3)]
print(greedy(T, lambda t: t[1]))
print(greedy(T, lambda t: t[1] / len(t[0])))

# Expected output:
# 10
# 11
