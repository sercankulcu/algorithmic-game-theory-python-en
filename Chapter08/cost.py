"""Chapter 8 · Code Trace: cost (BFS)

Computes a player's cost in the one-sided network creation game: alpha times
the number of links she bought plus the sum of the distances found by BFS.
cost is identical to the code on the "Code Trace: cost (BFS)" slide. The nbrs
helper it uses is not on the slide; it is added according to the definition in
the lecture notes.
"""


def nbrs(links, u):
  # Not on the slide: the neighbors of u, whoever bought the link
  return [b if a == u else a for (a, b) in links if u in (a, b)]


def cost(i, links, alpha):
  dist = {i: 0}; queue = [i]
  while queue:
    u = queue.pop(0)
    for v in nbrs(links, u):
      if v not in dist:
        dist[v] = dist[u] + 1
        queue.append(v)
  bought = sum(1 for (a, b) in links if a == i)
  return alpha * bought + sum(dist.values())


if __name__ == "__main__":
  # Example from the lecture notes: path network 1–2–3–4, alpha = 1.5
  path = [(1, 2), (2, 3), (3, 4)]
  print(cost(1, path, 1.5))
  # Deviation: player 1 also buys the link (1, 4)
  deviation = path + [(1, 4)]
  print(cost(1, deviation, 1.5))

# Expected output:
# 7.5
# 7.0
