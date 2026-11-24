"""Chapter 4 · TTC Code Trace

Top Trading Cycles: everyone points at the owner of their favorite remaining
room, and those in a cycle trade and leave. assign[k] is the owner of the room
k receives. The function is identical to the code on the slide; the preferences
are the example on the slide.
"""

def ttc(pref):
  left, assign = list(pref), {}
  while left:
    g = {i: next(j for j in pref[i]
             if j in left) for i in left}
    i, path = left[0], []
    while i not in path:          # follow arrows
      path.append(i); i = g[i]
    cycle = path[path.index(i):]
    for k in cycle:              # trade
      assign[k] = g[k]; left.remove(k)
  return assign


if __name__ == "__main__":
    pref = {'A': ['C', 'A', 'B'],
            'B': ['A', 'D', 'B'],
            'C': ['B', 'A', 'C'],
            'D': ['C', 'E', 'B', 'D'],
            'E': ['A', 'D', 'E']}
    print(ttc(pref))


# Expected output:
# {'A': 'C', 'C': 'B', 'B': 'A', 'D': 'E', 'E': 'D'}
