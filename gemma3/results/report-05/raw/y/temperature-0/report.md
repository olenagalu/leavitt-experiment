# Y topology auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 215.52 seconds
- Average total messages: 18.46
- Success rate: 12/50 (24.0%)
- Reconnect pauses: 1 across 1 trial(s); 4.01 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     170 |           170 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     181 |           181 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      91 |           185 |        49.2% (0.492) |                0.333 | 1.476 |                0.491 |
| y        | Agent3 | Agent2    |                  3 |      74 |           185 |        40.0% (0.400) |                0.333 | 1.200 |                0.399 |
| y        | Agent3 | Agent4    |                  3 |      20 |           185 |        10.8% (0.108) |                0.333 | 0.324 |                0.110 |
| y        | Agent4 | Agent3    |                  2 |     151 |           167 |        90.4% (0.904) |                0.500 | 1.808 |                0.902 |
| y        | Agent4 | Agent5    |                  2 |      16 |           167 |         9.6% (0.096) |                0.500 | 0.192 |                0.098 |
| y        | Agent5 | Agent4    |                  1 |     216 |           216 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent3 | client_assigned |     1 |
| y        | Agent4 | client_assigned |     2 |
| y        | Agent5 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Fail    | cross                                       | triangle       |             10 |         246.48 |           0 |             0.00 |
|     2 |           0 | Fail    | diamond                                     | asterisk       |             10 |          57.52 |           0 |             0.00 |
|     3 |           0 | Fail    | square                                      | circle         |             22 |         128.38 |           0 |             0.00 |
|     4 |           0 | Fail    | triangle                                    | asterisk       |             15 |          84.57 |           0 |             0.00 |
|     5 |           0 | Success | diamond                                     | diamond        |             15 |          91.21 |           0 |             0.00 |
|     6 |           0 | Fail    | diamond                                     | square         |             15 |          90.09 |           0 |             0.00 |
|     7 |           0 | Fail    | cross                                       | triangle       |             20 |         117.71 |           0 |             0.00 |
|     8 |           0 | Fail    | asterisk                                    | circle         |             39 |         224.94 |           0 |             0.00 |
|     9 |           0 | Success | diamond                                     | diamond        |             10 |          66.05 |           0 |             0.00 |
|    10 |           0 | Fail    | circle                                      | asterisk       |             16 |         178.71 |           0 |             0.00 |
|    11 |           0 | Fail    | circle                                      | cross          |             17 |         173.57 |           0 |             0.00 |
|    12 |           0 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2775.85 |           0 |             0.00 |
|    13 |           0 | Fail    | cross                                       | square         |             14 |         290.26 |           0 |             0.00 |
|    14 |           0 | Success | triangle                                    | triangle       |             24 |         142.57 |           0 |             0.00 |
|    15 |           0 | Fail    | cross                                       | triangle       |             10 |          58.18 |           0 |             0.00 |
|    16 |           0 | Fail    | circle                                      | asterisk       |             10 |          58.72 |           0 |             0.00 |
|    17 |           0 | Success | asterisk                                    | asterisk       |             12 |          70.20 |           0 |             0.00 |
|    18 |           0 | Fail    | diamond                                     | cross          |             18 |         107.84 |           0 |             0.00 |
|    19 |           0 | Fail    | circle                                      | square         |             20 |         119.91 |           0 |             0.00 |
|    20 |           0 | Success | square                                      | square         |             28 |         657.73 |           0 |             0.00 |
|    21 |           0 | Fail    | diamond                                     | asterisk       |             29 |         175.71 |           0 |             0.00 |
|    22 |           0 | Success | triangle                                    | triangle       |             28 |         233.58 |           0 |             0.00 |
|    23 |           0 | Fail    | diamond                                     | triangle       |             18 |         203.07 |           0 |             0.00 |
|    24 |           0 | Success | asterisk                                    | asterisk       |              7 |         181.68 |           0 |             0.00 |
|    25 |           0 | Fail    | diamond                                     | cross          |             16 |          93.11 |           0 |             0.00 |
|    26 |           0 | Fail    | square                                      | cross          |              9 |          54.06 |           0 |             0.00 |
|    27 |           0 | Fail    | diamond                                     | triangle       |             10 |          59.86 |           0 |             0.00 |
|    28 |           0 | Success | triangle                                    | triangle       |             21 |         134.03 |           0 |             0.00 |
|    29 |           0 | Fail    | cross                                       | asterisk       |             13 |         148.12 |           0 |             0.00 |
|    30 |           0 | Success | cross                                       | cross          |             24 |         143.73 |           0 |             0.00 |
|    31 |           0 | Fail    | cross                                       | circle         |             49 |         401.40 |           1 |             4.01 |
|    32 |           0 | Fail    | triangle                                    | diamond        |             14 |          93.83 |           0 |             0.00 |
|    33 |           0 | Fail    | square                                      | triangle       |             16 |         181.62 |           0 |             0.00 |
|    34 |           0 | Fail    | diamond                                     | asterisk       |             18 |         170.33 |           0 |             0.00 |
|    35 |           0 | Fail    | asterisk                                    | circle         |             33 |         394.59 |           0 |             0.00 |
|    36 |           0 | Fail    | cross                                       | asterisk       |             19 |         174.76 |           0 |             0.00 |
|    37 |           0 | Fail    | circle                                      | asterisk       |             13 |          78.29 |           0 |             0.00 |
|    38 |           0 | Fail    | circle                                      | square         |             22 |         124.78 |           0 |             0.00 |
|    39 |           0 | Success | asterisk                                    | asterisk       |             15 |          92.10 |           0 |             0.00 |
|    40 |           0 | Fail    | cross                                       | circle         |             12 |         215.71 |           0 |             0.00 |
|    41 |           0 | Fail    | diamond                                     | cross          |              6 |          37.88 |           0 |             0.00 |
|    42 |           0 | Fail    | cross                                       | asterisk       |             13 |          78.58 |           0 |             0.00 |
|    43 |           0 | Success | diamond                                     | diamond        |             11 |          69.29 |           0 |             0.00 |
|    44 |           0 | Fail    | triangle                                    | asterisk       |             26 |         344.29 |           0 |             0.00 |
|    45 |           0 | Fail    | diamond                                     | triangle       |              9 |         129.71 |           0 |             0.00 |
|    46 |           0 | Fail    | square                                      | circle         |             20 |         120.25 |           0 |             0.00 |
|    47 |           0 | Success | asterisk                                    | asterisk       |             18 |         200.87 |           0 |             0.00 |
|    48 |           0 | Fail    | triangle                                    | diamond        |             17 |         256.07 |           0 |             0.00 |
|    49 |           0 | Fail    | square                                      | cross          |             19 |         116.25 |           0 |             0.00 |
|    50 |           0 | Fail    | diamond                                     | triangle       |             23 |         327.89 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    31 | Agent4               | 2026-05-14T09:42:31.568336+00:00 | 2026-05-14T09:42:35.574977+00:00 |             4.01 |
```
