# Wheel auto-trial report

## Summary

- Batch: `temperature-0.05`
- Temperature: 0.05
- Completed trials: 50/50
- Average time: 199.91 seconds
- Average total messages: 17.56
- Success rate: 20/50 (40.0%)
- Reconnect pauses: 1 across 1 trial(s); 63.07 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     187 |           187 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     178 |           178 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     108 |           180 |        60.0% (0.600) |                0.250 | 2.400 |                0.596 |
| wheel    | Agent3 | Agent2    |                  4 |      61 |           180 |        33.9% (0.339) |                0.250 | 1.356 |                0.338 |
| wheel    | Agent3 | Agent4    |                  4 |       3 |           180 |         1.7% (0.017) |                0.250 | 0.067 |                0.019 |
| wheel    | Agent3 | Agent5    |                  4 |       8 |           180 |         4.4% (0.044) |                0.250 | 0.178 |                0.047 |
| wheel    | Agent4 | Agent3    |                  1 |     153 |           153 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     178 |           178 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| wheel    | Agent3 | client_assigned |     2 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |        0.05 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |         960.85 |           0 |             0.00 |
|     2 |        0.05 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        1238.24 |           0 |             0.00 |
|     3 |        0.05 | Success | square                                      | square         |             25 |         423.30 |           0 |             0.00 |
|     4 |        0.05 | Fail    | cross                                       | circle         |             17 |         109.75 |           0 |             0.00 |
|     5 |        0.05 | Success | diamond                                     | diamond        |             12 |          77.85 |           0 |             0.00 |
|     6 |        0.05 | Success | triangle                                    | triangle       |             21 |         124.32 |           0 |             0.00 |
|     7 |        0.05 | Fail    | triangle                                    | square         |             11 |          71.91 |           0 |             0.00 |
|     8 |        0.05 | Fail    | diamond                                     | asterisk       |             21 |         116.92 |           0 |             0.00 |
|     9 |        0.05 | Fail    | circle                                      | diamond        |             31 |         205.50 |           0 |             0.00 |
|    10 |        0.05 | Success | circle                                      | circle         |              7 |         118.42 |           0 |             0.00 |
|    11 |        0.05 | Fail    | circle                                      | square         |             25 |         160.47 |           0 |             0.00 |
|    12 |        0.05 | Fail    | diamond                                     | asterisk       |             15 |         132.11 |           0 |             0.00 |
|    13 |        0.05 | Fail    | triangle                                    | diamond        |             24 |         512.94 |           1 |            63.07 |
|    14 |        0.05 | Fail    | triangle                                    | circle         |              9 |          60.26 |           0 |             0.00 |
|    15 |        0.05 | Success | circle                                      | circle         |             18 |         107.67 |           0 |             0.00 |
|    16 |        0.05 | Success | square                                      | square         |             11 |          72.43 |           0 |             0.00 |
|    17 |        0.05 | Success | square                                      | square         |             11 |          71.73 |           0 |             0.00 |
|    18 |        0.05 | Success | asterisk                                    | asterisk       |             12 |          78.95 |           0 |             0.00 |
|    19 |        0.05 | Fail    | circle                                      | triangle       |             21 |         138.64 |           0 |             0.00 |
|    20 |        0.05 | Success | circle                                      | circle         |             33 |         355.45 |           0 |             0.00 |
|    21 |        0.05 | Success | diamond                                     | diamond        |             22 |         135.20 |           0 |             0.00 |
|    22 |        0.05 | Fail    | asterisk                                    | cross          |             14 |          88.02 |           0 |             0.00 |
|    23 |        0.05 | Fail    | triangle                                    | asterisk       |             28 |         307.26 |           0 |             0.00 |
|    24 |        0.05 | Success | diamond                                     | diamond        |             15 |         330.06 |           0 |             0.00 |
|    25 |        0.05 | Fail    | cross                                       | circle         |             13 |          86.54 |           0 |             0.00 |
|    26 |        0.05 | Fail    | triangle                                    | circle         |             14 |         154.62 |           0 |             0.00 |
|    27 |        0.05 | Fail    | cross                                       | circle         |             11 |          95.88 |           0 |             0.00 |
|    28 |        0.05 | Fail    | circle                                      | diamond        |             16 |         182.29 |           0 |             0.00 |
|    29 |        0.05 | Success | square                                      | square         |              9 |          58.80 |           0 |             0.00 |
|    30 |        0.05 | Fail    | square                                      | asterisk       |             13 |          81.69 |           0 |             0.00 |
|    31 |        0.05 | Success | triangle                                    | triangle       |              7 |          45.68 |           0 |             0.00 |
|    32 |        0.05 | Fail    | cross                                       | triangle       |              7 |          46.50 |           0 |             0.00 |
|    33 |        0.05 | Fail    | circle                                      | diamond        |              9 |          58.68 |           0 |             0.00 |
|    34 |        0.05 | Fail    | triangle                                    | asterisk       |             11 |         183.29 |           0 |             0.00 |
|    35 |        0.05 | Success | square                                      | square         |             28 |         386.68 |           0 |             0.00 |
|    36 |        0.05 | Fail    | diamond                                     | circle         |              8 |          53.36 |           0 |             0.00 |
|    37 |        0.05 | Success | circle                                      | circle         |             17 |         118.26 |           0 |             0.00 |
|    38 |        0.05 | Fail    | triangle                                    | square         |             14 |         234.23 |           0 |             0.00 |
|    39 |        0.05 | Success | cross                                       | cross          |             14 |          87.42 |           0 |             0.00 |
|    40 |        0.05 | Fail    | circle                                      | cross          |             20 |         120.33 |           0 |             0.00 |
|    41 |        0.05 | Fail    | circle                                      | cross          |             16 |         104.44 |           0 |             0.00 |
|    42 |        0.05 | Fail    | square                                      | circle         |             18 |         209.44 |           0 |             0.00 |
|    43 |        0.05 | Fail    | square                                      | triangle       |              9 |         138.58 |           0 |             0.00 |
|    44 |        0.05 | Success | square                                      | square         |             21 |         138.70 |           0 |             0.00 |
|    45 |        0.05 | Success | diamond                                     | diamond        |             14 |         321.31 |           0 |             0.00 |
|    46 |        0.05 | Success | cross                                       | cross          |             24 |         505.21 |           0 |             0.00 |
|    47 |        0.05 | Fail    | cross                                       | asterisk       |             13 |          83.41 |           0 |             0.00 |
|    48 |        0.05 | Fail    | asterisk                                    | diamond        |             13 |          78.23 |           0 |             0.00 |
|    49 |        0.05 | Success | diamond                                     | diamond        |             10 |          67.15 |           0 |             0.00 |
|    50 |        0.05 | Fail    | cross                                       | asterisk       |             26 |         356.58 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    13 | Agent4               | 2026-05-15T06:15:46.050635+00:00 | 2026-05-15T06:16:49.121087+00:00 |            63.07 |
```
