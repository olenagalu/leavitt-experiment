# Y topology auto-trial report

## Summary

- Batch: `temperature-1`
- Temperature: 1
- Completed trials: 50/50
- Average time: 181.72 seconds
- Average total messages: 17.58
- Success rate: 13/50 (26.0%)
- Reconnect pauses: 1 across 1 trial(s); 3.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     170 |           170 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     189 |           189 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      68 |           151 |        45.0% (0.450) |                0.333 | 1.351 |                0.449 |
| y        | Agent3 | Agent2    |                  3 |      61 |           151 |        40.4% (0.404) |                0.333 | 1.212 |                0.403 |
| y        | Agent3 | Agent4    |                  3 |      22 |           151 |        14.6% (0.146) |                0.333 | 0.437 |                0.148 |
| y        | Agent4 | Agent3    |                  2 |     144 |           173 |        83.2% (0.832) |                0.500 | 1.665 |                0.830 |
| y        | Agent4 | Agent5    |                  2 |      29 |           173 |        16.8% (0.168) |                0.500 | 0.335 |                0.170 |
| y        | Agent5 | Agent4    |                  1 |     193 |           193 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent2 | client_assigned |     1 |
| y        | Agent3 | client_assigned |     2 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           1 | Success | triangle         | triangle       |             15 |         271.40 |           0 |             0.00 |
|     2 |           1 | Fail    | diamond          | circle         |             14 |          83.60 |           0 |             0.00 |
|     3 |           1 | Success | cross            | cross          |             13 |          74.20 |           0 |             0.00 |
|     4 |           1 | Fail    | cross            | diamond        |             17 |          96.97 |           0 |             0.00 |
|     5 |           1 | Fail    | diamond          | square         |             25 |         142.09 |           0 |             0.00 |
|     6 |           1 | Fail    | triangle         | asterisk       |             18 |         101.60 |           0 |             0.00 |
|     7 |           1 | Success | triangle         | triangle       |             15 |          87.22 |           0 |             0.00 |
|     8 |           1 | Success | asterisk         | asterisk       |             12 |          69.59 |           0 |             0.00 |
|     9 |           1 | Fail    | cross            | triangle       |             14 |          92.44 |           0 |             0.00 |
|    10 |           1 | Fail    | triangle         | circle         |             26 |        1028.53 |           0 |             0.00 |
|    11 |           1 | Fail    | cross            | square         |             18 |         104.76 |           0 |             0.00 |
|    12 |           1 | Fail    | square           | circle         |             12 |          71.96 |           0 |             0.00 |
|    13 |           1 | Fail    | triangle         | asterisk       |             19 |         112.84 |           0 |             0.00 |
|    14 |           1 | Fail    | cross            | asterisk       |             20 |         117.86 |           0 |             0.00 |
|    15 |           1 | Fail    | asterisk         | cross          |             25 |         148.63 |           0 |             0.00 |
|    16 |           1 | Fail    | cross            | triangle       |             15 |          90.29 |           0 |             0.00 |
|    17 |           1 | Fail    | square           | asterisk       |              8 |          52.74 |           0 |             0.00 |
|    18 |           1 | Success | diamond          | diamond        |             27 |         303.97 |           0 |             0.00 |
|    19 |           1 | Fail    | cross            | diamond        |             11 |         156.68 |           0 |             0.00 |
|    20 |           1 | Fail    | circle           | diamond        |             13 |          88.99 |           0 |             0.00 |
|    21 |           1 | Fail    | diamond          | square         |             11 |         244.65 |           0 |             0.00 |
|    22 |           1 | Fail    | cross            | square         |             28 |         479.66 |           0 |             0.00 |
|    23 |           1 | Fail    | triangle         | cross          |             13 |          74.94 |           0 |             0.00 |
|    24 |           1 | Fail    | circle           | diamond        |             13 |          76.05 |           0 |             0.00 |
|    25 |           1 | Fail    | cross            | triangle       |             23 |         138.86 |           0 |             0.00 |
|    26 |           1 | Fail    | cross            | triangle       |             24 |         155.62 |           0 |             0.00 |
|    27 |           1 | Fail    | asterisk         | diamond        |             29 |         241.68 |           0 |             0.00 |
|    28 |           1 | Success | square           | square         |              9 |          56.51 |           0 |             0.00 |
|    29 |           1 | Success | triangle         | triangle       |             16 |          95.42 |           0 |             0.00 |
|    30 |           1 | Fail    | cross            | circle         |             10 |          59.37 |           0 |             0.00 |
|    31 |           1 | Fail    | square           | asterisk       |             12 |         187.38 |           0 |             0.00 |
|    32 |           1 | Fail    | circle           | diamond        |             33 |         796.87 |           0 |             0.00 |
|    33 |           1 | Success | diamond          | diamond        |             12 |         242.69 |           0 |             0.00 |
|    34 |           1 | Fail    | triangle         | square         |             16 |          91.94 |           0 |             0.00 |
|    35 |           1 | Fail    | square           | asterisk       |             22 |         130.88 |           0 |             0.00 |
|    36 |           1 | Fail    | asterisk         | triangle       |              9 |          54.90 |           0 |             0.00 |
|    37 |           1 | Fail    | circle           | square         |             27 |         153.85 |           0 |             0.00 |
|    38 |           1 | Success | circle           | circle         |             10 |          61.98 |           0 |             0.00 |
|    39 |           1 | Fail    | diamond          | square         |             19 |         109.80 |           0 |             0.00 |
|    40 |           1 | Fail    | circle           | cross          |             13 |         437.65 |           0 |             0.00 |
|    41 |           1 | Success | circle           | circle         |             41 |         924.70 |           1 |             3.00 |
|    42 |           1 | Fail    | cross            | triangle       |             10 |          59.13 |           0 |             0.00 |
|    43 |           1 | Success | cross            | cross          |             14 |          81.85 |           0 |             0.00 |
|    44 |           1 | Success | square           | square         |             19 |         106.55 |           0 |             0.00 |
|    45 |           1 | Success | cross            | cross          |              9 |          54.27 |           0 |             0.00 |
|    46 |           1 | Fail    | cross            | asterisk       |             34 |         191.02 |           0 |             0.00 |
|    47 |           1 | Fail    | square           | triangle       |             10 |          61.18 |           0 |             0.00 |
|    48 |           1 | Fail    | diamond          | triangle       |             10 |          64.44 |           0 |             0.00 |
|    49 |           1 | Fail    | asterisk         | circle         |             25 |         160.71 |           0 |             0.00 |
|    50 |           1 | Fail    | circle           | triangle       |             21 |         195.10 |           0 |             0.00 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    41 | Agent3               | 2026-05-14T22:43:50.971722+00:00 | 2026-05-14T22:43:53.976471+00:00 |             3.00 |
```
