# gemma4:e2b-it-qat — Circle auto-trial report

## Summary

- Model: `gemma4:e2b-it-qat`
- Batch: `temperature-0.5`
- Temperature: 0.5
- Completed trials: 32/50
- Average time: 959.69 seconds
- Average total messages: 19.91
- Success rate: 16/32 (50.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      53 |           105 |        50.5% (0.505) |                0.500 | 1.010 |                0.505 |
| circle   | Agent1 | Agent5    |                  2 |      52 |           105 |        49.5% (0.495) |                0.500 | 0.990 |                0.495 |
| circle   | Agent2 | Agent1    |                  2 |      69 |           151 |        45.7% (0.457) |                0.500 | 0.914 |                0.457 |
| circle   | Agent2 | Agent3    |                  2 |      82 |           151 |        54.3% (0.543) |                0.500 | 1.086 |                0.543 |
| circle   | Agent3 | Agent2    |                  2 |      72 |           136 |        52.9% (0.529) |                0.500 | 1.059 |                0.529 |
| circle   | Agent3 | Agent4    |                  2 |      64 |           136 |        47.1% (0.471) |                0.500 | 0.941 |                0.471 |
| circle   | Agent4 | Agent3    |                  2 |      70 |           111 |        63.1% (0.631) |                0.500 | 1.261 |                0.629 |
| circle   | Agent4 | Agent5    |                  2 |      41 |           111 |        36.9% (0.369) |                0.500 | 0.739 |                0.371 |
| circle   | Agent5 | Agent1    |                  2 |      60 |           121 |        49.6% (0.496) |                0.500 | 0.992 |                0.496 |
| circle   | Agent5 | Agent4    |                  2 |      61 |           121 |        50.4% (0.504) |                0.500 | 1.008 |                0.504 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| circle   | Agent1 | server_assigned |     4 |
| circle   | Agent3 | server_assigned |     2 |
| circle   | Agent4 | server_assigned |     4 |
| circle   | Agent5 | server_assigned |     3 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- |
|     1 |         0.5 | Fail    | cross            | circle         |             26 |        1426.58 |
|     2 |         0.5 | Fail    | cross            | asterisk       |             25 |        1129.89 |
|     3 |         0.5 | Fail    | cross            | square         |             14 |         550.71 |
|     4 |         0.5 | Success | diamond          | diamond        |             20 |        1055.72 |
|     5 |         0.5 | Success | circle           | circle         |             33 |        1917.36 |
|     6 |         0.5 | Success | square           | square         |             26 |        1233.88 |
|     7 |         0.5 | Fail    | cross            | circle         |             21 |        1096.45 |
|     8 |         0.5 | Success | diamond          | diamond        |             23 |         804.51 |
|     9 |         0.5 | Fail    | cross            | diamond        |             23 |         949.02 |
|    10 |         0.5 | Fail    | triangle         | diamond        |              8 |         382.57 |
|    11 |         0.5 | Success | triangle         | triangle       |             13 |         563.95 |
|    12 |         0.5 | Fail    | triangle         | cross          |             16 |         783.44 |
|    13 |         0.5 | Fail    | circle           | diamond        |             21 |         948.44 |
|    14 |         0.5 | Success | square           | square         |             12 |         544.60 |
|    15 |         0.5 | Success | triangle         | triangle       |             21 |        1097.90 |
|    16 |         0.5 | Success | square           | square         |             39 |        1978.71 |
|    17 |         0.5 | Success | square           | square         |             10 |         348.44 |
|    18 |         0.5 | Fail    | cross            | circle         |             13 |         568.23 |
|    19 |         0.5 | Success | asterisk         | asterisk       |             31 |        1568.86 |
|    20 |         0.5 | Fail    | square           | diamond        |             28 |        1621.84 |
|    21 |         0.5 | Fail    | triangle         | cross          |             18 |         702.37 |
|    22 |         0.5 | Fail    | diamond          | square         |             20 |        1026.62 |
|    23 |         0.5 | Fail    | circle           | diamond        |             12 |         470.13 |
|    24 |         0.5 | Success | circle           | circle         |             36 |        1817.71 |
|    25 |         0.5 | Fail    | cross            | triangle       |             12 |         599.62 |
|    26 |         0.5 | Fail    | triangle         | asterisk       |              8 |         368.16 |
|    27 |         0.5 | Success | triangle         | triangle       |              8 |         324.46 |
|    28 |         0.5 | Success | triangle         | triangle       |             21 |         923.87 |
|    29 |         0.5 | Fail    | square           | circle         |             23 |        1201.32 |
|    30 |         0.5 | Success | diamond          | diamond        |             20 |        1021.49 |
|    31 |         0.5 | Success | square           | square         |             16 |         644.61 |
|    32 |         0.5 | Success | asterisk         | asterisk       |             20 |        1038.47 |
```

## Timing table

Total trial time measures launch through completion. Experiment time starts with the first valid message. Response time measures the wait after a turn request is sent.

```text
| Trial | Temperature | Total trial (s) | Experiment time (s) | Longest response (s) | Response agent | Response turn |
| ----- | ----------- | --------------- | ------------------- | -------------------- | -------------- | ------------- |
|     1 |         0.5 |         1501.05 |             1426.58 |               120.25 | Agent5         |            18 |
|     2 |         0.5 |         1145.24 |             1129.89 |               109.83 | Agent5         |            26 |
|     3 |         0.5 |          566.31 |              550.71 |                78.78 | Agent1         |            12 |
|     4 |         0.5 |         1068.86 |             1055.72 |               101.57 | Agent4         |            21 |
|     5 |         0.5 |         1927.65 |             1917.36 |               120.34 | Agent1         |            22 |
|     6 |         0.5 |         1248.44 |             1233.88 |               113.13 | Agent1         |            16 |
|     7 |         0.5 |         1112.13 |             1096.45 |               120.14 | Agent3         |            15 |
|     8 |         0.5 |          820.43 |              804.51 |                89.12 | Agent1         |            23 |
|     9 |         0.5 |         1019.49 |              949.02 |               120.03 | Agent4         |            21 |
|    10 |         0.5 |          399.51 |              382.57 |                77.67 | Agent5         |             2 |
|    11 |         0.5 |          584.90 |              563.95 |                77.11 | Agent2         |             2 |
|    12 |         0.5 |          798.83 |              783.44 |               109.56 | Agent3         |            10 |
|    13 |         0.5 |          962.42 |              948.44 |               113.71 | Agent1         |            17 |
|    14 |         0.5 |          559.99 |              544.60 |                84.31 | Agent5         |            12 |
|    15 |         0.5 |         1112.45 |             1097.90 |               120.34 | Agent4         |            19 |
|    16 |         0.5 |         1991.14 |             1978.71 |               120.11 | Agent1         |            21 |
|    17 |         0.5 |          363.14 |              348.44 |                75.20 | Agent3         |            11 |
|    18 |         0.5 |          641.98 |              568.23 |                95.26 | Agent3         |            14 |
|    19 |         0.5 |         1587.02 |             1568.86 |               118.87 | Agent3         |            14 |
|    20 |         0.5 |         1635.53 |             1621.84 |               119.90 | Agent4         |            19 |
|    21 |         0.5 |          718.98 |              702.37 |               104.35 | Agent1         |             9 |
|    22 |         0.5 |         1044.35 |             1026.62 |               120.23 | Agent1         |            16 |
|    23 |         0.5 |          545.32 |              470.13 |                87.14 | Agent3         |             9 |
|    24 |         0.5 |         1833.67 |             1817.71 |               120.22 | Agent4         |            29 |
|    25 |         0.5 |          614.14 |              599.62 |                89.35 | Agent3         |             3 |
|    26 |         0.5 |          383.12 |              368.16 |                82.18 | Agent1         |             5 |
|    27 |         0.5 |          338.19 |              324.46 |                91.14 | Agent1         |             6 |
|    28 |         0.5 |          939.02 |              923.87 |                93.84 | Agent2         |            17 |
|    29 |         0.5 |         1271.46 |             1201.32 |               120.11 | Agent1         |            14 |
|    30 |         0.5 |         1099.45 |             1021.49 |               118.63 | Agent5         |            21 |
|    31 |         0.5 |          662.49 |              644.61 |               103.19 | Agent3         |            11 |
|    32 |         0.5 |         1052.22 |             1038.47 |               120.42 | Agent5         |            19 |
```
