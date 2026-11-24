"""Chapter 11 · Code Trace: group_b(q)

Tries to achieve equality of opportunity by randomization: in group B,
applicants with score 0.2 are approved with probability q; prints the TPR, the
FPR and the accuracy for each q. Identical to the slide code.
"""

def group_b(q):   # approve score 0.2 w.p. q
  TP = 16 + 16 * q
  FP = 4 + 64 * q
  tpr = TP / 32
  fpr = FP / 68
  hits = TP + (68 - FP)    # TP + TN
  return tpr, fpr, round(hits / 100, 3)

for q in [0, 0.2, 0.4, 0.6]:
  tpr, fpr, d = group_b(q)
  print(q, round(tpr, 2), round(fpr, 2), d)

# Expected output:
# 0 0.5 0.06 0.8
# 0.2 0.6 0.25 0.704
# 0.4 0.7 0.44 0.608
# 0.6 0.8 0.62 0.512
