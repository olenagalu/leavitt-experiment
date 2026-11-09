# Circle auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 172.76 seconds
- Average total messages: 14.30
- Success rate: 17/50 (34.0%)
- Reconnect pauses: 1 across 1 trial(s); 11.01 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      40 |           135 |        29.6% (0.296) |                0.500 | 0.593 |                0.298 |
| circle   | Agent1 | Agent5    |                  2 |      95 |           135 |        70.4% (0.704) |                0.500 | 1.407 |                0.702 |
| circle   | Agent2 | Agent1    |                  2 |     122 |           136 |        89.7% (0.897) |                0.500 | 1.794 |                0.894 |
| circle   | Agent2 | Agent3    |                  2 |      14 |           136 |        10.3% (0.103) |                0.500 | 0.206 |                0.106 |
| circle   | Agent3 | Agent2    |                  2 |     146 |           151 |        96.7% (0.967) |                0.500 | 1.934 |                0.964 |
| circle   | Agent3 | Agent4    |                  2 |       5 |           151 |         3.3% (0.033) |                0.500 | 0.066 |                0.036 |
| circle   | Agent4 | Agent3    |                  2 |     135 |           156 |        86.5% (0.865) |                0.500 | 1.731 |                0.863 |
| circle   | Agent4 | Agent5    |                  2 |      21 |           156 |        13.5% (0.135) |                0.500 | 0.269 |                0.137 |
| circle   | Agent5 | Agent1    |                  2 |      61 |           137 |        44.5% (0.445) |                0.500 | 0.891 |                0.446 |
| circle   | Agent5 | Agent4    |                  2 |      76 |           137 |        55.5% (0.555) |                0.500 | 1.109 |                0.554 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Success | cross            | cross          |             20 |         256.50 |           0 |             0.00 |
|     2 |           0 | Success | asterisk         | asterisk       |             15 |          83.35 |           0 |             0.00 |
|     3 |           0 | Fail    | square           | diamond        |              8 |          46.99 |           0 |             0.00 |
|     4 |           0 | Fail    | circle           | cross          |             11 |          63.96 |           0 |             0.00 |
|     5 |           0 | Fail    | cross            | asterisk       |             22 |         124.72 |           0 |             0.00 |
|     6 |           0 | Success | circle           | circle         |              7 |          42.53 |           0 |             0.00 |
|     7 |           0 | Success | triangle         | triangle       |             19 |         106.90 |           0 |             0.00 |
|     8 |           0 | Fail    | square           | diamond        |             14 |          78.21 |           0 |             0.00 |
|     9 |           0 | Fail    | diamond          | asterisk       |             24 |         138.02 |           0 |             0.00 |
|    10 |           0 | Fail    | triangle         | square         |             23 |         168.88 |           0 |             0.00 |
|    11 |           0 | Success | circle           | circle         |             10 |         414.73 |           0 |             0.00 |
|    12 |           0 | Fail    | triangle         | square         |              8 |         103.23 |           0 |             0.00 |
|    13 |           0 | Fail    | square           | asterisk       |             10 |          64.76 |           0 |             0.00 |
|    14 |           0 | Fail    | diamond          | asterisk       |              8 |          49.64 |           0 |             0.00 |
|    15 |           0 | Fail    | cross            | triangle       |             21 |         219.99 |           0 |             0.00 |
|    16 |           0 | Fail    | cross            | diamond        |             10 |          56.50 |           0 |             0.00 |
|    17 |           0 | Fail    | square           | circle         |             22 |         124.74 |           0 |             0.00 |
|    18 |           0 | Success | square           | square         |             11 |          61.38 |           0 |             0.00 |
|    19 |           0 | Fail    | circle           | square         |             10 |          58.30 |           0 |             0.00 |
|    20 |           0 | Success | square           | square         |             20 |         114.41 |           0 |             0.00 |
|    21 |           0 | Success | asterisk         | asterisk       |             35 |         221.23 |           0 |             0.00 |
|    22 |           0 | Fail    | triangle         | asterisk       |              7 |         121.86 |           0 |             0.00 |
|    23 |           0 | Success | circle           | circle         |             16 |         123.85 |           0 |             0.00 |
|    24 |           0 | Fail    | triangle         | asterisk       |             13 |         292.52 |           0 |             0.00 |
|    25 |           0 | Fail    | diamond          | triangle       |             19 |         494.26 |           0 |             0.00 |
|    26 |           0 | Success | triangle         | triangle       |             16 |         281.90 |           0 |             0.00 |
|    27 |           0 | Fail    | triangle         | diamond        |             14 |         174.21 |           0 |             0.00 |
|    28 |           0 | Fail    | triangle         | circle         |             32 |         235.74 |           0 |             0.00 |
|    29 |           0 | Fail    | diamond          | circle         |             15 |          88.23 |           0 |             0.00 |
|    30 |           0 | Success | circle           | circle         |              9 |          49.86 |           0 |             0.00 |
|    31 |           0 | Fail    | circle           | cross          |             16 |          94.77 |           0 |             0.00 |
|    32 |           0 | Success | cross            | cross          |              7 |          50.73 |           0 |             0.00 |
|    33 |           0 | Fail    | circle           | asterisk       |             12 |         185.74 |           0 |             0.00 |
|    34 |           0 | Fail    | triangle         | diamond        |             15 |         219.72 |           0 |             0.00 |
|    35 |           0 | Fail    | diamond          | circle         |             10 |         280.33 |           0 |             0.00 |
|    36 |           0 | Fail    | asterisk         | diamond        |             11 |         163.26 |           0 |             0.00 |
|    37 |           0 | Fail    | circle           | diamond        |             36 |         851.27 |           1 |            11.01 |
|    38 |           0 | Fail    | asterisk         | square         |             12 |          67.85 |           0 |             0.00 |
|    39 |           0 | Fail    | triangle         | cross          |             19 |         106.34 |           0 |             0.00 |
|    40 |           0 | Success | circle           | circle         |             12 |          68.65 |           0 |             0.00 |
|    41 |           0 | Fail    | asterisk         | circle         |             13 |          75.90 |           0 |             0.00 |
|    42 |           0 | Success | asterisk         | asterisk       |             15 |          88.31 |           0 |             0.00 |
|    43 |           0 | Fail    | square           | asterisk       |             20 |         117.34 |           0 |             0.00 |
|    44 |           0 | Fail    | cross            | triangle       |              5 |          30.86 |           0 |             0.00 |
|    45 |           0 | Success | cross            | cross          |              8 |          45.31 |           0 |             0.00 |
|    46 |           0 | Success | diamond          | diamond        |              7 |         138.90 |           0 |             0.00 |
|    47 |           0 | Success | diamond          | diamond        |              8 |         640.21 |           0 |             0.00 |
|    48 |           0 | Fail    | asterisk         | triangle       |              5 |         399.86 |           0 |             0.00 |
|    49 |           0 | Fail    | triangle         | diamond        |             11 |         437.09 |           0 |             0.00 |
|    50 |           0 | Fail    | square           | diamond        |              4 |         114.20 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    37 | Agent5               | 2026-05-13T02:42:50.817197+00:00 | 2026-05-13T02:43:01.830806+00:00 |            11.01 |
```
