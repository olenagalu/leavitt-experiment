# Wheel auto-trial report

## Summary

- Batch: `temperature-0.2`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 257.79 seconds
- Average total messages: 18.46
- Success rate: 15/50 (30.0%)
- Reconnect pauses: 1 across 1 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     166 |           166 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     181 |           181 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     100 |           179 |        55.9% (0.559) |                0.250 | 2.235 |                0.555 |
| wheel    | Agent3 | Agent2    |                  4 |      67 |           179 |        37.4% (0.374) |                0.250 | 1.497 |                0.373 |
| wheel    | Agent3 | Agent4    |                  4 |       5 |           179 |         2.8% (0.028) |                0.250 | 0.112 |                0.030 |
| wheel    | Agent3 | Agent5    |                  4 |       7 |           179 |         3.9% (0.039) |                0.250 | 0.156 |                0.041 |
| wheel    | Agent4 | Agent3    |                  1 |     181 |           181 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     203 |           203 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| wheel    | Agent1 | client_assigned |     1 |
| wheel    | Agent3 | client_assigned |    12 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.2 | Fail    | triangle                                    | square         |             49 |        2064.77 |           0 |             0.00 |
|     2 |         0.2 | Fail    | square                                      | diamond        |              6 |          82.55 |           0 |             0.00 |
|     3 |         0.2 | Fail    | diamond                                     | asterisk       |             13 |          80.11 |           0 |             0.00 |
|     4 |         0.2 | Success | circle                                      | circle         |              8 |          52.48 |           0 |             0.00 |
|     5 |         0.2 | Fail    | circle                                      | cross          |             18 |         113.50 |           0 |             0.00 |
|     6 |         0.2 | Fail    | cross                                       | triangle       |             10 |          58.34 |           0 |             0.00 |
|     7 |         0.2 | Success | cross                                       | cross          |             32 |         187.93 |           0 |             0.00 |
|     8 |         0.2 | Fail    | diamond                                     | asterisk       |             16 |         108.15 |           0 |             0.00 |
|     9 |         0.2 | Fail    | cross                                       | circle         |             15 |         170.17 |           0 |             0.00 |
|    10 |         0.2 | Fail    | cross                                       | square         |             25 |         155.15 |           0 |             0.00 |
|    11 |         0.2 | Fail    | square                                      | circle         |             24 |         323.70 |           0 |             0.00 |
|    12 |         0.2 | Fail    | circle                                      | asterisk       |             17 |         453.43 |           0 |             0.00 |
|    13 |         0.2 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        1388.66 |           0 |             0.00 |
|    14 |         0.2 | Fail    | square                                      | triangle       |             20 |         476.27 |           0 |             0.00 |
|    15 |         0.2 | Success | asterisk                                    | asterisk       |             17 |         110.64 |           0 |             0.00 |
|    16 |         0.2 | Success | cross                                       | cross          |              6 |          38.89 |           0 |             0.00 |
|    17 |         0.2 | Success | circle                                      | circle         |             10 |          66.24 |           0 |             0.00 |
|    18 |         0.2 | Fail    | asterisk                                    | triangle       |             19 |         114.28 |           0 |             0.00 |
|    19 |         0.2 | Fail    | cross                                       | circle         |             12 |          82.56 |           0 |             0.00 |
|    20 |         0.2 | Success | asterisk                                    | asterisk       |             24 |         153.33 |           0 |             0.00 |
|    21 |         0.2 | Success | square                                      | square         |             16 |         108.05 |           0 |             0.00 |
|    22 |         0.2 | Fail    | triangle                                    | square         |             13 |         155.79 |           0 |             0.00 |
|    23 |         0.2 | Fail    | triangle                                    | cross          |             10 |          76.84 |           0 |             0.00 |
|    24 |         0.2 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        1762.53 |           1 |             0.00 |
|    25 |         0.2 | Fail    | square                                      | asterisk       |             17 |         242.26 |           0 |             0.00 |
|    26 |         0.2 | Fail    | cross                                       | triangle       |             22 |         145.55 |           0 |             0.00 |
|    27 |         0.2 | Fail    | circle                                      | diamond        |             28 |         178.55 |           0 |             0.00 |
|    28 |         0.2 | Fail    | asterisk                                    | triangle       |             24 |         142.99 |           0 |             0.00 |
|    29 |         0.2 | Fail    | cross                                       | square         |             19 |         119.32 |           0 |             0.00 |
|    30 |         0.2 | Fail    | cross                                       | triangle       |             13 |          87.32 |           0 |             0.00 |
|    31 |         0.2 | Fail    | cross                                       | circle         |             12 |          76.13 |           0 |             0.00 |
|    32 |         0.2 | Fail    | cross                                       | square         |             12 |         234.98 |           0 |             0.00 |
|    33 |         0.2 | Fail    | asterisk                                    | triangle       |             40 |        1336.88 |           0 |             0.00 |
|    34 |         0.2 | Success | diamond                                     | diamond        |             17 |         111.03 |           0 |             0.00 |
|    35 |         0.2 | Fail    | circle                                      | asterisk       |             10 |          65.04 |           0 |             0.00 |
|    36 |         0.2 | Fail    | diamond                                     | triangle       |             11 |          75.54 |           0 |             0.00 |
|    37 |         0.2 | Fail    | asterisk                                    | circle         |             14 |          93.89 |           0 |             0.00 |
|    38 |         0.2 | Fail    | cross                                       | asterisk       |             11 |          65.98 |           0 |             0.00 |
|    39 |         0.2 | Fail    | circle                                      | triangle       |             11 |          68.67 |           0 |             0.00 |
|    40 |         0.2 | Success | asterisk                                    | asterisk       |              7 |          57.64 |           0 |             0.00 |
|    41 |         0.2 | Fail    | diamond                                     | cross          |             19 |         195.63 |           0 |             0.00 |
|    42 |         0.2 | Success | asterisk                                    | asterisk       |             16 |         102.29 |           0 |             0.00 |
|    43 |         0.2 | Success | asterisk                                    | asterisk       |             27 |         198.58 |           0 |             0.00 |
|    44 |         0.2 | Success | circle                                      | circle         |             12 |         272.48 |           0 |             0.00 |
|    45 |         0.2 | Success | circle                                      | circle         |             15 |          92.82 |           0 |             0.00 |
|    46 |         0.2 | Success | circle                                      | circle         |             18 |         111.63 |           0 |             0.00 |
|    47 |         0.2 | Fail    | square                                      | asterisk       |             22 |         137.94 |           0 |             0.00 |
|    48 |         0.2 | Fail    | asterisk                                    | cross          |             11 |          71.37 |           0 |             0.00 |
|    49 |         0.2 | Fail    | triangle                                    | asterisk       |             14 |          90.73 |           0 |             0.00 |
|    50 |         0.2 | Success | circle                                      | circle         |             21 |         130.14 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    24 | Agent4               | 2026-05-15T13:43:49.547968+00:00 | 2026-05-15T13:43:49.552391+00:00 |             0.00 |
```
