"""Chapter 11 · Code Trace: metrics()

Computes the selection rate, the TPR, the FPR and the PPV from a confusion
matrix and prints the fairness metrics of groups A and B side by side.
Identical to the slide code.
"""

def metrics(TP, FP, FN, TN):
  n = TP + FP + FN + TN
  sel = (TP + FP) / n     # demographic parity
  tpr = TP / (TP + FN)    # equalized odds
  fpr = FP / (FP + TN)
  ppv = TP / (TP + FP)    # predictive parity
  return sel, tpr, fpr, ppv

A = metrics(40, 10, 10, 40)
B = metrics(16, 4, 16, 64)
NAMES = ["sel", "TPR", "FPR", "PPV"]
for i, name in enumerate(NAMES):
  print(name, round(A[i], 3), round(B[i], 3))

# Expected output:
# sel 0.5 0.2
# TPR 0.8 0.5
# FPR 0.2 0.059
# PPV 0.8 0.8
