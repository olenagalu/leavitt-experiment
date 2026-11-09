# Chain auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 63.02 seconds
- Average total messages: 13.92
- Success rate: 11/50 (22.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     126 |           126 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     121 |           137 |        88.3% (0.883) |                0.500 | 1.766 |                0.880 |
| chain    | Agent2 | Agent3    |                  2 |      16 |           137 |        11.7% (0.117) |                0.500 | 0.234 |                0.120 |
| chain    | Agent3 | Agent2    |                  2 |     130 |           134 |        97.0% (0.970) |                0.500 | 1.940 |                0.967 |
| chain    | Agent3 | Agent4    |                  2 |       4 |           134 |         3.0% (0.030) |                0.500 | 0.060 |                0.033 |
| chain    | Agent4 | Agent3    |                  2 |      97 |           158 |        61.4% (0.614) |                0.500 | 1.228 |                0.613 |
| chain    | Agent4 | Agent5    |                  2 |      61 |           158 |        38.6% (0.386) |                0.500 | 0.772 |                0.387 |
| chain    | Agent5 | Agent4    |                  1 |     141 |           141 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- |
|     1 |           0 | Success | asterisk         | asterisk       |             21 |         264.69 |
|     2 |           0 | Fail    | cross            | circle         |             21 |          82.74 |
|     3 |           0 | Fail    | diamond          | cross          |              9 |          36.30 |
|     4 |           0 | Success | diamond          | diamond        |              8 |          35.34 |
|     5 |           0 | Fail    | cross            | circle         |             16 |          66.36 |
|     6 |           0 | Fail    | square           | diamond        |              9 |          40.04 |
|     7 |           0 | Fail    | asterisk         | diamond        |             18 |          71.44 |
|     8 |           0 | Fail    | cross            | square         |             20 |          88.96 |
|     9 |           0 | Fail    | triangle         | square         |             15 |          64.58 |
|    10 |           0 | Fail    | asterisk         | triangle       |             14 |          60.42 |
|    11 |           0 | Success | diamond          | diamond        |              6 |          25.96 |
|    12 |           0 | Fail    | square           | cross          |             11 |          47.92 |
|    13 |           0 | Fail    | triangle         | square         |             24 |         101.67 |
|    14 |           0 | Fail    | diamond          | circle         |             11 |          46.20 |
|    15 |           0 | Fail    | cross            | diamond        |              9 |          39.02 |
|    16 |           0 | Fail    | triangle         | circle         |             11 |          45.03 |
|    17 |           0 | Fail    | square           | cross          |             10 |          42.70 |
|    18 |           0 | Success | asterisk         | asterisk       |             11 |          46.34 |
|    19 |           0 | Fail    | circle           | asterisk       |             19 |          84.51 |
|    20 |           0 | Fail    | asterisk         | square         |             12 |          50.48 |
|    21 |           0 | Fail    | triangle         | square         |              8 |          34.58 |
|    22 |           0 | Fail    | diamond          | circle         |             12 |          53.90 |
|    23 |           0 | Fail    | circle           | cross          |             20 |          83.57 |
|    24 |           0 | Fail    | triangle         | square         |             13 |          57.58 |
|    25 |           0 | Fail    | asterisk         | diamond        |             20 |          80.53 |
|    26 |           0 | Fail    | triangle         | asterisk       |             12 |          53.56 |
|    27 |           0 | Fail    | square           | asterisk       |              9 |          39.83 |
|    28 |           0 | Fail    | cross            | triangle       |             11 |          44.63 |
|    29 |           0 | Success | triangle         | triangle       |             13 |          56.13 |
|    30 |           0 | Success | triangle         | triangle       |             10 |          44.39 |
|    31 |           0 | Success | diamond          | diamond        |             16 |          67.70 |
|    32 |           0 | Fail    | diamond          | triangle       |             38 |         158.89 |
|    33 |           0 | Fail    | triangle         | circle         |             10 |          44.15 |
|    34 |           0 | Fail    | cross            | diamond        |             10 |          43.33 |
|    35 |           0 | Fail    | circle           | square         |             14 |          60.55 |
|    36 |           0 | Success | asterisk         | asterisk       |             18 |          78.20 |
|    37 |           0 | Fail    | diamond          | square         |             11 |          47.67 |
|    38 |           0 | Fail    | circle           | square         |             12 |          51.37 |
|    39 |           0 | Fail    | diamond          | asterisk       |             16 |          72.20 |
|    40 |           0 | Fail    | cross            | asterisk       |             13 |          52.91 |
|    41 |           0 | Success | triangle         | triangle       |             12 |          52.33 |
|    42 |           0 | Fail    | triangle         | cross          |             13 |          58.20 |
|    43 |           0 | Fail    | triangle         | circle         |             10 |          42.20 |
|    44 |           0 | Fail    | circle           | cross          |             13 |          58.11 |
|    45 |           0 | Fail    | diamond          | square         |             13 |          56.18 |
|    46 |           0 | Fail    | circle           | triangle       |             22 |          92.75 |
|    47 |           0 | Fail    | square           | asterisk       |             19 |          78.59 |
|    48 |           0 | Fail    | asterisk         | cross          |             15 |          65.10 |
|    49 |           0 | Success | diamond          | diamond        |              9 |          40.42 |
|    50 |           0 | Success | asterisk         | asterisk       |              9 |          40.73 |
```
