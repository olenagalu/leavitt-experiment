# Circle auto-trial report

## Summary

- Batch: `temperature-0.5`
- Temperature: 0.5
- Completed trials: 50/50
- Average time: 56.44 seconds
- Average total messages: 12.00
- Success rate: 17/50 (34.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |       9 |           128 |         7.0% (0.070) |                0.500 | 0.141 |                0.074 |
| circle   | Agent1 | Agent5    |                  2 |     119 |           128 |        93.0% (0.930) |                0.500 | 1.859 |                0.926 |
| circle   | Agent2 | Agent1    |                  2 |      95 |           124 |        76.6% (0.766) |                0.500 | 1.532 |                0.764 |
| circle   | Agent2 | Agent3    |                  2 |      29 |           124 |        23.4% (0.234) |                0.500 | 0.468 |                0.236 |
| circle   | Agent3 | Agent2    |                  2 |     110 |           111 |        99.1% (0.991) |                0.500 | 1.982 |                0.987 |
| circle   | Agent3 | Agent4    |                  2 |       1 |           111 |         0.9% (0.009) |                0.500 | 0.018 |                0.013 |
| circle   | Agent4 | Agent3    |                  2 |      84 |           117 |        71.8% (0.718) |                0.500 | 1.436 |                0.716 |
| circle   | Agent4 | Agent5    |                  2 |      33 |           117 |        28.2% (0.282) |                0.500 | 0.564 |                0.284 |
| circle   | Agent5 | Agent1    |                  2 |      94 |           120 |        78.3% (0.783) |                0.500 | 1.567 |                0.781 |
| circle   | Agent5 | Agent4    |                  2 |      26 |           120 |        21.7% (0.217) |                0.500 | 0.433 |                0.219 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- |
|     1 |         0.5 | Fail    | cross            | asterisk       |              7 |         216.51 |
|     2 |         0.5 | Fail    | diamond          | square         |             14 |          62.22 |
|     3 |         0.5 | Success | circle           | circle         |             15 |          67.34 |
|     4 |         0.5 | Fail    | circle           | diamond        |              9 |          40.85 |
|     5 |         0.5 | Fail    | circle           | cross          |             10 |          43.82 |
|     6 |         0.5 | Fail    | cross            | triangle       |             14 |          59.31 |
|     7 |         0.5 | Fail    | circle           | triangle       |             10 |          45.20 |
|     8 |         0.5 | Success | triangle         | triangle       |             10 |          46.15 |
|     9 |         0.5 | Success | circle           | circle         |             10 |          43.16 |
|    10 |         0.5 | Fail    | cross            | triangle       |             11 |          48.03 |
|    11 |         0.5 | Success | circle           | circle         |              5 |          23.94 |
|    12 |         0.5 | Fail    | cross            | triangle       |              5 |          24.31 |
|    13 |         0.5 | Success | cross            | cross          |             19 |          83.28 |
|    14 |         0.5 | Success | circle           | circle         |              5 |          23.40 |
|    15 |         0.5 | Fail    | circle           | cross          |             10 |          44.61 |
|    16 |         0.5 | Success | triangle         | triangle       |             10 |          44.75 |
|    17 |         0.5 | Fail    | triangle         | asterisk       |             10 |          44.38 |
|    18 |         0.5 | Fail    | square           | circle         |             10 |          45.38 |
|    19 |         0.5 | Fail    | square           | asterisk       |             14 |          62.18 |
|    20 |         0.5 | Success | diamond          | diamond        |              5 |          23.00 |
|    21 |         0.5 | Fail    | circle           | asterisk       |              5 |          23.50 |
|    22 |         0.5 | Success | square           | square         |              5 |          22.97 |
|    23 |         0.5 | Fail    | cross            | triangle       |             10 |          44.22 |
|    24 |         0.5 | Fail    | circle           | diamond        |             18 |          73.97 |
|    25 |         0.5 | Fail    | square           | triangle       |             19 |          82.79 |
|    26 |         0.5 | Success | square           | square         |              7 |          31.34 |
|    27 |         0.5 | Success | square           | square         |             10 |          44.78 |
|    28 |         0.5 | Fail    | circle           | asterisk       |             10 |          43.19 |
|    29 |         0.5 | Success | square           | square         |             19 |          79.96 |
|    30 |         0.5 | Success | square           | square         |             10 |          45.14 |
|    31 |         0.5 | Fail    | circle           | asterisk       |             16 |          71.15 |
|    32 |         0.5 | Success | triangle         | triangle       |             11 |          49.92 |
|    33 |         0.5 | Fail    | square           | diamond        |             15 |          63.10 |
|    34 |         0.5 | Fail    | square           | diamond        |             18 |          77.07 |
|    35 |         0.5 | Fail    | square           | asterisk       |              5 |          23.76 |
|    36 |         0.5 | Fail    | square           | triangle       |             15 |          67.13 |
|    37 |         0.5 | Success | asterisk         | asterisk       |             25 |         104.81 |
|    38 |         0.5 | Fail    | square           | diamond        |              5 |          24.63 |
|    39 |         0.5 | Fail    | square           | triangle       |              5 |          23.68 |
|    40 |         0.5 | Fail    | circle           | square         |             10 |          45.90 |
|    41 |         0.5 | Fail    | triangle         | cross          |             15 |          65.06 |
|    42 |         0.5 | Fail    | cross            | asterisk       |              7 |          32.36 |
|    43 |         0.5 | Fail    | triangle         | asterisk       |             10 |          44.81 |
|    44 |         0.5 | Fail    | asterisk         | circle         |             35 |         145.30 |
|    45 |         0.5 | Fail    | square           | cross          |             20 |          83.31 |
|    46 |         0.5 | Fail    | triangle         | circle         |             10 |          46.79 |
|    47 |         0.5 | Fail    | triangle         | circle         |             23 |          98.96 |
|    48 |         0.5 | Success | circle           | circle         |             10 |          44.39 |
|    49 |         0.5 | Success | square           | square         |             11 |          51.04 |
|    50 |         0.5 | Fail    | triangle         | asterisk       |             18 |          75.31 |
```
