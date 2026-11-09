# Wheel auto-trial report

## Summary

- Batch: `temperature-0.2`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 264.94 seconds
- Average total messages: 18.92
- Success rate: 10/50 (20.0%)
- Reconnect pauses: 2 across 2 trial(s); 4.01 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     203 |           203 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     187 |           187 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     116 |           183 |        63.4% (0.634) |                0.250 | 2.536 |                0.630 |
| wheel    | Agent3 | Agent2    |                  4 |      59 |           183 |        32.2% (0.322) |                0.250 | 1.290 |                0.322 |
| wheel    | Agent3 | Agent4    |                  4 |       2 |           183 |         1.1% (0.011) |                0.250 | 0.044 |                0.014 |
| wheel    | Agent3 | Agent5    |                  4 |       6 |           183 |         3.3% (0.033) |                0.250 | 0.131 |                0.035 |
| wheel    | Agent4 | Agent3    |                  1 |     162 |           162 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     210 |           210 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| wheel    | Agent3 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.2 | Fail    | cross                                       | asterisk       |             15 |         778.64 |           0 |             0.00 |
|     2 |         0.2 | Fail    | square                                      | diamond        |              7 |          47.16 |           0 |             0.00 |
|     3 |         0.2 | Fail    | asterisk                                    | circle         |             18 |         115.23 |           0 |             0.00 |
|     4 |         0.2 | Fail    | diamond                                     | square         |             13 |          83.51 |           0 |             0.00 |
|     5 |         0.2 | Fail    | triangle                                    | asterisk       |             10 |          66.50 |           0 |             0.00 |
|     6 |         0.2 | Fail    | triangle                                    | cross          |             23 |         143.74 |           0 |             0.00 |
|     7 |         0.2 | Fail    | cross                                       | circle         |             15 |         103.81 |           0 |             0.00 |
|     8 |         0.2 | Fail    | cross                                       | circle         |             17 |         189.34 |           0 |             0.00 |
|     9 |         0.2 | Fail    | square                                      | diamond        |             12 |          79.60 |           0 |             0.00 |
|    10 |         0.2 | Fail    | diamond                                     | triangle       |             22 |         148.58 |           0 |             0.00 |
|    11 |         0.2 | Fail    | cross                                       | square         |             19 |         294.86 |           0 |             0.00 |
|    12 |         0.2 | Success | square                                      | square         |             23 |         504.76 |           1 |             4.01 |
|    13 |         0.2 | Success | diamond                                     | diamond        |             38 |         233.56 |           0 |             0.00 |
|    14 |         0.2 | Fail    | triangle                                    | asterisk       |             10 |          60.94 |           0 |             0.00 |
|    15 |         0.2 | Fail    | circle                                      | cross          |             20 |         121.81 |           0 |             0.00 |
|    16 |         0.2 | Fail    | circle                                      | triangle       |             12 |         152.30 |           0 |             0.00 |
|    17 |         0.2 | Fail    | cross                                       | asterisk       |             23 |         145.51 |           0 |             0.00 |
|    18 |         0.2 | Fail    | square                                      | diamond        |              9 |          63.32 |           0 |             0.00 |
|    19 |         0.2 | Success | triangle                                    | triangle       |             15 |          96.59 |           0 |             0.00 |
|    20 |         0.2 | Fail    | square                                      | asterisk       |             43 |         268.20 |           0 |             0.00 |
|    21 |         0.2 | Fail    | cross                                       | square         |             11 |          82.50 |           0 |             0.00 |
|    22 |         0.2 | Fail    | cross                                       | triangle       |              9 |         167.18 |           0 |             0.00 |
|    23 |         0.2 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1751.09 |           0 |             0.00 |
|    24 |         0.2 | Fail    | diamond                                     | triangle       |             10 |          62.22 |           0 |             0.00 |
|    25 |         0.2 | Fail    | asterisk                                    | circle         |             11 |          70.56 |           0 |             0.00 |
|    26 |         0.2 | Success | triangle                                    | triangle       |             15 |          89.31 |           0 |             0.00 |
|    27 |         0.2 | Fail    | circle                                      | cross          |              9 |          57.26 |           0 |             0.00 |
|    28 |         0.2 | Success | diamond                                     | diamond        |             18 |         108.10 |           0 |             0.00 |
|    29 |         0.2 | Success | circle                                      | circle         |             18 |         105.68 |           0 |             0.00 |
|    30 |         0.2 | Fail    | circle                                      | square         |             14 |         183.18 |           0 |             0.00 |
|    31 |         0.2 | Success | cross                                       | cross          |             22 |         291.86 |           0 |             0.00 |
|    32 |         0.2 | Success | triangle                                    | triangle       |             15 |          87.68 |           0 |             0.00 |
|    33 |         0.2 | Fail    | triangle                                    | asterisk       |             17 |         134.27 |           0 |             0.00 |
|    34 |         0.2 | Fail    | diamond                                     | square         |             26 |        1349.04 |           0 |             0.00 |
|    35 |         0.2 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |         834.55 |           0 |             0.00 |
|    36 |         0.2 | Fail    | cross                                       | asterisk       |             10 |          67.35 |           0 |             0.00 |
|    37 |         0.2 | Fail    | circle                                      | asterisk       |             10 |          65.44 |           0 |             0.00 |
|    38 |         0.2 | Fail    | cross                                       | triangle       |             20 |         120.03 |           0 |             0.00 |
|    39 |         0.2 | Fail    | cross                                       | triangle       |             16 |         100.96 |           0 |             0.00 |
|    40 |         0.2 | Fail    | circle                                      | diamond        |             22 |         141.61 |           0 |             0.00 |
|    41 |         0.2 | Success | circle                                      | circle         |             25 |         232.46 |           0 |             0.00 |
|    42 |         0.2 | Fail    | square                                      | circle         |             33 |         194.94 |           0 |             0.00 |
|    43 |         0.2 | Fail    | cross                                       | asterisk       |             13 |          83.01 |           0 |             0.00 |
|    44 |         0.2 | Fail    | triangle                                    | square         |              9 |         122.42 |           0 |             0.00 |
|    45 |         0.2 | Fail    | circle                                      | asterisk       |             12 |         194.44 |           0 |             0.00 |
|    46 |         0.2 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        1874.16 |           1 |             0.00 |
|    47 |         0.2 | Fail    | diamond                                     | cross          |             23 |         702.94 |           0 |             0.00 |
|    48 |         0.2 | Fail    | triangle                                    | square         |             12 |          79.20 |           0 |             0.00 |
|    49 |         0.2 | Success | diamond                                     | diamond        |             11 |          70.88 |           0 |             0.00 |
|    50 |         0.2 | Fail    | circle                                      | triangle       |             21 |         124.73 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    12 | Agent1               | 2026-05-15T12:10:04.504807+00:00 | 2026-05-15T12:10:08.511346+00:00 |             4.01 |
|    46 | Agent2               | 2026-05-15T14:38:48.647896+00:00 | 2026-05-15T14:38:48.650374+00:00 |             0.00 |
```
