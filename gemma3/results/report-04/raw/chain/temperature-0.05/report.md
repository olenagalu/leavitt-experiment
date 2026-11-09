# Chain auto-trial report

## Summary

- Batch: `temperature-0.05`
- Temperature: 0.05
- Completed trials: 50/50
- Average time: 206.12 seconds
- Average total messages: 16.42
- Success rate: 9/50 (18.0%)
- Reconnect pauses: 1 across 1 trial(s); 3.01 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     169 |           169 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     115 |           127 |        90.6% (0.906) |                0.500 | 1.811 |                0.902 |
| chain    | Agent2 | Agent3    |                  2 |      12 |           127 |         9.4% (0.094) |                0.500 | 0.189 |                0.098 |
| chain    | Agent3 | Agent2    |                  2 |     168 |           174 |        96.6% (0.966) |                0.500 | 1.931 |                0.963 |
| chain    | Agent3 | Agent4    |                  2 |       6 |           174 |         3.4% (0.034) |                0.500 | 0.069 |                0.037 |
| chain    | Agent4 | Agent3    |                  2 |     131 |           175 |        74.9% (0.749) |                0.500 | 1.497 |                0.747 |
| chain    | Agent4 | Agent5    |                  2 |      44 |           175 |        25.1% (0.251) |                0.500 | 0.503 |                0.253 |
| chain    | Agent5 | Agent4    |                  1 |     176 |           176 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |        0.05 | Success | square                                      | square         |              9 |         256.87 |           0 |             0.00 |
|     2 |        0.05 | Fail    | circle                                      | square         |              9 |          52.44 |           0 |             0.00 |
|     3 |        0.05 | Fail    | diamond                                     | triangle       |             20 |         114.47 |           0 |             0.00 |
|     4 |        0.05 | Fail    | triangle                                    | square         |             14 |          80.50 |           0 |             0.00 |
|     5 |        0.05 | Fail    | cross                                       | triangle       |             14 |          78.62 |           0 |             0.00 |
|     6 |        0.05 | Fail    | cross                                       | asterisk       |             12 |          69.41 |           0 |             0.00 |
|     7 |        0.05 | Fail    | triangle                                    | circle         |             15 |          90.31 |           0 |             0.00 |
|     8 |        0.05 | Fail    | diamond                                     | cross          |              6 |          35.76 |           0 |             0.00 |
|     9 |        0.05 | Fail    | circle                                      | asterisk       |              5 |          31.12 |           0 |             0.00 |
|    10 |        0.05 | Fail    | triangle                                    | diamond        |             24 |         141.98 |           0 |             0.00 |
|    11 |        0.05 | Fail    | diamond                                     | triangle       |             10 |          66.01 |           0 |             0.00 |
|    12 |        0.05 | Fail    | diamond                                     | circle         |             49 |         954.23 |           0 |             0.00 |
|    13 |        0.05 | Fail    | circle                                      | asterisk       |             15 |          85.54 |           0 |             0.00 |
|    14 |        0.05 | Fail    | square                                      | cross          |             16 |          94.10 |           0 |             0.00 |
|    15 |        0.05 | Success | triangle                                    | triangle       |              9 |          57.33 |           0 |             0.00 |
|    16 |        0.05 | Success | circle                                      | circle         |             16 |         227.33 |           0 |             0.00 |
|    17 |        0.05 | Fail    | cross                                       | triangle       |             12 |          68.97 |           0 |             0.00 |
|    18 |        0.05 | Fail    | square                                      | asterisk       |              7 |          41.76 |           0 |             0.00 |
|    19 |        0.05 | Fail    | triangle                                    | square         |              6 |          35.75 |           0 |             0.00 |
|    20 |        0.05 | Fail    | square                                      | asterisk       |             12 |          67.43 |           0 |             0.00 |
|    21 |        0.05 | Fail    | circle                                      | cross          |             26 |         151.13 |           0 |             0.00 |
|    22 |        0.05 | Fail    | asterisk                                    | cross          |              9 |          55.29 |           0 |             0.00 |
|    23 |        0.05 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1674.74 |           0 |             0.00 |
|    24 |        0.05 | Fail    | square                                      | asterisk       |             13 |         540.39 |           0 |             0.00 |
|    25 |        0.05 | Success | circle                                      | circle         |              7 |          93.60 |           0 |             0.00 |
|    26 |        0.05 | Fail    | cross                                       | circle         |             16 |          91.05 |           0 |             0.00 |
|    27 |        0.05 | Fail    | triangle                                    | diamond        |             10 |          57.90 |           0 |             0.00 |
|    28 |        0.05 | Fail    | asterisk                                    | diamond        |             16 |          95.52 |           0 |             0.00 |
|    29 |        0.05 | Fail    | circle                                      | square         |              6 |          34.87 |           0 |             0.00 |
|    30 |        0.05 | Fail    | triangle                                    | cross          |             16 |          92.25 |           0 |             0.00 |
|    31 |        0.05 | Fail    | square                                      | cross          |             16 |          94.66 |           0 |             0.00 |
|    32 |        0.05 | Fail    | diamond                                     | cross          |             22 |         127.56 |           0 |             0.00 |
|    33 |        0.05 | Fail    | cross                                       | triangle       |             15 |          97.86 |           0 |             0.00 |
|    34 |        0.05 | Fail    | asterisk                                    | square         |             44 |         743.41 |           0 |             0.00 |
|    35 |        0.05 | Fail    | triangle                                    | asterisk       |              7 |          40.16 |           0 |             0.00 |
|    36 |        0.05 | Success | circle                                      | circle         |             12 |          75.74 |           0 |             0.00 |
|    37 |        0.05 | Fail    | asterisk                                    | cross          |             48 |        1675.46 |           1 |             3.01 |
|    38 |        0.05 | Success | cross                                       | cross          |             16 |          92.99 |           0 |             0.00 |
|    39 |        0.05 | Success | triangle                                    | triangle       |             32 |         181.16 |           0 |             0.00 |
|    40 |        0.05 | Fail    | diamond                                     | asterisk       |             10 |          57.99 |           0 |             0.00 |
|    41 |        0.05 | Fail    | circle                                      | diamond        |             17 |          95.79 |           0 |             0.00 |
|    42 |        0.05 | Fail    | square                                      | triangle       |              8 |          45.00 |           0 |             0.00 |
|    43 |        0.05 | Success | diamond                                     | diamond        |             10 |          58.98 |           0 |             0.00 |
|    44 |        0.05 | Success | cross                                       | cross          |             10 |          57.24 |           0 |             0.00 |
|    45 |        0.05 | Fail    | diamond                                     | triangle       |             23 |         132.95 |           0 |             0.00 |
|    46 |        0.05 | Fail    | cross                                       | circle         |             11 |          68.07 |           0 |             0.00 |
|    47 |        0.05 | Fail    | asterisk                                    | cross          |             11 |          71.26 |           0 |             0.00 |
|    48 |        0.05 | Fail    | cross                                       | diamond        |             24 |         681.39 |           0 |             0.00 |
|    49 |        0.05 | Fail    | triangle                                    | square         |             19 |         117.21 |           0 |             0.00 |
|    50 |        0.05 | Fail    | asterisk                                    | diamond        |             17 |         254.38 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    37 | Agent3               | 2026-05-13T20:44:16.735997+00:00 | 2026-05-13T20:44:19.741113+00:00 |             3.01 |
```
