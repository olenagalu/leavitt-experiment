# Y topology auto-trial report

## Summary

- Batch: `temperature-0.1`
- Temperature: 0.1
- Completed trials: 50/50
- Average time: 194.69 seconds
- Average total messages: 17.00
- Success rate: 17/50 (34.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     174 |           174 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     160 |           160 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      82 |           170 |        48.2% (0.482) |                0.333 | 1.447 |                0.481 |
| y        | Agent3 | Agent2    |                  3 |      61 |           170 |        35.9% (0.359) |                0.333 | 1.076 |                0.359 |
| y        | Agent3 | Agent4    |                  3 |      27 |           170 |        15.9% (0.159) |                0.333 | 0.476 |                0.160 |
| y        | Agent4 | Agent3    |                  2 |     141 |           160 |        88.1% (0.881) |                0.500 | 1.762 |                0.879 |
| y        | Agent4 | Agent5    |                  2 |      19 |           160 |        11.9% (0.119) |                0.500 | 0.237 |                0.121 |
| y        | Agent5 | Agent4    |                  1 |     165 |           165 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent1 | client_assigned |     6 |
| y        | Agent3 | client_assigned |     6 |
| y        | Agent4 | client_assigned |     6 |
| y        | Agent5 | client_assigned |     3 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.1 | Success | circle                                      | circle         |             15 |         617.79 |           0 |             0.00 |
|     2 |         0.1 | Fail    | square                                      | diamond        |              8 |          48.76 |           0 |             0.00 |
|     3 |         0.1 | Fail    | cross                                       | square         |             15 |          86.47 |           0 |             0.00 |
|     4 |         0.1 | Fail    | diamond                                     | asterisk       |             15 |          84.00 |           0 |             0.00 |
|     5 |         0.1 | Fail    | cross                                       | square         |              8 |          55.31 |           0 |             0.00 |
|     6 |         0.1 | Fail    | square                                      | triangle       |             15 |          89.25 |           0 |             0.00 |
|     7 |         0.1 | Success | asterisk                                    | asterisk       |             20 |         115.32 |           0 |             0.00 |
|     8 |         0.1 | Success | cross                                       | cross          |             35 |         200.62 |           0 |             0.00 |
|     9 |         0.1 | Fail    | circle                                      | diamond        |             17 |         120.19 |           0 |             0.00 |
|    10 |         0.1 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        1297.29 |           0 |             0.00 |
|    11 |         0.1 | Success | triangle                                    | triangle       |             16 |         418.33 |           0 |             0.00 |
|    12 |         0.1 | Fail    | asterisk                                    | square         |             25 |         139.52 |           0 |             0.00 |
|    13 |         0.1 | Success | diamond                                     | diamond        |             14 |          82.16 |           0 |             0.00 |
|    14 |         0.1 | Success | diamond                                     | diamond        |              7 |          41.61 |           0 |             0.00 |
|    15 |         0.1 | Success | cross                                       | cross          |              9 |          53.57 |           0 |             0.00 |
|    16 |         0.1 | Fail    | triangle                                    | asterisk       |             20 |         116.64 |           0 |             0.00 |
|    17 |         0.1 | Fail    | circle                                      | triangle       |             12 |          71.98 |           0 |             0.00 |
|    18 |         0.1 | Success | square                                      | square         |             11 |          74.33 |           0 |             0.00 |
|    19 |         0.1 | Fail    | diamond                                     | square         |             14 |         288.37 |           0 |             0.00 |
|    20 |         0.1 | Success | diamond                                     | diamond        |             10 |         188.31 |           0 |             0.00 |
|    21 |         0.1 | Fail    | cross                                       | circle         |             24 |         224.87 |           0 |             0.00 |
|    22 |         0.1 | Fail    | cross                                       | square         |              6 |         104.94 |           0 |             0.00 |
|    23 |         0.1 | Fail    | square                                      | diamond        |             36 |         475.32 |           0 |             0.00 |
|    24 |         0.1 | Fail    | asterisk                                    | diamond        |             13 |          78.41 |           0 |             0.00 |
|    25 |         0.1 | Fail    | circle                                      | asterisk       |             14 |          83.76 |           0 |             0.00 |
|    26 |         0.1 | Fail    | triangle                                    | asterisk       |             15 |          91.37 |           0 |             0.00 |
|    27 |         0.1 | Fail    | square                                      | cross          |             17 |         111.68 |           0 |             0.00 |
|    28 |         0.1 | Fail    | cross                                       | triangle       |             16 |         274.23 |           0 |             0.00 |
|    29 |         0.1 | Fail    | square                                      | triangle       |              7 |         166.17 |           0 |             0.00 |
|    30 |         0.1 | Fail    | circle                                      | diamond        |             17 |         101.08 |           0 |             0.00 |
|    31 |         0.1 | Fail    | circle                                      | cross          |             19 |         123.01 |           0 |             0.00 |
|    32 |         0.1 | Success | cross                                       | cross          |             21 |         449.12 |           0 |             0.00 |
|    33 |         0.1 | Fail    | triangle                                    | circle         |              8 |          55.34 |           0 |             0.00 |
|    34 |         0.1 | Fail    | diamond                                     | asterisk       |             13 |          78.68 |           0 |             0.00 |
|    35 |         0.1 | Success | triangle                                    | triangle       |             13 |         140.27 |           0 |             0.00 |
|    36 |         0.1 | Success | circle                                      | circle         |             25 |         155.24 |           0 |             0.00 |
|    37 |         0.1 | Fail    | circle                                      | diamond        |             26 |         218.18 |           0 |             0.00 |
|    38 |         0.1 | Fail    | diamond                                     | square         |             13 |         159.88 |           0 |             0.00 |
|    39 |         0.1 | Success | circle                                      | circle         |             18 |         100.92 |           0 |             0.00 |
|    40 |         0.1 | Fail    | diamond                                     | circle         |             13 |          97.61 |           0 |             0.00 |
|    41 |         0.1 | Fail    | square                                      | triangle       |             28 |         271.78 |           0 |             0.00 |
|    42 |         0.1 | Success | square                                      | square         |              6 |          35.52 |           0 |             0.00 |
|    43 |         0.1 | Fail    | diamond                                     | triangle       |             13 |          75.18 |           0 |             0.00 |
|    44 |         0.1 | Fail    | triangle                                    | circle         |             12 |         100.76 |           0 |             0.00 |
|    45 |         0.1 | Fail    | diamond                                     | square         |             13 |         145.01 |           0 |             0.00 |
|    46 |         0.1 | Fail    | triangle                                    | cross          |             26 |         226.73 |           0 |             0.00 |
|    47 |         0.1 | Success | circle                                      | circle         |             23 |         812.76 |           0 |             0.00 |
|    48 |         0.1 | Fail    | circle                                      | square         |             19 |         355.79 |           0 |             0.00 |
|    49 |         0.1 | Success | circle                                      | circle         |             23 |         132.12 |           0 |             0.00 |
|    50 |         0.1 | Success | asterisk                                    | asterisk       |             17 |          99.12 |           0 |             0.00 |
```

## Reconnect details

No Jetson disconnects were recorded.
