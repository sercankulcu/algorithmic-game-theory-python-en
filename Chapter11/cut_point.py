"""Chapter 11 · Code Trace: cut_point()

In cut-and-choose division, finds Ayşe's cut point by bisection using
Robertson–Webb value queries. Identical to the slide code.
"""

def v_ayse(x):          # value of [0, x]
  if x <= 0.5: return x / 2
  return 0.25 + 1.5 * (x - 0.5)
def cut_point(v, target, steps):
  lo, hi = 0.0, 1.0
  for _ in range(steps):
    mid = (lo + hi) / 2
    if v(mid) < target: lo = mid
    else: hi = mid
  return (lo + hi) / 2
print(round(cut_point(v_ayse, 0.5, 8), 3))

# Expected output:
# 0.666
