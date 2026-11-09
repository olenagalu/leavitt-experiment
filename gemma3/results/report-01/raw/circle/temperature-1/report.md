# Circle auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 51.49 seconds
- Average total messages: 10.96
- Success rate: 20/50 (40.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      27 |           124 |        21.8% (0.218) |                0.500 | 0.435 |                0.220 |
| circle   | Agent1 | Agent5    |                  2 |      97 |           124 |        78.2% (0.782) |                0.500 | 1.565 |                0.780 |
| circle   | Agent2 | Agent1    |                  2 |      98 |           118 |        83.1% (0.831) |                0.500 | 1.661 |                0.828 |
| circle   | Agent2 | Agent3    |                  2 |      20 |           118 |        16.9% (0.169) |                0.500 | 0.339 |                0.172 |
| circle   | Agent3 | Agent2    |                  2 |      94 |           101 |        93.1% (0.931) |                0.500 | 1.861 |                0.926 |
| circle   | Agent3 | Agent4    |                  2 |       7 |           101 |         6.9% (0.069) |                0.500 | 0.139 |                0.074 |
| circle   | Agent4 | Agent3    |                  2 |      77 |           101 |        76.2% (0.762) |                0.500 | 1.525 |                0.760 |
| circle   | Agent4 | Agent5    |                  2 |      24 |           101 |        23.8% (0.238) |                0.500 | 0.475 |                0.240 |
| circle   | Agent5 | Agent1    |                  2 |      69 |           104 |        66.3% (0.663) |                0.500 | 1.327 |                0.662 |
| circle   | Agent5 | Agent4    |                  2 |      35 |           104 |        33.7% (0.337) |                0.500 | 0.673 |                0.338 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- |
|     1 |           1 | Fail    | asterisk                                    | circle         |             11 |         232.83 |
|     2 |           1 | Success | diamond                                     | diamond        |              8 |          35.48 |
|     3 |           1 | Fail    | square                                      | asterisk       |             11 |          48.18 |
|     4 |           1 | Fail    | asterisk                                    | diamond        |              7 |          30.67 |
|     5 |           1 | Success | square                                      | square         |             10 |          44.55 |
|     6 |           1 | Success | asterisk                                    | asterisk       |              7 |          32.38 |
|     7 |           1 | Fail    | triangle                                    | circle         |             11 |          47.18 |
|     8 |           1 | Fail    | circle                                      | triangle       |              5 |          23.67 |
|     9 |           1 | Success | circle                                      | circle         |             10 |          44.79 |
|    10 |           1 | Success | square                                      | square         |              7 |          30.78 |
|    11 |           1 | Fail    | diamond                                     | circle         |             10 |          42.24 |
|    12 |           1 | Success | circle                                      | circle         |              7 |          30.65 |
|    13 |           1 | Success | triangle                                    | triangle       |              7 |          30.56 |
|    14 |           1 | Fail    | cross                                       | asterisk       |             10 |          45.17 |
|    15 |           1 | Fail    | No figure submitted (message limit reached) | asterisk       |             40 |         161.38 |
|    16 |           1 | Fail    | cross                                       | asterisk       |             10 |          45.58 |
|    17 |           1 | Fail    | diamond                                     | square         |             37 |         152.69 |
|    18 |           1 | Fail    | diamond                                     | square         |             11 |          49.08 |
|    19 |           1 | Success | diamond                                     | diamond        |              5 |          23.00 |
|    20 |           1 | Success | cross                                       | cross          |             10 |          44.58 |
|    21 |           1 | Success | diamond                                     | diamond        |             14 |          60.06 |
|    22 |           1 | Fail    | cross                                       | square         |              7 |          32.76 |
|    23 |           1 | Fail    | triangle                                    | square         |             14 |          59.92 |
|    24 |           1 | Success | triangle                                    | triangle       |              5 |          24.16 |
|    25 |           1 | Fail    | square                                      | cross          |             14 |          58.27 |
|    26 |           1 | Fail    | asterisk                                    | triangle       |             18 |          76.91 |
|    27 |           1 | Fail    | circle                                      | diamond        |             15 |          65.04 |
|    28 |           1 | Success | diamond                                     | diamond        |              7 |          30.78 |
|    29 |           1 | Fail    | asterisk                                    | circle         |              8 |          35.71 |
|    30 |           1 | Fail    | asterisk                                    | circle         |             10 |          45.36 |
|    31 |           1 | Fail    | cross                                       | circle         |              5 |          22.86 |
|    32 |           1 | Success | square                                      | square         |             10 |          45.73 |
|    33 |           1 | Success | triangle                                    | triangle       |             12 |          51.38 |
|    34 |           1 | Fail    | diamond                                     | cross          |              7 |          30.54 |
|    35 |           1 | Fail    | triangle                                    | asterisk       |              5 |          23.93 |
|    36 |           1 | Success | diamond                                     | diamond        |             10 |          44.08 |
|    37 |           1 | Fail    | square                                      | asterisk       |              7 |          32.27 |
|    38 |           1 | Fail    | circle                                      | asterisk       |              5 |          24.14 |
|    39 |           1 | Fail    | triangle                                    | circle         |             10 |          44.04 |
|    40 |           1 | Fail    | diamond                                     | square         |              8 |          37.32 |
|    41 |           1 | Fail    | square                                      | asterisk       |             18 |          74.94 |
|    42 |           1 | Success | diamond                                     | diamond        |             10 |          42.94 |
|    43 |           1 | Fail    | cross                                       | diamond        |             10 |          44.49 |
|    44 |           1 | Success | square                                      | square         |             15 |          64.30 |
|    45 |           1 | Fail    | triangle                                    | square         |             10 |          44.50 |
|    46 |           1 | Success | circle                                      | circle         |              5 |          24.58 |
|    47 |           1 | Success | diamond                                     | diamond        |              8 |          36.39 |
|    48 |           1 | Success | square                                      | square         |             24 |         103.25 |
|    49 |           1 | Fail    | cross                                       | triangle       |              7 |          31.21 |
|    50 |           1 | Fail    | cross                                       | square         |             16 |          67.14 |
```
