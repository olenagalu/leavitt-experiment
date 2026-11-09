# Chain auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 177.91 seconds
- Average total messages: 16.48
- Success rate: 16/50 (32.0%)
- Reconnect pauses: 3 across 3 trial(s); 187.22 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     155 |           155 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     154 |           185 |        83.2% (0.832) |                0.500 | 1.665 |                0.831 |
| chain    | Agent2 | Agent3    |                  2 |      31 |           185 |        16.8% (0.168) |                0.500 | 0.335 |                0.169 |
| chain    | Agent3 | Agent2    |                  2 |     151 |           163 |        92.6% (0.926) |                0.500 | 1.853 |                0.924 |
| chain    | Agent3 | Agent4    |                  2 |      12 |           163 |         7.4% (0.074) |                0.500 | 0.147 |                0.076 |
| chain    | Agent4 | Agent3    |                  2 |     103 |           158 |        65.2% (0.652) |                0.500 | 1.304 |                0.651 |
| chain    | Agent4 | Agent5    |                  2 |      55 |           158 |        34.8% (0.348) |                0.500 | 0.696 |                0.349 |
| chain    | Agent5 | Agent4    |                  1 |     162 |           162 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| chain    | Agent2 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           1 | Success | cross                                       | cross          |             17 |         500.74 |           0 |             0.00 |
|     2 |           1 | Fail    | asterisk                                    | triangle       |              7 |          39.53 |           0 |             0.00 |
|     3 |           1 | Fail    | circle                                      | diamond        |             11 |          61.65 |           0 |             0.00 |
|     4 |           1 | Fail    | triangle                                    | square         |             18 |          99.52 |           0 |             0.00 |
|     5 |           1 | Success | circle                                      | circle         |             19 |         108.01 |           0 |             0.00 |
|     6 |           1 | Fail    | square                                      | circle         |              9 |          52.64 |           0 |             0.00 |
|     7 |           1 | Fail    | asterisk                                    | square         |             14 |          77.41 |           0 |             0.00 |
|     8 |           1 | Fail    | diamond                                     | square         |             10 |          59.07 |           0 |             0.00 |
|     9 |           1 | Fail    | cross                                       | triangle       |             14 |          76.64 |           0 |             0.00 |
|    10 |           1 | Fail    | diamond                                     | square         |             12 |          79.81 |           0 |             0.00 |
|    11 |           1 | Fail    | square                                      | circle         |             32 |         268.73 |           0 |             0.00 |
|    12 |           1 | Fail    | square                                      | asterisk       |             20 |         369.33 |           0 |             0.00 |
|    13 |           1 | Success | circle                                      | circle         |             26 |         507.49 |           0 |             0.00 |
|    14 |           1 | Fail    | diamond                                     | circle         |             19 |         133.61 |           0 |             0.00 |
|    15 |           1 | Success | square                                      | square         |             31 |         305.52 |           0 |             0.00 |
|    16 |           1 | Fail    | circle                                      | triangle       |             14 |          83.23 |           0 |             0.00 |
|    17 |           1 | Success | triangle                                    | triangle       |             31 |         171.61 |           0 |             0.00 |
|    18 |           1 | Fail    | square                                      | triangle       |              8 |          46.53 |           0 |             0.00 |
|    19 |           1 | Success | asterisk                                    | asterisk       |             12 |          68.55 |           0 |             0.00 |
|    20 |           1 | Success | circle                                      | circle         |              7 |          41.15 |           0 |             0.00 |
|    21 |           1 | Fail    | cross                                       | diamond        |             10 |          62.30 |           0 |             0.00 |
|    22 |           1 | Fail    | cross                                       | triangle       |             14 |         149.79 |           0 |             0.00 |
|    23 |           1 | Success | cross                                       | cross          |             10 |          56.54 |           0 |             0.00 |
|    24 |           1 | Success | square                                      | square         |             19 |         125.30 |           0 |             0.00 |
|    25 |           1 | Success | square                                      | square         |             19 |         515.36 |           1 |            62.07 |
|    26 |           1 | Fail    | asterisk                                    | triangle       |             10 |         121.05 |           0 |             0.00 |
|    27 |           1 | Fail    | diamond                                     | cross          |             16 |         153.13 |           0 |             0.00 |
|    28 |           1 | Fail    | circle                                      | square         |             11 |          63.91 |           0 |             0.00 |
|    29 |           1 | Fail    | circle                                      | square         |             10 |          57.47 |           0 |             0.00 |
|    30 |           1 | Fail    | triangle                                    | asterisk       |             14 |          79.72 |           0 |             0.00 |
|    31 |           1 | Fail    | square                                      | asterisk       |             15 |          85.13 |           0 |             0.00 |
|    32 |           1 | Fail    | diamond                                     | circle         |             21 |         114.06 |           0 |             0.00 |
|    33 |           1 | Success | triangle                                    | triangle       |             10 |          57.29 |           0 |             0.00 |
|    34 |           1 | Success | asterisk                                    | asterisk       |             12 |          72.41 |           0 |             0.00 |
|    35 |           1 | Fail    | cross                                       | diamond        |              8 |          53.27 |           0 |             0.00 |
|    36 |           1 | Success | square                                      | square         |             10 |         115.63 |           0 |             0.00 |
|    37 |           1 | Fail    | No figure submitted (message limit reached) | square         |             50 |        1682.76 |           0 |             0.00 |
|    38 |           1 | Fail    | diamond                                     | square         |             27 |         534.65 |           1 |            70.08 |
|    39 |           1 | Fail    | square                                      | circle         |             12 |          68.90 |           0 |             0.00 |
|    40 |           1 | Fail    | cross                                       | asterisk       |             20 |         111.38 |           0 |             0.00 |
|    41 |           1 | Success | cross                                       | cross          |             29 |         162.17 |           0 |             0.00 |
|    42 |           1 | Fail    | circle                                      | square         |             20 |         115.94 |           0 |             0.00 |
|    43 |           1 | Fail    | triangle                                    | square         |             13 |          71.44 |           0 |             0.00 |
|    44 |           1 | Fail    | cross                                       | triangle       |             22 |         118.44 |           0 |             0.00 |
|    45 |           1 | Success | diamond                                     | diamond        |             10 |          62.36 |           0 |             0.00 |
|    46 |           1 | Fail    | circle                                      | square         |             12 |          71.48 |           0 |             0.00 |
|    47 |           1 | Success | triangle                                    | triangle       |             15 |          97.33 |           0 |             0.00 |
|    48 |           1 | Fail    | triangle                                    | asterisk       |             16 |         348.79 |           0 |             0.00 |
|    49 |           1 | Fail    | asterisk                                    | circle         |             30 |         352.96 |           1 |            55.07 |
|    50 |           1 | Fail    | diamond                                     | circle         |              8 |          63.62 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    25 | Agent4               | 2026-05-14T04:47:17.422324+00:00 | 2026-05-14T04:48:19.494427+00:00 |            62.07 |
|    38 | Agent4               | 2026-05-14T05:44:00.168778+00:00 | 2026-05-14T05:45:10.249188+00:00 |            70.08 |
|    49 | Agent4               | 2026-05-14T06:14:08.548884+00:00 | 2026-05-14T06:15:03.614360+00:00 |            55.07 |
```
