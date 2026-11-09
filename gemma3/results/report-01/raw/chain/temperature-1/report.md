# Chain auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 67.86 seconds
- Average total messages: 15.64
- Success rate: 15/50 (30.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     125 |           125 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     150 |           177 |        84.7% (0.847) |                0.500 | 1.695 |                0.846 |
| chain    | Agent2 | Agent3    |                  2 |      27 |           177 |        15.3% (0.153) |                0.500 | 0.305 |                0.154 |
| chain    | Agent3 | Agent2    |                  2 |     162 |           166 |        97.6% (0.976) |                0.500 | 1.952 |                0.973 |
| chain    | Agent3 | Agent4    |                  2 |       4 |           166 |         2.4% (0.024) |                0.500 | 0.048 |                0.027 |
| chain    | Agent4 | Agent3    |                  2 |     104 |           159 |        65.4% (0.654) |                0.500 | 1.308 |                0.653 |
| chain    | Agent4 | Agent5    |                  2 |      55 |           159 |        34.6% (0.346) |                0.500 | 0.692 |                0.347 |
| chain    | Agent5 | Agent4    |                  1 |     155 |           155 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- |
|     1 |           1 | Fail    | cross            | diamond        |             17 |         224.14 |
|     2 |           1 | Fail    | cross            | asterisk       |             16 |          65.30 |
|     3 |           1 | Fail    | cross            | square         |             20 |          81.56 |
|     4 |           1 | Fail    | square           | asterisk       |             16 |          68.60 |
|     5 |           1 | Fail    | circle           | triangle       |             18 |          78.03 |
|     6 |           1 | Fail    | triangle         | square         |              9 |          35.68 |
|     7 |           1 | Success | triangle         | triangle       |              8 |          35.64 |
|     8 |           1 | Fail    | circle           | cross          |             21 |          79.78 |
|     9 |           1 | Fail    | cross            | asterisk       |             13 |          53.34 |
|    10 |           1 | Success | asterisk         | asterisk       |             19 |          77.70 |
|    11 |           1 | Success | cross            | cross          |             11 |          44.02 |
|    12 |           1 | Fail    | triangle         | cross          |             16 |          65.93 |
|    13 |           1 | Success | circle           | circle         |             11 |          45.89 |
|    14 |           1 | Success | diamond          | diamond        |              9 |          38.93 |
|    15 |           1 | Success | square           | square         |              9 |          38.26 |
|    16 |           1 | Fail    | cross            | square         |             27 |         108.62 |
|    17 |           1 | Fail    | triangle         | square         |             17 |          70.42 |
|    18 |           1 | Success | square           | square         |             27 |         105.96 |
|    19 |           1 | Fail    | asterisk         | cross          |             16 |          65.91 |
|    20 |           1 | Fail    | cross            | diamond        |             17 |          68.05 |
|    21 |           1 | Success | cross            | cross          |             31 |         130.08 |
|    22 |           1 | Fail    | cross            | circle         |             13 |          53.95 |
|    23 |           1 | Fail    | asterisk         | diamond        |             10 |          43.91 |
|    24 |           1 | Success | asterisk         | asterisk       |              6 |          25.87 |
|    25 |           1 | Fail    | cross            | square         |              8 |          35.30 |
|    26 |           1 | Fail    | circle           | square         |              9 |          36.87 |
|    27 |           1 | Fail    | circle           | square         |             15 |          65.66 |
|    28 |           1 | Fail    | asterisk         | circle         |             13 |          61.06 |
|    29 |           1 | Fail    | diamond          | asterisk       |             13 |          49.84 |
|    30 |           1 | Fail    | circle           | diamond        |             11 |          48.26 |
|    31 |           1 | Fail    | square           | cross          |             15 |          66.05 |
|    32 |           1 | Success | cross            | cross          |             43 |         161.66 |
|    33 |           1 | Fail    | circle           | cross          |             16 |          68.71 |
|    34 |           1 | Fail    | triangle         | circle         |             19 |          77.67 |
|    35 |           1 | Success | asterisk         | asterisk       |             10 |          44.40 |
|    36 |           1 | Fail    | cross            | triangle       |             14 |          59.14 |
|    37 |           1 | Fail    | triangle         | circle         |             19 |          79.42 |
|    38 |           1 | Fail    | triangle         | asterisk       |              8 |          33.58 |
|    39 |           1 | Fail    | cross            | circle         |             19 |          81.27 |
|    40 |           1 | Success | square           | square         |             26 |         101.54 |
|    41 |           1 | Fail    | cross            | circle         |             13 |          54.85 |
|    42 |           1 | Fail    | triangle         | asterisk       |             18 |          77.55 |
|    43 |           1 | Fail    | circle           | diamond        |             15 |          56.37 |
|    44 |           1 | Success | diamond          | diamond        |             13 |          59.18 |
|    45 |           1 | Fail    | circle           | diamond        |             15 |          62.92 |
|    46 |           1 | Fail    | cross            | triangle       |              9 |          40.70 |
|    47 |           1 | Success | square           | square         |             27 |         108.66 |
|    48 |           1 | Success | square           | square         |             18 |          74.76 |
|    49 |           1 | Fail    | cross            | circle         |              7 |          31.30 |
|    50 |           1 | Fail    | cross            | asterisk       |             12 |          50.69 |
```
