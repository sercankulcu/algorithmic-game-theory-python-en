"""Chapter 2 · Code Trace: solve()

Solves the tree of a perfect-information sequential game by backward induction;
prints the branch chosen at each node and returns the payoff vector of the
subgame perfect equilibrium. Identical to the code on the slide.
"""

def solve(d):
    if isinstance(d, tuple):         # leaf: payoffs
        return d
    name, player, branches = d
    best = None
    for move, child in branches:
        v = solve(child)
        if best is None or v[player] > best[player]:
            best, choice = v, move
    print(name, choice)
    return best
T = ['root', 0, [('Left', ['x', 1, [('a', (3, 1)), ('b', (1, 2))]]),
                ('Right', ['y', 1, [('c', (2, 1)), ('d', (0, 0))]])]]
print(solve(T))


# Expected output:
# x b
# y c
# root Right
# (2, 1)
