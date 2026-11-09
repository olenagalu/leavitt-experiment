# Wheel auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 214.09 seconds
- Average total messages: 18.24
- Success rate: 9/50 (18.0%)
- Reconnect pauses: 2 across 2 trial(s); 48.05 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     187 |           187 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     177 |           177 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |      90 |           169 |        53.3% (0.533) |                0.250 | 2.130 |                0.529 |
| wheel    | Agent3 | Agent2    |                  4 |      57 |           169 |        33.7% (0.337) |                0.250 | 1.349 |                0.336 |
| wheel    | Agent3 | Agent4    |                  4 |      14 |           169 |         8.3% (0.083) |                0.250 | 0.331 |                0.085 |
| wheel    | Agent3 | Agent5    |                  4 |       8 |           169 |         4.7% (0.047) |                0.250 | 0.189 |                0.050 |
| wheel    | Agent4 | Agent3    |                  1 |     191 |           191 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     179 |           179 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| wheel    | Agent1 | client_assigned |     3 |
| wheel    | Agent3 | client_assigned |     6 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           1 | Fail    | diamond                                     | circle         |              9 |         294.03 |           0 |             0.00 |
|     2 |           1 | Fail    | asterisk                                    | square         |             23 |         140.73 |           0 |             0.00 |
|     3 |           1 | Fail    | diamond                                     | circle         |             43 |         255.74 |           0 |             0.00 |
|     4 |           1 | Success | square                                      | square         |             14 |          87.62 |           0 |             0.00 |
|     5 |           1 | Fail    | square                                      | cross          |             11 |          71.33 |           0 |             0.00 |
|     6 |           1 | Fail    | cross                                       | diamond        |             14 |          82.63 |           0 |             0.00 |
|     7 |           1 | Fail    | circle                                      | triangle       |             34 |         203.27 |           0 |             0.00 |
|     8 |           1 | Fail    | cross                                       | diamond        |              8 |          66.83 |           0 |             0.00 |
|     9 |           1 | Fail    | square                                      | asterisk       |             16 |         157.65 |           0 |             0.00 |
|    10 |           1 | Fail    | cross                                       | square         |             15 |          93.18 |           0 |             0.00 |
|    11 |           1 | Fail    | circle                                      | square         |             31 |         190.48 |           0 |             0.00 |
|    12 |           1 | Fail    | asterisk                                    | square         |             12 |         258.56 |           0 |             0.00 |
|    13 |           1 | Fail    | No figure submitted (message limit reached) | circle         |             50 |         987.01 |           0 |             0.00 |
|    14 |           1 | Fail    | cross                                       | asterisk       |             20 |         422.18 |           1 |            48.05 |
|    15 |           1 | Fail    | triangle                                    | square         |             29 |         186.22 |           0 |             0.00 |
|    16 |           1 | Success | diamond                                     | diamond        |             12 |          77.20 |           0 |             0.00 |
|    17 |           1 | Fail    | diamond                                     | asterisk       |             10 |         127.15 |           0 |             0.00 |
|    18 |           1 | Fail    | diamond                                     | asterisk       |             11 |          69.53 |           0 |             0.00 |
|    19 |           1 | Fail    | circle                                      | diamond        |             14 |          86.68 |           0 |             0.00 |
|    20 |           1 | Fail    | circle                                      | diamond        |             15 |          93.27 |           0 |             0.00 |
|    21 |           1 | Fail    | square                                      | triangle       |             14 |          90.12 |           0 |             0.00 |
|    22 |           1 | Fail    | circle                                      | square         |             13 |          84.63 |           0 |             0.00 |
|    23 |           1 | Success | cross                                       | cross          |             11 |         190.73 |           0 |             0.00 |
|    24 |           1 | Fail    | circle                                      | diamond        |             34 |        2157.17 |           0 |             0.00 |
|    25 |           1 | Fail    | circle                                      | asterisk       |             16 |         151.08 |           0 |             0.00 |
|    26 |           1 | Success | circle                                      | circle         |             10 |          59.22 |           0 |             0.00 |
|    27 |           1 | Fail    | cross                                       | square         |             14 |          92.02 |           0 |             0.00 |
|    28 |           1 | Success | triangle                                    | triangle       |             14 |          92.32 |           0 |             0.00 |
|    29 |           1 | Fail    | circle                                      | triangle       |             18 |         115.08 |           0 |             0.00 |
|    30 |           1 | Fail    | cross                                       | triangle       |             20 |         122.58 |           0 |             0.00 |
|    31 |           1 | Success | triangle                                    | triangle       |             22 |         131.23 |           0 |             0.00 |
|    32 |           1 | Fail    | circle                                      | square         |             10 |         138.04 |           0 |             0.00 |
|    33 |           1 | Fail    | asterisk                                    | triangle       |             10 |          61.86 |           0 |             0.00 |
|    34 |           1 | Fail    | circle                                      | diamond        |             13 |         101.81 |           0 |             0.00 |
|    35 |           1 | Fail    | diamond                                     | circle         |             26 |         392.94 |           0 |             0.00 |
|    36 |           1 | Fail    | asterisk                                    | square         |             24 |         663.89 |           0 |             0.00 |
|    37 |           1 | Fail    | circle                                      | square         |             25 |         149.64 |           0 |             0.00 |
|    38 |           1 | Fail    | cross                                       | circle         |             18 |         109.96 |           0 |             0.00 |
|    39 |           1 | Fail    | asterisk                                    | cross          |             25 |         193.50 |           0 |             0.00 |
|    40 |           1 | Success | circle                                      | circle         |             15 |         164.39 |           0 |             0.00 |
|    41 |           1 | Fail    | circle                                      | diamond        |             15 |          87.10 |           0 |             0.00 |
|    42 |           1 | Fail    | asterisk                                    | triangle       |              9 |          57.66 |           0 |             0.00 |
|    43 |           1 | Success | circle                                      | circle         |             19 |         117.18 |           0 |             0.00 |
|    44 |           1 | Fail    | diamond                                     | asterisk       |             15 |          92.29 |           0 |             0.00 |
|    45 |           1 | Success | circle                                      | circle         |              6 |          42.01 |           0 |             0.00 |
|    46 |           1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |         346.46 |           0 |             0.00 |
|    47 |           1 | Fail    | triangle                                    | diamond        |             28 |         576.18 |           1 |             0.00 |
|    48 |           1 | Fail    | cross                                       | diamond        |              9 |          54.88 |           0 |             0.00 |
|    49 |           1 | Fail    | square                                      | triangle       |              8 |          53.20 |           0 |             0.00 |
|    50 |           1 | Fail    | triangle                                    | asterisk       |             10 |          64.03 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    14 | Agent4               | 2026-05-15T16:34:24.620701+00:00 | 2026-05-15T16:35:12.673182+00:00 |            48.05 |
|    47 | Agent5               | 2026-05-15T18:38:16.805657+00:00 | 2026-05-15T18:38:16.809544+00:00 |             0.00 |
```
