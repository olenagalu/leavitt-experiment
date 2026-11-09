# Wheel auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 84.72 seconds
- Average total messages: 18.00
- Success rate: 18/50 (36.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     174 |           174 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     168 |           168 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |      96 |           180 |        53.3% (0.533) |                0.250 | 2.133 |                0.530 |
| wheel    | Agent3 | Agent2    |                  4 |      69 |           180 |        38.3% (0.383) |                0.250 | 1.533 |                0.382 |
| wheel    | Agent3 | Agent4    |                  4 |       6 |           180 |         3.3% (0.033) |                0.250 | 0.133 |                0.036 |
| wheel    | Agent3 | Agent5    |                  4 |       9 |           180 |         5.0% (0.050) |                0.250 | 0.200 |                0.052 |
| wheel    | Agent4 | Agent3    |                  1 |     197 |           197 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     181 |           181 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- |
|     1 |           1 | Fail    | diamond                                     | triangle       |             17 |         235.69 |
|     2 |           1 | Success | triangle                                    | triangle       |             24 |          94.84 |
|     3 |           1 | Fail    | square                                      | asterisk       |             17 |          72.18 |
|     4 |           1 | Fail    | triangle                                    | diamond        |             15 |          68.35 |
|     5 |           1 | Fail    | circle                                      | triangle       |             13 |          57.94 |
|     6 |           1 | Fail    | circle                                      | triangle       |             16 |          75.65 |
|     7 |           1 | Fail    | square                                      | cross          |             24 |         114.69 |
|     8 |           1 | Fail    | circle                                      | triangle       |             12 |          58.88 |
|     9 |           1 | Success | circle                                      | circle         |             15 |          70.65 |
|    10 |           1 | Fail    | triangle                                    | square         |             19 |          80.80 |
|    11 |           1 | Success | asterisk                                    | asterisk       |             19 |          89.60 |
|    12 |           1 | Success | square                                      | square         |             18 |          79.95 |
|    13 |           1 | Fail    | circle                                      | square         |              8 |          36.52 |
|    14 |           1 | Fail    | No figure submitted (message limit reached) | square         |             50 |         236.75 |
|    15 |           1 | Success | circle                                      | circle         |             24 |         107.58 |
|    16 |           1 | Fail    | circle                                      | triangle       |             14 |          59.94 |
|    17 |           1 | Success | circle                                      | circle         |             19 |          96.84 |
|    18 |           1 | Fail    | circle                                      | diamond        |             12 |          52.66 |
|    19 |           1 | Success | diamond                                     | diamond        |             42 |         177.14 |
|    20 |           1 | Fail    | diamond                                     | square         |             20 |          90.61 |
|    21 |           1 | Fail    | asterisk                                    | square         |             11 |          49.81 |
|    22 |           1 | Fail    | circle                                      | cross          |             13 |          59.36 |
|    23 |           1 | Success | square                                      | square         |             12 |          57.18 |
|    24 |           1 | Fail    | square                                      | asterisk       |             22 |         100.65 |
|    25 |           1 | Success | circle                                      | circle         |              9 |          42.74 |
|    26 |           1 | Success | circle                                      | circle         |              9 |          41.43 |
|    27 |           1 | Fail    | diamond                                     | square         |              7 |          32.96 |
|    28 |           1 | Fail    | square                                      | asterisk       |              8 |          37.54 |
|    29 |           1 | Fail    | circle                                      | asterisk       |              7 |          35.24 |
|    30 |           1 | Fail    | circle                                      | cross          |             33 |         144.30 |
|    31 |           1 | Success | cross                                       | cross          |             14 |          59.82 |
|    32 |           1 | Fail    | square                                      | asterisk       |             29 |         121.43 |
|    33 |           1 | Fail    | cross                                       | diamond        |             12 |          54.71 |
|    34 |           1 | Success | diamond                                     | diamond        |             22 |         112.82 |
|    35 |           1 | Success | cross                                       | cross          |             19 |          87.41 |
|    36 |           1 | Fail    | asterisk                                    | triangle       |             27 |         128.00 |
|    37 |           1 | Fail    | cross                                       | diamond        |             32 |         131.07 |
|    38 |           1 | Fail    | square                                      | asterisk       |             23 |         102.14 |
|    39 |           1 | Fail    | circle                                      | cross          |             21 |          92.13 |
|    40 |           1 | Fail    | square                                      | circle         |              7 |          34.17 |
|    41 |           1 | Fail    | diamond                                     | triangle       |             14 |          65.56 |
|    42 |           1 | Success | triangle                                    | triangle       |             11 |          51.15 |
|    43 |           1 | Fail    | triangle                                    | cross          |             16 |          80.12 |
|    44 |           1 | Fail    | cross                                       | diamond        |             19 |          78.49 |
|    45 |           1 | Success | diamond                                     | diamond        |             20 |          88.81 |
|    46 |           1 | Fail    | triangle                                    | square         |             18 |          81.41 |
|    47 |           1 | Success | square                                      | square         |             11 |          52.71 |
|    48 |           1 | Success | square                                      | square         |             18 |          90.41 |
|    49 |           1 | Success | circle                                      | circle         |             20 |          86.06 |
|    50 |           1 | Fail    | diamond                                     | square         |             18 |          79.00 |
```
