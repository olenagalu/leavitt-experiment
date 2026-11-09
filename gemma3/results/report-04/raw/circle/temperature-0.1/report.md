# Circle auto-trial report

## Summary

- Batch: `temperature-0.1`
- Temperature: 0.1
- Completed trials: 50/50
- Average time: 173.60 seconds
- Average total messages: 16.28
- Success rate: 14/50 (28.0%)
- Reconnect pauses: 1 across 1 trial(s); 53.06 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      61 |           158 |        38.6% (0.386) |                0.500 | 0.772 |                0.387 |
| circle   | Agent1 | Agent5    |                  2 |      97 |           158 |        61.4% (0.614) |                0.500 | 1.228 |                0.613 |
| circle   | Agent2 | Agent1    |                  2 |     158 |           167 |        94.6% (0.946) |                0.500 | 1.892 |                0.943 |
| circle   | Agent2 | Agent3    |                  2 |       9 |           167 |         5.4% (0.054) |                0.500 | 0.108 |                0.057 |
| circle   | Agent3 | Agent2    |                  2 |     154 |           162 |        95.1% (0.951) |                0.500 | 1.901 |                0.948 |
| circle   | Agent3 | Agent4    |                  2 |       8 |           162 |         4.9% (0.049) |                0.500 | 0.099 |                0.052 |
| circle   | Agent4 | Agent3    |                  2 |     144 |           169 |        85.2% (0.852) |                0.500 | 1.704 |                0.850 |
| circle   | Agent4 | Agent5    |                  2 |      25 |           169 |        14.8% (0.148) |                0.500 | 0.296 |                0.150 |
| circle   | Agent5 | Agent1    |                  2 |      53 |           158 |        33.5% (0.335) |                0.500 | 0.671 |                0.336 |
| circle   | Agent5 | Agent4    |                  2 |     105 |           158 |        66.5% (0.665) |                0.500 | 1.329 |                0.664 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.1 | Fail    | diamond                                     | circle         |              7 |         257.29 |           0 |             0.00 |
|     2 |         0.1 | Fail    | asterisk                                    | circle         |             24 |         138.27 |           0 |             0.00 |
|     3 |         0.1 | Success | circle                                      | circle         |             11 |          65.85 |           0 |             0.00 |
|     4 |         0.1 | Fail    | cross                                       | triangle       |             38 |         208.05 |           0 |             0.00 |
|     5 |         0.1 | Fail    | triangle                                    | cross          |              7 |          44.30 |           0 |             0.00 |
|     6 |         0.1 | Fail    | square                                      | asterisk       |             10 |          59.12 |           0 |             0.00 |
|     7 |         0.1 | Fail    | diamond                                     | asterisk       |             19 |         105.24 |           0 |             0.00 |
|     8 |         0.1 | Fail    | square                                      | asterisk       |             10 |          61.71 |           0 |             0.00 |
|     9 |         0.1 | Fail    | asterisk                                    | circle         |             10 |          58.11 |           0 |             0.00 |
|    10 |         0.1 | Fail    | triangle                                    | asterisk       |             12 |          72.40 |           0 |             0.00 |
|    11 |         0.1 | Fail    | cross                                       | diamond        |             18 |         114.08 |           0 |             0.00 |
|    12 |         0.1 | Fail    | square                                      | circle         |              9 |         469.71 |           0 |             0.00 |
|    13 |         0.1 | Fail    | diamond                                     | circle         |              8 |         370.70 |           1 |            53.06 |
|    14 |         0.1 | Fail    | circle                                      | cross          |             37 |         468.40 |           0 |             0.00 |
|    15 |         0.1 | Fail    | circle                                      | asterisk       |             21 |         122.26 |           0 |             0.00 |
|    16 |         0.1 | Success | circle                                      | circle         |             24 |         130.74 |           0 |             0.00 |
|    17 |         0.1 | Fail    | triangle                                    | circle         |             19 |         108.43 |           0 |             0.00 |
|    18 |         0.1 | Fail    | square                                      | diamond        |              6 |          35.40 |           0 |             0.00 |
|    19 |         0.1 | Fail    | square                                      | asterisk       |             32 |         175.38 |           0 |             0.00 |
|    20 |         0.1 | Fail    | cross                                       | triangle       |             12 |          67.83 |           0 |             0.00 |
|    21 |         0.1 | Success | diamond                                     | diamond        |             21 |         120.12 |           0 |             0.00 |
|    22 |         0.1 | Fail    | circle                                      | cross          |             11 |          70.20 |           0 |             0.00 |
|    23 |         0.1 | Success | triangle                                    | triangle       |              9 |          89.02 |           0 |             0.00 |
|    24 |         0.1 | Fail    | cross                                       | asterisk       |             11 |         271.28 |           0 |             0.00 |
|    25 |         0.1 | Fail    | No figure submitted (message limit reached) | square         |             40 |         484.50 |           0 |             0.00 |
|    26 |         0.1 | Success | circle                                      | circle         |             10 |         139.01 |           0 |             0.00 |
|    27 |         0.1 | Fail    | square                                      | circle         |             16 |         170.95 |           0 |             0.00 |
|    28 |         0.1 | Success | triangle                                    | triangle       |             10 |          59.48 |           0 |             0.00 |
|    29 |         0.1 | Success | cross                                       | cross          |             13 |          70.60 |           0 |             0.00 |
|    30 |         0.1 | Fail    | square                                      | asterisk       |             12 |          70.36 |           0 |             0.00 |
|    31 |         0.1 | Success | cross                                       | cross          |             17 |         100.19 |           0 |             0.00 |
|    32 |         0.1 | Fail    | cross                                       | circle         |             27 |         151.28 |           0 |             0.00 |
|    33 |         0.1 | Fail    | cross                                       | circle         |             14 |          82.18 |           0 |             0.00 |
|    34 |         0.1 | Success | square                                      | square         |             21 |         167.02 |           0 |             0.00 |
|    35 |         0.1 | Fail    | cross                                       | asterisk       |             13 |        1156.44 |           0 |             0.00 |
|    36 |         0.1 | Fail    | triangle                                    | cross          |             10 |         112.80 |           0 |             0.00 |
|    37 |         0.1 | Fail    | diamond                                     | triangle       |             14 |          79.88 |           0 |             0.00 |
|    38 |         0.1 | Success | triangle                                    | triangle       |              8 |          49.36 |           0 |             0.00 |
|    39 |         0.1 | Fail    | circle                                      | square         |             17 |         100.48 |           0 |             0.00 |
|    40 |         0.1 | Success | asterisk                                    | asterisk       |              8 |          47.02 |           0 |             0.00 |
|    41 |         0.1 | Fail    | square                                      | diamond        |             14 |          79.83 |           0 |             0.00 |
|    42 |         0.1 | Fail    | cross                                       | asterisk       |              4 |          21.61 |           0 |             0.00 |
|    43 |         0.1 | Success | diamond                                     | diamond        |             31 |         166.48 |           0 |             0.00 |
|    44 |         0.1 | Success | cross                                       | cross          |             15 |          87.53 |           0 |             0.00 |
|    45 |         0.1 | Fail    | circle                                      | square         |             19 |         125.16 |           0 |             0.00 |
|    46 |         0.1 | Fail    | No figure submitted (message limit reached) | cross          |             40 |         540.95 |           0 |             0.00 |
|    47 |         0.1 | Fail    | square                                      | circle         |             13 |         141.54 |           0 |             0.00 |
|    48 |         0.1 | Fail    | diamond                                     | cross          |              9 |         428.72 |           0 |             0.00 |
|    49 |         0.1 | Fail    | square                                      | cross          |             26 |         322.73 |           0 |             0.00 |
|    50 |         0.1 | Success | square                                      | square         |              7 |          40.13 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    13 | Agent4               | 2026-05-13T07:21:23.597456+00:00 | 2026-05-13T07:22:16.661676+00:00 |            53.06 |
```
