# Wheel auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 268.77 seconds
- Average total messages: 20.56
- Success rate: 13/50 (26.0%)
- Reconnect pauses: 4 across 4 trial(s); 194.24 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     204 |           204 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     195 |           195 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     143 |           243 |        58.8% (0.588) |                0.250 | 2.354 |                0.586 |
| wheel    | Agent3 | Agent2    |                  4 |      91 |           243 |        37.4% (0.374) |                0.250 | 1.498 |                0.373 |
| wheel    | Agent3 | Agent4    |                  4 |       4 |           243 |         1.6% (0.016) |                0.250 | 0.066 |                0.018 |
| wheel    | Agent3 | Agent5    |                  4 |       5 |           243 |         2.1% (0.021) |                0.250 | 0.082 |                0.022 |
| wheel    | Agent4 | Agent3    |                  1 |     203 |           203 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     181 |           181 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| wheel    | Agent1 | client_assigned |     1 |
| wheel    | Agent3 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Success | square                                      | square         |             37 |        1336.91 |           0 |             0.00 |
|     2 |           0 | Fail    | square                                      | cross          |             11 |          69.02 |           0 |             0.00 |
|     3 |           0 | Fail    | cross                                       | diamond        |             17 |         111.43 |           0 |             0.00 |
|     4 |           0 | Fail    | circle                                      | triangle       |             17 |         112.17 |           0 |             0.00 |
|     5 |           0 | Fail    | circle                                      | diamond        |             23 |         138.01 |           0 |             0.00 |
|     6 |           0 | Fail    | cross                                       | square         |             11 |          68.13 |           0 |             0.00 |
|     7 |           0 | Fail    | cross                                       | circle         |             15 |          98.68 |           0 |             0.00 |
|     8 |           0 | Success | diamond                                     | diamond        |             29 |         213.11 |           0 |             0.00 |
|     9 |           0 | Fail    | cross                                       | triangle       |             22 |         226.80 |           0 |             0.00 |
|    10 |           0 | Success | cross                                       | cross          |             10 |          63.89 |           0 |             0.00 |
|    11 |           0 | Fail    | circle                                      | square         |             16 |         114.05 |           0 |             0.00 |
|    12 |           0 | Fail    | circle                                      | cross          |             13 |         702.88 |           0 |             0.00 |
|    13 |           0 | Success | cross                                       | cross          |             34 |         529.46 |           0 |             0.00 |
|    14 |           0 | Fail    | triangle                                    | circle         |             40 |         239.96 |           0 |             0.00 |
|    15 |           0 | Fail    | triangle                                    | diamond        |             25 |         143.50 |           0 |             0.00 |
|    16 |           0 | Fail    | cross                                       | asterisk       |              9 |          59.62 |           0 |             0.00 |
|    17 |           0 | Fail    | circle                                      | asterisk       |             12 |          79.75 |           0 |             0.00 |
|    18 |           0 | Fail    | square                                      | triangle       |             26 |         157.52 |           0 |             0.00 |
|    19 |           0 | Fail    | asterisk                                    | triangle       |             10 |         180.64 |           0 |             0.00 |
|    20 |           0 | Fail    | asterisk                                    | square         |             22 |         136.31 |           0 |             0.00 |
|    21 |           0 | Fail    | circle                                      | diamond        |             20 |         117.68 |           0 |             0.00 |
|    22 |           0 | Fail    | triangle                                    | circle         |             19 |         122.47 |           0 |             0.00 |
|    23 |           0 | Fail    | triangle                                    | asterisk       |             16 |        1015.13 |           0 |             0.00 |
|    24 |           0 | Fail    | square                                      | triangle       |             38 |        1602.82 |           0 |             0.00 |
|    25 |           0 | Success | asterisk                                    | asterisk       |             16 |          96.01 |           0 |             0.00 |
|    26 |           0 | Success | square                                      | square         |             10 |          63.01 |           0 |             0.00 |
|    27 |           0 | Fail    | square                                      | asterisk       |              6 |          40.48 |           0 |             0.00 |
|    28 |           0 | Success | square                                      | square         |             14 |          91.28 |           0 |             0.00 |
|    29 |           0 | Success | cross                                       | cross          |             11 |          67.14 |           0 |             0.00 |
|    30 |           0 | Fail    | circle                                      | square         |             14 |          87.02 |           0 |             0.00 |
|    31 |           0 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |         420.67 |           0 |             0.00 |
|    32 |           0 | Fail    | circle                                      | square         |             14 |         173.34 |           0 |             0.00 |
|    33 |           0 | Success | asterisk                                    | asterisk       |             16 |         105.70 |           0 |             0.00 |
|    34 |           0 | Success | asterisk                                    | asterisk       |             29 |         310.61 |           1 |            65.08 |
|    35 |           0 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        1189.58 |           1 |             0.00 |
|    36 |           0 | Fail    | cross                                       | triangle       |             43 |         984.84 |           0 |             0.00 |
|    37 |           0 | Success | diamond                                     | diamond        |             11 |          74.81 |           0 |             0.00 |
|    38 |           0 | Fail    | asterisk                                    | square         |             15 |          92.90 |           0 |             0.00 |
|    39 |           0 | Fail    | square                                      | asterisk       |             25 |         156.94 |           0 |             0.00 |
|    40 |           0 | Fail    | triangle                                    | diamond        |             28 |         174.07 |           0 |             0.00 |
|    41 |           0 | Fail    | circle                                      | square         |             12 |          80.39 |           0 |             0.00 |
|    42 |           0 | Fail    | triangle                                    | asterisk       |             16 |         108.92 |           0 |             0.00 |
|    43 |           0 | Success | circle                                      | circle         |             20 |         204.93 |           0 |             0.00 |
|    44 |           0 | Fail    | cross                                       | triangle       |             22 |         133.09 |           0 |             0.00 |
|    45 |           0 | Success | triangle                                    | triangle       |             32 |         321.28 |           1 |            66.08 |
|    46 |           0 | Fail    | diamond                                     | square         |             14 |         400.39 |           1 |            63.08 |
|    47 |           0 | Fail    | asterisk                                    | circle         |             10 |          61.80 |           0 |             0.00 |
|    48 |           0 | Fail    | cross                                       | diamond        |             21 |         120.67 |           0 |             0.00 |
|    49 |           0 | Fail    | asterisk                                    | square         |             21 |         132.41 |           0 |             0.00 |
|    50 |           0 | Fail    | circle                                      | cross          |             16 |         106.13 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    34 | Agent5               | 2026-05-15T03:37:48.787237+00:00 | 2026-05-15T03:38:53.864066+00:00 |            65.08 |
|    35 | Agent4               | 2026-05-15T03:43:20.835510+00:00 | 2026-05-15T03:43:20.837745+00:00 |             0.00 |
|    45 | Agent4               | 2026-05-15T04:39:42.273865+00:00 | 2026-05-15T04:40:48.351668+00:00 |            66.08 |
|    46 | Agent5               | 2026-05-15T04:48:02.975496+00:00 | 2026-05-15T04:49:06.050670+00:00 |            63.08 |
```
