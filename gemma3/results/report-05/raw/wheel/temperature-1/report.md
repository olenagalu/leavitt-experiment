# Wheel auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 248.53 seconds
- Average total messages: 17.82
- Success rate: 13/50 (26.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     157 |           157 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     187 |           187 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |      98 |           175 |        56.0% (0.560) |                0.250 | 2.240 |                0.556 |
| wheel    | Agent3 | Agent2    |                  4 |      59 |           175 |        33.7% (0.337) |                0.250 | 1.349 |                0.336 |
| wheel    | Agent3 | Agent4    |                  4 |       9 |           175 |         5.1% (0.051) |                0.250 | 0.206 |                0.054 |
| wheel    | Agent3 | Agent5    |                  4 |       9 |           175 |         5.1% (0.051) |                0.250 | 0.206 |                0.054 |
| wheel    | Agent4 | Agent3    |                  1 |     185 |           185 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     185 |           185 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
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
|     1 |           1 | Fail    | circle                                      | square         |             24 |         340.20 |           0 |             0.00 |
|     2 |           1 | Fail    | asterisk                                    | triangle       |             15 |          90.49 |           0 |             0.00 |
|     3 |           1 | Fail    | diamond                                     | square         |             11 |          64.15 |           0 |             0.00 |
|     4 |           1 | Success | cross                                       | cross          |              6 |          37.76 |           0 |             0.00 |
|     5 |           1 | Fail    | cross                                       | asterisk       |             19 |         121.50 |           0 |             0.00 |
|     6 |           1 | Fail    | cross                                       | asterisk       |             13 |          86.15 |           0 |             0.00 |
|     7 |           1 | Fail    | cross                                       | asterisk       |             13 |          75.68 |           0 |             0.00 |
|     8 |           1 | Fail    | cross                                       | triangle       |             13 |          82.56 |           0 |             0.00 |
|     9 |           1 | Success | circle                                      | circle         |             23 |         218.78 |           0 |             0.00 |
|    10 |           1 | Fail    | circle                                      | asterisk       |             13 |          80.87 |           0 |             0.00 |
|    11 |           1 | Fail    | triangle                                    | cross          |             12 |         105.14 |           0 |             0.00 |
|    12 |           1 | Fail    | asterisk                                    | cross          |             45 |        2479.98 |           0 |             0.00 |
|    13 |           1 | Success | cross                                       | cross          |             10 |         119.71 |           0 |             0.00 |
|    14 |           1 | Fail    | circle                                      | diamond        |             19 |         116.13 |           0 |             0.00 |
|    15 |           1 | Success | square                                      | square         |              9 |          58.71 |           0 |             0.00 |
|    16 |           1 | Success | asterisk                                    | asterisk       |              8 |          52.47 |           0 |             0.00 |
|    17 |           1 | Success | asterisk                                    | asterisk       |             12 |          79.55 |           0 |             0.00 |
|    18 |           1 | Fail    | circle                                      | cross          |             22 |         141.43 |           0 |             0.00 |
|    19 |           1 | Fail    | cross                                       | circle         |             21 |         279.06 |           0 |             0.00 |
|    20 |           1 | Success | diamond                                     | diamond        |             22 |         439.33 |           0 |             0.00 |
|    21 |           1 | Fail    | square                                      | triangle       |             13 |          78.15 |           0 |             0.00 |
|    22 |           1 | Fail    | asterisk                                    | circle         |             20 |         171.06 |           0 |             0.00 |
|    23 |           1 | Fail    | cross                                       | triangle       |              9 |         330.93 |           0 |             0.00 |
|    24 |           1 | Fail    | diamond                                     | cross          |             18 |         303.28 |           0 |             0.00 |
|    25 |           1 | Fail    | circle                                      | cross          |              9 |         124.77 |           0 |             0.00 |
|    26 |           1 | Fail    | triangle                                    | diamond        |             24 |         150.90 |           0 |             0.00 |
|    27 |           1 | Fail    | circle                                      | square         |             10 |          66.30 |           0 |             0.00 |
|    28 |           1 | Fail    | triangle                                    | square         |             24 |         148.90 |           0 |             0.00 |
|    29 |           1 | Fail    | triangle                                    | circle         |             12 |          75.28 |           0 |             0.00 |
|    30 |           1 | Fail    | cross                                       | triangle       |             29 |         176.03 |           0 |             0.00 |
|    31 |           1 | Fail    | circle                                      | cross          |             15 |         155.41 |           0 |             0.00 |
|    32 |           1 | Fail    | diamond                                     | circle         |             12 |          81.14 |           0 |             0.00 |
|    33 |           1 | Fail    | triangle                                    | diamond        |              9 |         370.90 |           0 |             0.00 |
|    34 |           1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1193.57 |           0 |             0.00 |
|    35 |           1 | Fail    | circle                                      | diamond        |             16 |         117.78 |           0 |             0.00 |
|    36 |           1 | Fail    | diamond                                     | triangle       |             13 |         279.38 |           0 |             0.00 |
|    37 |           1 | Success | square                                      | square         |             35 |        1098.74 |           0 |             0.00 |
|    38 |           1 | Success | circle                                      | circle         |             14 |          84.12 |           0 |             0.00 |
|    39 |           1 | Fail    | cross                                       | square         |              8 |          52.60 |           0 |             0.00 |
|    40 |           1 | Fail    | square                                      | asterisk       |             12 |          79.05 |           0 |             0.00 |
|    41 |           1 | Fail    | circle                                      | triangle       |             12 |          75.38 |           0 |             0.00 |
|    42 |           1 | Success | square                                      | square         |             35 |         211.71 |           0 |             0.00 |
|    43 |           1 | Fail    | triangle                                    | circle         |             15 |          90.96 |           0 |             0.00 |
|    44 |           1 | Success | circle                                      | circle         |             14 |         151.73 |           0 |             0.00 |
|    45 |           1 | Success | circle                                      | circle         |             17 |         107.20 |           0 |             0.00 |
|    46 |           1 | Success | square                                      | square         |             20 |         128.20 |           0 |             0.00 |
|    47 |           1 | Fail    | circle                                      | triangle       |             20 |         283.29 |           0 |             0.00 |
|    48 |           1 | Fail    | diamond                                     | triangle       |             41 |         961.36 |           0 |             0.00 |
|    49 |           1 | Fail    | cross                                       | triangle       |             24 |         140.98 |           0 |             0.00 |
|    50 |           1 | Fail    | diamond                                     | asterisk       |             11 |          67.70 |           0 |             0.00 |
```

## Reconnect details

No Jetson disconnects were recorded.
