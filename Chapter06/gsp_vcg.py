"""Chapter 6 · GSP/VCG Code Trace

In a sponsored-search auction, computes the total GSP and VCG payments of each
slot for the same bids. The function is identical to the code on the
"GSP/VCG Code Trace" slide.
"""


def gsp_vcg(bids, ctr):
  m = len(ctr)
  b = sorted(bids, reverse=True) + [0]*m
  a = ctr + [0]     # dummy slot: 0 clicks
  gsp, vcg = [0]*m, [0]*(m + 1)
  for j in range(m):
    gsp[j] = a[j] * b[j+1]   # next bid
  for j in range(m-1, -1, -1):  # bottom up
    extra = (a[j] - a[j+1]) * b[j+1]
    vcg[j] = vcg[j+1] + extra
  return gsp, vcg[:m]


if __name__ == "__main__":
  # Example from the lecture notes: four advertisers, three slots
  gsp, vcg = gsp_vcg([10, 8, 5, 2], [300, 200, 100])
  print("GSP:", gsp, "total", sum(gsp))
  print("VCG:", vcg, "total", sum(vcg))
  # Call with a single slot: the two rules coincide
  print(gsp_vcg([10, 8, 5], [100]))


# Expected output:
# GSP: [2400, 1000, 200] total 3600
# VCG: [1500, 700, 200] total 2400
# ([800], [800])
