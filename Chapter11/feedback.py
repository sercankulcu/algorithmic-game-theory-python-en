"""Chapter 11 · Code Trace: Feedback Loop

Self-confirming data: the patrol goes every day to the district with more
records and incidents are recorded only there; although the true incident
counts are equal, district 0's share of the records grows every day. Identical
to the slide code.
"""

records = [6, 5]   # past records (district 0, 1)
actual = [3, 3]    # true daily incidents: equal!
for day in range(1, 5):
  target = 0 if records[0] >= records[1] else 1
  records[target] += actual[target]  # only there
  share = records[0] / sum(records)
  print(day, target, records, round(share, 2))

# Expected output:
# 1 0 [9, 5] 0.64
# 2 0 [12, 5] 0.71
# 3 0 [15, 5] 0.75
# 4 0 [18, 5] 0.78
