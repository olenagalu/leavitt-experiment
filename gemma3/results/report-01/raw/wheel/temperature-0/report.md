# Wheel auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 75.82 seconds
- Average total messages: 16.04
- Success rate: 13/50 (26.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     145 |           145 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     169 |           169 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     102 |           170 |        60.0% (0.600) |                0.250 | 2.400 |                0.596 |
| wheel    | Agent3 | Agent2    |                  4 |      64 |           170 |        37.6% (0.376) |                0.250 | 1.506 |                0.375 |
| wheel    | Agent3 | Agent4    |                  4 |       2 |           170 |         1.2% (0.012) |                0.250 | 0.047 |                0.015 |
| wheel    | Agent3 | Agent5    |                  4 |       2 |           170 |         1.2% (0.012) |                0.250 | 0.047 |                0.015 |
| wheel    | Agent4 | Agent3    |                  1 |     163 |           163 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     155 |           155 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- |
|     1 |           0 | Fail    | circle           | diamond        |             16 |         240.36 |
|     2 |           0 | Success | circle           | circle         |             19 |          87.20 |
|     3 |           0 | Fail    | square           | circle         |             14 |          61.46 |
|     4 |           0 | Fail    | asterisk         | circle         |             12 |          58.47 |
|     5 |           0 | Fail    | diamond          | triangle       |             12 |          52.64 |
|     6 |           0 | Fail    | circle           | square         |             25 |         115.83 |
|     7 |           0 | Success | triangle         | triangle       |             10 |          50.40 |
|     8 |           0 | Fail    | square           | triangle       |             12 |          54.27 |
|     9 |           0 | Fail    | cross            | square         |             10 |          47.47 |
|    10 |           0 | Fail    | circle           | square         |             21 |          88.55 |
|    11 |           0 | Fail    | cross            | circle         |             13 |          58.94 |
|    12 |           0 | Fail    | asterisk         | diamond        |             14 |          63.29 |
|    13 |           0 | Fail    | diamond          | triangle       |             13 |          60.05 |
|    14 |           0 | Fail    | circle           | cross          |             13 |          61.35 |
|    15 |           0 | Fail    | diamond          | asterisk       |             19 |          86.57 |
|    16 |           0 | Fail    | circle           | asterisk       |             16 |          70.11 |
|    17 |           0 | Fail    | diamond          | circle         |             33 |         142.05 |
|    18 |           0 | Fail    | diamond          | circle         |             16 |          74.83 |
|    19 |           0 | Fail    | cross            | triangle       |              9 |          43.57 |
|    20 |           0 | Fail    | triangle         | circle         |             24 |         105.13 |
|    21 |           0 | Success | square           | square         |             22 |          97.50 |
|    22 |           0 | Fail    | diamond          | asterisk       |             12 |          56.10 |
|    23 |           0 | Fail    | circle           | square         |             19 |          79.93 |
|    24 |           0 | Fail    | diamond          | triangle       |             10 |          45.51 |
|    25 |           0 | Success | diamond          | diamond        |             47 |         192.83 |
|    26 |           0 | Success | cross            | cross          |             10 |          42.47 |
|    27 |           0 | Fail    | square           | diamond        |             18 |          86.41 |
|    28 |           0 | Fail    | circle           | diamond        |             14 |          63.78 |
|    29 |           0 | Success | circle           | circle         |              7 |          35.25 |
|    30 |           0 | Success | square           | square         |              8 |          38.58 |
|    31 |           0 | Fail    | cross            | diamond        |             18 |          79.69 |
|    32 |           0 | Success | diamond          | diamond        |             21 |          93.39 |
|    33 |           0 | Fail    | asterisk         | triangle       |             24 |         107.03 |
|    34 |           0 | Success | triangle         | triangle       |             18 |          84.31 |
|    35 |           0 | Fail    | diamond          | asterisk       |             10 |          44.77 |
|    36 |           0 | Fail    | circle           | cross          |             10 |          45.90 |
|    37 |           0 | Fail    | cross            | diamond        |             19 |          82.44 |
|    38 |           0 | Fail    | triangle         | square         |             18 |          77.68 |
|    39 |           0 | Fail    | triangle         | asterisk       |             14 |          61.66 |
|    40 |           0 | Fail    | circle           | cross          |             21 |          91.14 |
|    41 |           0 | Fail    | triangle         | circle         |              9 |          44.33 |
|    42 |           0 | Success | triangle         | triangle       |             13 |          57.66 |
|    43 |           0 | Success | cross            | cross          |             11 |          54.14 |
|    44 |           0 | Fail    | circle           | triangle       |             14 |          69.16 |
|    45 |           0 | Success | diamond          | diamond        |             12 |          55.51 |
|    46 |           0 | Fail    | diamond          | circle         |             13 |          64.10 |
|    47 |           0 | Fail    | diamond          | square         |             15 |          67.43 |
|    48 |           0 | Success | square           | square         |             13 |          59.34 |
|    49 |           0 | Fail    | circle           | diamond        |             15 |          70.15 |
|    50 |           0 | Fail    | asterisk         | square         |             26 |         120.24 |
```
