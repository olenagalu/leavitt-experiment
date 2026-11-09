# Chain auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 221.85 seconds
- Average total messages: 16.90
- Success rate: 9/50 (18.0%)
- Reconnect pauses: 1 across 1 trial(s); 51.06 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     194 |           194 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     155 |           170 |        91.2% (0.912) |                0.500 | 1.824 |                0.909 |
| chain    | Agent2 | Agent3    |                  2 |      15 |           170 |         8.8% (0.088) |                0.500 | 0.176 |                0.091 |
| chain    | Agent3 | Agent2    |                  2 |     185 |           197 |        93.9% (0.939) |                0.500 | 1.878 |                0.937 |
| chain    | Agent3 | Agent4    |                  2 |      12 |           197 |         6.1% (0.061) |                0.500 | 0.122 |                0.063 |
| chain    | Agent4 | Agent3    |                  2 |      85 |           167 |        50.9% (0.509) |                0.500 | 1.018 |                0.509 |
| chain    | Agent4 | Agent5    |                  2 |      82 |           167 |        49.1% (0.491) |                0.500 | 0.982 |                0.491 |
| chain    | Agent5 | Agent4    |                  1 |     116 |           116 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| chain    | Agent3 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Fail    | square                                      | asterisk       |             16 |         277.83 |           0 |             0.00 |
|     2 |           0 | Fail    | square                                      | triangle       |             20 |         113.02 |           0 |             0.00 |
|     3 |           0 | Fail    | diamond                                     | asterisk       |             10 |          58.57 |           0 |             0.00 |
|     4 |           0 | Success | diamond                                     | diamond        |             10 |          60.17 |           0 |             0.00 |
|     5 |           0 | Success | circle                                      | circle         |             10 |          58.94 |           0 |             0.00 |
|     6 |           0 | Fail    | triangle                                    | square         |              8 |          46.84 |           0 |             0.00 |
|     7 |           0 | Fail    | square                                      | triangle       |             17 |          99.46 |           0 |             0.00 |
|     8 |           0 | Fail    | circle                                      | triangle       |             11 |          65.77 |           0 |             0.00 |
|     9 |           0 | Fail    | cross                                       | circle         |             18 |         105.53 |           0 |             0.00 |
|    10 |           0 | Fail    | asterisk                                    | diamond        |             14 |          80.78 |           0 |             0.00 |
|    11 |           0 | Fail    | circle                                      | cross          |              9 |          60.84 |           0 |             0.00 |
|    12 |           0 | Fail    | square                                      | asterisk       |             19 |         329.93 |           0 |             0.00 |
|    13 |           0 | Fail    | diamond                                     | cross          |             15 |         220.89 |           0 |             0.00 |
|    14 |           0 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |         937.44 |           0 |             0.00 |
|    15 |           0 | Fail    | circle                                      | square         |             40 |        1294.08 |           0 |             0.00 |
|    16 |           0 | Fail    | square                                      | diamond        |             18 |         139.75 |           0 |             0.00 |
|    17 |           0 | Fail    | square                                      | diamond        |             11 |          64.94 |           0 |             0.00 |
|    18 |           0 | Fail    | asterisk                                    | diamond        |              8 |          46.90 |           0 |             0.00 |
|    19 |           0 | Fail    | triangle                                    | cross          |             10 |          58.73 |           0 |             0.00 |
|    20 |           0 | Fail    | cross                                       | square         |             20 |         116.19 |           0 |             0.00 |
|    21 |           0 | Fail    | circle                                      | triangle       |             29 |         158.32 |           0 |             0.00 |
|    22 |           0 | Success | circle                                      | circle         |             14 |          82.90 |           0 |             0.00 |
|    23 |           0 | Fail    | asterisk                                    | cross          |              9 |          53.76 |           0 |             0.00 |
|    24 |           0 | Success | cross                                       | cross          |             22 |         123.75 |           0 |             0.00 |
|    25 |           0 | Fail    | cross                                       | square         |             10 |          61.04 |           0 |             0.00 |
|    26 |           0 | Success | triangle                                    | triangle       |             15 |         210.69 |           0 |             0.00 |
|    27 |           0 | Fail    | square                                      | asterisk       |             22 |        1653.79 |           0 |             0.00 |
|    28 |           0 | Fail    | cross                                       | diamond        |             26 |         504.76 |           0 |             0.00 |
|    29 |           0 | Fail    | diamond                                     | triangle       |             11 |          64.92 |           0 |             0.00 |
|    30 |           0 | Fail    | circle                                      | triangle       |             10 |          58.86 |           0 |             0.00 |
|    31 |           0 | Fail    | diamond                                     | circle         |              6 |          35.20 |           0 |             0.00 |
|    32 |           0 | Fail    | circle                                      | square         |             21 |         119.71 |           0 |             0.00 |
|    33 |           0 | Success | circle                                      | circle         |             13 |          77.08 |           0 |             0.00 |
|    34 |           0 | Fail    | circle                                      | square         |             11 |          66.36 |           0 |             0.00 |
|    35 |           0 | Fail    | square                                      | asterisk       |             24 |         138.95 |           0 |             0.00 |
|    36 |           0 | Fail    | diamond                                     | cross          |             14 |          81.05 |           0 |             0.00 |
|    37 |           0 | Fail    | diamond                                     | asterisk       |             16 |          96.22 |           0 |             0.00 |
|    38 |           0 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        1450.09 |           0 |             0.00 |
|    39 |           0 | Fail    | diamond                                     | square         |             15 |          89.79 |           0 |             0.00 |
|    40 |           0 | Success | cross                                       | cross          |             20 |         113.81 |           0 |             0.00 |
|    41 |           0 | Fail    | triangle                                    | cross          |             21 |         114.82 |           0 |             0.00 |
|    42 |           0 | Fail    | triangle                                    | asterisk       |             13 |          76.45 |           0 |             0.00 |
|    43 |           0 | Fail    | diamond                                     | asterisk       |             10 |          58.02 |           0 |             0.00 |
|    44 |           0 | Fail    | triangle                                    | diamond        |             17 |         100.33 |           0 |             0.00 |
|    45 |           0 | Fail    | triangle                                    | cross          |             17 |         105.34 |           0 |             0.00 |
|    46 |           0 | Fail    | cross                                       | triangle       |             12 |          70.99 |           0 |             0.00 |
|    47 |           0 | Success | circle                                      | circle         |              7 |          60.36 |           0 |             0.00 |
|    48 |           0 | Success | cross                                       | cross          |             25 |         422.28 |           0 |             0.00 |
|    49 |           0 | Fail    | diamond                                     | asterisk       |              8 |         292.79 |           0 |             0.00 |
|    50 |           0 | Fail    | diamond                                     | cross          |             23 |         313.71 |           1 |            51.06 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    50 | Agent3               | 2026-05-13T18:10:06.405247+00:00 | 2026-05-13T18:10:57.466753+00:00 |            51.06 |
```
