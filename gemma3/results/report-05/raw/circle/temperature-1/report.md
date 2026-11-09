# Circle auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 219.01 seconds
- Average total messages: 14.86
- Success rate: 8/50 (16.0%)
- Reconnect pauses: 2 across 1 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      46 |           159 |        28.9% (0.289) |                0.500 | 0.579 |                0.291 |
| circle   | Agent1 | Agent5    |                  2 |     113 |           159 |        71.1% (0.711) |                0.500 | 1.421 |                0.709 |
| circle   | Agent2 | Agent1    |                  2 |     131 |           152 |        86.2% (0.862) |                0.500 | 1.724 |                0.859 |
| circle   | Agent2 | Agent3    |                  2 |      21 |           152 |        13.8% (0.138) |                0.500 | 0.276 |                0.141 |
| circle   | Agent3 | Agent2    |                  2 |     157 |           162 |        96.9% (0.969) |                0.500 | 1.938 |                0.966 |
| circle   | Agent3 | Agent4    |                  2 |       5 |           162 |         3.1% (0.031) |                0.500 | 0.062 |                0.034 |
| circle   | Agent4 | Agent3    |                  2 |     116 |           157 |        73.9% (0.739) |                0.500 | 1.478 |                0.737 |
| circle   | Agent4 | Agent5    |                  2 |      41 |           157 |        26.1% (0.261) |                0.500 | 0.522 |                0.263 |
| circle   | Agent5 | Agent1    |                  2 |      45 |           112 |        40.2% (0.402) |                0.500 | 0.804 |                0.403 |
| circle   | Agent5 | Agent4    |                  2 |      67 |           112 |        59.8% (0.598) |                0.500 | 1.196 |                0.597 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| circle   | Agent3 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           1 | Fail    | circle                                      | asterisk       |             13 |         666.06 |           0 |             0.00 |
|     2 |           1 | Fail    | cross                                       | asterisk       |              6 |         215.69 |           0 |             0.00 |
|     3 |           1 | Fail    | triangle                                    | asterisk       |             23 |         685.70 |           0 |             0.00 |
|     4 |           1 | Fail    | diamond                                     | triangle       |              7 |          41.42 |           0 |             0.00 |
|     5 |           1 | Success | asterisk                                    | asterisk       |              7 |          40.06 |           0 |             0.00 |
|     6 |           1 | Success | square                                      | square         |              6 |          36.28 |           0 |             0.00 |
|     7 |           1 | Fail    | square                                      | asterisk       |              9 |          54.08 |           0 |             0.00 |
|     8 |           1 | Fail    | circle                                      | diamond        |              4 |          24.91 |           0 |             0.00 |
|     9 |           1 | Fail    | asterisk                                    | square         |             16 |          92.69 |           0 |             0.00 |
|    10 |           1 | Fail    | asterisk                                    | triangle       |              9 |          55.67 |           0 |             0.00 |
|    11 |           1 | Fail    | circle                                      | asterisk       |              7 |          43.56 |           0 |             0.00 |
|    12 |           1 | Success | cross                                       | cross          |             26 |         149.31 |           0 |             0.00 |
|    13 |           1 | Fail    | square                                      | cross          |             10 |          56.74 |           0 |             0.00 |
|    14 |           1 | Fail    | square                                      | circle         |              5 |          33.61 |           0 |             0.00 |
|    15 |           1 | Fail    | triangle                                    | cross          |             11 |         263.93 |           0 |             0.00 |
|    16 |           1 | Fail    | triangle                                    | diamond        |             21 |        1089.66 |           2 |             0.00 |
|    17 |           1 | Fail    | triangle                                    | asterisk       |             26 |         137.61 |           0 |             0.00 |
|    18 |           1 | Fail    | cross                                       | circle         |              6 |          34.35 |           0 |             0.00 |
|    19 |           1 | Fail    | diamond                                     | circle         |             19 |         110.26 |           0 |             0.00 |
|    20 |           1 | Fail    | circle                                      | cross          |             19 |         107.84 |           0 |             0.00 |
|    21 |           1 | Fail    | No figure submitted (message limit reached) | triangle       |             40 |         211.82 |           0 |             0.00 |
|    22 |           1 | Success | square                                      | square         |              7 |          42.81 |           0 |             0.00 |
|    23 |           1 | Fail    | square                                      | cross          |             16 |          94.77 |           0 |             0.00 |
|    24 |           1 | Fail    | cross                                       | asterisk       |             27 |         155.51 |           0 |             0.00 |
|    25 |           1 | Success | cross                                       | cross          |              7 |          45.67 |           0 |             0.00 |
|    26 |           1 | Fail    | circle                                      | cross          |             15 |         174.22 |           0 |             0.00 |
|    27 |           1 | Fail    | diamond                                     | asterisk       |             14 |         405.48 |           0 |             0.00 |
|    28 |           1 | Fail    | square                                      | cross          |             26 |        1202.93 |           0 |             0.00 |
|    29 |           1 | Fail    | cross                                       | triangle       |             18 |         206.06 |           0 |             0.00 |
|    30 |           1 | Fail    | diamond                                     | circle         |             12 |          69.57 |           0 |             0.00 |
|    31 |           1 | Fail    | triangle                                    | diamond        |             15 |          89.15 |           0 |             0.00 |
|    32 |           1 | Fail    | triangle                                    | diamond        |             30 |         166.63 |           0 |             0.00 |
|    33 |           1 | Fail    | square                                      | diamond        |              3 |          18.35 |           0 |             0.00 |
|    34 |           1 | Fail    | asterisk                                    | triangle       |             12 |          67.52 |           0 |             0.00 |
|    35 |           1 | Fail    | triangle                                    | square         |             11 |          64.90 |           0 |             0.00 |
|    36 |           1 | Fail    | cross                                       | asterisk       |              7 |          42.29 |           0 |             0.00 |
|    37 |           1 | Fail    | triangle                                    | square         |             12 |          70.50 |           0 |             0.00 |
|    38 |           1 | Fail    | asterisk                                    | cross          |             24 |         147.27 |           0 |             0.00 |
|    39 |           1 | Fail    | square                                      | circle         |             18 |         299.37 |           0 |             0.00 |
|    40 |           1 | Fail    | cross                                       | asterisk       |             15 |         333.35 |           0 |             0.00 |
|    41 |           1 | Success | cross                                       | cross          |              8 |         227.06 |           0 |             0.00 |
|    42 |           1 | Fail    | triangle                                    | diamond        |             32 |        1488.97 |           0 |             0.00 |
|    43 |           1 | Fail    | diamond                                     | square         |             15 |         667.93 |           0 |             0.00 |
|    44 |           1 | Fail    | diamond                                     | cross          |             15 |         178.40 |           0 |             0.00 |
|    45 |           1 | Fail    | circle                                      | cross          |             11 |          64.53 |           0 |             0.00 |
|    46 |           1 | Success | diamond                                     | diamond        |             23 |         130.18 |           0 |             0.00 |
|    47 |           1 | Fail    | asterisk                                    | square         |              6 |          35.96 |           0 |             0.00 |
|    48 |           1 | Fail    | cross                                       | diamond        |             31 |         175.04 |           0 |             0.00 |
|    49 |           1 | Success | diamond                                     | diamond        |             12 |          68.12 |           0 |             0.00 |
|    50 |           1 | Fail    | square                                      | asterisk       |             11 |          66.79 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    16 | Agent1               | 2026-05-13T13:20:12.543990+00:00 | 2026-05-13T13:20:12.545277+00:00 |             0.00 |
|    16 | Agent5               | 2026-05-13T13:27:54.787700+00:00 | 2026-05-13T13:27:54.789011+00:00 |             0.00 |
```
