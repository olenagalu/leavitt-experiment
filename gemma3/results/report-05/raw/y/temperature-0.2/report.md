# Y topology auto-trial report

## Summary

- Batch: `temperature-0.2`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 228.75 seconds
- Average total messages: 17.42
- Success rate: 15/50 (30.0%)
- Reconnect pauses: 2 across 2 trial(s); 4.02 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     168 |           168 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     205 |           205 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      76 |           171 |        44.4% (0.444) |                0.333 | 1.333 |                0.443 |
| y        | Agent3 | Agent2    |                  3 |      68 |           171 |        39.8% (0.398) |                0.333 | 1.193 |                0.397 |
| y        | Agent3 | Agent4    |                  3 |      27 |           171 |        15.8% (0.158) |                0.333 | 0.474 |                0.159 |
| y        | Agent4 | Agent3    |                  2 |     134 |           158 |        84.8% (0.848) |                0.500 | 1.696 |                0.846 |
| y        | Agent4 | Agent5    |                  2 |      24 |           158 |        15.2% (0.152) |                0.500 | 0.304 |                0.154 |
| y        | Agent5 | Agent4    |                  1 |     150 |           150 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent1 | client_assigned |     7 |
| y        | Agent2 | client_assigned |     6 |
| y        | Agent3 | client_assigned |     6 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.2 | Fail    | circle                                      | triangle       |             37 |         998.42 |           0 |             0.00 |
|     2 |         0.2 | Fail    | triangle                                    | asterisk       |              7 |          44.54 |           0 |             0.00 |
|     3 |         0.2 | Fail    | diamond                                     | triangle       |             13 |          76.60 |           0 |             0.00 |
|     4 |         0.2 | Fail    | triangle                                    | circle         |             17 |         101.47 |           0 |             0.00 |
|     5 |         0.2 | Success | circle                                      | circle         |             14 |          85.71 |           0 |             0.00 |
|     6 |         0.2 | Success | cross                                       | cross          |             14 |          85.86 |           0 |             0.00 |
|     7 |         0.2 | Fail    | diamond                                     | square         |              7 |          44.66 |           0 |             0.00 |
|     8 |         0.2 | Fail    | cross                                       | asterisk       |             24 |         140.70 |           0 |             0.00 |
|     9 |         0.2 | Success | square                                      | square         |             19 |         218.15 |           0 |             0.00 |
|    10 |         0.2 | Success | triangle                                    | triangle       |             17 |         117.26 |           0 |             0.00 |
|    11 |         0.2 | Success | diamond                                     | diamond        |             20 |         191.63 |           0 |             0.00 |
|    12 |         0.2 | Fail    | diamond                                     | asterisk       |             11 |          92.08 |           0 |             0.00 |
|    13 |         0.2 | Fail    | triangle                                    | square         |             26 |         335.43 |           0 |             0.00 |
|    14 |         0.2 | Success | triangle                                    | triangle       |             13 |         121.18 |           0 |             0.00 |
|    15 |         0.2 | Fail    | diamond                                     | cross          |             10 |         239.60 |           1 |             4.01 |
|    16 |         0.2 | Fail    | cross                                       | circle         |              9 |          56.31 |           0 |             0.00 |
|    17 |         0.2 | Fail    | square                                      | triangle       |             12 |         132.42 |           0 |             0.00 |
|    18 |         0.2 | Success | circle                                      | circle         |             13 |          79.48 |           0 |             0.00 |
|    19 |         0.2 | Success | square                                      | square         |             18 |         105.50 |           0 |             0.00 |
|    20 |         0.2 | Success | triangle                                    | triangle       |             10 |          75.25 |           0 |             0.00 |
|    21 |         0.2 | Fail    | square                                      | cross          |             19 |         339.23 |           1 |             0.01 |
|    22 |         0.2 | Success | asterisk                                    | asterisk       |              8 |          45.66 |           0 |             0.00 |
|    23 |         0.2 | Fail    | cross                                       | square         |             20 |         124.62 |           0 |             0.00 |
|    24 |         0.2 | Success | diamond                                     | diamond        |             16 |         272.14 |           0 |             0.00 |
|    25 |         0.2 | Fail    | cross                                       | asterisk       |             30 |        1268.31 |           0 |             0.00 |
|    26 |         0.2 | Fail    | square                                      | circle         |              6 |         215.31 |           0 |             0.00 |
|    27 |         0.2 | Success | cross                                       | cross          |             14 |          83.88 |           0 |             0.00 |
|    28 |         0.2 | Fail    | triangle                                    | diamond        |             14 |          81.28 |           0 |             0.00 |
|    29 |         0.2 | Fail    | square                                      | triangle       |             14 |          79.20 |           0 |             0.00 |
|    30 |         0.2 | Fail    | diamond                                     | triangle       |             17 |         101.66 |           0 |             0.00 |
|    31 |         0.2 | Fail    | cross                                       | triangle       |             23 |         133.88 |           0 |             0.00 |
|    32 |         0.2 | Fail    | diamond                                     | circle         |             13 |          81.27 |           0 |             0.00 |
|    33 |         0.2 | Fail    | cross                                       | square         |             10 |          59.75 |           0 |             0.00 |
|    34 |         0.2 | Fail    | circle                                      | diamond        |             12 |          77.35 |           0 |             0.00 |
|    35 |         0.2 | Fail    | asterisk                                    | triangle       |             15 |         182.28 |           0 |             0.00 |
|    36 |         0.2 | Success | circle                                      | circle         |             18 |         261.40 |           0 |             0.00 |
|    37 |         0.2 | Success | cross                                       | cross          |             12 |         374.53 |           0 |             0.00 |
|    38 |         0.2 | Fail    | asterisk                                    | square         |             41 |         266.41 |           0 |             0.00 |
|    39 |         0.2 | Success | asterisk                                    | asterisk       |             13 |          76.66 |           0 |             0.00 |
|    40 |         0.2 | Fail    | cross                                       | circle         |             25 |         138.46 |           0 |             0.00 |
|    41 |         0.2 | Fail    | square                                      | cross          |             37 |         209.56 |           0 |             0.00 |
|    42 |         0.2 | Fail    | triangle                                    | cross          |              9 |          57.41 |           0 |             0.00 |
|    43 |         0.2 | Fail    | cross                                       | asterisk       |              6 |          37.02 |           0 |             0.00 |
|    44 |         0.2 | Fail    | diamond                                     | triangle       |             11 |          66.39 |           0 |             0.00 |
|    45 |         0.2 | Fail    | cross                                       | square         |             15 |         122.12 |           0 |             0.00 |
|    46 |         0.2 | Fail    | circle                                      | asterisk       |             17 |         280.21 |           0 |             0.00 |
|    47 |         0.2 | Fail    | square                                      | diamond        |             10 |          71.49 |           0 |             0.00 |
|    48 |         0.2 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1258.94 |           0 |             0.00 |
|    49 |         0.2 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1515.26 |           0 |             0.00 |
|    50 |         0.2 | Fail    | triangle                                    | square         |             15 |         213.65 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    15 | Agent1               | 2026-05-14T17:45:59.911310+00:00 | 2026-05-14T17:46:03.916487+00:00 |             4.01 |
|    21 | Agent4               | 2026-05-14T17:58:14.939392+00:00 | 2026-05-14T17:58:14.944400+00:00 |             0.01 |
```
