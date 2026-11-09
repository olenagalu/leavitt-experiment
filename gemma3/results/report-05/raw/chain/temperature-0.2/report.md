# Chain auto-trial report

## Summary

- Batch: `temperature-0.2`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 239.68 seconds
- Average total messages: 16.50
- Success rate: 19/50 (38.0%)
- Reconnect pauses: 1 across 1 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     159 |           159 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     154 |           175 |        88.0% (0.880) |                0.500 | 1.760 |                0.878 |
| chain    | Agent2 | Agent3    |                  2 |      21 |           175 |        12.0% (0.120) |                0.500 | 0.240 |                0.122 |
| chain    | Agent3 | Agent2    |                  2 |     169 |           182 |        92.9% (0.929) |                0.500 | 1.857 |                0.926 |
| chain    | Agent3 | Agent4    |                  2 |      13 |           182 |         7.1% (0.071) |                0.500 | 0.143 |                0.074 |
| chain    | Agent4 | Agent3    |                  2 |      87 |           144 |        60.4% (0.604) |                0.500 | 1.208 |                0.603 |
| chain    | Agent4 | Agent5    |                  2 |      57 |           144 |        39.6% (0.396) |                0.500 | 0.792 |                0.397 |
| chain    | Agent5 | Agent4    |                  1 |     164 |           164 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
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
|     1 |         0.2 | Success | triangle                                    | triangle       |             16 |         476.58 |           0 |             0.00 |
|     2 |         0.2 | Success | circle                                      | circle         |             12 |          68.00 |           0 |             0.00 |
|     3 |         0.2 | Fail    | triangle                                    | cross          |             14 |          82.37 |           0 |             0.00 |
|     4 |         0.2 | Success | asterisk                                    | asterisk       |              6 |          36.04 |           0 |             0.00 |
|     5 |         0.2 | Fail    | asterisk                                    | diamond        |             13 |          74.03 |           0 |             0.00 |
|     6 |         0.2 | Fail    | triangle                                    | cross          |             10 |          57.90 |           0 |             0.00 |
|     7 |         0.2 | Fail    | asterisk                                    | triangle       |             13 |          75.27 |           0 |             0.00 |
|     8 |         0.2 | Fail    | square                                      | cross          |             12 |          71.64 |           0 |             0.00 |
|     9 |         0.2 | Success | triangle                                    | triangle       |             10 |          62.31 |           0 |             0.00 |
|    10 |         0.2 | Fail    | square                                      | cross          |             10 |          61.48 |           0 |             0.00 |
|    11 |         0.2 | Fail    | diamond                                     | triangle       |              8 |          57.98 |           0 |             0.00 |
|    12 |         0.2 | Success | diamond                                     | diamond        |             10 |         159.08 |           0 |             0.00 |
|    13 |         0.2 | Success | triangle                                    | triangle       |             15 |         231.51 |           0 |             0.00 |
|    14 |         0.2 | Success | cross                                       | cross          |              9 |         113.13 |           0 |             0.00 |
|    15 |         0.2 | Fail    | triangle                                    | asterisk       |              6 |          43.18 |           0 |             0.00 |
|    16 |         0.2 | Fail    | asterisk                                    | triangle       |             23 |         241.18 |           0 |             0.00 |
|    17 |         0.2 | Success | diamond                                     | diamond        |              8 |          47.55 |           0 |             0.00 |
|    18 |         0.2 | Fail    | square                                      | circle         |             29 |         156.48 |           0 |             0.00 |
|    19 |         0.2 | Success | diamond                                     | diamond        |             10 |          59.16 |           0 |             0.00 |
|    20 |         0.2 | Fail    | circle                                      | square         |              9 |          52.25 |           0 |             0.00 |
|    21 |         0.2 | Fail    | triangle                                    | square         |             18 |         100.93 |           0 |             0.00 |
|    22 |         0.2 | Fail    | square                                      | cross          |             27 |         146.44 |           0 |             0.00 |
|    23 |         0.2 | Fail    | square                                      | diamond        |             14 |          90.84 |           0 |             0.00 |
|    24 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             50 |         973.26 |           0 |             0.00 |
|    25 |         0.2 | Fail    | asterisk                                    | circle         |             15 |         157.69 |           0 |             0.00 |
|    26 |         0.2 | Fail    | diamond                                     | square         |             36 |         753.99 |           0 |             0.00 |
|    27 |         0.2 | Fail    | asterisk                                    | cross          |             13 |          75.97 |           0 |             0.00 |
|    28 |         0.2 | Fail    | triangle                                    | diamond        |             13 |          87.55 |           0 |             0.00 |
|    29 |         0.2 | Success | cross                                       | cross          |             19 |         103.51 |           0 |             0.00 |
|    30 |         0.2 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        1508.98 |           0 |             0.00 |
|    31 |         0.2 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        1780.96 |           0 |             0.00 |
|    32 |         0.2 | Success | square                                      | square         |             16 |         141.88 |           0 |             0.00 |
|    33 |         0.2 | Fail    | triangle                                    | square         |             18 |         100.26 |           0 |             0.00 |
|    34 |         0.2 | Fail    | triangle                                    | diamond        |             13 |          73.13 |           0 |             0.00 |
|    35 |         0.2 | Success | diamond                                     | diamond        |             13 |          74.26 |           0 |             0.00 |
|    36 |         0.2 | Success | diamond                                     | diamond        |              6 |          35.75 |           0 |             0.00 |
|    37 |         0.2 | Fail    | cross                                       | triangle       |             25 |         146.04 |           0 |             0.00 |
|    38 |         0.2 | Success | square                                      | square         |             11 |          63.09 |           0 |             0.00 |
|    39 |         0.2 | Fail    | cross                                       | circle         |             12 |          69.02 |           0 |             0.00 |
|    40 |         0.2 | Success | triangle                                    | triangle       |              9 |          53.33 |           0 |             0.00 |
|    41 |         0.2 | Success | cross                                       | cross          |             15 |         120.27 |           0 |             0.00 |
|    42 |         0.2 | Success | cross                                       | cross          |             16 |         867.55 |           0 |             0.00 |
|    43 |         0.2 | Success | square                                      | square         |             11 |         274.52 |           1 |             0.00 |
|    44 |         0.2 | Fail    | diamond                                     | square         |              9 |          57.53 |           0 |             0.00 |
|    45 |         0.2 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        1544.53 |           0 |             0.00 |
|    46 |         0.2 | Success | cross                                       | cross          |              8 |          97.60 |           0 |             0.00 |
|    47 |         0.2 | Fail    | triangle                                    | cross          |             19 |         107.62 |           0 |             0.00 |
|    48 |         0.2 | Fail    | triangle                                    | square         |              7 |          40.84 |           0 |             0.00 |
|    49 |         0.2 | Fail    | diamond                                     | square         |             12 |          69.36 |           0 |             0.00 |
|    50 |         0.2 | Fail    | cross                                       | triangle       |              7 |          40.12 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    43 | Agent4               | 2026-05-14T03:38:43.469127+00:00 | 2026-05-14T03:38:43.471181+00:00 |             0.00 |
```
