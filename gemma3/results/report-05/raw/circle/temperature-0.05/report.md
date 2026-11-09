# Circle auto-trial report

## Summary

- Batch: `temperature-0.05`
- Temperature: 0.05
- Completed trials: 50/50
- Average time: 170.52 seconds
- Average total messages: 15.36
- Success rate: 12/50 (24.0%)
- Reconnect pauses: 2 across 2 trial(s); 2.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      35 |           141 |        24.8% (0.248) |                0.500 | 0.496 |                0.250 |
| circle   | Agent1 | Agent5    |                  2 |     106 |           141 |        75.2% (0.752) |                0.500 | 1.504 |                0.750 |
| circle   | Agent2 | Agent1    |                  2 |     147 |           162 |        90.7% (0.907) |                0.500 | 1.815 |                0.905 |
| circle   | Agent2 | Agent3    |                  2 |      15 |           162 |         9.3% (0.093) |                0.500 | 0.185 |                0.095 |
| circle   | Agent3 | Agent2    |                  2 |     149 |           153 |        97.4% (0.974) |                0.500 | 1.948 |                0.971 |
| circle   | Agent3 | Agent4    |                  2 |       4 |           153 |         2.6% (0.026) |                0.500 | 0.052 |                0.029 |
| circle   | Agent4 | Agent3    |                  2 |     126 |           146 |        86.3% (0.863) |                0.500 | 1.726 |                0.861 |
| circle   | Agent4 | Agent5    |                  2 |      20 |           146 |        13.7% (0.137) |                0.500 | 0.274 |                0.139 |
| circle   | Agent5 | Agent1    |                  2 |      82 |           166 |        49.4% (0.494) |                0.500 | 0.988 |                0.494 |
| circle   | Agent5 | Agent4    |                  2 |      84 |           166 |        50.6% (0.506) |                0.500 | 1.012 |                0.506 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |        0.05 | Fail    | circle                                      | triangle       |             12 |         293.43 |           0 |             0.00 |
|     2 |        0.05 | Success | triangle                                    | triangle       |             10 |          57.03 |           0 |             0.00 |
|     3 |        0.05 | Success | diamond                                     | diamond        |              8 |          46.73 |           0 |             0.00 |
|     4 |        0.05 | Fail    | triangle                                    | diamond        |             15 |          83.07 |           0 |             0.00 |
|     5 |        0.05 | Fail    | cross                                       | square         |             12 |          71.54 |           0 |             0.00 |
|     6 |        0.05 | Success | cross                                       | cross          |              8 |          47.21 |           0 |             0.00 |
|     7 |        0.05 | Fail    | cross                                       | square         |             10 |          57.01 |           0 |             0.00 |
|     8 |        0.05 | Fail    | cross                                       | triangle       |             12 |          69.45 |           0 |             0.00 |
|     9 |        0.05 | Fail    | cross                                       | diamond        |             11 |          66.38 |           0 |             0.00 |
|    10 |        0.05 | Fail    | No figure submitted (message limit reached) | cross          |             40 |         781.34 |           1 |             0.00 |
|    11 |        0.05 | Success | triangle                                    | triangle       |              8 |         156.67 |           0 |             0.00 |
|    12 |        0.05 | Fail    | square                                      | cross          |             16 |         343.64 |           0 |             0.00 |
|    13 |        0.05 | Fail    | cross                                       | asterisk       |             10 |          58.48 |           0 |             0.00 |
|    14 |        0.05 | Fail    | diamond                                     | triangle       |             29 |         165.38 |           0 |             0.00 |
|    15 |        0.05 | Fail    | cross                                       | square         |              9 |          53.01 |           0 |             0.00 |
|    16 |        0.05 | Success | cross                                       | cross          |             30 |         165.63 |           0 |             0.00 |
|    17 |        0.05 | Fail    | circle                                      | asterisk       |              8 |          47.22 |           0 |             0.00 |
|    18 |        0.05 | Fail    | cross                                       | circle         |             38 |         216.25 |           0 |             0.00 |
|    19 |        0.05 | Fail    | square                                      | circle         |             17 |          94.02 |           0 |             0.00 |
|    20 |        0.05 | Fail    | asterisk                                    | triangle       |             17 |         107.34 |           0 |             0.00 |
|    21 |        0.05 | Fail    | square                                      | asterisk       |             36 |         311.27 |           0 |             0.00 |
|    22 |        0.05 | Fail    | cross                                       | circle         |              8 |         138.09 |           0 |             0.00 |
|    23 |        0.05 | Success | square                                      | square         |             19 |         447.07 |           0 |             0.00 |
|    24 |        0.05 | Fail    | diamond                                     | asterisk       |              8 |          45.99 |           0 |             0.00 |
|    25 |        0.05 | Fail    | cross                                       | diamond        |             28 |         155.93 |           0 |             0.00 |
|    26 |        0.05 | Fail    | asterisk                                    | square         |              8 |          48.24 |           0 |             0.00 |
|    27 |        0.05 | Fail    | square                                      | cross          |             14 |          81.47 |           0 |             0.00 |
|    28 |        0.05 | Fail    | No figure submitted (message limit reached) | square         |             40 |         207.44 |           0 |             0.00 |
|    29 |        0.05 | Fail    | circle                                      | triangle       |              7 |          41.44 |           0 |             0.00 |
|    30 |        0.05 | Fail    | asterisk                                    | circle         |             11 |          64.88 |           0 |             0.00 |
|    31 |        0.05 | Success | diamond                                     | diamond        |              3 |          17.95 |           0 |             0.00 |
|    32 |        0.05 | Success | triangle                                    | triangle       |             13 |          80.46 |           0 |             0.00 |
|    33 |        0.05 | Fail    | diamond                                     | circle         |             12 |         312.73 |           0 |             0.00 |
|    34 |        0.05 | Fail    | cross                                       | diamond        |             19 |         491.90 |           0 |             0.00 |
|    35 |        0.05 | Fail    | square                                      | diamond        |              9 |         352.63 |           0 |             0.00 |
|    36 |        0.05 | Success | square                                      | square         |             11 |         121.07 |           0 |             0.00 |
|    37 |        0.05 | Success | diamond                                     | diamond        |             15 |          85.97 |           0 |             0.00 |
|    38 |        0.05 | Fail    | cross                                       | triangle       |             13 |          74.99 |           0 |             0.00 |
|    39 |        0.05 | Fail    | diamond                                     | asterisk       |             14 |          80.64 |           0 |             0.00 |
|    40 |        0.05 | Fail    | triangle                                    | cross          |             11 |          62.87 |           0 |             0.00 |
|    41 |        0.05 | Fail    | No figure submitted (message limit reached) | circle         |             40 |         228.42 |           0 |             0.00 |
|    42 |        0.05 | Fail    | circle                                      | diamond        |             13 |          78.12 |           0 |             0.00 |
|    43 |        0.05 | Success | square                                      | square         |             13 |          74.79 |           0 |             0.00 |
|    44 |        0.05 | Success | triangle                                    | triangle       |              8 |          49.61 |           0 |             0.00 |
|    45 |        0.05 | Fail    | cross                                       | circle         |             15 |         213.90 |           0 |             0.00 |
|    46 |        0.05 | Fail    | triangle                                    | circle         |             13 |         297.05 |           0 |             0.00 |
|    47 |        0.05 | Fail    | diamond                                     | circle         |              7 |         328.07 |           1 |             2.00 |
|    48 |        0.05 | Fail    | triangle                                    | diamond        |             12 |         712.67 |           0 |             0.00 |
|    49 |        0.05 | Fail    | asterisk                                    | circle         |             19 |         288.29 |           0 |             0.00 |
|    50 |        0.05 | Fail    | triangle                                    | asterisk       |              9 |          51.35 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    10 | Agent3               | 2026-05-13T04:51:13.987362+00:00 | 2026-05-13T04:51:13.990065+00:00 |             0.00 |
|    47 | Agent2               | 2026-05-13T06:41:16.073769+00:00 | 2026-05-13T06:41:18.077548+00:00 |             2.00 |
```
