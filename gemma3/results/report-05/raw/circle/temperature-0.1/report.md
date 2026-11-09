# Circle auto-trial report

## Summary

- Batch: `temperature-0.1`
- Temperature: 0.1
- Completed trials: 50/50
- Average time: 163.34 seconds
- Average total messages: 15.18
- Success rate: 17/50 (34.0%)
- Reconnect pauses: 2 across 2 trial(s); 3.01 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      40 |           145 |        27.6% (0.276) |                0.500 | 0.552 |                0.277 |
| circle   | Agent1 | Agent5    |                  2 |     105 |           145 |        72.4% (0.724) |                0.500 | 1.448 |                0.723 |
| circle   | Agent2 | Agent1    |                  2 |     132 |           149 |        88.6% (0.886) |                0.500 | 1.772 |                0.883 |
| circle   | Agent2 | Agent3    |                  2 |      17 |           149 |        11.4% (0.114) |                0.500 | 0.228 |                0.117 |
| circle   | Agent3 | Agent2    |                  2 |     142 |           144 |        98.6% (0.986) |                0.500 | 1.972 |                0.983 |
| circle   | Agent3 | Agent4    |                  2 |       2 |           144 |         1.4% (0.014) |                0.500 | 0.028 |                0.017 |
| circle   | Agent4 | Agent3    |                  2 |     137 |           167 |        82.0% (0.820) |                0.500 | 1.641 |                0.818 |
| circle   | Agent4 | Agent5    |                  2 |      30 |           167 |        18.0% (0.180) |                0.500 | 0.359 |                0.182 |
| circle   | Agent5 | Agent1    |                  2 |      60 |           154 |        39.0% (0.390) |                0.500 | 0.779 |                0.390 |
| circle   | Agent5 | Agent4    |                  2 |      94 |           154 |        61.0% (0.610) |                0.500 | 1.221 |                0.610 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.1 | Fail    | cross            | diamond        |              9 |         206.57 |           0 |             0.00 |
|     2 |         0.1 | Success | cross            | cross          |              5 |          78.01 |           0 |             0.00 |
|     3 |         0.1 | Fail    | cross            | diamond        |             11 |          61.59 |           0 |             0.00 |
|     4 |         0.1 | Success | triangle         | triangle       |              5 |          29.77 |           0 |             0.00 |
|     5 |         0.1 | Success | asterisk         | asterisk       |             11 |          63.99 |           0 |             0.00 |
|     6 |         0.1 | Success | circle           | circle         |             17 |          96.57 |           0 |             0.00 |
|     7 |         0.1 | Fail    | diamond          | asterisk       |             23 |         128.39 |           0 |             0.00 |
|     8 |         0.1 | Success | circle           | circle         |              6 |          36.55 |           0 |             0.00 |
|     9 |         0.1 | Fail    | triangle         | square         |             17 |          94.77 |           0 |             0.00 |
|    10 |         0.1 | Success | square           | square         |             16 |          92.49 |           0 |             0.00 |
|    11 |         0.1 | Fail    | square           | asterisk       |             12 |          71.29 |           0 |             0.00 |
|    12 |         0.1 | Fail    | triangle         | cross          |             18 |         226.79 |           0 |             0.00 |
|    13 |         0.1 | Fail    | diamond          | square         |             10 |         402.67 |           0 |             0.00 |
|    14 |         0.1 | Fail    | asterisk         | triangle       |             19 |         385.77 |           0 |             0.00 |
|    15 |         0.1 | Success | triangle         | triangle       |             19 |         486.04 |           0 |             0.00 |
|    16 |         0.1 | Success | cross            | cross          |             12 |          69.46 |           0 |             0.00 |
|    17 |         0.1 | Fail    | asterisk         | circle         |              4 |          24.28 |           0 |             0.00 |
|    18 |         0.1 | Fail    | square           | asterisk       |             14 |          81.64 |           0 |             0.00 |
|    19 |         0.1 | Fail    | square           | asterisk       |             16 |          93.50 |           0 |             0.00 |
|    20 |         0.1 | Fail    | triangle         | asterisk       |             13 |          75.10 |           0 |             0.00 |
|    21 |         0.1 | Fail    | square           | asterisk       |             16 |          93.65 |           0 |             0.00 |
|    22 |         0.1 | Fail    | circle           | square         |             25 |         143.76 |           0 |             0.00 |
|    23 |         0.1 | Fail    | circle           | cross          |             20 |         405.57 |           0 |             0.00 |
|    24 |         0.1 | Success | cross            | cross          |             20 |         383.95 |           1 |             3.01 |
|    25 |         0.1 | Success | circle           | circle         |             11 |          84.81 |           0 |             0.00 |
|    26 |         0.1 | Fail    | diamond          | cross          |             34 |         614.71 |           0 |             0.00 |
|    27 |         0.1 | Success | asterisk         | asterisk       |              8 |          47.55 |           0 |             0.00 |
|    28 |         0.1 | Fail    | cross            | diamond        |             24 |         139.28 |           0 |             0.00 |
|    29 |         0.1 | Success | diamond          | diamond        |             28 |         159.31 |           0 |             0.00 |
|    30 |         0.1 | Success | square           | square         |             17 |          99.00 |           0 |             0.00 |
|    31 |         0.1 | Success | cross            | cross          |             24 |         138.93 |           0 |             0.00 |
|    32 |         0.1 | Fail    | cross            | asterisk       |              7 |          39.99 |           0 |             0.00 |
|    33 |         0.1 | Fail    | asterisk         | square         |             18 |         109.34 |           0 |             0.00 |
|    34 |         0.1 | Fail    | circle           | triangle       |              9 |          88.36 |           0 |             0.00 |
|    35 |         0.1 | Fail    | square           | diamond        |              3 |          28.40 |           0 |             0.00 |
|    36 |         0.1 | Fail    | triangle         | square         |             21 |         200.84 |           0 |             0.00 |
|    37 |         0.1 | Fail    | asterisk         | square         |             19 |         513.32 |           0 |             0.00 |
|    38 |         0.1 | Fail    | cross            | asterisk       |              8 |          47.57 |           0 |             0.00 |
|    39 |         0.1 | Success | square           | square         |             18 |         499.68 |           0 |             0.00 |
|    40 |         0.1 | Fail    | triangle         | square         |              8 |         149.98 |           1 |             0.00 |
|    41 |         0.1 | Fail    | triangle         | diamond        |             25 |         138.52 |           0 |             0.00 |
|    42 |         0.1 | Fail    | asterisk         | cross          |              7 |          41.32 |           0 |             0.00 |
|    43 |         0.1 | Fail    | asterisk         | circle         |             11 |          64.01 |           0 |             0.00 |
|    44 |         0.1 | Success | cross            | cross          |             15 |          88.60 |           0 |             0.00 |
|    45 |         0.1 | Fail    | asterisk         | cross          |             11 |          66.22 |           0 |             0.00 |
|    46 |         0.1 | Fail    | square           | asterisk       |             12 |          74.77 |           0 |             0.00 |
|    47 |         0.1 | Fail    | circle           | asterisk       |             14 |         241.88 |           0 |             0.00 |
|    48 |         0.1 | Fail    | square           | asterisk       |             21 |         333.46 |           0 |             0.00 |
|    49 |         0.1 | Fail    | cross            | asterisk       |             13 |         117.78 |           0 |             0.00 |
|    50 |         0.1 | Success | square           | square         |             35 |         207.05 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    24 | Agent4               | 2026-05-13T08:17:33.770774+00:00 | 2026-05-13T08:17:36.776158+00:00 |             3.01 |
|    40 | Agent3               | 2026-05-13T09:10:19.553652+00:00 | 2026-05-13T09:10:19.555341+00:00 |             0.00 |
```
