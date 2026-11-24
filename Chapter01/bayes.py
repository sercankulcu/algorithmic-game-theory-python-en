"""Chapter 1 · Code Trace: bayes()

Updates a prior probability step by step with Bayes' rule from the successive
results of a disease test and prints the posterior after each step. The function
follows the code in the lecture notes; the sample call is the trace from the notes.
"""

def bayes(p, sens, fp, tests):
  for res in tests:
    if res == "+":
      num = sens * p
      den = num + fp * (1 - p)
    elif res == "-":
      num = (1 - sens) * p
      den = num + (1 - fp) * (1 - p)
    else:
      raise ValueError("result must be + or -")
    if den == 0:
      raise ValueError("impossible result")
    p = num / den
    print(res, round(p, 4))
  return p


if __name__ == "__main__":
    final = bayes(0.01, 0.9, 0.09, ["+", "+", "-"])
    print("final probability:", round(final, 4))


# Expected output:
# + 0.0917
# + 0.5025
# - 0.0999
# final probability: 0.0999
