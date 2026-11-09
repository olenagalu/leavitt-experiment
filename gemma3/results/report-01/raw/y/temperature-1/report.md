# Y topology auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 81.41 seconds
- Average total messages: 18.78
- Success rate: 19/50 (38.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     205 |           205 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     181 |           181 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      83 |           195 |        42.6% (0.426) |                0.333 | 1.277 |                0.425 |
| y        | Agent3 | Agent2    |                  3 |      75 |           195 |        38.5% (0.385) |                0.333 | 1.154 |                0.384 |
| y        | Agent3 | Agent4    |                  3 |      37 |           195 |        19.0% (0.190) |                0.333 | 0.569 |                0.191 |
| y        | Agent4 | Agent3    |                  2 |     151 |           183 |        82.5% (0.825) |                0.500 | 1.650 |                0.823 |
| y        | Agent4 | Agent5    |                  2 |      32 |           183 |        17.5% (0.175) |                0.500 | 0.350 |                0.177 |
| y        | Agent5 | Agent4    |                  1 |     175 |           175 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- |
|     1 |           1 | Fail    | diamond                                     | circle         |             21 |         259.12 |
|     2 |           1 | Success | diamond                                     | diamond        |             14 |          56.03 |
|     3 |           1 | Success | diamond                                     | diamond        |             11 |          48.61 |
|     4 |           1 | Success | circle                                      | circle         |             24 |          96.17 |
|     5 |           1 | Fail    | triangle                                    | diamond        |             27 |         103.16 |
|     6 |           1 | Success | triangle                                    | triangle       |             13 |          57.66 |
|     7 |           1 | Fail    | diamond                                     | cross          |             24 |          99.15 |
|     8 |           1 | Fail    | cross                                       | diamond        |             10 |          45.30 |
|     9 |           1 | Fail    | cross                                       | asterisk       |             22 |          89.97 |
|    10 |           1 | Fail    | asterisk                                    | triangle       |             30 |         124.83 |
|    11 |           1 | Success | cross                                       | cross          |             14 |          57.23 |
|    12 |           1 | Fail    | triangle                                    | cross          |             32 |         131.68 |
|    13 |           1 | Fail    | square                                      | circle         |             30 |         121.06 |
|    14 |           1 | Fail    | square                                      | asterisk       |             11 |          46.91 |
|    15 |           1 | Fail    | circle                                      | square         |             11 |          46.40 |
|    16 |           1 | Fail    | triangle                                    | circle         |             16 |          68.69 |
|    17 |           1 | Fail    | circle                                      | diamond        |             22 |          86.53 |
|    18 |           1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |         193.23 |
|    19 |           1 | Success | circle                                      | circle         |             13 |          59.28 |
|    20 |           1 | Success | asterisk                                    | asterisk       |             22 |          96.34 |
|    21 |           1 | Success | triangle                                    | triangle       |             12 |          56.64 |
|    22 |           1 | Fail    | circle                                      | triangle       |             13 |          59.61 |
|    23 |           1 | Fail    | square                                      | asterisk       |             22 |          88.81 |
|    24 |           1 | Success | cross                                       | cross          |             20 |          87.47 |
|    25 |           1 | Fail    | cross                                       | square         |             24 |          99.31 |
|    26 |           1 | Fail    | circle                                      | square         |             14 |          60.07 |
|    27 |           1 | Success | circle                                      | circle         |             14 |          54.35 |
|    28 |           1 | Fail    | circle                                      | diamond        |             26 |         110.94 |
|    29 |           1 | Success | circle                                      | circle         |             14 |          59.97 |
|    30 |           1 | Success | square                                      | square         |             10 |          44.21 |
|    31 |           1 | Fail    | triangle                                    | cross          |              8 |          34.82 |
|    32 |           1 | Success | cross                                       | cross          |             13 |          56.09 |
|    33 |           1 | Success | diamond                                     | diamond        |             16 |          67.50 |
|    34 |           1 | Fail    | square                                      | diamond        |             17 |          69.52 |
|    35 |           1 | Fail    | triangle                                    | circle         |             12 |          50.97 |
|    36 |           1 | Fail    | cross                                       | diamond        |             13 |          56.98 |
|    37 |           1 | Fail    | No figure submitted (message limit reached) | square         |             50 |         187.14 |
|    38 |           1 | Success | circle                                      | circle         |             15 |          67.12 |
|    39 |           1 | Fail    | cross                                       | asterisk       |             32 |         133.56 |
|    40 |           1 | Success | square                                      | square         |             16 |          65.05 |
|    41 |           1 | Success | diamond                                     | diamond        |             10 |          41.82 |
|    42 |           1 | Success | cross                                       | cross          |             21 |          87.03 |
|    43 |           1 | Fail    | triangle                                    | cross          |             18 |          72.87 |
|    44 |           1 | Fail    | cross                                       | triangle       |              6 |          26.84 |
|    45 |           1 | Fail    | square                                      | circle         |             18 |          76.32 |
|    46 |           1 | Fail    | asterisk                                    | triangle       |             15 |          65.05 |
|    47 |           1 | Fail    | triangle                                    | asterisk       |             40 |         160.47 |
|    48 |           1 | Fail    | circle                                      | asterisk       |              8 |          37.17 |
|    49 |           1 | Success | cross                                       | cross          |             10 |          44.43 |
|    50 |           1 | Fail    | diamond                                     | cross          |             15 |          60.98 |
```
