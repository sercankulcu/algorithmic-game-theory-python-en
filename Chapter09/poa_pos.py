"""Chapter 9 · Code Trace: poa_pos

Scans all assignments in the load balancing game; returns the ratio of the
worst and the best pure Nash equilibrium to the optimum, that is, the Price of
Anarchy (PoA) and the Price of Stability (PoS). poa_pos and the last two lines
are identical to the "Code Trace: poa_pos" slide. The is_nash it uses is not on
this slide; it is taken as is from the previous slide ("Code Trace: is_nash").
"""

def is_nash(sizes, assign, m):
  # Not on this slide: taken from the "Code Trace: is_nash" slide
  load = [0] * m
  for j, k in enumerate(assign):
    load[k] += sizes[j]
  for j, k in enumerate(assign):
    for h in range(m):
      if load[h] + sizes[j] < load[k]:
        return False      # j moves
  return True             # nobody moves


from itertools import product
def poa_pos(sizes, m):
  opt, eqs = float("inf"), []
  for assign in product(range(m), repeat=len(sizes)):
    load = [0] * m
    for j, k in enumerate(assign):
      load[k] += sizes[j]
    opt = min(opt, max(load))
    if is_nash(sizes, assign, m):       # eq. test
      eqs.append(max(load))
  return max(eqs) / opt, min(eqs) / opt
r = poa_pos([2, 2, 1, 1], 2)
print(round(r[0], 3), r[1])

# Expected output:
# 1.333 1.0
