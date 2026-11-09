# Wheel auto-trial report

## Summary

- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 238.37 seconds
- Average total messages: 20.68
- Success rate: 12/50 (24.0%)
- Reconnect pauses: 1 across 1 trial(s); 4.01 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     209 |           209 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     200 |           200 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     109 |           180 |        60.6% (0.606) |                0.250 | 2.422 |                0.602 |
| wheel    | Agent3 | Agent2    |                  4 |      65 |           180 |        36.1% (0.361) |                0.250 | 1.444 |                0.360 |
| wheel    | Agent3 | Agent4    |                  4 |       4 |           180 |         2.2% (0.022) |                0.250 | 0.089 |                0.025 |
| wheel    | Agent3 | Agent5    |                  4 |       2 |           180 |         1.1% (0.011) |                0.250 | 0.044 |                0.014 |
| wheel    | Agent4 | Agent3    |                  1 |     217 |           217 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     227 |           227 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| wheel    | Agent3 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Fail    | square                                      | diamond        |             15 |         412.18 |           0 |             0.00 |
|     2 |           0 | Fail    | asterisk                                    | diamond        |             15 |          92.57 |           0 |             0.00 |
|     3 |           0 | Success | cross                                       | cross          |             13 |          80.24 |           0 |             0.00 |
|     4 |           0 | Fail    | asterisk                                    | square         |             10 |          65.07 |           0 |             0.00 |
|     5 |           0 | Fail    | triangle                                    | diamond        |             29 |         169.96 |           0 |             0.00 |
|     6 |           0 | Fail    | triangle                                    | square         |             13 |          79.64 |           0 |             0.00 |
|     7 |           0 | Fail    | diamond                                     | square         |              5 |          35.19 |           0 |             0.00 |
|     8 |           0 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |         690.52 |           0 |             0.00 |
|     9 |           0 | Fail    | No figure submitted (message limit reached) | cross          |             50 |         904.58 |           0 |             0.00 |
|    10 |           0 | Fail    | triangle                                    | cross          |             21 |         135.48 |           0 |             0.00 |
|    11 |           0 | Success | cross                                       | cross          |             25 |         226.72 |           0 |             0.00 |
|    12 |           0 | Fail    | cross                                       | square         |             19 |         593.83 |           0 |             0.00 |
|    13 |           0 | Success | circle                                      | circle         |             48 |         280.64 |           0 |             0.00 |
|    14 |           0 | Fail    | square                                      | asterisk       |              9 |          58.99 |           0 |             0.00 |
|    15 |           0 | Fail    | asterisk                                    | cross          |             18 |         114.01 |           0 |             0.00 |
|    16 |           0 | Fail    | triangle                                    | asterisk       |             25 |         157.70 |           0 |             0.00 |
|    17 |           0 | Success | circle                                      | circle         |              7 |          44.53 |           0 |             0.00 |
|    18 |           0 | Fail    | triangle                                    | asterisk       |             21 |         125.96 |           0 |             0.00 |
|    19 |           0 | Fail    | triangle                                    | circle         |             17 |         108.68 |           0 |             0.00 |
|    20 |           0 | Fail    | triangle                                    | cross          |             16 |         108.69 |           0 |             0.00 |
|    21 |           0 | Fail    | square                                      | asterisk       |             29 |         256.93 |           0 |             0.00 |
|    22 |           0 | Success | asterisk                                    | asterisk       |             15 |         763.42 |           0 |             0.00 |
|    23 |           0 | Fail    | cross                                       | triangle       |             44 |         974.30 |           0 |             0.00 |
|    24 |           0 | Fail    | circle                                      | square         |             12 |          72.51 |           0 |             0.00 |
|    25 |           0 | Success | square                                      | square         |             15 |          96.36 |           0 |             0.00 |
|    26 |           0 | Success | square                                      | square         |             32 |         189.47 |           0 |             0.00 |
|    27 |           0 | Fail    | diamond                                     | circle         |             18 |         114.54 |           0 |             0.00 |
|    28 |           0 | Fail    | square                                      | circle         |             29 |         182.70 |           0 |             0.00 |
|    29 |           0 | Fail    | square                                      | asterisk       |             19 |         114.69 |           0 |             0.00 |
|    30 |           0 | Fail    | cross                                       | asterisk       |             34 |         645.40 |           0 |             0.00 |
|    31 |           0 | Fail    | square                                      | circle         |             18 |         113.80 |           0 |             0.00 |
|    32 |           0 | Fail    | square                                      | asterisk       |             21 |         144.05 |           0 |             0.00 |
|    33 |           0 | Fail    | square                                      | asterisk       |             16 |         420.67 |           0 |             0.00 |
|    34 |           0 | Success | asterisk                                    | asterisk       |             14 |         288.36 |           0 |             0.00 |
|    35 |           0 | Fail    | square                                      | asterisk       |             22 |         133.57 |           0 |             0.00 |
|    36 |           0 | Fail    | cross                                       | asterisk       |              8 |          51.74 |           0 |             0.00 |
|    37 |           0 | Fail    | triangle                                    | cross          |             15 |          96.38 |           0 |             0.00 |
|    38 |           0 | Fail    | cross                                       | asterisk       |             42 |         398.56 |           0 |             0.00 |
|    39 |           0 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |         301.74 |           0 |             0.00 |
|    40 |           0 | Fail    | square                                      | triangle       |             11 |          74.14 |           0 |             0.00 |
|    41 |           0 | Success | square                                      | square         |              9 |          60.78 |           0 |             0.00 |
|    42 |           0 | Fail    | circle                                      | triangle       |             17 |         105.06 |           0 |             0.00 |
|    43 |           0 | Success | circle                                      | circle         |             15 |         106.61 |           0 |             0.00 |
|    44 |           0 | Success | square                                      | square         |             12 |         436.67 |           0 |             0.00 |
|    45 |           0 | Success | square                                      | square         |             22 |         670.76 |           1 |             4.01 |
|    46 |           0 | Fail    | circle                                      | diamond        |             18 |         308.13 |           0 |             0.00 |
|    47 |           0 | Fail    | circle                                      | diamond        |              7 |          44.32 |           0 |             0.00 |
|    48 |           0 | Fail    | cross                                       | square         |              7 |          44.83 |           0 |             0.00 |
|    49 |           0 | Fail    | cross                                       | triangle       |             25 |         151.69 |           0 |             0.00 |
|    50 |           0 | Fail    | asterisk                                    | circle         |             12 |          71.25 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    45 | Agent5               | 2026-05-15T02:39:43.735724+00:00 | 2026-05-15T02:39:47.742173+00:00 |             4.01 |
```
