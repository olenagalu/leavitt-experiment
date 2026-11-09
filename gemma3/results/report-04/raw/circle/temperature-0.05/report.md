# Circle auto-trial report

## Summary

- Batch: `temperature-0.05`
- Temperature: 0.05
- Completed trials: 50/50
- Average time: 195.25 seconds
- Average total messages: 19.00
- Success rate: 11/50 (22.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      45 |           176 |        25.6% (0.256) |                0.500 | 0.511 |                0.257 |
| circle   | Agent1 | Agent5    |                  2 |     131 |           176 |        74.4% (0.744) |                0.500 | 1.489 |                0.743 |
| circle   | Agent2 | Agent1    |                  2 |     193 |           211 |        91.5% (0.915) |                0.500 | 1.829 |                0.913 |
| circle   | Agent2 | Agent3    |                  2 |      18 |           211 |         8.5% (0.085) |                0.500 | 0.171 |                0.087 |
| circle   | Agent3 | Agent2    |                  2 |     187 |           198 |        94.4% (0.944) |                0.500 | 1.889 |                0.942 |
| circle   | Agent3 | Agent4    |                  2 |      11 |           198 |         5.6% (0.056) |                0.500 | 0.111 |                0.058 |
| circle   | Agent4 | Agent3    |                  2 |     168 |           186 |        90.3% (0.903) |                0.500 | 1.806 |                0.901 |
| circle   | Agent4 | Agent5    |                  2 |      18 |           186 |         9.7% (0.097) |                0.500 | 0.194 |                0.099 |
| circle   | Agent5 | Agent1    |                  2 |      84 |           179 |        46.9% (0.469) |                0.500 | 0.939 |                0.469 |
| circle   | Agent5 | Agent4    |                  2 |      95 |           179 |        53.1% (0.531) |                0.500 | 1.061 |                0.531 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |        0.05 | Success | cross                                       | cross          |             12 |         293.89 |           0 |             0.00 |
|     2 |        0.05 | Fail    | square                                      | cross          |             12 |          68.15 |           0 |             0.00 |
|     3 |        0.05 | Fail    | diamond                                     | square         |             12 |          73.71 |           0 |             0.00 |
|     4 |        0.05 | Fail    | triangle                                    | square         |             16 |          90.69 |           0 |             0.00 |
|     5 |        0.05 | Success | circle                                      | circle         |             19 |         108.78 |           0 |             0.00 |
|     6 |        0.05 | Fail    | cross                                       | asterisk       |             13 |          77.78 |           0 |             0.00 |
|     7 |        0.05 | Fail    | circle                                      | triangle       |             13 |          78.17 |           0 |             0.00 |
|     8 |        0.05 | Fail    | triangle                                    | cross          |              9 |          52.33 |           0 |             0.00 |
|     9 |        0.05 | Fail    | triangle                                    | square         |             14 |          79.09 |           0 |             0.00 |
|    10 |        0.05 | Fail    | cross                                       | diamond        |             10 |          56.02 |           0 |             0.00 |
|    11 |        0.05 | Fail    | asterisk                                    | triangle       |              9 |          64.47 |           0 |             0.00 |
|    12 |        0.05 | Fail    | No figure submitted (message limit reached) | asterisk       |             40 |        1107.16 |           0 |             0.00 |
|    13 |        0.05 | Fail    | circle                                      | square         |             20 |         115.19 |           0 |             0.00 |
|    14 |        0.05 | Fail    | cross                                       | diamond        |             16 |          88.15 |           0 |             0.00 |
|    15 |        0.05 | Fail    | No figure submitted (message limit reached) | diamond        |             40 |         220.95 |           0 |             0.00 |
|    16 |        0.05 | Fail    | cross                                       | square         |             10 |          56.60 |           0 |             0.00 |
|    17 |        0.05 | Fail    | circle                                      | square         |             13 |          75.57 |           0 |             0.00 |
|    18 |        0.05 | Success | triangle                                    | triangle       |             36 |         199.17 |           0 |             0.00 |
|    19 |        0.05 | Fail    | asterisk                                    | diamond        |             11 |          62.68 |           0 |             0.00 |
|    20 |        0.05 | Success | diamond                                     | diamond        |             30 |         163.54 |           0 |             0.00 |
|    21 |        0.05 | Fail    | No figure submitted (message limit reached) | cross          |             40 |         259.03 |           0 |             0.00 |
|    22 |        0.05 | Success | cross                                       | cross          |             15 |         476.56 |           0 |             0.00 |
|    23 |        0.05 | Fail    | cross                                       | asterisk       |             18 |         101.12 |           0 |             0.00 |
|    24 |        0.05 | Success | square                                      | square         |             16 |          92.34 |           0 |             0.00 |
|    25 |        0.05 | Fail    | No figure submitted (message limit reached) | diamond        |             40 |         208.50 |           0 |             0.00 |
|    26 |        0.05 | Success | asterisk                                    | asterisk       |              9 |          54.23 |           0 |             0.00 |
|    27 |        0.05 | Fail    | No figure submitted (message limit reached) | cross          |             40 |         215.08 |           0 |             0.00 |
|    28 |        0.05 | Fail    | cross                                       | triangle       |             16 |          92.66 |           0 |             0.00 |
|    29 |        0.05 | Fail    | cross                                       | circle         |             12 |          69.00 |           0 |             0.00 |
|    30 |        0.05 | Success | asterisk                                    | asterisk       |             17 |         100.20 |           0 |             0.00 |
|    31 |        0.05 | Fail    | diamond                                     | circle         |             17 |          98.67 |           0 |             0.00 |
|    32 |        0.05 | Fail    | square                                      | asterisk       |             16 |         218.38 |           0 |             0.00 |
|    33 |        0.05 | Fail    | cross                                       | asterisk       |             22 |         971.82 |           0 |             0.00 |
|    34 |        0.05 | Fail    | diamond                                     | circle         |              5 |         205.06 |           0 |             0.00 |
|    35 |        0.05 | Fail    | square                                      | asterisk       |             20 |         209.98 |           0 |             0.00 |
|    36 |        0.05 | Fail    | cross                                       | square         |             10 |          58.60 |           0 |             0.00 |
|    37 |        0.05 | Fail    | circle                                      | square         |             13 |          74.34 |           0 |             0.00 |
|    38 |        0.05 | Fail    | square                                      | asterisk       |              8 |          48.20 |           0 |             0.00 |
|    39 |        0.05 | Success | triangle                                    | triangle       |             11 |          66.29 |           0 |             0.00 |
|    40 |        0.05 | Fail    | No figure submitted (message limit reached) | diamond        |             40 |         220.84 |           0 |             0.00 |
|    41 |        0.05 | Fail    | asterisk                                    | circle         |             15 |          87.74 |           0 |             0.00 |
|    42 |        0.05 | Fail    | cross                                       | square         |             14 |          80.12 |           0 |             0.00 |
|    43 |        0.05 | Fail    | square                                      | circle         |             12 |          77.90 |           0 |             0.00 |
|    44 |        0.05 | Success | diamond                                     | diamond        |             33 |         547.09 |           0 |             0.00 |
|    45 |        0.05 | Fail    | square                                      | asterisk       |             27 |         167.03 |           0 |             0.00 |
|    46 |        0.05 | Fail    | circle                                      | asterisk       |             12 |         414.51 |           0 |             0.00 |
|    47 |        0.05 | Fail    | triangle                                    | cross          |             11 |         137.16 |           0 |             0.00 |
|    48 |        0.05 | Fail    | No figure submitted (message limit reached) | triangle       |             40 |         621.08 |           0 |             0.00 |
|    49 |        0.05 | Fail    | cross                                       | diamond        |             27 |         249.95 |           0 |             0.00 |
|    50 |        0.05 | Success | triangle                                    | triangle       |             19 |         406.88 |           0 |             0.00 |
```

## Reconnect details

No Jetson disconnects were recorded.
