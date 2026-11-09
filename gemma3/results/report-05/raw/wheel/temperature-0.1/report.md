# Wheel auto-trial report

## Summary

- Batch: `temperature-0.1`
- Temperature: 0.1
- Completed trials: 50/50
- Average time: 279.15 seconds
- Average total messages: 20.00
- Success rate: 18/50 (36.0%)
- Reconnect pauses: 3 across 3 trial(s); 1.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     216 |           216 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     215 |           215 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     106 |           186 |        57.0% (0.570) |                0.250 | 2.280 |                0.566 |
| wheel    | Agent3 | Agent2    |                  4 |      66 |           186 |        35.5% (0.355) |                0.250 | 1.419 |                0.354 |
| wheel    | Agent3 | Agent4    |                  4 |       3 |           186 |         1.6% (0.016) |                0.250 | 0.065 |                0.019 |
| wheel    | Agent3 | Agent5    |                  4 |      11 |           186 |         5.9% (0.059) |                0.250 | 0.237 |                0.061 |
| wheel    | Agent4 | Agent3    |                  1 |     159 |           159 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     219 |           219 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| wheel    | Agent3 | client_assigned |     5 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.1 | Success | asterisk                                    | asterisk       |              5 |         226.93 |           0 |             0.00 |
|     2 |         0.1 | Fail    | circle                                      | asterisk       |             10 |          67.37 |           0 |             0.00 |
|     3 |         0.1 | Fail    | circle                                      | square         |             15 |          89.19 |           0 |             0.00 |
|     4 |         0.1 | Fail    | circle                                      | triangle       |             11 |          71.01 |           0 |             0.00 |
|     5 |         0.1 | Success | circle                                      | circle         |             10 |          66.06 |           0 |             0.00 |
|     6 |         0.1 | Fail    | diamond                                     | asterisk       |             11 |          69.72 |           0 |             0.00 |
|     7 |         0.1 | Fail    | square                                      | circle         |             27 |         165.66 |           0 |             0.00 |
|     8 |         0.1 | Success | circle                                      | circle         |             17 |         187.64 |           0 |             0.00 |
|     9 |         0.1 | Fail    | circle                                      | cross          |             26 |         166.21 |           0 |             0.00 |
|    10 |         0.1 | Fail    | cross                                       | square         |             24 |         148.82 |           0 |             0.00 |
|    11 |         0.1 | Fail    | triangle                                    | asterisk       |             12 |          87.22 |           0 |             0.00 |
|    12 |         0.1 | Success | circle                                      | circle         |             18 |         761.79 |           1 |             0.00 |
|    13 |         0.1 | Fail    | triangle                                    | cross          |             13 |         312.36 |           0 |             0.00 |
|    14 |         0.1 | Fail    | circle                                      | square         |             27 |         177.90 |           0 |             0.00 |
|    15 |         0.1 | Success | circle                                      | circle         |              7 |          46.66 |           0 |             0.00 |
|    16 |         0.1 | Fail    | square                                      | triangle       |             10 |          61.07 |           0 |             0.00 |
|    17 |         0.1 | Fail    | circle                                      | asterisk       |             18 |         112.35 |           0 |             0.00 |
|    18 |         0.1 | Success | circle                                      | circle         |             23 |         141.60 |           0 |             0.00 |
|    19 |         0.1 | Fail    | circle                                      | triangle       |             17 |         116.04 |           0 |             0.00 |
|    20 |         0.1 | Fail    | asterisk                                    | cross          |              9 |         131.60 |           0 |             0.00 |
|    21 |         0.1 | Success | circle                                      | circle         |             12 |          75.14 |           0 |             0.00 |
|    22 |         0.1 | Fail    | diamond                                     | asterisk       |              8 |          52.83 |           0 |             0.00 |
|    23 |         0.1 | Fail    | diamond                                     | triangle       |             10 |          77.49 |           0 |             0.00 |
|    24 |         0.1 | Fail    | asterisk                                    | circle         |             34 |         760.18 |           1 |             1.00 |
|    25 |         0.1 | Fail    | asterisk                                    | circle         |             40 |         503.21 |           0 |             0.00 |
|    26 |         0.1 | Fail    | circle                                      | cross          |             23 |         136.24 |           0 |             0.00 |
|    27 |         0.1 | Fail    | diamond                                     | asterisk       |             12 |          78.37 |           0 |             0.00 |
|    28 |         0.1 | Fail    | circle                                      | diamond        |             15 |         379.39 |           0 |             0.00 |
|    29 |         0.1 | Fail    | cross                                       | asterisk       |             31 |         397.48 |           0 |             0.00 |
|    30 |         0.1 | Success | diamond                                     | diamond        |             27 |         170.39 |           0 |             0.00 |
|    31 |         0.1 | Fail    | asterisk                                    | square         |              7 |          45.58 |           0 |             0.00 |
|    32 |         0.1 | Fail    | triangle                                    | square         |             15 |          97.15 |           0 |             0.00 |
|    33 |         0.1 | Success | circle                                      | circle         |             14 |          94.33 |           0 |             0.00 |
|    34 |         0.1 | Fail    | circle                                      | asterisk       |             17 |         441.52 |           1 |             0.00 |
|    35 |         0.1 | Fail    | square                                      | circle         |             18 |         299.68 |           0 |             0.00 |
|    36 |         0.1 | Success | asterisk                                    | asterisk       |             15 |         166.10 |           0 |             0.00 |
|    37 |         0.1 | Success | diamond                                     | diamond        |             20 |         122.78 |           0 |             0.00 |
|    38 |         0.1 | Success | circle                                      | circle         |             13 |          91.30 |           0 |             0.00 |
|    39 |         0.1 | Success | circle                                      | circle         |             32 |         970.35 |           0 |             0.00 |
|    40 |         0.1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1543.60 |           0 |             0.00 |
|    41 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        1063.08 |           0 |             0.00 |
|    42 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        1099.97 |           0 |             0.00 |
|    43 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |         884.42 |           0 |             0.00 |
|    44 |         0.1 | Success | asterisk                                    | asterisk       |             42 |         589.31 |           0 |             0.00 |
|    45 |         0.1 | Fail    | triangle                                    | cross          |              6 |          36.52 |           0 |             0.00 |
|    46 |         0.1 | Success | cross                                       | cross          |             21 |         131.20 |           0 |             0.00 |
|    47 |         0.1 | Success | cross                                       | cross          |             14 |          83.32 |           0 |             0.00 |
|    48 |         0.1 | Success | asterisk                                    | asterisk       |             23 |         150.41 |           0 |             0.00 |
|    49 |         0.1 | Fail    | square                                      | cross          |              7 |          53.61 |           0 |             0.00 |
|    50 |         0.1 | Success | circle                                      | circle         |             14 |         155.59 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    12 | Agent4               | 2026-05-15T07:44:40.012441+00:00 | 2026-05-15T07:44:40.014592+00:00 |             0.00 |
|    24 | Agent4               | 2026-05-15T08:22:58.130201+00:00 | 2026-05-15T08:22:59.133086+00:00 |             1.00 |
|    34 | Agent4               | 2026-05-15T09:07:37.139859+00:00 | 2026-05-15T09:07:37.142137+00:00 |             0.00 |
```
