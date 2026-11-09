# Y topology auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 74.31 seconds
- Average total messages: 17.04
- Success rate: 13/50 (26.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     168 |           168 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     164 |           164 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      71 |           167 |        42.5% (0.425) |                0.333 | 1.275 |                0.424 |
| y        | Agent3 | Agent2    |                  3 |      63 |           167 |        37.7% (0.377) |                0.333 | 1.132 |                0.377 |
| y        | Agent3 | Agent4    |                  3 |      33 |           167 |        19.8% (0.198) |                0.333 | 0.593 |                0.199 |
| y        | Agent4 | Agent3    |                  2 |     128 |           168 |        76.2% (0.762) |                0.500 | 1.524 |                0.760 |
| y        | Agent4 | Agent5    |                  2 |      40 |           168 |        23.8% (0.238) |                0.500 | 0.476 |                0.240 |
| y        | Agent5 | Agent4    |                  1 |     184 |           184 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent3 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- |
|     1 |           0 | Fail    | circle                                      | triangle       |             21 |         275.27 |
|     2 |           0 | Success | square                                      | square         |              9 |          37.87 |
|     3 |           0 | Success | diamond                                     | diamond        |             17 |          74.09 |
|     4 |           0 | Fail    | circle                                      | triangle       |             34 |         140.39 |
|     5 |           0 | Fail    | circle                                      | square         |             12 |          50.16 |
|     6 |           0 | Fail    | circle                                      | triangle       |             15 |          61.36 |
|     7 |           0 | Fail    | diamond                                     | square         |             15 |          64.29 |
|     8 |           0 | Fail    | triangle                                    | diamond        |             14 |          66.06 |
|     9 |           0 | Fail    | cross                                       | diamond        |             10 |          43.12 |
|    10 |           0 | Success | circle                                      | circle         |             18 |          75.44 |
|    11 |           0 | Fail    | circle                                      | cross          |             23 |          98.31 |
|    12 |           0 | Success | cross                                       | cross          |              8 |          34.66 |
|    13 |           0 | Fail    | square                                      | triangle       |             16 |          59.37 |
|    14 |           0 | Fail    | square                                      | cross          |             11 |          49.23 |
|    15 |           0 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |         201.89 |
|    16 |           0 | Fail    | triangle                                    | diamond        |             12 |          51.13 |
|    17 |           0 | Fail    | cross                                       | circle         |             23 |          98.70 |
|    18 |           0 | Fail    | diamond                                     | cross          |             13 |          47.97 |
|    19 |           0 | Fail    | asterisk                                    | circle         |             14 |          57.90 |
|    20 |           0 | Success | cross                                       | cross          |             10 |          44.02 |
|    21 |           0 | Fail    | diamond                                     | cross          |              9 |          38.00 |
|    22 |           0 | Success | asterisk                                    | asterisk       |             22 |          94.25 |
|    23 |           0 | Fail    | asterisk                                    | triangle       |             20 |          79.21 |
|    24 |           0 | Fail    | diamond                                     | square         |             16 |          62.83 |
|    25 |           0 | Fail    | cross                                       | triangle       |             16 |          68.13 |
|    26 |           0 | Fail    | square                                      | circle         |             13 |          56.14 |
|    27 |           0 | Fail    | square                                      | diamond        |             12 |          49.51 |
|    28 |           0 | Fail    | cross                                       | asterisk       |             16 |          67.74 |
|    29 |           0 | Success | square                                      | square         |             26 |         100.99 |
|    30 |           0 | Fail    | diamond                                     | circle         |             17 |          75.49 |
|    31 |           0 | Success | circle                                      | circle         |             19 |          82.11 |
|    32 |           0 | Fail    | asterisk                                    | diamond        |             11 |          44.68 |
|    33 |           0 | Fail    | diamond                                     | asterisk       |             14 |          60.12 |
|    34 |           0 | Success | triangle                                    | triangle       |              8 |          34.37 |
|    35 |           0 | Fail    | triangle                                    | circle         |             20 |          79.62 |
|    36 |           0 | Fail    | square                                      | triangle       |             20 |          80.76 |
|    37 |           0 | Success | square                                      | square         |              8 |          34.17 |
|    38 |           0 | Fail    | circle                                      | square         |             21 |          84.38 |
|    39 |           0 | Fail    | diamond                                     | asterisk       |             10 |          44.49 |
|    40 |           0 | Fail    | No figure submitted (message limit reached) | cross          |             50 |         186.35 |
|    41 |           0 | Success | diamond                                     | diamond        |             25 |         101.60 |
|    42 |           0 | Fail    | triangle                                    | circle         |             12 |          53.50 |
|    43 |           0 | Fail    | circle                                      | cross          |             26 |         100.08 |
|    44 |           0 | Fail    | square                                      | triangle       |             21 |          89.59 |
|    45 |           0 | Fail    | diamond                                     | cross          |             14 |          55.64 |
|    46 |           0 | Success | diamond                                     | diamond        |              7 |          29.57 |
|    47 |           0 | Fail    | cross                                       | diamond        |             13 |          56.81 |
|    48 |           0 | Fail    | cross                                       | asterisk       |              8 |          36.90 |
|    49 |           0 | Fail    | circle                                      | cross          |             24 |          96.87 |
|    50 |           0 | Success | circle                                      | circle         |              9 |          40.14 |
```
