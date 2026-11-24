"""Chapter 4 · Gale–Shapley Code Trace

Matches students to projects stably with student-proposing Gale–Shapley deferred
acceptance. The function follows the code in the lecture notes; the preference
lists are the example from the notes (proj[p][s]: the rank p gives s, 0 = best).
"""

def gale_shapley(stu, proj):
  free, match = list(stu), {}
  nxt = {s: 0 for s in stu}
  while free:
    s = free.pop(0)
    p = stu[s][nxt[s]]        # next choice
    nxt[s] += 1
    r = match.get(p)              # p's holder
    if r is None or proj[p][s] < proj[p][r]:
      match[p] = s                # accept
      if r is not None: free.append(r)
    else: free.append(s)    # reject
  return match


if __name__ == "__main__":
    stu = {'A': ['X', 'Y', 'Z'],
           'B': ['X', 'Z', 'Y'],
           'C': ['Y', 'X', 'Z']}
    proj = {'X': {'B': 0, 'A': 1, 'C': 2},
            'Y': {'A': 0, 'C': 1, 'B': 2},
            'Z': {'A': 0, 'B': 1, 'C': 2}}
    print(gale_shapley(stu, proj))


# Expected output:
# {'X': 'B', 'Y': 'A', 'Z': 'C'}
