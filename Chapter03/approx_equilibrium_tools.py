"""Chapter 3 · Approximate Equilibrium and Tools

Finds the Nash equilibrium of the worker-manager inspection game with the
nashpy library's support enumeration. Identical to the code on the slide.

Required package: pip install nashpy
"""

import nashpy as nash
A = [[2, 2], [0, 4]]    # worker: Work / Shirk
B = [[1, 2], [-1, -4]]  # manager: Inspect / Don't
game = nash.Game(A, B)
for x, y in game.support_enumeration():
    print(x, y)  # [0.75 0.25] [0.5 0.5]


# Expected output:
# [0.75 0.25] [0.5 0.5]
