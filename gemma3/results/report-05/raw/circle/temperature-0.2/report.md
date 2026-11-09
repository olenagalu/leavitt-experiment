# Circle auto-trial report

## Summary

- Batch: `temperature-0.2`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 181.16 seconds
- Average total messages: 16.00
- Success rate: 19/50 (38.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      51 |           163 |        31.3% (0.313) |                0.500 | 0.626 |                0.314 |
| circle   | Agent1 | Agent5    |                  2 |     112 |           163 |        68.7% (0.687) |                0.500 | 1.374 |                0.686 |
| circle   | Agent2 | Agent1    |                  2 |     132 |           147 |        89.8% (0.898) |                0.500 | 1.796 |                0.895 |
| circle   | Agent2 | Agent3    |                  2 |      15 |           147 |        10.2% (0.102) |                0.500 | 0.204 |                0.105 |
| circle   | Agent3 | Agent2    |                  2 |     176 |           180 |        97.8% (0.978) |                0.500 | 1.956 |                0.975 |
| circle   | Agent3 | Agent4    |                  2 |       4 |           180 |         2.2% (0.022) |                0.500 | 0.044 |                0.025 |
| circle   | Agent4 | Agent3    |                  2 |     127 |           159 |        79.9% (0.799) |                0.500 | 1.597 |                0.797 |
| circle   | Agent4 | Agent5    |                  2 |      32 |           159 |        20.1% (0.201) |                0.500 | 0.403 |                0.203 |
| circle   | Agent5 | Agent1    |                  2 |      52 |           151 |        34.4% (0.344) |                0.500 | 0.689 |                0.345 |
| circle   | Agent5 | Agent4    |                  2 |      99 |           151 |        65.6% (0.656) |                0.500 | 1.311 |                0.655 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.2 | Fail    | asterisk                                    | cross          |             21 |         326.86 |           0 |             0.00 |
|     2 |         0.2 | Success | triangle                                    | triangle       |             15 |          82.63 |           0 |             0.00 |
|     3 |         0.2 | Fail    | square                                      | diamond        |             33 |         185.25 |           0 |             0.00 |
|     4 |         0.2 | Success | triangle                                    | triangle       |             10 |          57.91 |           0 |             0.00 |
|     5 |         0.2 | Fail    | square                                      | circle         |             21 |         116.07 |           0 |             0.00 |
|     6 |         0.2 | Fail    | triangle                                    | circle         |             16 |          92.49 |           0 |             0.00 |
|     7 |         0.2 | Success | cross                                       | cross          |             11 |          63.71 |           0 |             0.00 |
|     8 |         0.2 | Fail    | diamond                                     | square         |             13 |          77.81 |           0 |             0.00 |
|     9 |         0.2 | Success | square                                      | square         |             35 |         191.09 |           0 |             0.00 |
|    10 |         0.2 | Fail    | square                                      | diamond        |              8 |          51.13 |           0 |             0.00 |
|    11 |         0.2 | Fail    | cross                                       | asterisk       |              9 |          57.67 |           0 |             0.00 |
|    12 |         0.2 | Fail    | circle                                      | diamond        |              7 |         422.87 |           0 |             0.00 |
|    13 |         0.2 | Fail    | asterisk                                    | diamond        |             15 |         396.43 |           0 |             0.00 |
|    14 |         0.2 | Success | cross                                       | cross          |             17 |         289.13 |           0 |             0.00 |
|    15 |         0.2 | Success | cross                                       | cross          |             12 |         676.25 |           0 |             0.00 |
|    16 |         0.2 | Success | square                                      | square         |             19 |         155.13 |           0 |             0.00 |
|    17 |         0.2 | Success | cross                                       | cross          |             24 |         137.60 |           0 |             0.00 |
|    18 |         0.2 | Fail    | asterisk                                    | square         |             18 |         102.95 |           0 |             0.00 |
|    19 |         0.2 | Fail    | cross                                       | square         |             19 |         109.96 |           0 |             0.00 |
|    20 |         0.2 | Fail    | circle                                      | triangle       |              5 |          29.41 |           0 |             0.00 |
|    21 |         0.2 | Fail    | cross                                       | circle         |              4 |          23.83 |           0 |             0.00 |
|    22 |         0.2 | Fail    | cross                                       | asterisk       |              5 |          30.25 |           0 |             0.00 |
|    23 |         0.2 | Success | square                                      | square         |             16 |          94.57 |           0 |             0.00 |
|    24 |         0.2 | Success | diamond                                     | diamond        |             25 |         140.47 |           0 |             0.00 |
|    25 |         0.2 | Fail    | circle                                      | cross          |              7 |          51.29 |           0 |             0.00 |
|    26 |         0.2 | Fail    | cross                                       | asterisk       |             16 |         411.69 |           0 |             0.00 |
|    27 |         0.2 | Fail    | diamond                                     | asterisk       |             17 |         618.72 |           0 |             0.00 |
|    28 |         0.2 | Success | cross                                       | cross          |             21 |         525.56 |           0 |             0.00 |
|    29 |         0.2 | Fail    | cross                                       | square         |             16 |         238.47 |           0 |             0.00 |
|    30 |         0.2 | Fail    | cross                                       | asterisk       |             10 |          54.71 |           0 |             0.00 |
|    31 |         0.2 | Success | cross                                       | cross          |             18 |         104.11 |           0 |             0.00 |
|    32 |         0.2 | Success | triangle                                    | triangle       |             15 |          86.31 |           0 |             0.00 |
|    33 |         0.2 | Fail    | triangle                                    | asterisk       |              9 |          51.64 |           0 |             0.00 |
|    34 |         0.2 | Fail    | cross                                       | square         |              7 |          41.76 |           0 |             0.00 |
|    35 |         0.2 | Fail    | diamond                                     | asterisk       |             14 |          81.34 |           0 |             0.00 |
|    36 |         0.2 | Fail    | square                                      | triangle       |             12 |          72.60 |           0 |             0.00 |
|    37 |         0.2 | Fail    | cross                                       | square         |              9 |          70.13 |           0 |             0.00 |
|    38 |         0.2 | Success | square                                      | square         |             18 |         192.55 |           0 |             0.00 |
|    39 |         0.2 | Success | circle                                      | circle         |             20 |         150.12 |           0 |             0.00 |
|    40 |         0.2 | Fail    | diamond                                     | triangle       |              8 |         259.24 |           0 |             0.00 |
|    41 |         0.2 | Fail    | square                                      | asterisk       |             35 |         468.34 |           0 |             0.00 |
|    42 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             40 |         930.03 |           0 |             0.00 |
|    43 |         0.2 | Success | diamond                                     | diamond        |             21 |         121.15 |           0 |             0.00 |
|    44 |         0.2 | Success | asterisk                                    | asterisk       |             23 |         133.61 |           0 |             0.00 |
|    45 |         0.2 | Success | diamond                                     | diamond        |             19 |         104.43 |           0 |             0.00 |
|    46 |         0.2 | Fail    | circle                                      | square         |              7 |          41.58 |           0 |             0.00 |
|    47 |         0.2 | Fail    | circle                                      | asterisk       |              8 |          46.38 |           0 |             0.00 |
|    48 |         0.2 | Fail    | asterisk                                    | circle         |             14 |          81.68 |           0 |             0.00 |
|    49 |         0.2 | Success | triangle                                    | triangle       |             32 |         174.19 |           0 |             0.00 |
|    50 |         0.2 | Fail    | asterisk                                    | square         |              6 |          34.86 |           0 |             0.00 |
```

## Reconnect details

No Jetson disconnects were recorded.
