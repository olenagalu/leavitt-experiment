# Y topology auto-trial report

## Summary

- Batch: `temperature-0.05`
- Temperature: 0.05
- Completed trials: 50/50
- Average time: 178.59 seconds
- Average total messages: 18.50
- Success rate: 10/50 (20.0%)
- Reconnect pauses: 2 across 2 trial(s); 1.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     145 |           145 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     197 |           197 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      80 |           200 |        40.0% (0.400) |                0.333 | 1.200 |                0.400 |
| y        | Agent3 | Agent2    |                  3 |      79 |           200 |        39.5% (0.395) |                0.333 | 1.185 |                0.395 |
| y        | Agent3 | Agent4    |                  3 |      41 |           200 |        20.5% (0.205) |                0.333 | 0.615 |                0.206 |
| y        | Agent4 | Agent3    |                  2 |     167 |           184 |        90.8% (0.908) |                0.500 | 1.815 |                0.905 |
| y        | Agent4 | Agent5    |                  2 |      17 |           184 |         9.2% (0.092) |                0.500 | 0.185 |                0.095 |
| y        | Agent5 | Agent4    |                  1 |     194 |           194 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent1 | client_assigned |     1 |
| y        | Agent2 | client_assigned |     2 |
| y        | Agent3 | client_assigned |     2 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |        0.05 | Fail    | cross            | triangle       |             14 |         337.58 |           0 |             0.00 |
|     2 |        0.05 | Fail    | triangle         | square         |             38 |         215.11 |           0 |             0.00 |
|     3 |        0.05 | Success | circle           | circle         |             14 |          83.15 |           0 |             0.00 |
|     4 |        0.05 | Fail    | square           | diamond        |             36 |         202.19 |           0 |             0.00 |
|     5 |        0.05 | Fail    | cross            | square         |             19 |         112.03 |           0 |             0.00 |
|     6 |        0.05 | Fail    | circle           | triangle       |             24 |         137.16 |           0 |             0.00 |
|     7 |        0.05 | Fail    | circle           | square         |             19 |         113.10 |           0 |             0.00 |
|     8 |        0.05 | Fail    | circle           | square         |             17 |         105.15 |           0 |             0.00 |
|     9 |        0.05 | Fail    | diamond          | triangle       |             14 |         540.45 |           0 |             0.00 |
|    10 |        0.05 | Fail    | diamond          | asterisk       |             18 |         468.86 |           0 |             0.00 |
|    11 |        0.05 | Fail    | circle           | cross          |             29 |         162.27 |           0 |             0.00 |
|    12 |        0.05 | Fail    | circle           | diamond        |             29 |         161.14 |           0 |             0.00 |
|    13 |        0.05 | Fail    | cross            | circle         |             14 |          79.74 |           0 |             0.00 |
|    14 |        0.05 | Success | asterisk         | asterisk       |             16 |          96.10 |           0 |             0.00 |
|    15 |        0.05 | Fail    | asterisk         | circle         |             15 |          86.05 |           0 |             0.00 |
|    16 |        0.05 | Fail    | cross            | square         |             21 |         121.50 |           0 |             0.00 |
|    17 |        0.05 | Fail    | asterisk         | diamond        |              8 |          49.29 |           0 |             0.00 |
|    18 |        0.05 | Success | triangle         | triangle       |             14 |          86.37 |           0 |             0.00 |
|    19 |        0.05 | Fail    | asterisk         | triangle       |             25 |         635.63 |           1 |             0.00 |
|    20 |        0.05 | Success | circle           | circle         |             15 |         296.89 |           0 |             0.00 |
|    21 |        0.05 | Fail    | square           | asterisk       |             10 |         140.57 |           0 |             0.00 |
|    22 |        0.05 | Fail    | asterisk         | triangle       |             15 |          87.69 |           0 |             0.00 |
|    23 |        0.05 | Success | square           | square         |              9 |          56.19 |           0 |             0.00 |
|    24 |        0.05 | Fail    | diamond          | asterisk       |             13 |          76.54 |           0 |             0.00 |
|    25 |        0.05 | Fail    | circle           | triangle       |             22 |         128.14 |           0 |             0.00 |
|    26 |        0.05 | Fail    | asterisk         | circle         |             36 |         206.51 |           0 |             0.00 |
|    27 |        0.05 | Fail    | diamond          | circle         |             12 |         108.84 |           0 |             0.00 |
|    28 |        0.05 | Fail    | cross            | square         |             17 |         182.88 |           0 |             0.00 |
|    29 |        0.05 | Fail    | triangle         | circle         |             17 |         102.57 |           0 |             0.00 |
|    30 |        0.05 | Success | cross            | cross          |             37 |         694.49 |           1 |             1.00 |
|    31 |        0.05 | Fail    | cross            | asterisk       |             15 |         140.29 |           0 |             0.00 |
|    32 |        0.05 | Success | cross            | cross          |             12 |         247.24 |           0 |             0.00 |
|    33 |        0.05 | Success | square           | square         |             19 |         183.50 |           0 |             0.00 |
|    34 |        0.05 | Fail    | triangle         | square         |             15 |          90.23 |           0 |             0.00 |
|    35 |        0.05 | Fail    | square           | triangle       |             15 |          89.37 |           0 |             0.00 |
|    36 |        0.05 | Fail    | square           | circle         |             26 |         171.76 |           0 |             0.00 |
|    37 |        0.05 | Fail    | cross            | square         |             22 |         195.95 |           0 |             0.00 |
|    38 |        0.05 | Fail    | cross            | diamond        |             16 |          92.68 |           0 |             0.00 |
|    39 |        0.05 | Fail    | circle           | diamond        |             19 |         109.33 |           0 |             0.00 |
|    40 |        0.05 | Fail    | triangle         | diamond        |             13 |          75.53 |           0 |             0.00 |
|    41 |        0.05 | Fail    | cross            | triangle       |              8 |          67.84 |           0 |             0.00 |
|    42 |        0.05 | Fail    | circle           | diamond        |             18 |         518.25 |           0 |             0.00 |
|    43 |        0.05 | Success | cross            | cross          |             19 |         201.52 |           0 |             0.00 |
|    44 |        0.05 | Success | asterisk         | asterisk       |             10 |         117.21 |           0 |             0.00 |
|    45 |        0.05 | Fail    | cross            | diamond        |             25 |         144.19 |           0 |             0.00 |
|    46 |        0.05 | Fail    | square           | asterisk       |             16 |         106.02 |           0 |             0.00 |
|    47 |        0.05 | Fail    | diamond          | triangle       |             16 |         163.88 |           0 |             0.00 |
|    48 |        0.05 | Fail    | square           | circle         |             18 |         104.54 |           0 |             0.00 |
|    49 |        0.05 | Fail    | circle           | triangle       |             21 |         121.59 |           0 |             0.00 |
|    50 |        0.05 | Fail    | cross            | triangle       |             15 |         114.32 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    19 | Agent4               | 2026-05-14T11:55:20.478570+00:00 | 2026-05-14T11:55:20.480512+00:00 |             0.00 |
|    30 | Agent4               | 2026-05-14T12:32:58.528222+00:00 | 2026-05-14T12:32:59.531338+00:00 |             1.00 |
```
