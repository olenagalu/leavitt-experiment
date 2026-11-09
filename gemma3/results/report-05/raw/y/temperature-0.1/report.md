# Y topology auto-trial report

## Summary

- Batch: `temperature-0.1`
- Temperature: 0.1
- Completed trials: 50/50
- Average time: 221.16 seconds
- Average total messages: 18.30
- Success rate: 16/50 (32.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     176 |           176 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     186 |           186 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      89 |           198 |        44.9% (0.449) |                0.333 | 1.348 |                0.449 |
| y        | Agent3 | Agent2    |                  3 |      76 |           198 |        38.4% (0.384) |                0.333 | 1.152 |                0.383 |
| y        | Agent3 | Agent4    |                  3 |      33 |           198 |        16.7% (0.167) |                0.333 | 0.500 |                0.168 |
| y        | Agent4 | Agent3    |                  2 |     125 |           144 |        86.8% (0.868) |                0.500 | 1.736 |                0.866 |
| y        | Agent4 | Agent5    |                  2 |      19 |           144 |        13.2% (0.132) |                0.500 | 0.264 |                0.134 |
| y        | Agent5 | Agent4    |                  1 |     204 |           204 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent1 | client_assigned |     2 |
| y        | Agent3 | client_assigned |     4 |
| y        | Agent4 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.1 | Fail    | cross                                       | triangle       |             40 |         559.54 |           0 |             0.00 |
|     2 |         0.1 | Fail    | square                                      | triangle       |             11 |          64.61 |           0 |             0.00 |
|     3 |         0.1 | Success | triangle                                    | triangle       |             17 |          99.48 |           0 |             0.00 |
|     4 |         0.1 | Fail    | square                                      | cross          |             10 |          59.48 |           0 |             0.00 |
|     5 |         0.1 | Fail    | diamond                                     | square         |             27 |         157.86 |           0 |             0.00 |
|     6 |         0.1 | Fail    | cross                                       | diamond        |             17 |         102.44 |           0 |             0.00 |
|     7 |         0.1 | Fail    | square                                      | triangle       |             19 |         108.43 |           0 |             0.00 |
|     8 |         0.1 | Fail    | cross                                       | square         |             17 |         103.45 |           0 |             0.00 |
|     9 |         0.1 | Fail    | square                                      | asterisk       |             17 |         113.70 |           0 |             0.00 |
|    10 |         0.1 | Fail    | square                                      | asterisk       |             19 |         338.05 |           0 |             0.00 |
|    11 |         0.1 | Success | diamond                                     | diamond        |             16 |         307.63 |           0 |             0.00 |
|    12 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2057.81 |           0 |             0.00 |
|    13 |         0.1 | Success | square                                      | square         |             19 |         245.31 |           0 |             0.00 |
|    14 |         0.1 | Success | diamond                                     | diamond        |              8 |          46.07 |           0 |             0.00 |
|    15 |         0.1 | Fail    | triangle                                    | square         |             19 |         108.08 |           0 |             0.00 |
|    16 |         0.1 | Fail    | diamond                                     | circle         |             17 |          99.68 |           0 |             0.00 |
|    17 |         0.1 | Success | cross                                       | cross          |             13 |          76.99 |           0 |             0.00 |
|    18 |         0.1 | Fail    | asterisk                                    | triangle       |             13 |          75.42 |           0 |             0.00 |
|    19 |         0.1 | Success | circle                                      | circle         |             10 |          62.25 |           0 |             0.00 |
|    20 |         0.1 | Fail    | cross                                       | diamond        |              9 |          76.86 |           0 |             0.00 |
|    21 |         0.1 | Fail    | square                                      | diamond        |              9 |         132.24 |           0 |             0.00 |
|    22 |         0.1 | Fail    | cross                                       | circle         |             13 |          89.18 |           0 |             0.00 |
|    23 |         0.1 | Fail    | cross                                       | asterisk       |             46 |         451.66 |           0 |             0.00 |
|    24 |         0.1 | Fail    | square                                      | cross          |             13 |         305.51 |           0 |             0.00 |
|    25 |         0.1 | Success | diamond                                     | diamond        |             16 |          94.57 |           0 |             0.00 |
|    26 |         0.1 | Fail    | asterisk                                    | square         |             22 |         124.43 |           0 |             0.00 |
|    27 |         0.1 | Fail    | cross                                       | diamond        |             17 |          97.55 |           0 |             0.00 |
|    28 |         0.1 | Fail    | triangle                                    | square         |             31 |         174.87 |           0 |             0.00 |
|    29 |         0.1 | Success | cross                                       | cross          |             18 |         141.65 |           0 |             0.00 |
|    30 |         0.1 | Fail    | cross                                       | diamond        |             27 |         226.39 |           0 |             0.00 |
|    31 |         0.1 | Fail    | diamond                                     | cross          |              9 |          55.73 |           0 |             0.00 |
|    32 |         0.1 | Fail    | diamond                                     | asterisk       |             23 |         203.95 |           0 |             0.00 |
|    33 |         0.1 | Fail    | triangle                                    | circle         |             40 |        1748.66 |           0 |             0.00 |
|    34 |         0.1 | Success | square                                      | square         |             18 |         191.26 |           0 |             0.00 |
|    35 |         0.1 | Fail    | diamond                                     | cross          |             12 |          63.69 |           0 |             0.00 |
|    36 |         0.1 | Success | diamond                                     | diamond        |             22 |         120.96 |           0 |             0.00 |
|    37 |         0.1 | Success | circle                                      | circle         |             14 |          81.38 |           0 |             0.00 |
|    38 |         0.1 | Fail    | diamond                                     | asterisk       |             16 |         114.02 |           0 |             0.00 |
|    39 |         0.1 | Success | circle                                      | circle         |             11 |         139.04 |           0 |             0.00 |
|    40 |         0.1 | Fail    | cross                                       | circle         |             20 |         118.24 |           0 |             0.00 |
|    41 |         0.1 | Success | cross                                       | cross          |             17 |          96.52 |           0 |             0.00 |
|    42 |         0.1 | Success | cross                                       | cross          |             16 |          91.79 |           0 |             0.00 |
|    43 |         0.1 | Fail    | diamond                                     | asterisk       |             15 |         160.10 |           0 |             0.00 |
|    44 |         0.1 | Fail    | circle                                      | triangle       |             16 |         352.90 |           0 |             0.00 |
|    45 |         0.1 | Success | asterisk                                    | asterisk       |             14 |         401.74 |           0 |             0.00 |
|    46 |         0.1 | Fail    | cross                                       | square         |             14 |          82.60 |           0 |             0.00 |
|    47 |         0.1 | Fail    | square                                      | triangle       |              9 |          52.87 |           0 |             0.00 |
|    48 |         0.1 | Fail    | square                                      | circle         |             12 |          72.18 |           0 |             0.00 |
|    49 |         0.1 | Success | cross                                       | cross          |             27 |         150.37 |           0 |             0.00 |
|    50 |         0.1 | Fail    | square                                      | diamond        |             10 |          58.64 |           0 |             0.00 |
```

## Reconnect details

No Jetson disconnects were recorded.
