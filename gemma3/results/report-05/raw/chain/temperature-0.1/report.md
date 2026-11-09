# Chain auto-trial report

## Summary

- Batch: `temperature-0.1`
- Temperature: 0.1
- Completed trials: 50/50
- Average time: 206.82 seconds
- Average total messages: 17.74
- Success rate: 12/50 (24.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     189 |           189 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     151 |           171 |        88.3% (0.883) |                0.500 | 1.766 |                0.881 |
| chain    | Agent2 | Agent3    |                  2 |      20 |           171 |        11.7% (0.117) |                0.500 | 0.234 |                0.119 |
| chain    | Agent3 | Agent2    |                  2 |     189 |           193 |        97.9% (0.979) |                0.500 | 1.959 |                0.977 |
| chain    | Agent3 | Agent4    |                  2 |       4 |           193 |         2.1% (0.021) |                0.500 | 0.041 |                0.023 |
| chain    | Agent4 | Agent3    |                  2 |     107 |           174 |        61.5% (0.615) |                0.500 | 1.230 |                0.614 |
| chain    | Agent4 | Agent5    |                  2 |      67 |           174 |        38.5% (0.385) |                0.500 | 0.770 |                0.386 |
| chain    | Agent5 | Agent4    |                  1 |     160 |           160 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.1 | Fail    | square                                      | asterisk       |             33 |         667.10 |           0 |             0.00 |
|     2 |         0.1 | Fail    | cross                                       | circle         |             17 |          98.21 |           0 |             0.00 |
|     3 |         0.1 | Fail    | cross                                       | circle         |             27 |         143.31 |           0 |             0.00 |
|     4 |         0.1 | Fail    | square                                      | triangle       |             19 |         105.72 |           0 |             0.00 |
|     5 |         0.1 | Success | cross                                       | cross          |              5 |          30.72 |           0 |             0.00 |
|     6 |         0.1 | Success | asterisk                                    | asterisk       |             10 |          57.89 |           0 |             0.00 |
|     7 |         0.1 | Fail    | square                                      | circle         |             17 |          96.64 |           0 |             0.00 |
|     8 |         0.1 | Fail    | square                                      | circle         |             17 |          99.07 |           0 |             0.00 |
|     9 |         0.1 | Fail    | triangle                                    | square         |              6 |          37.05 |           0 |             0.00 |
|    10 |         0.1 | Fail    | asterisk                                    | triangle       |              9 |          56.78 |           0 |             0.00 |
|    11 |         0.1 | Success | asterisk                                    | asterisk       |             11 |          62.91 |           0 |             0.00 |
|    12 |         0.1 | Fail    | cross                                       | circle         |             15 |         115.50 |           0 |             0.00 |
|    13 |         0.1 | Fail    | square                                      | asterisk       |             28 |         460.61 |           0 |             0.00 |
|    14 |         0.1 | Success | circle                                      | circle         |             15 |          91.43 |           0 |             0.00 |
|    15 |         0.1 | Success | triangle                                    | triangle       |             17 |         103.96 |           0 |             0.00 |
|    16 |         0.1 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        1265.17 |           0 |             0.00 |
|    17 |         0.1 | Success | asterisk                                    | asterisk       |             24 |         366.67 |           0 |             0.00 |
|    18 |         0.1 | Fail    | triangle                                    | asterisk       |             18 |         303.27 |           0 |             0.00 |
|    19 |         0.1 | Fail    | cross                                       | asterisk       |             19 |         108.63 |           0 |             0.00 |
|    20 |         0.1 | Fail    | triangle                                    | diamond        |             13 |          79.85 |           0 |             0.00 |
|    21 |         0.1 | Fail    | asterisk                                    | square         |              7 |          41.67 |           0 |             0.00 |
|    22 |         0.1 | Fail    | circle                                      | diamond        |             16 |          93.42 |           0 |             0.00 |
|    23 |         0.1 | Fail    | circle                                      | square         |             18 |         113.80 |           0 |             0.00 |
|    24 |         0.1 | Fail    | triangle                                    | circle         |             27 |         215.48 |           0 |             0.00 |
|    25 |         0.1 | Fail    | cross                                       | triangle       |             10 |          56.45 |           0 |             0.00 |
|    26 |         0.1 | Fail    | circle                                      | square         |              8 |          74.51 |           0 |             0.00 |
|    27 |         0.1 | Success | square                                      | square         |             11 |         204.52 |           0 |             0.00 |
|    28 |         0.1 | Success | triangle                                    | triangle       |             11 |         183.94 |           0 |             0.00 |
|    29 |         0.1 | Fail    | triangle                                    | square         |             16 |          93.32 |           0 |             0.00 |
|    30 |         0.1 | Fail    | triangle                                    | asterisk       |             25 |         142.41 |           0 |             0.00 |
|    31 |         0.1 | Fail    | triangle                                    | cross          |             20 |         114.26 |           0 |             0.00 |
|    32 |         0.1 | Fail    | triangle                                    | cross          |             11 |          71.30 |           0 |             0.00 |
|    33 |         0.1 | Success | triangle                                    | triangle       |             26 |         230.88 |           0 |             0.00 |
|    34 |         0.1 | Success | diamond                                     | diamond        |             21 |         118.93 |           0 |             0.00 |
|    35 |         0.1 | Fail    | cross                                       | asterisk       |             15 |          87.35 |           0 |             0.00 |
|    36 |         0.1 | Fail    | cross                                       | triangle       |             26 |         363.67 |           0 |             0.00 |
|    37 |         0.1 | Fail    | diamond                                     | asterisk       |             14 |          85.59 |           0 |             0.00 |
|    38 |         0.1 | Fail    | diamond                                     | circle         |              6 |          42.74 |           0 |             0.00 |
|    39 |         0.1 | Fail    | No figure submitted (message limit reached) | square         |             50 |        1614.48 |           0 |             0.00 |
|    40 |         0.1 | Fail    | diamond                                     | cross          |             14 |         131.16 |           0 |             0.00 |
|    41 |         0.1 | Fail    | diamond                                     | cross          |             17 |          94.56 |           0 |             0.00 |
|    42 |         0.1 | Success | asterisk                                    | asterisk       |              9 |          51.63 |           0 |             0.00 |
|    43 |         0.1 | Success | asterisk                                    | asterisk       |             14 |          78.50 |           0 |             0.00 |
|    44 |         0.1 | Fail    | cross                                       | diamond        |             14 |          82.77 |           0 |             0.00 |
|    45 |         0.1 | Fail    | square                                      | diamond        |              9 |          67.42 |           0 |             0.00 |
|    46 |         0.1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |         848.96 |           0 |             0.00 |
|    47 |         0.1 | Fail    | triangle                                    | asterisk       |             12 |         362.88 |           0 |             0.00 |
|    48 |         0.1 | Fail    | triangle                                    | cross          |             16 |          92.66 |           0 |             0.00 |
|    49 |         0.1 | Fail    | cross                                       | circle         |             14 |          87.97 |           0 |             0.00 |
|    50 |         0.1 | Fail    | cross                                       | diamond        |             10 |         143.13 |           0 |             0.00 |
```

## Reconnect details

No Jetson disconnects were recorded.
