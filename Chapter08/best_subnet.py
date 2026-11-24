"""Chapter 8 · Code Trace: best_subnet

Tries deleting the edges of a network one at a time and finds the edge whose
removal shortens the travel time at the Wardrop equilibrium the most (Braess
paradox). best_subnet is identical to the code on the "Code Trace: best_subnet"
slide. The eq_time helper it uses is not on the slide; it is added here as a
simple method that shifts flow between shortest paths (minimizing the Beckmann
potential).
"""


def eq_time(net, r):
  # Not on the slide. Edge: (u, v, a, b), delay b + a * x.
  # Find all paths from s to t; shift flow from the slowest used path
  # to the fastest path until the two travel times are equal.
  paths = []
  def search(u, path, seen):
    if u == "t":
      paths.append(path)
      return
    for k in net:
      if k[0] == u and k[1] not in seen:
        search(k[1], path + [k], seen | {k[1]})
  search("s", [], {"s"})
  if not paths:
    return float("inf")   # inf if there is no path
  flow = [r] + [0] * (len(paths) - 1)
  def times():
    load = {k: 0 for k in net}
    for f, path in zip(flow, paths):
      for k in path:
        load[k] += f
    return [sum(k[3] + k[2] * load[k] for k in path) for path in paths]
  for _ in range(1000):
    c = times()
    used = [i for i in range(len(paths)) if flow[i] > 1e-9]
    slow = max(used, key=lambda i: c[i])
    fast = min(range(len(paths)), key=lambda i: c[i])
    if c[slow] - c[fast] < 1e-9:
      break
    diff = [k for k in paths[slow] if k not in paths[fast]] + \
           [k for k in paths[fast] if k not in paths[slow]]
    slope = sum(k[2] for k in diff)
    d = flow[slow] if slope == 0 else min(flow[slow], (c[slow] - c[fast]) / slope)
    flow[slow] -= d
    flow[fast] += d
  c = times()
  return max(c[i] for i in range(len(paths)) if flow[i] > 1e-9)


def best_subnet(net, r):
  best, cut = eq_time(net, r), None
  for e in net:
    sub = [k for k in net if k != e]
    d = eq_time(sub, r)   # inf if no path
    if d < best:
      best, cut = d, e
  return cut, best


if __name__ == "__main__":
  # Braess network from the lecture notes, 4,000 cars: (start, end, a, b)
  braess = [("s", "A", 1 / 100, 0),   # x/100
            ("A", "t", 0, 45),        # 45
            ("s", "B", 0, 45),        # 45
            ("B", "t", 1 / 100, 0),   # x/100
            ("A", "B", 0, 0)]         # shortcut, 0
  print("initial:", round(eq_time(braess, 4000), 2))
  for e in braess:
    sub = [k for k in braess if k != e]
    print(e[0] + "→" + e[1], "removed:", round(eq_time(sub, 4000), 2))
  cut, best = best_subnet(braess, 4000)
  print("cut:", cut[0] + "→" + cut[1], "time:", round(best, 2))

# Expected output:
# initial: 80.0
# s→A removed: 85.0
# A→t removed: 80.0
# s→B removed: 80.0
# B→t removed: 85.0
# A→B removed: 65.0
# cut: A→B time: 65.0
