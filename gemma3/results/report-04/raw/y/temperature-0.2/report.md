# Y topology auto-trial report

## Summary

- Batch: `temperature-0.2`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 302.10 seconds
- Average total messages: 19.56
- Success rate: 11/50 (22.0%)
- Reconnect pauses: 3 across 3 trial(s); 127.14 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     209 |           209 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     203 |           203 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |     100 |           185 |        54.1% (0.541) |                0.333 | 1.622 |                0.539 |
| y        | Agent3 | Agent2    |                  3 |      65 |           185 |        35.1% (0.351) |                0.333 | 1.054 |                0.351 |
| y        | Agent3 | Agent4    |                  3 |      20 |           185 |        10.8% (0.108) |                0.333 | 0.324 |                0.110 |
| y        | Agent4 | Agent3    |                  2 |     119 |           143 |        83.2% (0.832) |                0.500 | 1.664 |                0.830 |
| y        | Agent4 | Agent5    |                  2 |      24 |           143 |        16.8% (0.168) |                0.500 | 0.336 |                0.170 |
| y        | Agent5 | Agent4    |                  1 |     229 |           229 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent1 | client_assigned |     3 |
| y        | Agent2 | client_assigned |     3 |
| y        | Agent3 | client_assigned |     3 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.2 | Fail    | circle                                      | asterisk       |             17 |         314.80 |           0 |             0.00 |
|     2 |         0.2 | Success | cross                                       | cross          |             19 |         146.80 |           0 |             0.00 |
|     3 |         0.2 | Fail    | asterisk                                    | cross          |             11 |          65.72 |           0 |             0.00 |
|     4 |         0.2 | Fail    | square                                      | triangle       |             19 |         110.45 |           0 |             0.00 |
|     5 |         0.2 | Fail    | cross                                       | triangle       |             12 |          71.29 |           0 |             0.00 |
|     6 |         0.2 | Fail    | diamond                                     | triangle       |             16 |          93.12 |           0 |             0.00 |
|     7 |         0.2 | Fail    | cross                                       | square         |             25 |         140.62 |           0 |             0.00 |
|     8 |         0.2 | Fail    | circle                                      | square         |             14 |          83.95 |           0 |             0.00 |
|     9 |         0.2 | Success | diamond                                     | diamond        |             17 |         473.59 |           0 |             0.00 |
|    10 |         0.2 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        1415.87 |           0 |             0.00 |
|    11 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             50 |        1319.43 |           0 |             0.00 |
|    12 |         0.2 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        1422.47 |           0 |             0.00 |
|    13 |         0.2 | Fail    | asterisk                                    | cross          |             20 |         371.70 |           0 |             0.00 |
|    14 |         0.2 | Fail    | cross                                       | diamond        |             16 |          97.83 |           0 |             0.00 |
|    15 |         0.2 | Fail    | circle                                      | diamond        |             21 |         120.59 |           0 |             0.00 |
|    16 |         0.2 | Success | circle                                      | circle         |             12 |          69.62 |           0 |             0.00 |
|    17 |         0.2 | Fail    | triangle                                    | square         |             18 |         107.69 |           0 |             0.00 |
|    18 |         0.2 | Fail    | asterisk                                    | circle         |             13 |          78.74 |           0 |             0.00 |
|    19 |         0.2 | Success | square                                      | square         |             19 |         109.64 |           0 |             0.00 |
|    20 |         0.2 | Fail    | diamond                                     | cross          |             26 |         187.19 |           0 |             0.00 |
|    21 |         0.2 | Fail    | diamond                                     | asterisk       |             14 |         157.80 |           0 |             0.00 |
|    22 |         0.2 | Fail    | square                                      | triangle       |             17 |         320.35 |           0 |             0.00 |
|    23 |         0.2 | Success | circle                                      | circle         |             40 |        1351.39 |           0 |             0.00 |
|    24 |         0.2 | Fail    | square                                      | cross          |             19 |         114.87 |           0 |             0.00 |
|    25 |         0.2 | Success | cross                                       | cross          |              9 |          53.30 |           0 |             0.00 |
|    26 |         0.2 | Success | asterisk                                    | asterisk       |             13 |          76.25 |           0 |             0.00 |
|    27 |         0.2 | Fail    | diamond                                     | circle         |             14 |          85.17 |           0 |             0.00 |
|    28 |         0.2 | Fail    | cross                                       | asterisk       |             15 |          81.54 |           0 |             0.00 |
|    29 |         0.2 | Fail    | cross                                       | triangle       |             15 |          91.60 |           0 |             0.00 |
|    30 |         0.2 | Fail    | circle                                      | square         |              8 |          52.46 |           0 |             0.00 |
|    31 |         0.2 | Success | diamond                                     | diamond        |             17 |         256.50 |           1 |            63.07 |
|    32 |         0.2 | Fail    | asterisk                                    | triangle       |             12 |         231.07 |           1 |            64.07 |
|    33 |         0.2 | Fail    | triangle                                    | cross          |             19 |         116.74 |           0 |             0.00 |
|    34 |         0.2 | Fail    | diamond                                     | asterisk       |             11 |         104.36 |           0 |             0.00 |
|    35 |         0.2 | Success | asterisk                                    | asterisk       |              9 |         261.07 |           0 |             0.00 |
|    36 |         0.2 | Fail    | asterisk                                    | triangle       |             10 |          59.98 |           0 |             0.00 |
|    37 |         0.2 | Fail    | cross                                       | square         |             10 |          60.16 |           0 |             0.00 |
|    38 |         0.2 | Fail    | diamond                                     | square         |             32 |         181.75 |           0 |             0.00 |
|    39 |         0.2 | Fail    | triangle                                    | diamond        |             13 |          82.88 |           0 |             0.00 |
|    40 |         0.2 | Fail    | diamond                                     | asterisk       |             35 |         952.87 |           0 |             0.00 |
|    41 |         0.2 | Fail    | circle                                      | diamond        |             13 |         461.80 |           1 |             0.00 |
|    42 |         0.2 | Fail    | cross                                       | diamond        |              7 |          42.12 |           0 |             0.00 |
|    43 |         0.2 | Success | square                                      | square         |             13 |          75.37 |           0 |             0.00 |
|    44 |         0.2 | Success | asterisk                                    | asterisk       |             25 |         139.15 |           0 |             0.00 |
|    45 |         0.2 | Fail    | cross                                       | square         |             10 |          57.87 |           0 |             0.00 |
|    46 |         0.2 | Fail    | square                                      | asterisk       |             24 |         496.12 |           0 |             0.00 |
|    47 |         0.2 | Fail    | asterisk                                    | circle         |             11 |         725.41 |           0 |             0.00 |
|    48 |         0.2 | Fail    | diamond                                     | cross          |             38 |         651.88 |           0 |             0.00 |
|    49 |         0.2 | Fail    | triangle                                    | cross          |             10 |          58.51 |           0 |             0.00 |
|    50 |         0.2 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |         903.75 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    31 | Agent4               | 2026-05-14T19:17:45.489055+00:00 | 2026-05-14T19:18:48.558699+00:00 |            63.07 |
|    32 | Agent3               | 2026-05-14T19:22:55.361321+00:00 | 2026-05-14T19:23:59.433873+00:00 |            64.07 |
|    41 | Agent4               | 2026-05-14T20:03:36.952753+00:00 | 2026-05-14T20:03:36.955433+00:00 |             0.00 |
```
