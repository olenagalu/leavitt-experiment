# Chain auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 197.64 seconds
- Average total messages: 15.82
- Success rate: 20/50 (40.0%)
- Reconnect pauses: 2 across 2 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     133 |           133 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     153 |           168 |        91.1% (0.911) |                0.500 | 1.821 |                0.908 |
| chain    | Agent2 | Agent3    |                  2 |      15 |           168 |         8.9% (0.089) |                0.500 | 0.179 |                0.092 |
| chain    | Agent3 | Agent2    |                  2 |     154 |           160 |        96.2% (0.963) |                0.500 | 1.925 |                0.960 |
| chain    | Agent3 | Agent4    |                  2 |       6 |           160 |         3.8% (0.037) |                0.500 | 0.075 |                0.040 |
| chain    | Agent4 | Agent3    |                  2 |     107 |           171 |        62.6% (0.626) |                0.500 | 1.251 |                0.625 |
| chain    | Agent4 | Agent5    |                  2 |      64 |           171 |        37.4% (0.374) |                0.500 | 0.749 |                0.375 |
| chain    | Agent5 | Agent4    |                  1 |     158 |           158 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| chain    | Agent1 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           1 | Fail    | square           | cross          |             20 |         306.09 |           0 |             0.00 |
|     2 |           1 | Success | cross            | cross          |             15 |          85.90 |           0 |             0.00 |
|     3 |           1 | Fail    | triangle         | asterisk       |             10 |          59.01 |           0 |             0.00 |
|     4 |           1 | Fail    | diamond          | cross          |             13 |          72.94 |           0 |             0.00 |
|     5 |           1 | Success | cross            | cross          |             10 |          56.97 |           0 |             0.00 |
|     6 |           1 | Fail    | cross            | circle         |              9 |          53.10 |           0 |             0.00 |
|     7 |           1 | Success | square           | square         |             16 |          89.06 |           0 |             0.00 |
|     8 |           1 | Success | triangle         | triangle       |             28 |         168.83 |           0 |             0.00 |
|     9 |           1 | Fail    | square           | cross          |             20 |         116.83 |           0 |             0.00 |
|    10 |           1 | Fail    | diamond          | cross          |              6 |          36.35 |           0 |             0.00 |
|    11 |           1 | Fail    | circle           | cross          |             17 |         102.62 |           0 |             0.00 |
|    12 |           1 | Fail    | cross            | triangle       |             24 |         455.97 |           0 |             0.00 |
|    13 |           1 | Success | triangle         | triangle       |             19 |         726.55 |           0 |             0.00 |
|    14 |           1 | Fail    | cross            | diamond        |             19 |         189.99 |           0 |             0.00 |
|    15 |           1 | Fail    | asterisk         | triangle       |             16 |          94.68 |           0 |             0.00 |
|    16 |           1 | Fail    | diamond          | square         |             21 |         121.88 |           0 |             0.00 |
|    17 |           1 | Fail    | asterisk         | cross          |             10 |          58.66 |           0 |             0.00 |
|    18 |           1 | Fail    | cross            | circle         |             19 |         105.16 |           0 |             0.00 |
|    19 |           1 | Fail    | triangle         | diamond        |             11 |          63.10 |           0 |             0.00 |
|    20 |           1 | Success | cross            | cross          |             12 |          67.85 |           0 |             0.00 |
|    21 |           1 | Fail    | square           | cross          |             17 |          95.21 |           0 |             0.00 |
|    22 |           1 | Fail    | triangle         | circle         |             25 |         135.64 |           0 |             0.00 |
|    23 |           1 | Success | asterisk         | asterisk       |              7 |          43.04 |           0 |             0.00 |
|    24 |           1 | Success | circle           | circle         |              6 |         216.40 |           0 |             0.00 |
|    25 |           1 | Fail    | triangle         | square         |             33 |        1986.31 |           1 |             0.00 |
|    26 |           1 | Success | circle           | circle         |             15 |          83.75 |           0 |             0.00 |
|    27 |           1 | Success | triangle         | triangle       |              9 |          51.74 |           0 |             0.00 |
|    28 |           1 | Fail    | diamond          | triangle       |             12 |          69.89 |           0 |             0.00 |
|    29 |           1 | Success | cross            | cross          |             29 |         165.35 |           0 |             0.00 |
|    30 |           1 | Success | circle           | circle         |              6 |          36.07 |           0 |             0.00 |
|    31 |           1 | Fail    | triangle         | circle         |             16 |          92.13 |           0 |             0.00 |
|    32 |           1 | Success | cross            | cross          |             17 |          93.25 |           0 |             0.00 |
|    33 |           1 | Success | triangle         | triangle       |             17 |          93.38 |           0 |             0.00 |
|    34 |           1 | Fail    | cross            | circle         |             20 |         119.53 |           0 |             0.00 |
|    35 |           1 | Success | triangle         | triangle       |             13 |          81.08 |           0 |             0.00 |
|    36 |           1 | Success | cross            | cross          |             16 |         169.97 |           0 |             0.00 |
|    37 |           1 | Fail    | diamond          | circle         |             25 |         334.07 |           0 |             0.00 |
|    38 |           1 | Fail    | square           | cross          |              7 |          52.17 |           0 |             0.00 |
|    39 |           1 | Fail    | square           | circle         |             11 |         140.56 |           0 |             0.00 |
|    40 |           1 | Fail    | triangle         | square         |             21 |         512.51 |           1 |             0.00 |
|    41 |           1 | Fail    | triangle         | diamond        |             18 |         101.79 |           0 |             0.00 |
|    42 |           1 | Fail    | square           | asterisk       |              8 |          46.16 |           0 |             0.00 |
|    43 |           1 | Success | diamond          | diamond        |             19 |         106.50 |           0 |             0.00 |
|    44 |           1 | Success | square           | square         |              8 |          45.65 |           0 |             0.00 |
|    45 |           1 | Success | triangle         | triangle       |             10 |          55.26 |           0 |             0.00 |
|    46 |           1 | Fail    | cross            | asterisk       |             10 |          60.36 |           0 |             0.00 |
|    47 |           1 | Success | asterisk         | asterisk       |             26 |         145.72 |           0 |             0.00 |
|    48 |           1 | Fail    | cross            | asterisk       |             13 |         186.48 |           0 |             0.00 |
|    49 |           1 | Fail    | cross            | diamond        |             35 |        1431.45 |           0 |             0.00 |
|    50 |           1 | Fail    | circle           | cross          |              7 |          98.99 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    25 | Agent4               | 2026-05-14T05:49:51.256461+00:00 | 2026-05-14T05:49:51.258776+00:00 |             0.00 |
|    40 | Agent5               | 2026-05-14T06:35:58.460402+00:00 | 2026-05-14T06:35:58.462792+00:00 |             0.00 |
```
