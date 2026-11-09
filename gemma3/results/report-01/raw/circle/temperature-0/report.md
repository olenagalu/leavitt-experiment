# Circle auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 57.35 seconds
- Average total messages: 12.36
- Success rate: 10/50 (20.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      10 |           138 |         7.2% (0.072) |                0.500 | 0.145 |                0.076 |
| circle   | Agent1 | Agent5    |                  2 |     128 |           138 |        92.8% (0.928) |                0.500 | 1.855 |                0.924 |
| circle   | Agent2 | Agent1    |                  2 |     102 |           131 |        77.9% (0.779) |                0.500 | 1.557 |                0.777 |
| circle   | Agent2 | Agent3    |                  2 |      29 |           131 |        22.1% (0.221) |                0.500 | 0.443 |                0.223 |
| circle   | Agent3 | Agent2    |                  2 |     107 |           110 |        97.3% (0.973) |                0.500 | 1.945 |                0.968 |
| circle   | Agent3 | Agent4    |                  2 |       3 |           110 |         2.7% (0.027) |                0.500 | 0.055 |                0.032 |
| circle   | Agent4 | Agent3    |                  2 |      84 |           117 |        71.8% (0.718) |                0.500 | 1.436 |                0.716 |
| circle   | Agent4 | Agent5    |                  2 |      33 |           117 |        28.2% (0.282) |                0.500 | 0.564 |                0.284 |
| circle   | Agent5 | Agent1    |                  2 |      90 |           122 |        73.8% (0.738) |                0.500 | 1.475 |                0.736 |
| circle   | Agent5 | Agent4    |                  2 |      32 |           122 |        26.2% (0.262) |                0.500 | 0.525 |                0.264 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- |
|     1 |           0 | Fail    | circle                                      | cross          |              7 |         214.90 |
|     2 |           0 | Success | circle                                      | circle         |             16 |          68.28 |
|     3 |           0 | Fail    | asterisk                                    | square         |             15 |          62.76 |
|     4 |           0 | Fail    | square                                      | circle         |             18 |          76.22 |
|     5 |           0 | Fail    | asterisk                                    | square         |              5 |          23.34 |
|     6 |           0 | Fail    | triangle                                    | circle         |             14 |          60.69 |
|     7 |           0 | Success | square                                      | square         |             19 |          82.48 |
|     8 |           0 | Success | diamond                                     | diamond        |              5 |          23.55 |
|     9 |           0 | Fail    | triangle                                    | square         |             13 |          56.96 |
|    10 |           0 | Success | cross                                       | cross          |             10 |          42.93 |
|    11 |           0 | Fail    | diamond                                     | triangle       |             10 |          44.96 |
|    12 |           0 | Fail    | circle                                      | triangle       |             10 |          43.01 |
|    13 |           0 | Fail    | diamond                                     | cross          |              7 |          30.62 |
|    14 |           0 | Fail    | triangle                                    | cross          |             19 |          83.48 |
|    15 |           0 | Fail    | cross                                       | asterisk       |             11 |          48.39 |
|    16 |           0 | Fail    | cross                                       | diamond        |             10 |          46.03 |
|    17 |           0 | Fail    | circle                                      | asterisk       |              5 |          23.63 |
|    18 |           0 | Fail    | cross                                       | triangle       |             10 |          42.42 |
|    19 |           0 | Fail    | cross                                       | diamond        |              7 |          31.57 |
|    20 |           0 | Success | cross                                       | cross          |             18 |          79.82 |
|    21 |           0 | Fail    | cross                                       | triangle       |             12 |          52.24 |
|    22 |           0 | Fail    | square                                      | asterisk       |             15 |          64.82 |
|    23 |           0 | Fail    | cross                                       | triangle       |             12 |          50.85 |
|    24 |           0 | Fail    | circle                                      | cross          |             14 |          64.87 |
|    25 |           0 | Fail    | diamond                                     | triangle       |              7 |          30.48 |
|    26 |           0 | Fail    | circle                                      | asterisk       |             18 |          76.17 |
|    27 |           0 | Fail    | diamond                                     | square         |             21 |          88.33 |
|    28 |           0 | Fail    | diamond                                     | triangle       |             14 |          59.38 |
|    29 |           0 | Fail    | square                                      | diamond        |             14 |          60.59 |
|    30 |           0 | Success | diamond                                     | diamond        |              5 |          23.67 |
|    31 |           0 | Fail    | asterisk                                    | circle         |             10 |          45.01 |
|    32 |           0 | Fail    | No figure submitted (message limit reached) | diamond        |             40 |         158.60 |
|    33 |           0 | Fail    | diamond                                     | asterisk       |             11 |          47.53 |
|    34 |           0 | Success | circle                                      | circle         |              5 |          23.84 |
|    35 |           0 | Fail    | cross                                       | circle         |             23 |          97.77 |
|    36 |           0 | Fail    | circle                                      | cross          |              7 |          30.96 |
|    37 |           0 | Fail    | triangle                                    | diamond        |              7 |          32.20 |
|    38 |           0 | Fail    | square                                      | triangle       |              5 |          23.11 |
|    39 |           0 | Fail    | cross                                       | diamond        |             11 |          47.33 |
|    40 |           0 | Fail    | square                                      | triangle       |             10 |          44.86 |
|    41 |           0 | Fail    | triangle                                    | asterisk       |             10 |          44.66 |
|    42 |           0 | Fail    | square                                      | diamond        |             15 |          68.01 |
|    43 |           0 | Fail    | circle                                      | asterisk       |              5 |          23.61 |
|    44 |           0 | Fail    | cross                                       | circle         |             15 |          63.14 |
|    45 |           0 | Success | square                                      | square         |             10 |          45.38 |
|    46 |           0 | Fail    | circle                                      | square         |             11 |          47.51 |
|    47 |           0 | Success | circle                                      | circle         |             10 |          43.48 |
|    48 |           0 | Fail    | square                                      | circle         |             22 |          94.44 |
|    49 |           0 | Success | triangle                                    | triangle       |             16 |          64.94 |
|    50 |           0 | Fail    | square                                      | diamond        |             14 |          63.82 |
```
