# Chain auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 159.62 seconds
- Average total messages: 16.18
- Success rate: 7/50 (14.0%)
- Reconnect pauses: 1 across 1 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     152 |           152 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     160 |           177 |        90.4% (0.904) |                0.500 | 1.808 |                0.902 |
| chain    | Agent2 | Agent3    |                  2 |      17 |           177 |         9.6% (0.096) |                0.500 | 0.192 |                0.098 |
| chain    | Agent3 | Agent2    |                  2 |     162 |           169 |        95.9% (0.959) |                0.500 | 1.917 |                0.956 |
| chain    | Agent3 | Agent4    |                  2 |       7 |           169 |         4.1% (0.041) |                0.500 | 0.083 |                0.044 |
| chain    | Agent4 | Agent3    |                  2 |      98 |           151 |        64.9% (0.649) |                0.500 | 1.298 |                0.648 |
| chain    | Agent4 | Agent5    |                  2 |      53 |           151 |        35.1% (0.351) |                0.500 | 0.702 |                0.352 |
| chain    | Agent5 | Agent4    |                  1 |     160 |           160 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Fail    | square                                      | circle         |             13 |         304.18 |           0 |             0.00 |
|     2 |           0 | Fail    | diamond                                     | cross          |             12 |          67.32 |           0 |             0.00 |
|     3 |           0 | Fail    | circle                                      | asterisk       |             17 |          98.04 |           0 |             0.00 |
|     4 |           0 | Fail    | diamond                                     | asterisk       |             22 |         122.13 |           0 |             0.00 |
|     5 |           0 | Fail    | cross                                       | square         |              8 |          47.20 |           0 |             0.00 |
|     6 |           0 | Fail    | triangle                                    | diamond        |             10 |          59.39 |           0 |             0.00 |
|     7 |           0 | Fail    | cross                                       | square         |              9 |          52.97 |           0 |             0.00 |
|     8 |           0 | Fail    | circle                                      | asterisk       |             11 |          61.81 |           0 |             0.00 |
|     9 |           0 | Fail    | square                                      | triangle       |             18 |         109.03 |           0 |             0.00 |
|    10 |           0 | Fail    | cross                                       | circle         |             14 |          92.27 |           0 |             0.00 |
|    11 |           0 | Fail    | circle                                      | asterisk       |             12 |         131.37 |           0 |             0.00 |
|    12 |           0 | Fail    | diamond                                     | asterisk       |              7 |          49.54 |           0 |             0.00 |
|    13 |           0 | Fail    | cross                                       | diamond        |              9 |         159.41 |           0 |             0.00 |
|    14 |           0 | Fail    | cross                                       | asterisk       |             16 |         241.77 |           0 |             0.00 |
|    15 |           0 | Fail    | cross                                       | circle         |             19 |         386.47 |           0 |             0.00 |
|    16 |           0 | Fail    | square                                      | triangle       |             12 |         153.92 |           0 |             0.00 |
|    17 |           0 | Fail    | asterisk                                    | triangle       |              9 |          52.19 |           0 |             0.00 |
|    18 |           0 | Fail    | diamond                                     | circle         |              8 |          46.05 |           0 |             0.00 |
|    19 |           0 | Fail    | cross                                       | square         |             12 |          68.51 |           0 |             0.00 |
|    20 |           0 | Success | square                                      | square         |              9 |          54.20 |           0 |             0.00 |
|    21 |           0 | Success | circle                                      | circle         |             11 |          71.76 |           0 |             0.00 |
|    22 |           0 | Fail    | square                                      | triangle       |              8 |         132.21 |           0 |             0.00 |
|    23 |           0 | Success | square                                      | square         |             18 |         101.21 |           0 |             0.00 |
|    24 |           0 | Fail    | square                                      | cross          |             11 |          63.77 |           0 |             0.00 |
|    25 |           0 | Fail    | No figure submitted (message limit reached) | square         |             50 |        1056.69 |           0 |             0.00 |
|    26 |           0 | Success | asterisk                                    | asterisk       |             48 |         361.42 |           0 |             0.00 |
|    27 |           0 | Fail    | cross                                       | triangle       |             29 |         162.36 |           0 |             0.00 |
|    28 |           0 | Fail    | circle                                      | diamond        |              9 |          54.35 |           0 |             0.00 |
|    29 |           0 | Fail    | square                                      | triangle       |             23 |         132.71 |           0 |             0.00 |
|    30 |           0 | Fail    | square                                      | asterisk       |             15 |          84.57 |           0 |             0.00 |
|    31 |           0 | Fail    | diamond                                     | circle         |              9 |          53.00 |           0 |             0.00 |
|    32 |           0 | Fail    | triangle                                    | circle         |             19 |         110.79 |           0 |             0.00 |
|    33 |           0 | Fail    | diamond                                     | circle         |              9 |          51.35 |           0 |             0.00 |
|    34 |           0 | Success | circle                                      | circle         |             14 |          87.29 |           0 |             0.00 |
|    35 |           0 | Fail    | circle                                      | cross          |              8 |         136.94 |           0 |             0.00 |
|    36 |           0 | Fail    | square                                      | triangle       |             12 |         159.26 |           0 |             0.00 |
|    37 |           0 | Fail    | circle                                      | triangle       |             12 |         493.41 |           1 |             0.00 |
|    38 |           0 | Fail    | cross                                       | triangle       |             21 |         172.65 |           0 |             0.00 |
|    39 |           0 | Fail    | triangle                                    | asterisk       |             15 |          84.98 |           0 |             0.00 |
|    40 |           0 | Fail    | asterisk                                    | square         |             11 |          66.01 |           0 |             0.00 |
|    41 |           0 | Fail    | circle                                      | cross          |             15 |          85.29 |           0 |             0.00 |
|    42 |           0 | Fail    | circle                                      | diamond        |             34 |         187.30 |           0 |             0.00 |
|    43 |           0 | Fail    | cross                                       | asterisk       |             40 |         226.45 |           0 |             0.00 |
|    44 |           0 | Success | asterisk                                    | asterisk       |              9 |          52.23 |           0 |             0.00 |
|    45 |           0 | Fail    | triangle                                    | circle         |              9 |          55.38 |           0 |             0.00 |
|    46 |           0 | Success | diamond                                     | diamond        |             26 |         144.25 |           0 |             0.00 |
|    47 |           0 | Fail    | square                                      | circle         |             12 |          75.12 |           0 |             0.00 |
|    48 |           0 | Fail    | cross                                       | square         |             42 |         984.53 |           0 |             0.00 |
|    49 |           0 | Fail    | square                                      | cross          |             11 |         107.62 |           0 |             0.00 |
|    50 |           0 | Fail    | cross                                       | triangle       |             12 |          68.48 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    37 | Agent4               | 2026-05-13T17:38:57.566245+00:00 | 2026-05-13T17:38:57.568958+00:00 |             0.00 |
```
