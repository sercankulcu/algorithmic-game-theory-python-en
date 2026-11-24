"""Chapter 1 · Code Trace: value()

Solves a decision tree recursively: the largest value at a decision node, the
expected value at a chance node. The function is identical to the code on the
slide; the launch tree (tree) is taken from the lecture notes.
"""

def value(n):
    if not isinstance(n, tuple):    # leaf
        return n
    kind, branches = n
    if kind == "C":                  # chance node
        return sum(p * value(c) for p, c in branches)
    return max(value(c) for name, c in branches)  # decision


if __name__ == "__main__":
    # "D": decision node, "C": chance node
    tree = ("D", [
        ("Research", ("C", [
            (0.38, ("D", [("Drive", ("C", [(16/19, 480), (3/19, -220)])),
                          ("Don't drive", -20)])),
            (0.62, ("D", [("Drive", ("C", [(4/31, 480), (27/31, -220)])),
                          ("Don't drive", -20)]))])),
        ("Directly", ("D", [("Drive", ("C", [(0.4, 500), (0.6, -200)])),
                            ("Don't drive", 0)]))])
    print(value(tree))


# Expected output:
# 128.0
