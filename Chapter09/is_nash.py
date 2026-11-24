"""Chapter 9 · Code Trace: is_nash

Checks whether a job assignment in the load balancing game is a pure Nash
equilibrium: returns True if no job finishes earlier by moving to another
machine. The function is identical to the code on the "Code Trace: is_nash"
slide.
"""


def is_nash(sizes, assign, m):
  load = [0] * m
  for j, k in enumerate(assign):
    load[k] += sizes[j]
  for j, k in enumerate(assign):
    for h in range(m):
      if load[h] + sizes[j] < load[k]:
        return False      # j moves
  return True             # nobody moves


if __name__ == "__main__":
  # Example from the lecture notes: jobs {2, 2, 1, 1}, two machines
  sizes = [2, 2, 1, 1]
  print(is_nash(sizes, (0, 0, 1, 1), 2))   # {2, 2} | {1, 1}
  print(is_nash(sizes, (0, 0, 0, 1), 2))   # {2, 2, 1} | {1}

# Expected output:
# True
# False
