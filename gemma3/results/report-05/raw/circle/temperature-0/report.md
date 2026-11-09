# Circle auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 156.92 seconds
- Average total messages: 15.70
- Success rate: 12/50 (24.0%)
- Reconnect pauses: 2 across 2 trial(s); 6.01 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      48 |           157 |        30.6% (0.306) |                0.500 | 0.611 |                0.307 |
| circle   | Agent1 | Agent5    |                  2 |     109 |           157 |        69.4% (0.694) |                0.500 | 1.389 |                0.693 |
| circle   | Agent2 | Agent1    |                  2 |     149 |           159 |        93.7% (0.937) |                0.500 | 1.874 |                0.934 |
| circle   | Agent2 | Agent3    |                  2 |      10 |           159 |         6.3% (0.063) |                0.500 | 0.126 |                0.066 |
| circle   | Agent3 | Agent2    |                  2 |     155 |           161 |        96.3% (0.963) |                0.500 | 1.925 |                0.960 |
| circle   | Agent3 | Agent4    |                  2 |       6 |           161 |         3.7% (0.037) |                0.500 | 0.075 |                0.040 |
| circle   | Agent4 | Agent3    |                  2 |     126 |           151 |        83.4% (0.834) |                0.500 | 1.669 |                0.832 |
| circle   | Agent4 | Agent5    |                  2 |      25 |           151 |        16.6% (0.166) |                0.500 | 0.331 |                0.168 |
| circle   | Agent5 | Agent1    |                  2 |      66 |           157 |        42.0% (0.420) |                0.500 | 0.841 |                0.421 |
| circle   | Agent5 | Agent4    |                  2 |      91 |           157 |        58.0% (0.580) |                0.500 | 1.159 |                0.579 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Fail    | cross                                       | diamond        |              6 |         135.82 |           0 |             0.00 |
|     2 |           0 | Fail    | circle                                      | cross          |             15 |         150.56 |           0 |             0.00 |
|     3 |           0 | Fail    | square                                      | triangle       |             19 |         105.32 |           0 |             0.00 |
|     4 |           0 | Fail    | diamond                                     | asterisk       |             12 |          68.73 |           0 |             0.00 |
|     5 |           0 | Success | circle                                      | circle         |             17 |          96.12 |           0 |             0.00 |
|     6 |           0 | Fail    | cross                                       | circle         |             17 |          98.28 |           0 |             0.00 |
|     7 |           0 | Fail    | triangle                                    | diamond        |              7 |          40.22 |           0 |             0.00 |
|     8 |           0 | Fail    | circle                                      | asterisk       |             12 |          69.53 |           0 |             0.00 |
|     9 |           0 | Fail    | diamond                                     | asterisk       |             14 |          85.26 |           0 |             0.00 |
|    10 |           0 | Fail    | asterisk                                    | diamond        |             17 |         156.10 |           0 |             0.00 |
|    11 |           0 | Fail    | square                                      | cross          |             16 |         793.40 |           0 |             0.00 |
|    12 |           0 | Fail    | diamond                                     | cross          |             12 |         257.35 |           0 |             0.00 |
|    13 |           0 | Success | circle                                      | circle         |             28 |         148.42 |           0 |             0.00 |
|    14 |           0 | Success | circle                                      | circle         |              6 |          35.33 |           0 |             0.00 |
|    15 |           0 | Success | square                                      | square         |              7 |          40.01 |           0 |             0.00 |
|    16 |           0 | Success | diamond                                     | diamond        |             28 |         147.39 |           0 |             0.00 |
|    17 |           0 | Fail    | cross                                       | triangle       |              6 |          35.94 |           0 |             0.00 |
|    18 |           0 | Fail    | circle                                      | cross          |              5 |          26.90 |           0 |             0.00 |
|    19 |           0 | Fail    | circle                                      | triangle       |             13 |          73.31 |           0 |             0.00 |
|    20 |           0 | Fail    | triangle                                    | circle         |             16 |         131.80 |           0 |             0.00 |
|    21 |           0 | Success | square                                      | square         |             15 |         505.53 |           0 |             0.00 |
|    22 |           0 | Fail    | square                                      | circle         |             11 |         231.19 |           1 |             3.01 |
|    23 |           0 | Fail    | diamond                                     | cross          |             11 |          63.32 |           0 |             0.00 |
|    24 |           0 | Fail    | triangle                                    | cross          |             37 |         204.09 |           0 |             0.00 |
|    25 |           0 | Fail    | square                                      | circle         |             22 |         115.94 |           0 |             0.00 |
|    26 |           0 | Success | circle                                      | circle         |             11 |          67.13 |           0 |             0.00 |
|    27 |           0 | Fail    | square                                      | asterisk       |              9 |          52.72 |           0 |             0.00 |
|    28 |           0 | Fail    | asterisk                                    | circle         |              8 |          47.55 |           0 |             0.00 |
|    29 |           0 | Fail    | triangle                                    | asterisk       |              8 |          46.74 |           0 |             0.00 |
|    30 |           0 | Fail    | cross                                       | square         |             11 |          71.14 |           0 |             0.00 |
|    31 |           0 | Success | triangle                                    | triangle       |             25 |         767.86 |           1 |             3.00 |
|    32 |           0 | Fail    | circle                                      | cross          |             10 |         180.44 |           0 |             0.00 |
|    33 |           0 | Fail    | diamond                                     | circle         |             12 |         126.66 |           0 |             0.00 |
|    34 |           0 | Success | square                                      | square         |             18 |         100.03 |           0 |             0.00 |
|    35 |           0 | Success | square                                      | square         |             14 |          76.77 |           0 |             0.00 |
|    36 |           0 | Fail    | No figure submitted (message limit reached) | cross          |             40 |         219.36 |           0 |             0.00 |
|    37 |           0 | Fail    | diamond                                     | asterisk       |             33 |         179.37 |           0 |             0.00 |
|    38 |           0 | Fail    | cross                                       | asterisk       |             10 |          55.08 |           0 |             0.00 |
|    39 |           0 | Fail    | cross                                       | diamond        |              8 |          47.07 |           0 |             0.00 |
|    40 |           0 | Success | square                                      | square         |             12 |         123.58 |           0 |             0.00 |
|    41 |           0 | Fail    | square                                      | triangle       |             12 |         289.95 |           0 |             0.00 |
|    42 |           0 | Fail    | asterisk                                    | triangle       |             18 |         454.19 |           0 |             0.00 |
|    43 |           0 | Fail    | square                                      | diamond        |             17 |         166.32 |           0 |             0.00 |
|    44 |           0 | Fail    | square                                      | asterisk       |             26 |         224.88 |           0 |             0.00 |
|    45 |           0 | Fail    | diamond                                     | square         |             23 |         192.55 |           0 |             0.00 |
|    46 |           0 | Success | triangle                                    | triangle       |             16 |          88.49 |           0 |             0.00 |
|    47 |           0 | Fail    | diamond                                     | triangle       |             11 |          61.37 |           0 |             0.00 |
|    48 |           0 | Fail    | asterisk                                    | triangle       |             13 |          73.32 |           0 |             0.00 |
|    49 |           0 | Fail    | triangle                                    | diamond        |             12 |          70.56 |           0 |             0.00 |
|    50 |           0 | Fail    | cross                                       | square         |             39 |         246.80 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    22 | Agent5               | 2026-05-13T03:01:50.517907+00:00 | 2026-05-13T03:01:53.523156+00:00 |             3.01 |
|    31 | Agent2               | 2026-05-13T03:26:47.594310+00:00 | 2026-05-13T03:26:50.598227+00:00 |             3.00 |
```
