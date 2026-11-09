# Wheel auto-trial report

## Summary

- Batch: `temperature-0.5`
- Temperature: 0.5
- Completed trials: 50/50
- Average time: 81.32 seconds
- Average total messages: 17.06
- Success rate: 11/50 (22.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     175 |           175 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     180 |           180 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |      91 |           166 |        54.8% (0.548) |                0.250 | 2.193 |                0.545 |
| wheel    | Agent3 | Agent2    |                  4 |      67 |           166 |        40.4% (0.404) |                0.250 | 1.614 |                0.402 |
| wheel    | Agent3 | Agent4    |                  4 |       4 |           166 |         2.4% (0.024) |                0.250 | 0.096 |                0.027 |
| wheel    | Agent3 | Agent5    |                  4 |       4 |           166 |         2.4% (0.024) |                0.250 | 0.096 |                0.027 |
| wheel    | Agent4 | Agent3    |                  1 |     159 |           159 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     173 |           173 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- |
|     1 |         0.5 | Success | diamond          | diamond        |             14 |         219.80 |
|     2 |         0.5 | Success | circle           | circle         |             21 |          96.75 |
|     3 |         0.5 | Fail    | square           | diamond        |             23 |         109.34 |
|     4 |         0.5 | Fail    | diamond          | square         |              8 |          34.35 |
|     5 |         0.5 | Fail    | cross            | asterisk       |             19 |          81.03 |
|     6 |         0.5 | Fail    | square           | circle         |             10 |          48.96 |
|     7 |         0.5 | Fail    | cross            | circle         |             16 |          72.21 |
|     8 |         0.5 | Success | diamond          | diamond        |             17 |          80.96 |
|     9 |         0.5 | Fail    | asterisk         | circle         |             23 |          97.98 |
|    10 |         0.5 | Fail    | circle           | diamond        |             27 |         123.57 |
|    11 |         0.5 | Fail    | triangle         | diamond        |             17 |          83.95 |
|    12 |         0.5 | Fail    | asterisk         | cross          |             12 |          50.82 |
|    13 |         0.5 | Fail    | cross            | diamond        |             22 |         100.01 |
|    14 |         0.5 | Fail    | cross            | square         |             12 |          57.30 |
|    15 |         0.5 | Fail    | circle           | diamond        |             19 |          88.14 |
|    16 |         0.5 | Fail    | cross            | circle         |             12 |          58.19 |
|    17 |         0.5 | Fail    | circle           | cross          |             25 |         119.25 |
|    18 |         0.5 | Fail    | cross            | triangle       |             17 |          71.09 |
|    19 |         0.5 | Fail    | circle           | square         |             11 |          51.64 |
|    20 |         0.5 | Fail    | cross            | triangle       |             27 |         123.35 |
|    21 |         0.5 | Success | circle           | circle         |             39 |         173.85 |
|    22 |         0.5 | Fail    | triangle         | asterisk       |             13 |          63.57 |
|    23 |         0.5 | Success | circle           | circle         |             25 |         114.09 |
|    24 |         0.5 | Fail    | triangle         | asterisk       |             24 |          99.24 |
|    25 |         0.5 | Success | triangle         | triangle       |             13 |          64.55 |
|    26 |         0.5 | Success | cross            | cross          |             11 |          54.72 |
|    27 |         0.5 | Fail    | circle           | square         |             22 |          94.35 |
|    28 |         0.5 | Fail    | circle           | diamond        |             12 |          54.90 |
|    29 |         0.5 | Fail    | diamond          | square         |             16 |          71.08 |
|    30 |         0.5 | Fail    | asterisk         | triangle       |              9 |          44.69 |
|    31 |         0.5 | Fail    | asterisk         | square         |             10 |          46.78 |
|    32 |         0.5 | Success | asterisk         | asterisk       |             15 |          68.57 |
|    33 |         0.5 | Fail    | circle           | square         |             14 |          63.63 |
|    34 |         0.5 | Fail    | cross            | circle         |             12 |          55.69 |
|    35 |         0.5 | Fail    | cross            | diamond        |             20 |          91.13 |
|    36 |         0.5 | Fail    | circle           | cross          |             12 |          59.16 |
|    37 |         0.5 | Fail    | diamond          | asterisk       |             10 |          44.02 |
|    38 |         0.5 | Fail    | circle           | asterisk       |             24 |         101.97 |
|    39 |         0.5 | Fail    | cross            | triangle       |             12 |          56.00 |
|    40 |         0.5 | Success | circle           | circle         |             18 |          84.75 |
|    41 |         0.5 | Fail    | circle           | diamond        |             15 |          67.04 |
|    42 |         0.5 | Fail    | square           | diamond        |             21 |         107.66 |
|    43 |         0.5 | Fail    | cross            | circle         |              7 |          30.93 |
|    44 |         0.5 | Fail    | square           | cross          |             25 |         106.88 |
|    45 |         0.5 | Success | circle           | circle         |             13 |          57.92 |
|    46 |         0.5 | Success | diamond          | diamond        |             10 |          47.39 |
|    47 |         0.5 | Fail    | circle           | triangle       |             18 |          91.29 |
|    48 |         0.5 | Fail    | cross            | square         |             14 |          63.27 |
|    49 |         0.5 | Fail    | square           | diamond        |             23 |         109.56 |
|    50 |         0.5 | Fail    | triangle         | diamond        |             24 |         108.79 |
```
