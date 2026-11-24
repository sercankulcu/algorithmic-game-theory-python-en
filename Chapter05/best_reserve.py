"""Chapter 5 · Reserve Code Trace

For a second-price auction with two bidders whose values are U[0, 1], computes
the expected revenue of a reserve price on a grid (revenue) and picks the best
reserve among r = 0, 0.1, ..., 1 (best_reserve). Both functions are identical to
the code on the "Reserve Code Trace" slide.
"""


def revenue(r, m=100):      # 2 bidders, U[0,1]
  v = [(i + .5) / m for i in range(m)]
  total = sum(max(min(a, c), r) for a in v
            for c in v if max(a, c) >= r)
  return total / m**2       # mean payment
def best_reserve(step=0.1):
  best, r_best = -1, None
  for k in range(round(1/step) + 1):
    R = revenue(k * step)
    if R > best: best, r_best = R, k * step
  return r_best, best


if __name__ == "__main__":
  # Table from the lecture notes: revenue for each reserve, then the best reserve
  for k in range(11):
    print(round(k * 0.1, 1), round(revenue(k * 0.1), 3))
  reserve, top_revenue = best_reserve()
  print("best:", reserve, round(top_revenue, 3))


# Expected output:
# 0.0 0.333
# 0.1 0.342
# 0.2 0.363
# 0.3 0.387
# 0.4 0.408
# 0.5 0.417
# 0.6 0.405
# 0.7 0.366
# 0.8 0.291
# 0.9 0.171
# 1.0 0.0
# best: 0.5 0.417
