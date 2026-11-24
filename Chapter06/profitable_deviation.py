"""Chapter 6 · Code Trace: profitable_dev

In a GSP auction, tries candidate bids for one advertiser in turn and returns the
first deviation that raises its utility (None if there is none). profitable_dev
is identical to the code on the "Code Trace: profitable_dev" slide. The helper
gsp_utility it uses is not on the slide; it was added following the definition
in the lecture notes.
"""


def gsp_utility(i, b, v, ctr):
  # Not on the slide: bids are sorted; if i is in slot j the utility is
  # ctr[j] * (v[i] - next bid down), and 0 if i is outside the slots
  rank = sorted(range(len(b)), key=lambda k: -b[k])
  j = rank.index(i)
  if j >= len(ctr):
    return 0
  below = b[rank[j + 1]] if j + 1 < len(rank) else 0
  return ctr[j] * (v[i] - below)


def profitable_dev(i, b, v, ctr, cands):
  old = gsp_utility(i, b, v, ctr)
  for x in cands:
    b2 = b[:]; b2[i] = x   # only i changes
    u = gsp_utility(i, b2, v, ctr)
    if u > old:
      return x, u   # profitable
  return None     # no deviation


if __name__ == "__main__":
  # Example from the lecture notes: two profiles for A (i = 0)
  v = [10, 8, 5, 2]
  ctr = [300, 200, 100]
  cands = [9, 6, 4, 3, 1]
  print(profitable_dev(0, [10, 8, 5, 2], v, ctr, cands))    # truthful profile
  print(profitable_dev(0, [10, 5, 3.5, 2], v, ctr, cands))  # equilibrium profile


# Expected output:
# (6, 1000)
# None
