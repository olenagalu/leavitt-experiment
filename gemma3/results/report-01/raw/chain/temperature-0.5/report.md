# Chain auto-trial report

## Summary

- Batch: `temperature-0.5`
- Temperature: 0.5
- Completed trials: 50/50
- Average time: 66.85 seconds
- Average total messages: 15.24
- Success rate: 15/50 (30.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     134 |           134 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     124 |           145 |        85.5% (0.855) |                0.500 | 1.710 |                0.853 |
| chain    | Agent2 | Agent3    |                  2 |      21 |           145 |        14.5% (0.145) |                0.500 | 0.290 |                0.147 |
| chain    | Agent3 | Agent2    |                  2 |     145 |           153 |        94.8% (0.948) |                0.500 | 1.895 |                0.945 |
| chain    | Agent3 | Agent4    |                  2 |       8 |           153 |         5.2% (0.052) |                0.500 | 0.105 |                0.055 |
| chain    | Agent4 | Agent3    |                  2 |     114 |           170 |        67.1% (0.671) |                0.500 | 1.341 |                0.670 |
| chain    | Agent4 | Agent5    |                  2 |      56 |           170 |        32.9% (0.329) |                0.500 | 0.659 |                0.330 |
| chain    | Agent5 | Agent4    |                  1 |     160 |           160 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- |
|     1 |         0.5 | Fail    | diamond          | square         |             10 |         197.80 |
|     2 |         0.5 | Fail    | triangle         | cross          |              7 |          30.47 |
|     3 |         0.5 | Success | cross            | cross          |             19 |          74.51 |
|     4 |         0.5 | Fail    | square           | asterisk       |             17 |          70.56 |
|     5 |         0.5 | Fail    | triangle         | asterisk       |             11 |          46.87 |
|     6 |         0.5 | Success | circle           | circle         |             20 |          81.10 |
|     7 |         0.5 | Success | diamond          | diamond        |             22 |          93.59 |
|     8 |         0.5 | Success | circle           | circle         |             10 |          45.33 |
|     9 |         0.5 | Fail    | cross            | square         |             14 |          57.64 |
|    10 |         0.5 | Fail    | cross            | circle         |             15 |          65.83 |
|    11 |         0.5 | Fail    | cross            | diamond        |             11 |          46.57 |
|    12 |         0.5 | Fail    | circle           | square         |             24 |          94.93 |
|    13 |         0.5 | Fail    | triangle         | diamond        |             18 |          68.13 |
|    14 |         0.5 | Success | asterisk         | asterisk       |             11 |          48.24 |
|    15 |         0.5 | Fail    | cross            | diamond        |             23 |          94.23 |
|    16 |         0.5 | Fail    | triangle         | diamond        |              6 |          26.64 |
|    17 |         0.5 | Fail    | diamond          | circle         |             12 |          52.90 |
|    18 |         0.5 | Fail    | square           | triangle       |             10 |          45.33 |
|    19 |         0.5 | Fail    | diamond          | circle         |             31 |         119.82 |
|    20 |         0.5 | Fail    | square           | asterisk       |             16 |          69.47 |
|    21 |         0.5 | Fail    | diamond          | triangle       |             22 |          86.04 |
|    22 |         0.5 | Fail    | circle           | cross          |             14 |          59.44 |
|    23 |         0.5 | Fail    | asterisk         | diamond        |             15 |          62.11 |
|    24 |         0.5 | Fail    | square           | triangle       |             17 |          70.62 |
|    25 |         0.5 | Success | circle           | circle         |             15 |          60.33 |
|    26 |         0.5 | Fail    | cross            | square         |             16 |          64.71 |
|    27 |         0.5 | Success | cross            | cross          |             27 |         113.66 |
|    28 |         0.5 | Fail    | asterisk         | cross          |             11 |          45.76 |
|    29 |         0.5 | Fail    | cross            | asterisk       |             17 |          71.68 |
|    30 |         0.5 | Fail    | triangle         | square         |             14 |          56.66 |
|    31 |         0.5 | Fail    | diamond          | cross          |             32 |         135.80 |
|    32 |         0.5 | Success | square           | square         |             11 |          48.66 |
|    33 |         0.5 | Success | diamond          | diamond        |              7 |          31.35 |
|    34 |         0.5 | Fail    | circle           | cross          |             23 |          95.12 |
|    35 |         0.5 | Success | cross            | cross          |             16 |          70.41 |
|    36 |         0.5 | Success | asterisk         | asterisk       |             22 |          98.99 |
|    37 |         0.5 | Fail    | triangle         | cross          |              6 |          26.10 |
|    38 |         0.5 | Fail    | diamond          | square         |             13 |          56.48 |
|    39 |         0.5 | Fail    | square           | cross          |             10 |          43.71 |
|    40 |         0.5 | Fail    | square           | diamond        |             13 |          49.08 |
|    41 |         0.5 | Fail    | square           | diamond        |              9 |          39.13 |
|    42 |         0.5 | Fail    | diamond          | cross          |             18 |          74.71 |
|    43 |         0.5 | Success | diamond          | diamond        |             12 |          53.63 |
|    44 |         0.5 | Fail    | circle           | triangle       |             18 |          79.75 |
|    45 |         0.5 | Fail    | square           | diamond        |             12 |          53.43 |
|    46 |         0.5 | Success | square           | square         |             18 |          71.74 |
|    47 |         0.5 | Fail    | diamond          | triangle       |              9 |          37.34 |
|    48 |         0.5 | Fail    | cross            | triangle       |              9 |          37.43 |
|    49 |         0.5 | Success | triangle         | triangle       |             13 |          57.69 |
|    50 |         0.5 | Success | cross            | cross          |             16 |          60.77 |
```
