# Wheel auto-trial report

## Summary

- Batch: `temperature-0.1`
- Temperature: 0.1
- Completed trials: 50/50
- Average time: 218.88 seconds
- Average total messages: 18.32
- Success rate: 11/50 (22.0%)
- Reconnect pauses: 2 across 2 trial(s); 101.12 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     165 |           165 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     184 |           184 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     105 |           186 |        56.5% (0.565) |                0.250 | 2.258 |                0.561 |
| wheel    | Agent3 | Agent2    |                  4 |      70 |           186 |        37.6% (0.376) |                0.250 | 1.505 |                0.375 |
| wheel    | Agent3 | Agent4    |                  4 |       5 |           186 |         2.7% (0.027) |                0.250 | 0.108 |                0.029 |
| wheel    | Agent3 | Agent5    |                  4 |       6 |           186 |         3.2% (0.032) |                0.250 | 0.129 |                0.035 |
| wheel    | Agent4 | Agent3    |                  1 |     190 |           190 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     191 |           191 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.1 | Success | circle           | circle         |             17 |         304.38 |           0 |             0.00 |
|     2 |         0.1 | Success | cross            | cross          |              8 |          51.73 |           0 |             0.00 |
|     3 |         0.1 | Success | circle           | circle         |             21 |         124.64 |           0 |             0.00 |
|     4 |         0.1 | Fail    | diamond          | cross          |              8 |          50.07 |           0 |             0.00 |
|     5 |         0.1 | Fail    | cross            | diamond        |             18 |         119.42 |           0 |             0.00 |
|     6 |         0.1 | Fail    | circle           | asterisk       |             25 |         152.13 |           0 |             0.00 |
|     7 |         0.1 | Fail    | cross            | asterisk       |             30 |         176.83 |           0 |             0.00 |
|     8 |         0.1 | Fail    | diamond          | triangle       |              9 |          60.84 |           0 |             0.00 |
|     9 |         0.1 | Fail    | square           | cross          |             30 |         872.19 |           0 |             0.00 |
|    10 |         0.1 | Fail    | square           | cross          |             22 |         387.67 |           0 |             0.00 |
|    11 |         0.1 | Fail    | diamond          | asterisk       |             25 |         151.31 |           0 |             0.00 |
|    12 |         0.1 | Fail    | diamond          | triangle       |             35 |         264.95 |           0 |             0.00 |
|    13 |         0.1 | Success | triangle         | triangle       |              7 |          45.65 |           0 |             0.00 |
|    14 |         0.1 | Fail    | diamond          | square         |             23 |         145.78 |           0 |             0.00 |
|    15 |         0.1 | Fail    | circle           | triangle       |              9 |          60.17 |           0 |             0.00 |
|    16 |         0.1 | Fail    | circle           | square         |             17 |         184.55 |           0 |             0.00 |
|    17 |         0.1 | Fail    | cross            | square         |             16 |         105.72 |           0 |             0.00 |
|    18 |         0.1 | Fail    | circle           | square         |             16 |         106.52 |           0 |             0.00 |
|    19 |         0.1 | Fail    | square           | diamond        |              7 |          72.41 |           0 |             0.00 |
|    20 |         0.1 | Success | diamond          | diamond        |             16 |         334.92 |           0 |             0.00 |
|    21 |         0.1 | Fail    | cross            | asterisk       |             40 |        1248.29 |           1 |            34.04 |
|    22 |         0.1 | Fail    | square           | asterisk       |             11 |         118.38 |           0 |             0.00 |
|    23 |         0.1 | Fail    | circle           | square         |             12 |          73.98 |           0 |             0.00 |
|    24 |         0.1 | Success | cross            | cross          |             20 |         124.78 |           0 |             0.00 |
|    25 |         0.1 | Fail    | circle           | diamond        |             19 |         126.18 |           0 |             0.00 |
|    26 |         0.1 | Fail    | asterisk         | square         |             12 |          76.26 |           0 |             0.00 |
|    27 |         0.1 | Fail    | cross            | square         |             15 |          94.15 |           0 |             0.00 |
|    28 |         0.1 | Success | triangle         | triangle       |             19 |         116.51 |           0 |             0.00 |
|    29 |         0.1 | Fail    | square           | triangle       |             42 |        1075.36 |           0 |             0.00 |
|    30 |         0.1 | Success | asterisk         | asterisk       |             16 |         106.09 |           0 |             0.00 |
|    31 |         0.1 | Fail    | asterisk         | diamond        |             22 |         160.30 |           0 |             0.00 |
|    32 |         0.1 | Success | diamond          | diamond        |             44 |         981.89 |           0 |             0.00 |
|    33 |         0.1 | Fail    | asterisk         | cross          |             11 |          70.78 |           0 |             0.00 |
|    34 |         0.1 | Fail    | triangle         | cross          |              9 |          56.13 |           0 |             0.00 |
|    35 |         0.1 | Fail    | cross            | asterisk       |              9 |          57.51 |           0 |             0.00 |
|    36 |         0.1 | Fail    | asterisk         | cross          |             12 |          72.07 |           0 |             0.00 |
|    37 |         0.1 | Fail    | cross            | triangle       |             13 |          81.70 |           0 |             0.00 |
|    38 |         0.1 | Fail    | triangle         | asterisk       |              6 |          39.82 |           0 |             0.00 |
|    39 |         0.1 | Fail    | cross            | asterisk       |             13 |         103.13 |           0 |             0.00 |
|    40 |         0.1 | Fail    | square           | triangle       |             33 |        1122.13 |           1 |            67.08 |
|    41 |         0.1 | Fail    | cross            | square         |             32 |         237.02 |           0 |             0.00 |
|    42 |         0.1 | Fail    | square           | asterisk       |             23 |         132.66 |           0 |             0.00 |
|    43 |         0.1 | Success | diamond          | diamond        |             11 |          72.00 |           0 |             0.00 |
|    44 |         0.1 | Fail    | square           | circle         |             19 |         115.19 |           0 |             0.00 |
|    45 |         0.1 | Fail    | cross            | square         |             18 |         116.41 |           0 |             0.00 |
|    46 |         0.1 | Fail    | square           | asterisk       |             11 |          73.08 |           0 |             0.00 |
|    47 |         0.1 | Fail    | triangle         | cross          |             25 |         161.39 |           0 |             0.00 |
|    48 |         0.1 | Success | asterisk         | asterisk       |             14 |          97.61 |           0 |             0.00 |
|    49 |         0.1 | Fail    | diamond          | asterisk       |             13 |         143.42 |           0 |             0.00 |
|    50 |         0.1 | Fail    | diamond          | square         |             13 |         117.92 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    21 | Agent2               | 2026-05-15T09:40:01.398854+00:00 | 2026-05-15T09:40:35.439731+00:00 |            34.04 |
|    40 | Agent4               | 2026-05-15T11:04:32.920721+00:00 | 2026-05-15T11:05:39.995911+00:00 |            67.08 |
```
