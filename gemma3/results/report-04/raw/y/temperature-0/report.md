# Y topology auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 245.22 seconds
- Average total messages: 18.48
- Success rate: 14/50 (28.0%)
- Reconnect pauses: 1 across 1 trial(s); 62.07 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     176 |           176 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     174 |           174 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      92 |           181 |        50.8% (0.508) |                0.333 | 1.525 |                0.507 |
| y        | Agent3 | Agent2    |                  3 |      63 |           181 |        34.8% (0.348) |                0.333 | 1.044 |                0.348 |
| y        | Agent3 | Agent4    |                  3 |      26 |           181 |        14.4% (0.144) |                0.333 | 0.431 |                0.145 |
| y        | Agent4 | Agent3    |                  2 |     153 |           173 |        88.4% (0.884) |                0.500 | 1.769 |                0.882 |
| y        | Agent4 | Agent5    |                  2 |      20 |           173 |        11.6% (0.116) |                0.500 | 0.231 |                0.118 |
| y        | Agent5 | Agent4    |                  1 |     211 |           211 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent1 | client_assigned |     4 |
| y        | Agent3 | client_assigned |     4 |
| y        | Agent4 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Fail    | cross                                       | circle         |             19 |         355.21 |           0 |             0.00 |
|     2 |           0 | Fail    | diamond                                     | asterisk       |             15 |          85.29 |           0 |             0.00 |
|     3 |           0 | Fail    | circle                                      | diamond        |             11 |          65.25 |           0 |             0.00 |
|     4 |           0 | Success | diamond                                     | diamond        |             21 |         124.25 |           0 |             0.00 |
|     5 |           0 | Fail    | cross                                       | diamond        |             11 |          65.15 |           0 |             0.00 |
|     6 |           0 | Fail    | triangle                                    | asterisk       |             26 |         154.54 |           0 |             0.00 |
|     7 |           0 | Fail    | circle                                      | square         |             14 |          87.71 |           0 |             0.00 |
|     8 |           0 | Fail    | triangle                                    | square         |             10 |          59.21 |           0 |             0.00 |
|     9 |           0 | Fail    | cross                                       | square         |              8 |          52.31 |           0 |             0.00 |
|    10 |           0 | Fail    | circle                                      | square         |             20 |         199.80 |           0 |             0.00 |
|    11 |           0 | Fail    | diamond                                     | asterisk       |             22 |         285.24 |           0 |             0.00 |
|    12 |           0 | Fail    | cross                                       | triangle       |             17 |         235.17 |           0 |             0.00 |
|    13 |           0 | Fail    | No figure submitted (message limit reached) | square         |             50 |        1561.33 |           0 |             0.00 |
|    14 |           0 | Success | circle                                      | circle         |             12 |          67.06 |           0 |             0.00 |
|    15 |           0 | Fail    | square                                      | circle         |             20 |         115.42 |           0 |             0.00 |
|    16 |           0 | Fail    | diamond                                     | asterisk       |              7 |          45.17 |           0 |             0.00 |
|    17 |           0 | Fail    | circle                                      | asterisk       |              7 |          43.10 |           0 |             0.00 |
|    18 |           0 | Success | diamond                                     | diamond        |             22 |         122.75 |           0 |             0.00 |
|    19 |           0 | Success | circle                                      | circle         |             33 |         194.65 |           0 |             0.00 |
|    20 |           0 | Success | triangle                                    | triangle       |             15 |          92.32 |           0 |             0.00 |
|    21 |           0 | Fail    | circle                                      | square         |             23 |         131.17 |           0 |             0.00 |
|    22 |           0 | Fail    | square                                      | triangle       |             40 |        1091.32 |           0 |             0.00 |
|    23 |           0 | Success | cross                                       | cross          |             22 |         590.64 |           0 |             0.00 |
|    24 |           0 | Fail    | triangle                                    | circle         |             18 |         106.22 |           0 |             0.00 |
|    25 |           0 | Fail    | square                                      | triangle       |             34 |         813.93 |           0 |             0.00 |
|    26 |           0 | Fail    | triangle                                    | square         |              9 |          53.84 |           0 |             0.00 |
|    27 |           0 | Fail    | cross                                       | square         |             10 |          60.75 |           0 |             0.00 |
|    28 |           0 | Fail    | square                                      | cross          |             11 |          64.92 |           0 |             0.00 |
|    29 |           0 | Success | cross                                       | cross          |             17 |          99.50 |           0 |             0.00 |
|    30 |           0 | Fail    | square                                      | diamond        |              7 |          43.87 |           0 |             0.00 |
|    31 |           0 | Fail    | square                                      | asterisk       |             13 |          76.08 |           0 |             0.00 |
|    32 |           0 | Success | triangle                                    | triangle       |             10 |         163.63 |           0 |             0.00 |
|    33 |           0 | Fail    | triangle                                    | square         |              9 |         230.50 |           0 |             0.00 |
|    34 |           0 | Success | square                                      | square         |             14 |         211.87 |           0 |             0.00 |
|    35 |           0 | Fail    | cross                                       | square         |             11 |          70.85 |           0 |             0.00 |
|    36 |           0 | Fail    | cross                                       | asterisk       |             37 |        1180.79 |           0 |             0.00 |
|    37 |           0 | Success | square                                      | square         |             18 |         157.23 |           0 |             0.00 |
|    38 |           0 | Fail    | circle                                      | triangle       |             11 |          64.06 |           0 |             0.00 |
|    39 |           0 | Fail    | cross                                       | circle         |             21 |         124.18 |           0 |             0.00 |
|    40 |           0 | Fail    | circle                                      | square         |             21 |         121.09 |           0 |             0.00 |
|    41 |           0 | Success | triangle                                    | triangle       |              6 |          46.84 |           0 |             0.00 |
|    42 |           0 | Fail    | triangle                                    | asterisk       |             22 |         288.58 |           1 |            62.07 |
|    43 |           0 | Fail    | circle                                      | cross          |             32 |         184.21 |           0 |             0.00 |
|    44 |           0 | Fail    | asterisk                                    | triangle       |             15 |          87.96 |           0 |             0.00 |
|    45 |           0 | Success | asterisk                                    | asterisk       |             11 |          66.52 |           0 |             0.00 |
|    46 |           0 | Success | circle                                      | circle         |             19 |         200.74 |           0 |             0.00 |
|    47 |           0 | Fail    | cross                                       | asterisk       |             38 |        1207.84 |           0 |             0.00 |
|    48 |           0 | Fail    | asterisk                                    | circle         |             23 |         462.00 |           0 |             0.00 |
|    49 |           0 | Success | diamond                                     | diamond        |             10 |          59.43 |           0 |             0.00 |
|    50 |           0 | Fail    | square                                      | circle         |             32 |         189.70 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    42 | Agent4               | 2026-05-14T09:24:35.948878+00:00 | 2026-05-14T09:25:38.019930+00:00 |            62.07 |
```
