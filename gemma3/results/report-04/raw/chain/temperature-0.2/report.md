# Chain auto-trial report

## Summary

- Batch: `temperature-0.2`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 203.26 seconds
- Average total messages: 17.12
- Success rate: 13/50 (26.0%)
- Reconnect pauses: 1 across 1 trial(s); 18.02 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     167 |           167 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     148 |           166 |        89.2% (0.892) |                0.500 | 1.783 |                0.889 |
| chain    | Agent2 | Agent3    |                  2 |      18 |           166 |        10.8% (0.108) |                0.500 | 0.217 |                0.111 |
| chain    | Agent3 | Agent2    |                  2 |     170 |           179 |        95.0% (0.950) |                0.500 | 1.899 |                0.947 |
| chain    | Agent3 | Agent4    |                  2 |       9 |           179 |         5.0% (0.050) |                0.500 | 0.101 |                0.053 |
| chain    | Agent4 | Agent3    |                  2 |     118 |           157 |        75.2% (0.752) |                0.500 | 1.503 |                0.750 |
| chain    | Agent4 | Agent5    |                  2 |      39 |           157 |        24.8% (0.248) |                0.500 | 0.497 |                0.250 |
| chain    | Agent5 | Agent4    |                  1 |     187 |           187 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.2 | Fail    | cross            | asterisk       |             28 |         912.35 |           0 |             0.00 |
|     2 |         0.2 | Fail    | square           | diamond        |             15 |         131.21 |           0 |             0.00 |
|     3 |         0.2 | Fail    | cross            | triangle       |              9 |          51.09 |           0 |             0.00 |
|     4 |         0.2 | Fail    | diamond          | triangle       |             13 |          75.51 |           0 |             0.00 |
|     5 |         0.2 | Fail    | triangle         | cross          |             11 |          64.74 |           0 |             0.00 |
|     6 |         0.2 | Success | asterisk         | asterisk       |             13 |          73.52 |           0 |             0.00 |
|     7 |         0.2 | Success | triangle         | triangle       |             19 |         106.85 |           0 |             0.00 |
|     8 |         0.2 | Fail    | asterisk         | circle         |             16 |          95.00 |           0 |             0.00 |
|     9 |         0.2 | Success | circle           | circle         |              7 |          42.11 |           0 |             0.00 |
|    10 |         0.2 | Success | cross            | cross          |             17 |          97.06 |           0 |             0.00 |
|    11 |         0.2 | Fail    | square           | asterisk       |             18 |         109.52 |           0 |             0.00 |
|    12 |         0.2 | Success | triangle         | triangle       |             10 |          66.85 |           0 |             0.00 |
|    13 |         0.2 | Fail    | cross            | circle         |             44 |        1347.26 |           0 |             0.00 |
|    14 |         0.2 | Fail    | cross            | asterisk       |             16 |         133.73 |           0 |             0.00 |
|    15 |         0.2 | Fail    | asterisk         | diamond        |             13 |          71.95 |           0 |             0.00 |
|    16 |         0.2 | Fail    | diamond          | cross          |             14 |          79.07 |           0 |             0.00 |
|    17 |         0.2 | Success | circle           | circle         |             17 |          96.59 |           0 |             0.00 |
|    18 |         0.2 | Fail    | cross            | diamond        |              6 |          33.62 |           0 |             0.00 |
|    19 |         0.2 | Fail    | diamond          | square         |             15 |          85.06 |           0 |             0.00 |
|    20 |         0.2 | Fail    | diamond          | square         |             14 |          80.98 |           0 |             0.00 |
|    21 |         0.2 | Fail    | square           | asterisk       |             25 |         139.28 |           0 |             0.00 |
|    22 |         0.2 | Success | cross            | cross          |             28 |         156.13 |           0 |             0.00 |
|    23 |         0.2 | Fail    | cross            | circle         |             27 |         178.81 |           0 |             0.00 |
|    24 |         0.2 | Fail    | cross            | square         |             15 |         271.17 |           0 |             0.00 |
|    25 |         0.2 | Fail    | diamond          | asterisk       |              8 |         132.83 |           0 |             0.00 |
|    26 |         0.2 | Fail    | triangle         | diamond        |             38 |        1533.00 |           0 |             0.00 |
|    27 |         0.2 | Success | circle           | circle         |             43 |         929.92 |           0 |             0.00 |
|    28 |         0.2 | Success | cross            | cross          |             20 |         109.49 |           0 |             0.00 |
|    29 |         0.2 | Fail    | cross            | diamond        |             33 |         183.67 |           0 |             0.00 |
|    30 |         0.2 | Fail    | circle           | triangle       |              8 |          44.85 |           0 |             0.00 |
|    31 |         0.2 | Fail    | diamond          | asterisk       |             16 |          94.04 |           0 |             0.00 |
|    32 |         0.2 | Fail    | triangle         | circle         |             17 |          92.67 |           0 |             0.00 |
|    33 |         0.2 | Fail    | diamond          | triangle       |             16 |          88.44 |           0 |             0.00 |
|    34 |         0.2 | Fail    | diamond          | cross          |              7 |          43.78 |           0 |             0.00 |
|    35 |         0.2 | Fail    | square           | circle         |             15 |          92.70 |           0 |             0.00 |
|    36 |         0.2 | Fail    | triangle         | diamond        |             12 |          78.40 |           0 |             0.00 |
|    37 |         0.2 | Fail    | cross            | square         |              9 |         113.70 |           0 |             0.00 |
|    38 |         0.2 | Fail    | cross            | square         |             13 |         425.44 |           0 |             0.00 |
|    39 |         0.2 | Success | cross            | cross          |             13 |         348.04 |           0 |             0.00 |
|    40 |         0.2 | Fail    | circle           | cross          |             33 |         377.42 |           1 |            18.02 |
|    41 |         0.2 | Fail    | triangle         | asterisk       |             20 |         110.63 |           0 |             0.00 |
|    42 |         0.2 | Fail    | square           | circle         |              9 |          53.04 |           0 |             0.00 |
|    43 |         0.2 | Fail    | diamond          | square         |             14 |          81.04 |           0 |             0.00 |
|    44 |         0.2 | Success | cross            | cross          |             16 |          91.36 |           0 |             0.00 |
|    45 |         0.2 | Fail    | triangle         | square         |             20 |         113.57 |           0 |             0.00 |
|    46 |         0.2 | Fail    | cross            | triangle       |             11 |          63.96 |           0 |             0.00 |
|    47 |         0.2 | Success | diamond          | diamond        |             12 |          73.98 |           0 |             0.00 |
|    48 |         0.2 | Success | triangle         | triangle       |             18 |         152.34 |           0 |             0.00 |
|    49 |         0.2 | Fail    | square           | cross          |              9 |         147.50 |           0 |             0.00 |
|    50 |         0.2 | Fail    | cross            | triangle       |             16 |          87.51 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    40 | Agent5               | 2026-05-14T03:07:39.417828+00:00 | 2026-05-14T03:07:57.436055+00:00 |            18.02 |
```
