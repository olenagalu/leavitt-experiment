# Circle auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 159.27 seconds
- Average total messages: 14.44
- Success rate: 8/50 (16.0%)
- Reconnect pauses: 2 across 2 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      33 |           121 |        27.3% (0.273) |                0.500 | 0.545 |                0.275 |
| circle   | Agent1 | Agent5    |                  2 |      88 |           121 |        72.7% (0.727) |                0.500 | 1.455 |                0.725 |
| circle   | Agent2 | Agent1    |                  2 |     142 |           159 |        89.3% (0.893) |                0.500 | 1.786 |                0.891 |
| circle   | Agent2 | Agent3    |                  2 |      17 |           159 |        10.7% (0.107) |                0.500 | 0.214 |                0.109 |
| circle   | Agent3 | Agent2    |                  2 |     132 |           139 |        95.0% (0.950) |                0.500 | 1.899 |                0.946 |
| circle   | Agent3 | Agent4    |                  2 |       7 |           139 |         5.0% (0.050) |                0.500 | 0.101 |                0.054 |
| circle   | Agent4 | Agent3    |                  2 |     122 |           158 |        77.2% (0.772) |                0.500 | 1.544 |                0.770 |
| circle   | Agent4 | Agent5    |                  2 |      36 |           158 |        22.8% (0.228) |                0.500 | 0.456 |                0.230 |
| circle   | Agent5 | Agent1    |                  2 |      57 |           145 |        39.3% (0.393) |                0.500 | 0.786 |                0.394 |
| circle   | Agent5 | Agent4    |                  2 |      88 |           145 |        60.7% (0.607) |                0.500 | 1.214 |                0.606 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           1 | Fail    | triangle         | cross          |             10 |         276.56 |           0 |             0.00 |
|     2 |           1 | Fail    | square           | triangle       |              8 |          47.57 |           0 |             0.00 |
|     3 |           1 | Fail    | diamond          | circle         |             15 |          85.51 |           0 |             0.00 |
|     4 |           1 | Fail    | triangle         | square         |             23 |         135.27 |           0 |             0.00 |
|     5 |           1 | Success | circle           | circle         |              8 |          44.56 |           0 |             0.00 |
|     6 |           1 | Fail    | cross            | triangle       |             13 |          77.00 |           0 |             0.00 |
|     7 |           1 | Fail    | square           | asterisk       |             18 |         106.00 |           0 |             0.00 |
|     8 |           1 | Fail    | square           | diamond        |              5 |          27.99 |           0 |             0.00 |
|     9 |           1 | Success | diamond          | diamond        |              6 |          37.23 |           0 |             0.00 |
|    10 |           1 | Fail    | diamond          | circle         |             21 |         123.54 |           0 |             0.00 |
|    11 |           1 | Fail    | circle           | asterisk       |             18 |         106.93 |           0 |             0.00 |
|    12 |           1 | Success | square           | square         |              5 |          29.63 |           0 |             0.00 |
|    13 |           1 | Fail    | diamond          | square         |             10 |         584.07 |           1 |             0.00 |
|    14 |           1 | Fail    | asterisk         | diamond        |             13 |         236.23 |           0 |             0.00 |
|    15 |           1 | Fail    | diamond          | circle         |              7 |          40.15 |           0 |             0.00 |
|    16 |           1 | Fail    | diamond          | cross          |             15 |          88.19 |           0 |             0.00 |
|    17 |           1 | Fail    | asterisk         | square         |             21 |         119.14 |           0 |             0.00 |
|    18 |           1 | Fail    | asterisk         | diamond        |              6 |          34.75 |           0 |             0.00 |
|    19 |           1 | Fail    | diamond          | cross          |             13 |          77.63 |           0 |             0.00 |
|    20 |           1 | Fail    | circle           | diamond        |              8 |          46.56 |           0 |             0.00 |
|    21 |           1 | Fail    | diamond          | cross          |              5 |          29.91 |           0 |             0.00 |
|    22 |           1 | Fail    | asterisk         | square         |             13 |          76.67 |           0 |             0.00 |
|    23 |           1 | Fail    | circle           | diamond        |             12 |          81.33 |           0 |             0.00 |
|    24 |           1 | Fail    | asterisk         | circle         |             18 |         199.12 |           0 |             0.00 |
|    25 |           1 | Fail    | cross            | square         |             12 |          83.61 |           0 |             0.00 |
|    26 |           1 | Success | square           | square         |              6 |         454.27 |           1 |             0.00 |
|    27 |           1 | Fail    | circle           | asterisk       |             32 |         564.32 |           0 |             0.00 |
|    28 |           1 | Success | square           | square         |             17 |          98.43 |           0 |             0.00 |
|    29 |           1 | Fail    | cross            | asterisk       |             20 |         111.08 |           0 |             0.00 |
|    30 |           1 | Fail    | square           | diamond        |             36 |         203.88 |           0 |             0.00 |
|    31 |           1 | Fail    | cross            | triangle       |              8 |          48.17 |           0 |             0.00 |
|    32 |           1 | Success | square           | square         |             17 |          98.91 |           0 |             0.00 |
|    33 |           1 | Success | triangle         | triangle       |             19 |         109.83 |           0 |             0.00 |
|    34 |           1 | Fail    | circle           | triangle       |             26 |         154.05 |           0 |             0.00 |
|    35 |           1 | Fail    | square           | diamond        |             18 |         105.25 |           0 |             0.00 |
|    36 |           1 | Fail    | circle           | square         |             29 |        1392.20 |           0 |             0.00 |
|    37 |           1 | Fail    | diamond          | square         |              9 |         154.47 |           0 |             0.00 |
|    38 |           1 | Fail    | asterisk         | diamond        |             12 |          67.97 |           0 |             0.00 |
|    39 |           1 | Fail    | cross            | square         |             21 |         122.98 |           0 |             0.00 |
|    40 |           1 | Fail    | square           | asterisk       |             22 |         123.50 |           0 |             0.00 |
|    41 |           1 | Success | triangle         | triangle       |              4 |          23.19 |           0 |             0.00 |
|    42 |           1 | Fail    | circle           | asterisk       |              5 |          30.56 |           0 |             0.00 |
|    43 |           1 | Fail    | diamond          | asterisk       |             27 |         150.02 |           0 |             0.00 |
|    44 |           1 | Fail    | square           | asterisk       |              9 |          54.53 |           0 |             0.00 |
|    45 |           1 | Fail    | diamond          | square         |             17 |         100.23 |           0 |             0.00 |
|    46 |           1 | Fail    | cross            | diamond        |              9 |          64.92 |           0 |             0.00 |
|    47 |           1 | Fail    | circle           | asterisk       |             18 |         607.99 |           0 |             0.00 |
|    48 |           1 | Fail    | asterisk         | cross          |             11 |          77.68 |           0 |             0.00 |
|    49 |           1 | Fail    | cross            | circle         |             14 |         117.72 |           0 |             0.00 |
|    50 |           1 | Fail    | square           | cross          |             13 |         132.36 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    13 | Agent5               | 2026-05-13T12:43:44.965515+00:00 | 2026-05-13T12:43:44.969501+00:00 |             0.00 |
|    26 | Agent3               | 2026-05-13T13:10:46.302414+00:00 | 2026-05-13T13:10:46.304590+00:00 |             0.00 |
```
