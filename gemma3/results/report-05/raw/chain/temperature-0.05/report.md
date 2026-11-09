# Chain auto-trial report

## Summary

- Batch: `temperature-0.05`
- Temperature: 0.05
- Completed trials: 50/50
- Average time: 191.09 seconds
- Average total messages: 16.24
- Success rate: 14/50 (28.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     151 |           151 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     148 |           162 |        91.4% (0.914) |                0.500 | 1.827 |                0.911 |
| chain    | Agent2 | Agent3    |                  2 |      14 |           162 |         8.6% (0.086) |                0.500 | 0.173 |                0.089 |
| chain    | Agent3 | Agent2    |                  2 |     177 |           182 |        97.3% (0.973) |                0.500 | 1.945 |                0.970 |
| chain    | Agent3 | Agent4    |                  2 |       5 |           182 |         2.7% (0.027) |                0.500 | 0.055 |                0.030 |
| chain    | Agent4 | Agent3    |                  2 |      98 |           150 |        65.3% (0.653) |                0.500 | 1.307 |                0.652 |
| chain    | Agent4 | Agent5    |                  2 |      52 |           150 |        34.7% (0.347) |                0.500 | 0.693 |                0.348 |
| chain    | Agent5 | Agent4    |                  1 |     167 |           167 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |        0.05 | Success | diamond                                     | diamond        |             11 |         272.95 |           0 |             0.00 |
|     2 |        0.05 | Success | circle                                      | circle         |             10 |          58.86 |           0 |             0.00 |
|     3 |        0.05 | Success | triangle                                    | triangle       |             19 |         107.77 |           0 |             0.00 |
|     4 |        0.05 | Fail    | cross                                       | circle         |             18 |         100.81 |           0 |             0.00 |
|     5 |        0.05 | Fail    | circle                                      | triangle       |              9 |          52.66 |           0 |             0.00 |
|     6 |        0.05 | Fail    | triangle                                    | asterisk       |             19 |         111.54 |           0 |             0.00 |
|     7 |        0.05 | Fail    | square                                      | diamond        |             13 |          76.77 |           0 |             0.00 |
|     8 |        0.05 | Fail    | triangle                                    | square         |             18 |         104.83 |           0 |             0.00 |
|     9 |        0.05 | Fail    | triangle                                    | circle         |             14 |          80.94 |           0 |             0.00 |
|    10 |        0.05 | Success | triangle                                    | triangle       |             19 |         124.85 |           0 |             0.00 |
|    11 |        0.05 | Success | circle                                      | circle         |             10 |         159.20 |           0 |             0.00 |
|    12 |        0.05 | Fail    | cross                                       | triangle       |             11 |         130.80 |           0 |             0.00 |
|    13 |        0.05 | Success | diamond                                     | diamond        |             21 |         149.51 |           0 |             0.00 |
|    14 |        0.05 | Fail    | triangle                                    | square         |              7 |         238.37 |           0 |             0.00 |
|    15 |        0.05 | Fail    | triangle                                    | square         |              9 |         115.62 |           0 |             0.00 |
|    16 |        0.05 | Fail    | triangle                                    | circle         |             24 |         136.95 |           0 |             0.00 |
|    17 |        0.05 | Fail    | triangle                                    | circle         |              9 |          50.93 |           0 |             0.00 |
|    18 |        0.05 | Success | triangle                                    | triangle       |             18 |         103.90 |           0 |             0.00 |
|    19 |        0.05 | Fail    | cross                                       | circle         |             11 |          64.71 |           0 |             0.00 |
|    20 |        0.05 | Fail    | asterisk                                    | circle         |             13 |          75.28 |           0 |             0.00 |
|    21 |        0.05 | Success | diamond                                     | diamond        |             12 |          68.03 |           0 |             0.00 |
|    22 |        0.05 | Fail    | square                                      | asterisk       |             16 |          94.42 |           0 |             0.00 |
|    23 |        0.05 | Fail    | square                                      | circle         |             13 |         116.97 |           0 |             0.00 |
|    24 |        0.05 | Fail    | circle                                      | cross          |             10 |         194.93 |           0 |             0.00 |
|    25 |        0.05 | Fail    | asterisk                                    | diamond        |             20 |         224.81 |           0 |             0.00 |
|    26 |        0.05 | Fail    | circle                                      | diamond        |             41 |         883.13 |           0 |             0.00 |
|    27 |        0.05 | Fail    | cross                                       | circle         |             18 |         120.97 |           0 |             0.00 |
|    28 |        0.05 | Fail    | cross                                       | circle         |             19 |         254.33 |           0 |             0.00 |
|    29 |        0.05 | Success | circle                                      | circle         |             21 |         198.94 |           0 |             0.00 |
|    30 |        0.05 | Success | asterisk                                    | asterisk       |             17 |          97.54 |           0 |             0.00 |
|    31 |        0.05 | Fail    | square                                      | asterisk       |             14 |          78.80 |           0 |             0.00 |
|    32 |        0.05 | Fail    | square                                      | diamond        |             11 |          64.80 |           0 |             0.00 |
|    33 |        0.05 | Success | triangle                                    | triangle       |             11 |          64.25 |           0 |             0.00 |
|    34 |        0.05 | Fail    | square                                      | asterisk       |              8 |          46.90 |           0 |             0.00 |
|    35 |        0.05 | Fail    | square                                      | triangle       |             12 |          69.97 |           0 |             0.00 |
|    36 |        0.05 | Fail    | cross                                       | triangle       |             14 |          83.16 |           0 |             0.00 |
|    37 |        0.05 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |         832.25 |           0 |             0.00 |
|    38 |        0.05 | Fail    | circle                                      | asterisk       |             23 |         655.78 |           0 |             0.00 |
|    39 |        0.05 | Fail    | cross                                       | triangle       |             15 |         147.78 |           0 |             0.00 |
|    40 |        0.05 | Fail    | triangle                                    | square         |             15 |          89.94 |           0 |             0.00 |
|    41 |        0.05 | Success | cross                                       | cross          |             15 |          86.15 |           0 |             0.00 |
|    42 |        0.05 | Success | triangle                                    | triangle       |             16 |          88.47 |           0 |             0.00 |
|    43 |        0.05 | Fail    | circle                                      | diamond        |             14 |          79.53 |           0 |             0.00 |
|    44 |        0.05 | Fail    | circle                                      | diamond        |             11 |          64.65 |           0 |             0.00 |
|    45 |        0.05 | Fail    | square                                      | circle         |             10 |          58.27 |           0 |             0.00 |
|    46 |        0.05 | Fail    | cross                                       | square         |              7 |          42.37 |           0 |             0.00 |
|    47 |        0.05 | Fail    | cross                                       | triangle       |             16 |          97.00 |           0 |             0.00 |
|    48 |        0.05 | Success | triangle                                    | triangle       |             31 |         718.12 |           0 |             0.00 |
|    49 |        0.05 | Fail    | cross                                       | square         |             13 |          77.85 |           0 |             0.00 |
|    50 |        0.05 | Fail    | triangle                                    | cross          |             36 |        1537.33 |           0 |             0.00 |
```

## Reconnect details

No Jetson disconnects were recorded.
