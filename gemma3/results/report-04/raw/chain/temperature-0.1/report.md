# Chain auto-trial report

## Summary

- Batch: `temperature-0.1`
- Temperature: 0.1
- Completed trials: 50/50
- Average time: 202.54 seconds
- Average total messages: 18.76
- Success rate: 10/50 (20.0%)
- Reconnect pauses: 1 across 1 trial(s); 46.05 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     165 |           165 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     140 |           159 |        88.1% (0.881) |                0.500 | 1.761 |                0.878 |
| chain    | Agent2 | Agent3    |                  2 |      19 |           159 |        11.9% (0.119) |                0.500 | 0.239 |                0.122 |
| chain    | Agent3 | Agent2    |                  2 |     204 |           210 |        97.1% (0.971) |                0.500 | 1.943 |                0.969 |
| chain    | Agent3 | Agent4    |                  2 |       6 |           210 |         2.9% (0.029) |                0.500 | 0.057 |                0.031 |
| chain    | Agent4 | Agent3    |                  2 |     152 |           188 |        80.9% (0.809) |                0.500 | 1.617 |                0.807 |
| chain    | Agent4 | Agent5    |                  2 |      36 |           188 |        19.1% (0.191) |                0.500 | 0.383 |                0.193 |
| chain    | Agent5 | Agent4    |                  1 |     209 |           209 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| chain    | Agent2 | client_assigned |     1 |
| chain    | Agent3 | client_assigned |     2 |
| chain    | Agent4 | client_assigned |     2 |
| chain    | Agent5 | client_assigned |     2 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.1 | Fail    | asterisk                                    | square         |              9 |         288.81 |           0 |             0.00 |
|     2 |         0.1 | Fail    | triangle                                    | diamond        |             20 |         112.35 |           0 |             0.00 |
|     3 |         0.1 | Fail    | cross                                       | asterisk       |             15 |          87.43 |           0 |             0.00 |
|     4 |         0.1 | Fail    | asterisk                                    | cross          |             14 |          79.01 |           0 |             0.00 |
|     5 |         0.1 | Fail    | diamond                                     | square         |             19 |         108.22 |           0 |             0.00 |
|     6 |         0.1 | Fail    | asterisk                                    | triangle       |             19 |         110.87 |           0 |             0.00 |
|     7 |         0.1 | Fail    | circle                                      | square         |             16 |          91.10 |           0 |             0.00 |
|     8 |         0.1 | Fail    | circle                                      | asterisk       |             15 |          90.94 |           0 |             0.00 |
|     9 |         0.1 | Success | triangle                                    | triangle       |             22 |         125.37 |           0 |             0.00 |
|    10 |         0.1 | Fail    | diamond                                     | asterisk       |             12 |          70.80 |           0 |             0.00 |
|    11 |         0.1 | Fail    | square                                      | triangle       |             10 |          64.37 |           0 |             0.00 |
|    12 |         0.1 | Success | cross                                       | cross          |             32 |         491.92 |           0 |             0.00 |
|    13 |         0.1 | Fail    | triangle                                    | diamond        |             20 |         368.92 |           1 |            46.05 |
|    14 |         0.1 | Fail    | square                                      | cross          |             20 |         149.58 |           0 |             0.00 |
|    15 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        1924.07 |           0 |             0.00 |
|    16 |         0.1 | Fail    | square                                      | triangle       |             27 |         144.06 |           0 |             0.00 |
|    17 |         0.1 | Fail    | diamond                                     | cross          |             13 |          74.87 |           0 |             0.00 |
|    18 |         0.1 | Fail    | diamond                                     | square         |              9 |          51.22 |           0 |             0.00 |
|    19 |         0.1 | Fail    | diamond                                     | triangle       |             31 |         171.98 |           0 |             0.00 |
|    20 |         0.1 | Fail    | square                                      | circle         |             18 |         103.33 |           0 |             0.00 |
|    21 |         0.1 | Fail    | asterisk                                    | circle         |             11 |          63.68 |           0 |             0.00 |
|    22 |         0.1 | Success | triangle                                    | triangle       |             16 |          93.19 |           0 |             0.00 |
|    23 |         0.1 | Fail    | square                                      | diamond        |             12 |          72.20 |           0 |             0.00 |
|    24 |         0.1 | Success | triangle                                    | triangle       |             30 |         168.75 |           0 |             0.00 |
|    25 |         0.1 | Fail    | square                                      | asterisk       |             23 |         248.20 |           0 |             0.00 |
|    26 |         0.1 | Success | circle                                      | circle         |             20 |         204.65 |           0 |             0.00 |
|    27 |         0.1 | Fail    | diamond                                     | circle         |             27 |         233.27 |           0 |             0.00 |
|    28 |         0.1 | Fail    | diamond                                     | square         |             22 |         188.20 |           0 |             0.00 |
|    29 |         0.1 | Fail    | square                                      | circle         |              9 |         106.64 |           0 |             0.00 |
|    30 |         0.1 | Fail    | cross                                       | asterisk       |             22 |         178.30 |           0 |             0.00 |
|    31 |         0.1 | Fail    | cross                                       | circle         |              9 |          53.10 |           0 |             0.00 |
|    32 |         0.1 | Fail    | square                                      | circle         |             17 |          95.79 |           0 |             0.00 |
|    33 |         0.1 | Fail    | triangle                                    | diamond        |             25 |         138.56 |           0 |             0.00 |
|    34 |         0.1 | Fail    | square                                      | cross          |             11 |          68.08 |           0 |             0.00 |
|    35 |         0.1 | Fail    | triangle                                    | cross          |             23 |         694.09 |           0 |             0.00 |
|    36 |         0.1 | Success | square                                      | square         |             20 |         111.73 |           0 |             0.00 |
|    37 |         0.1 | Fail    | cross                                       | diamond        |             24 |         136.39 |           0 |             0.00 |
|    38 |         0.1 | Success | triangle                                    | triangle       |              8 |          46.74 |           0 |             0.00 |
|    39 |         0.1 | Fail    | cross                                       | circle         |             12 |          66.31 |           0 |             0.00 |
|    40 |         0.1 | Success | square                                      | square         |             16 |          86.42 |           0 |             0.00 |
|    41 |         0.1 | Success | diamond                                     | diamond        |             17 |          95.55 |           0 |             0.00 |
|    42 |         0.1 | Fail    | square                                      | asterisk       |             17 |          93.11 |           0 |             0.00 |
|    43 |         0.1 | Fail    | asterisk                                    | square         |             14 |          84.82 |           0 |             0.00 |
|    44 |         0.1 | Fail    | circle                                      | diamond        |             12 |          72.21 |           0 |             0.00 |
|    45 |         0.1 | Fail    | circle                                      | triangle       |             15 |          87.89 |           0 |             0.00 |
|    46 |         0.1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1238.58 |           0 |             0.00 |
|    47 |         0.1 | Fail    | triangle                                    | square         |             12 |         249.34 |           0 |             0.00 |
|    48 |         0.1 | Success | triangle                                    | triangle       |             19 |         101.43 |           0 |             0.00 |
|    49 |         0.1 | Fail    | square                                      | circle         |             19 |         106.88 |           0 |             0.00 |
|    50 |         0.1 | Fail    | cross                                       | triangle       |             15 |         233.81 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    13 | Agent4               | 2026-05-13T22:00:34.023799+00:00 | 2026-05-13T22:01:20.077444+00:00 |            46.05 |
```
