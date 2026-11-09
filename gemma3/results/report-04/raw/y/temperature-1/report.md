# Y topology auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 246.11 seconds
- Average total messages: 20.22
- Success rate: 12/50 (24.0%)
- Reconnect pauses: 2 across 2 trial(s); 67.08 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     199 |           199 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     221 |           221 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      86 |           195 |        44.1% (0.441) |                0.333 | 1.323 |                0.440 |
| y        | Agent3 | Agent2    |                  3 |      74 |           195 |        37.9% (0.379) |                0.333 | 1.138 |                0.379 |
| y        | Agent3 | Agent4    |                  3 |      35 |           195 |        17.9% (0.179) |                0.333 | 0.538 |                0.181 |
| y        | Agent4 | Agent3    |                  2 |     148 |           176 |        84.1% (0.841) |                0.500 | 1.682 |                0.839 |
| y        | Agent4 | Agent5    |                  2 |      28 |           176 |        15.9% (0.159) |                0.500 | 0.318 |                0.161 |
| y        | Agent5 | Agent4    |                  1 |     213 |           213 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent1 | client_assigned |     2 |
| y        | Agent2 | client_assigned |     3 |
| y        | Agent3 | client_assigned |     2 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           1 | Fail    | circle                                      | asterisk       |             18 |         363.11 |           0 |             0.00 |
|     2 |           1 | Fail    | cross                                       | triangle       |             25 |         140.80 |           0 |             0.00 |
|     3 |           1 | Success | cross                                       | cross          |             40 |         223.38 |           0 |             0.00 |
|     4 |           1 | Fail    | cross                                       | triangle       |             13 |          76.20 |           0 |             0.00 |
|     5 |           1 | Fail    | circle                                      | diamond        |             20 |         116.30 |           0 |             0.00 |
|     6 |           1 | Fail    | asterisk                                    | cross          |             16 |          92.90 |           0 |             0.00 |
|     7 |           1 | Fail    | diamond                                     | asterisk       |             12 |          73.16 |           0 |             0.00 |
|     8 |           1 | Fail    | cross                                       | square         |             10 |         113.37 |           0 |             0.00 |
|     9 |           1 | Success | circle                                      | circle         |             21 |         247.22 |           0 |             0.00 |
|    10 |           1 | Fail    | diamond                                     | asterisk       |             15 |         210.32 |           0 |             0.00 |
|    11 |           1 | Fail    | diamond                                     | circle         |             30 |         179.40 |           0 |             0.00 |
|    12 |           1 | Success | triangle                                    | triangle       |             28 |         633.88 |           0 |             0.00 |
|    13 |           1 | Fail    | cross                                       | circle         |             11 |         112.71 |           0 |             0.00 |
|    14 |           1 | Fail    | cross                                       | square         |              9 |          51.62 |           0 |             0.00 |
|    15 |           1 | Fail    | cross                                       | triangle       |             13 |          75.99 |           0 |             0.00 |
|    16 |           1 | Success | asterisk                                    | asterisk       |             40 |         212.24 |           0 |             0.00 |
|    17 |           1 | Fail    | diamond                                     | cross          |              6 |          36.94 |           0 |             0.00 |
|    18 |           1 | Fail    | circle                                      | asterisk       |             24 |         157.16 |           0 |             0.00 |
|    19 |           1 | Fail    | diamond                                     | circle         |             12 |         710.37 |           1 |            67.08 |
|    20 |           1 | Fail    | square                                      | diamond        |             23 |         134.18 |           0 |             0.00 |
|    21 |           1 | Fail    | circle                                      | diamond        |             16 |          93.88 |           0 |             0.00 |
|    22 |           1 | Fail    | cross                                       | circle         |             12 |          72.09 |           0 |             0.00 |
|    23 |           1 | Success | triangle                                    | triangle       |             12 |          70.78 |           0 |             0.00 |
|    24 |           1 | Fail    | asterisk                                    | circle         |             14 |          83.55 |           0 |             0.00 |
|    25 |           1 | Fail    | cross                                       | square         |             10 |          63.24 |           0 |             0.00 |
|    26 |           1 | Success | cross                                       | cross          |             23 |         131.94 |           0 |             0.00 |
|    27 |           1 | Success | square                                      | square         |              7 |          61.76 |           0 |             0.00 |
|    28 |           1 | Fail    | asterisk                                    | circle         |             25 |         666.44 |           0 |             0.00 |
|    29 |           1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        1468.25 |           1 |             0.00 |
|    30 |           1 | Fail    | square                                      | cross          |             15 |          83.91 |           0 |             0.00 |
|    31 |           1 | Fail    | diamond                                     | triangle       |             14 |          82.24 |           0 |             0.00 |
|    32 |           1 | Fail    | cross                                       | circle         |             26 |         146.07 |           0 |             0.00 |
|    33 |           1 | Fail    | triangle                                    | circle         |             11 |          65.62 |           0 |             0.00 |
|    34 |           1 | Fail    | diamond                                     | circle         |             22 |         128.42 |           0 |             0.00 |
|    35 |           1 | Fail    | triangle                                    | cross          |             46 |         261.39 |           0 |             0.00 |
|    36 |           1 | Success | circle                                      | circle         |             18 |         110.91 |           0 |             0.00 |
|    37 |           1 | Fail    | asterisk                                    | circle         |             15 |          94.55 |           0 |             0.00 |
|    38 |           1 | Fail    | square                                      | triangle       |             11 |         147.70 |           0 |             0.00 |
|    39 |           1 | Fail    | diamond                                     | cross          |             11 |          70.71 |           0 |             0.00 |
|    40 |           1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2071.55 |           0 |             0.00 |
|    41 |           1 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        1050.71 |           0 |             0.00 |
|    42 |           1 | Success | cross                                       | cross          |             13 |         149.68 |           0 |             0.00 |
|    43 |           1 | Fail    | cross                                       | circle         |             27 |         148.06 |           0 |             0.00 |
|    44 |           1 | Fail    | cross                                       | asterisk       |             21 |         120.85 |           0 |             0.00 |
|    45 |           1 | Success | square                                      | square         |             18 |         103.61 |           0 |             0.00 |
|    46 |           1 | Success | diamond                                     | diamond        |             23 |         130.23 |           0 |             0.00 |
|    47 |           1 | Fail    | circle                                      | square         |             14 |          85.08 |           0 |             0.00 |
|    48 |           1 | Fail    | triangle                                    | circle         |             15 |          88.98 |           0 |             0.00 |
|    49 |           1 | Success | triangle                                    | triangle       |             12 |          80.59 |           0 |             0.00 |
|    50 |           1 | Fail    | cross                                       | asterisk       |             24 |         411.67 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    19 | Agent4               | 2026-05-14T22:13:02.022612+00:00 | 2026-05-14T22:14:09.101165+00:00 |            67.08 |
|    29 | Agent4               | 2026-05-14T23:03:15.604634+00:00 | 2026-05-14T23:03:15.607353+00:00 |             0.00 |
```
