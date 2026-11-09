# Wheel auto-trial report

## Summary

- Batch: `temperature-0.05`
- Temperature: 0.05
- Completed trials: 50/50
- Average time: 282.80 seconds
- Average total messages: 21.18
- Success rate: 11/50 (22.0%)
- Reconnect pauses: 1 across 1 trial(s); 2.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     219 |           219 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     201 |           201 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     131 |           210 |        62.4% (0.624) |                0.250 | 2.495 |                0.620 |
| wheel    | Agent3 | Agent2    |                  4 |      72 |           210 |        34.3% (0.343) |                0.250 | 1.371 |                0.342 |
| wheel    | Agent3 | Agent4    |                  4 |       1 |           210 |         0.5% (0.005) |                0.250 | 0.019 |                0.007 |
| wheel    | Agent3 | Agent5    |                  4 |       6 |           210 |         2.9% (0.029) |                0.250 | 0.114 |                0.031 |
| wheel    | Agent4 | Agent3    |                  1 |     191 |           191 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     235 |           235 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| wheel    | Agent3 | client_assigned |     3 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |        0.05 | Fail    | diamond                                     | asterisk       |             19 |         333.76 |           0 |             0.00 |
|     2 |        0.05 | Success | diamond                                     | diamond        |             15 |          90.15 |           0 |             0.00 |
|     3 |        0.05 | Fail    | cross                                       | asterisk       |             29 |         176.00 |           0 |             0.00 |
|     4 |        0.05 | Fail    | cross                                       | square         |             16 |         104.21 |           0 |             0.00 |
|     5 |        0.05 | Fail    | asterisk                                    | cross          |             10 |          59.78 |           0 |             0.00 |
|     6 |        0.05 | Success | asterisk                                    | asterisk       |             23 |         145.80 |           0 |             0.00 |
|     7 |        0.05 | Success | cross                                       | cross          |             11 |          71.67 |           0 |             0.00 |
|     8 |        0.05 | Fail    | circle                                      | triangle       |             49 |         866.77 |           0 |             0.00 |
|     9 |        0.05 | Fail    | triangle                                    | diamond        |             11 |          73.35 |           0 |             0.00 |
|    10 |        0.05 | Fail    | cross                                       | diamond        |             14 |          94.00 |           0 |             0.00 |
|    11 |        0.05 | Fail    | circle                                      | square         |             32 |         211.89 |           0 |             0.00 |
|    12 |        0.05 | Fail    | circle                                      | diamond        |             14 |         143.71 |           0 |             0.00 |
|    13 |        0.05 | Success | cross                                       | cross          |             36 |         657.35 |           0 |             0.00 |
|    14 |        0.05 | Fail    | diamond                                     | triangle       |             10 |          62.39 |           0 |             0.00 |
|    15 |        0.05 | Fail    | circle                                      | square         |             23 |         262.59 |           0 |             0.00 |
|    16 |        0.05 | Success | square                                      | square         |              9 |          67.53 |           0 |             0.00 |
|    17 |        0.05 | Fail    | diamond                                     | cross          |             11 |          76.12 |           0 |             0.00 |
|    18 |        0.05 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1529.66 |           0 |             0.00 |
|    19 |        0.05 | Fail    | circle                                      | square         |             14 |         697.81 |           1 |             2.00 |
|    20 |        0.05 | Success | circle                                      | circle         |             33 |         242.33 |           0 |             0.00 |
|    21 |        0.05 | Fail    | square                                      | asterisk       |             29 |         170.59 |           0 |             0.00 |
|    22 |        0.05 | Fail    | square                                      | triangle       |              9 |          58.29 |           0 |             0.00 |
|    23 |        0.05 | Fail    | triangle                                    | circle         |             15 |          98.23 |           0 |             0.00 |
|    24 |        0.05 | Fail    | cross                                       | triangle       |             39 |         231.00 |           0 |             0.00 |
|    25 |        0.05 | Fail    | circle                                      | asterisk       |             17 |         104.44 |           0 |             0.00 |
|    26 |        0.05 | Success | cross                                       | cross          |             12 |          83.48 |           0 |             0.00 |
|    27 |        0.05 | Fail    | square                                      | asterisk       |             18 |         189.00 |           0 |             0.00 |
|    28 |        0.05 | Success | square                                      | square         |             27 |         254.82 |           0 |             0.00 |
|    29 |        0.05 | Fail    | triangle                                    | square         |             25 |         252.24 |           0 |             0.00 |
|    30 |        0.05 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        1068.86 |           0 |             0.00 |
|    31 |        0.05 | Fail    | cross                                       | diamond        |             22 |         136.95 |           0 |             0.00 |
|    32 |        0.05 | Fail    | asterisk                                    | triangle       |             12 |          77.63 |           0 |             0.00 |
|    33 |        0.05 | Fail    | asterisk                                    | cross          |             12 |          80.21 |           0 |             0.00 |
|    34 |        0.05 | Fail    | diamond                                     | triangle       |             43 |        1233.84 |           0 |             0.00 |
|    35 |        0.05 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1129.23 |           0 |             0.00 |
|    36 |        0.05 | Fail    | cross                                       | asterisk       |             23 |         578.84 |           0 |             0.00 |
|    37 |        0.05 | Fail    | circle                                      | asterisk       |             14 |          86.21 |           0 |             0.00 |
|    38 |        0.05 | Fail    | diamond                                     | square         |              9 |          57.47 |           0 |             0.00 |
|    39 |        0.05 | Fail    | triangle                                    | cross          |             19 |         116.95 |           0 |             0.00 |
|    40 |        0.05 | Success | asterisk                                    | asterisk       |              6 |          39.70 |           0 |             0.00 |
|    41 |        0.05 | Fail    | circle                                      | diamond        |              9 |          79.45 |           0 |             0.00 |
|    42 |        0.05 | Fail    | circle                                      | triangle       |             14 |         237.32 |           0 |             0.00 |
|    43 |        0.05 | Fail    | cross                                       | square         |             22 |         124.95 |           0 |             0.00 |
|    44 |        0.05 | Fail    | diamond                                     | asterisk       |             13 |          85.19 |           0 |             0.00 |
|    45 |        0.05 | Fail    | circle                                      | square         |             22 |         175.36 |           0 |             0.00 |
|    46 |        0.05 | Fail    | square                                      | asterisk       |             23 |         203.10 |           0 |             0.00 |
|    47 |        0.05 | Fail    | asterisk                                    | circle         |             35 |         816.88 |           0 |             0.00 |
|    48 |        0.05 | Success | square                                      | square         |              9 |          58.72 |           0 |             0.00 |
|    49 |        0.05 | Success | diamond                                     | diamond        |             19 |         257.48 |           0 |             0.00 |
|    50 |        0.05 | Fail    | diamond                                     | cross          |             13 |          86.64 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    19 | Agent4               | 2026-05-15T04:37:33.976864+00:00 | 2026-05-15T04:37:35.981076+00:00 |             2.00 |
```
