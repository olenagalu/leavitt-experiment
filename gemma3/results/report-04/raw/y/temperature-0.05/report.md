# Y topology auto-trial report

## Summary

- Batch: `temperature-0.05`
- Temperature: 0.05
- Completed trials: 50/50
- Average time: 212.86 seconds
- Average total messages: 18.62
- Success rate: 16/50 (32.0%)
- Reconnect pauses: 1 across 1 trial(s); 64.07 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     177 |           177 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     169 |           169 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      80 |           180 |        44.4% (0.444) |                0.333 | 1.333 |                0.444 |
| y        | Agent3 | Agent2    |                  3 |      67 |           180 |        37.2% (0.372) |                0.333 | 1.117 |                0.372 |
| y        | Agent3 | Agent4    |                  3 |      33 |           180 |        18.3% (0.183) |                0.333 | 0.550 |                0.185 |
| y        | Agent4 | Agent3    |                  2 |     158 |           175 |        90.3% (0.903) |                0.500 | 1.806 |                0.901 |
| y        | Agent4 | Agent5    |                  2 |      17 |           175 |         9.7% (0.097) |                0.500 | 0.194 |                0.099 |
| y        | Agent5 | Agent4    |                  1 |     208 |           208 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent1 | client_assigned |     7 |
| y        | Agent2 | client_assigned |     7 |
| y        | Agent3 | client_assigned |     7 |
| y        | Agent4 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |        0.05 | Success | triangle                                    | triangle       |             19 |         329.93 |           0 |             0.00 |
|     2 |        0.05 | Fail    | triangle                                    | square         |             15 |          86.90 |           0 |             0.00 |
|     3 |        0.05 | Success | triangle                                    | triangle       |             15 |          86.09 |           0 |             0.00 |
|     4 |        0.05 | Fail    | triangle                                    | circle         |             21 |         123.89 |           0 |             0.00 |
|     5 |        0.05 | Fail    | square                                      | asterisk       |             19 |         113.94 |           0 |             0.00 |
|     6 |        0.05 | Success | diamond                                     | diamond        |              9 |          53.05 |           0 |             0.00 |
|     7 |        0.05 | Fail    | asterisk                                    | triangle       |             36 |         201.74 |           0 |             0.00 |
|     8 |        0.05 | Fail    | triangle                                    | cross          |             23 |         135.61 |           0 |             0.00 |
|     9 |        0.05 | Fail    | cross                                       | triangle       |             41 |         762.25 |           0 |             0.00 |
|    10 |        0.05 | Fail    | square                                      | circle         |              9 |         142.03 |           0 |             0.00 |
|    11 |        0.05 | Fail    | triangle                                    | cross          |             12 |          85.43 |           0 |             0.00 |
|    12 |        0.05 | Fail    | diamond                                     | cross          |             24 |         792.44 |           0 |             0.00 |
|    13 |        0.05 | Fail    | triangle                                    | cross          |             22 |         122.51 |           0 |             0.00 |
|    14 |        0.05 | Success | diamond                                     | diamond        |             14 |          81.65 |           0 |             0.00 |
|    15 |        0.05 | Success | diamond                                     | diamond        |             15 |          85.73 |           0 |             0.00 |
|    16 |        0.05 | Fail    | diamond                                     | circle         |              9 |          54.94 |           0 |             0.00 |
|    17 |        0.05 | Fail    | triangle                                    | square         |              9 |          55.23 |           0 |             0.00 |
|    18 |        0.05 | Success | diamond                                     | diamond        |              7 |         154.78 |           0 |             0.00 |
|    19 |        0.05 | Success | triangle                                    | triangle       |             38 |         796.51 |           0 |             0.00 |
|    20 |        0.05 | Success | cross                                       | cross          |             14 |          83.44 |           0 |             0.00 |
|    21 |        0.05 | Fail    | cross                                       | asterisk       |             13 |         234.19 |           0 |             0.00 |
|    22 |        0.05 | Fail    | cross                                       | diamond        |             16 |         277.72 |           0 |             0.00 |
|    23 |        0.05 | Success | triangle                                    | triangle       |              8 |          53.87 |           0 |             0.00 |
|    24 |        0.05 | Fail    | square                                      | circle         |             30 |         264.29 |           0 |             0.00 |
|    25 |        0.05 | Success | cross                                       | cross          |             27 |         149.66 |           0 |             0.00 |
|    26 |        0.05 | Fail    | circle                                      | square         |             15 |          88.43 |           0 |             0.00 |
|    27 |        0.05 | Success | square                                      | square         |             13 |          88.23 |           0 |             0.00 |
|    28 |        0.05 | Fail    | cross                                       | circle         |             12 |         127.40 |           0 |             0.00 |
|    29 |        0.05 | Success | square                                      | square         |              8 |          49.74 |           0 |             0.00 |
|    30 |        0.05 | Fail    | diamond                                     | asterisk       |             17 |         206.78 |           0 |             0.00 |
|    31 |        0.05 | Fail    | asterisk                                    | circle         |             41 |        1198.43 |           1 |            64.07 |
|    32 |        0.05 | Fail    | triangle                                    | circle         |             11 |          63.66 |           0 |             0.00 |
|    33 |        0.05 | Success | diamond                                     | diamond        |             27 |         155.20 |           0 |             0.00 |
|    34 |        0.05 | Fail    | circle                                      | triangle       |             13 |          76.51 |           0 |             0.00 |
|    35 |        0.05 | Fail    | circle                                      | square         |             29 |         160.27 |           0 |             0.00 |
|    36 |        0.05 | Success | asterisk                                    | asterisk       |             14 |          90.96 |           0 |             0.00 |
|    37 |        0.05 | Fail    | cross                                       | diamond        |             19 |         183.97 |           0 |             0.00 |
|    38 |        0.05 | Fail    | No figure submitted (message limit reached) | square         |             50 |         282.26 |           0 |             0.00 |
|    39 |        0.05 | Fail    | cross                                       | asterisk       |             25 |         179.77 |           0 |             0.00 |
|    40 |        0.05 | Fail    | square                                      | diamond        |             13 |         166.02 |           0 |             0.00 |
|    41 |        0.05 | Fail    | diamond                                     | asterisk       |              8 |          56.15 |           0 |             0.00 |
|    42 |        0.05 | Fail    | cross                                       | asterisk       |             37 |        1464.35 |           0 |             0.00 |
|    43 |        0.05 | Fail    | diamond                                     | square         |             10 |          59.78 |           0 |             0.00 |
|    44 |        0.05 | Fail    | triangle                                    | diamond        |             19 |         111.42 |           0 |             0.00 |
|    45 |        0.05 | Success | square                                      | square         |             11 |          66.46 |           0 |             0.00 |
|    46 |        0.05 | Fail    | diamond                                     | triangle       |              7 |          44.45 |           0 |             0.00 |
|    47 |        0.05 | Success | diamond                                     | diamond        |             10 |          58.68 |           0 |             0.00 |
|    48 |        0.05 | Fail    | cross                                       | square         |             14 |          81.32 |           0 |             0.00 |
|    49 |        0.05 | Fail    | cross                                       | square         |             15 |          90.29 |           0 |             0.00 |
|    50 |        0.05 | Fail    | triangle                                    | asterisk       |             28 |         164.66 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    31 | Agent4               | 2026-05-14T12:22:36.827042+00:00 | 2026-05-14T12:23:40.895129+00:00 |            64.07 |
```
