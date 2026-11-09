# Circle auto-trial report

## Summary

- Batch: `temperature-0.2`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 158.73 seconds
- Average total messages: 14.24
- Success rate: 13/50 (26.0%)
- Reconnect pauses: 1 across 1 trial(s); 56.06 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      42 |           139 |        30.2% (0.302) |                0.500 | 0.604 |                0.304 |
| circle   | Agent1 | Agent5    |                  2 |      97 |           139 |        69.8% (0.698) |                0.500 | 1.396 |                0.696 |
| circle   | Agent2 | Agent1    |                  2 |     124 |           136 |        91.2% (0.912) |                0.500 | 1.824 |                0.909 |
| circle   | Agent2 | Agent3    |                  2 |      12 |           136 |         8.8% (0.088) |                0.500 | 0.176 |                0.091 |
| circle   | Agent3 | Agent2    |                  2 |     146 |           148 |        98.6% (0.986) |                0.500 | 1.973 |                0.983 |
| circle   | Agent3 | Agent4    |                  2 |       2 |           148 |         1.4% (0.014) |                0.500 | 0.027 |                0.017 |
| circle   | Agent4 | Agent3    |                  2 |     122 |           150 |        81.3% (0.813) |                0.500 | 1.627 |                0.811 |
| circle   | Agent4 | Agent5    |                  2 |      28 |           150 |        18.7% (0.187) |                0.500 | 0.373 |                0.189 |
| circle   | Agent5 | Agent1    |                  2 |      64 |           139 |        46.0% (0.460) |                0.500 | 0.921 |                0.461 |
| circle   | Agent5 | Agent4    |                  2 |      75 |           139 |        54.0% (0.540) |                0.500 | 1.079 |                0.539 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.2 | Fail    | cross                                       | asterisk       |             14 |         314.06 |           0 |             0.00 |
|     2 |         0.2 | Success | square                                      | square         |             11 |         106.89 |           0 |             0.00 |
|     3 |         0.2 | Fail    | circle                                      | diamond        |             12 |          72.29 |           0 |             0.00 |
|     4 |         0.2 | Fail    | diamond                                     | asterisk       |             20 |         114.59 |           0 |             0.00 |
|     5 |         0.2 | Fail    | triangle                                    | diamond        |             12 |          71.83 |           0 |             0.00 |
|     6 |         0.2 | Fail    | triangle                                    | cross          |             20 |         113.01 |           0 |             0.00 |
|     7 |         0.2 | Fail    | diamond                                     | square         |             16 |          90.43 |           0 |             0.00 |
|     8 |         0.2 | Fail    | cross                                       | square         |             23 |         124.46 |           0 |             0.00 |
|     9 |         0.2 | Fail    | asterisk                                    | triangle       |              7 |          42.64 |           0 |             0.00 |
|    10 |         0.2 | Fail    | circle                                      | square         |             14 |          85.25 |           0 |             0.00 |
|    11 |         0.2 | Success | triangle                                    | triangle       |             14 |          88.48 |           0 |             0.00 |
|    12 |         0.2 | Fail    | square                                      | circle         |             14 |         156.36 |           0 |             0.00 |
|    13 |         0.2 | Success | circle                                      | circle         |              4 |         137.55 |           0 |             0.00 |
|    14 |         0.2 | Success | cross                                       | cross          |             18 |         393.39 |           1 |            56.06 |
|    15 |         0.2 | Fail    | square                                      | diamond        |             33 |         233.73 |           0 |             0.00 |
|    16 |         0.2 | Fail    | square                                      | asterisk       |             12 |          69.36 |           0 |             0.00 |
|    17 |         0.2 | Fail    | cross                                       | asterisk       |             12 |          71.02 |           0 |             0.00 |
|    18 |         0.2 | Success | cross                                       | cross          |             24 |         139.40 |           0 |             0.00 |
|    19 |         0.2 | Success | circle                                      | circle         |             10 |          58.96 |           0 |             0.00 |
|    20 |         0.2 | Fail    | square                                      | diamond        |             11 |          64.40 |           0 |             0.00 |
|    21 |         0.2 | Fail    | cross                                       | asterisk       |             16 |          92.54 |           0 |             0.00 |
|    22 |         0.2 | Fail    | square                                      | cross          |             20 |         112.00 |           0 |             0.00 |
|    23 |         0.2 | Success | diamond                                     | diamond        |              5 |         219.71 |           0 |             0.00 |
|    24 |         0.2 | Fail    | circle                                      | cross          |             18 |         342.02 |           0 |             0.00 |
|    25 |         0.2 | Fail    | cross                                       | triangle       |             22 |         130.39 |           0 |             0.00 |
|    26 |         0.2 | Fail    | cross                                       | diamond        |             14 |         122.54 |           0 |             0.00 |
|    27 |         0.2 | Fail    | square                                      | cross          |              7 |          44.85 |           0 |             0.00 |
|    28 |         0.2 | Fail    | circle                                      | triangle       |             11 |          63.35 |           0 |             0.00 |
|    29 |         0.2 | Fail    | diamond                                     | cross          |              8 |         251.32 |           0 |             0.00 |
|    30 |         0.2 | Success | triangle                                    | triangle       |             15 |         278.79 |           0 |             0.00 |
|    31 |         0.2 | Fail    | diamond                                     | cross          |              7 |          42.40 |           0 |             0.00 |
|    32 |         0.2 | Fail    | diamond                                     | square         |              7 |         139.78 |           0 |             0.00 |
|    33 |         0.2 | Success | cross                                       | cross          |             11 |         257.36 |           0 |             0.00 |
|    34 |         0.2 | Fail    | triangle                                    | cross          |              5 |         317.29 |           0 |             0.00 |
|    35 |         0.2 | Fail    | circle                                      | square         |             11 |         349.90 |           0 |             0.00 |
|    36 |         0.2 | Fail    | cross                                       | triangle       |             12 |         211.07 |           0 |             0.00 |
|    37 |         0.2 | Fail    | diamond                                     | square         |             13 |         273.38 |           0 |             0.00 |
|    38 |         0.2 | Success | square                                      | square         |              7 |          41.34 |           0 |             0.00 |
|    39 |         0.2 | Success | cross                                       | cross          |             15 |          85.68 |           0 |             0.00 |
|    40 |         0.2 | Fail    | triangle                                    | diamond        |              8 |          48.83 |           0 |             0.00 |
|    41 |         0.2 | Fail    | circle                                      | cross          |             17 |          98.87 |           0 |             0.00 |
|    42 |         0.2 | Fail    | circle                                      | cross          |              5 |          30.54 |           0 |             0.00 |
|    43 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             40 |         228.69 |           0 |             0.00 |
|    44 |         0.2 | Fail    | diamond                                     | triangle       |              3 |          18.19 |           0 |             0.00 |
|    45 |         0.2 | Fail    | circle                                      | triangle       |             34 |         194.42 |           0 |             0.00 |
|    46 |         0.2 | Success | asterisk                                    | asterisk       |             14 |         306.35 |           0 |             0.00 |
|    47 |         0.2 | Success | circle                                      | circle         |             26 |         855.50 |           0 |             0.00 |
|    48 |         0.2 | Fail    | cross                                       | diamond        |             18 |         104.40 |           0 |             0.00 |
|    49 |         0.2 | Fail    | cross                                       | asterisk       |              8 |          46.93 |           0 |             0.00 |
|    50 |         0.2 | Fail    | circle                                      | triangle       |             14 |          80.00 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    14 | Agent1               | 2026-05-13T10:06:05.482230+00:00 | 2026-05-13T10:07:01.546486+00:00 |            56.06 |
```
