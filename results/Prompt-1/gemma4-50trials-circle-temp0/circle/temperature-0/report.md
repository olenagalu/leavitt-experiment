# gemma4:e2b-it-qat — Circle auto-trial report

## Summary

- Model: `gemma4:e2b-it-qat`
- Batch: `temperature-0`
- Temperature: 0
- Completed trials: 50/50
- Average time: 783.43 seconds
- Average total messages: 17.44
- Success rate: 19/50 (38.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      95 |           188 |        50.5% (0.505) |                0.500 | 1.011 |                0.505 |
| circle   | Agent1 | Agent5    |                  2 |      93 |           188 |        49.5% (0.495) |                0.500 | 0.989 |                0.495 |
| circle   | Agent2 | Agent1    |                  2 |      87 |           172 |        50.6% (0.506) |                0.500 | 1.012 |                0.506 |
| circle   | Agent2 | Agent3    |                  2 |      85 |           172 |        49.4% (0.494) |                0.500 | 0.988 |                0.494 |
| circle   | Agent3 | Agent2    |                  2 |      78 |           166 |        47.0% (0.470) |                0.500 | 0.940 |                0.470 |
| circle   | Agent3 | Agent4    |                  2 |      88 |           166 |        53.0% (0.530) |                0.500 | 1.060 |                0.530 |
| circle   | Agent4 | Agent3    |                  2 |     104 |           180 |        57.8% (0.578) |                0.500 | 1.156 |                0.577 |
| circle   | Agent4 | Agent5    |                  2 |      76 |           180 |        42.2% (0.422) |                0.500 | 0.844 |                0.423 |
| circle   | Agent5 | Agent1    |                  2 |      76 |           164 |        46.3% (0.463) |                0.500 | 0.927 |                0.464 |
| circle   | Agent5 | Agent4    |                  2 |      88 |           164 |        53.7% (0.537) |                0.500 | 1.073 |                0.536 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| circle   | Agent2 | server_assigned |     1 |
| circle   | Agent5 | server_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- |
|     1 |           0 | Fail    | square           | asterisk       |             20 |        1128.02 |
|     2 |           0 | Fail    | cross            | triangle       |             19 |        1178.61 |
|     3 |           0 | Fail    | square           | circle         |              8 |         372.52 |
|     4 |           0 | Success | cross            | cross          |             15 |         764.37 |
|     5 |           0 | Fail    | triangle         | asterisk       |             26 |        1564.94 |
|     6 |           0 | Fail    | cross            | diamond        |             25 |         956.91 |
|     7 |           0 | Fail    | square           | triangle       |             19 |         674.12 |
|     8 |           0 | Success | triangle         | triangle       |             16 |         643.95 |
|     9 |           0 | Fail    | diamond          | square         |             18 |         796.05 |
|    10 |           0 | Fail    | diamond          | cross          |              4 |         142.90 |
|    11 |           0 | Fail    | cross            | circle         |             10 |         404.27 |
|    12 |           0 | Fail    | circle           | triangle       |             13 |         672.85 |
|    13 |           0 | Success | circle           | circle         |             13 |         620.81 |
|    14 |           0 | Fail    | square           | cross          |             16 |         572.74 |
|    15 |           0 | Fail    | diamond          | circle         |             21 |         800.24 |
|    16 |           0 | Success | circle           | circle         |             10 |         381.09 |
|    17 |           0 | Fail    | circle           | cross          |             14 |         560.34 |
|    18 |           0 | Fail    | triangle         | circle         |              6 |         241.86 |
|    19 |           0 | Fail    | diamond          | asterisk       |             22 |         873.63 |
|    20 |           0 | Success | circle           | circle         |             15 |         610.50 |
|    21 |           0 | Success | circle           | circle         |             15 |         441.95 |
|    22 |           0 | Fail    | cross            | square         |             13 |         643.14 |
|    23 |           0 | Success | square           | square         |             18 |         890.64 |
|    24 |           0 | Fail    | cross            | square         |             24 |        1080.47 |
|    25 |           0 | Fail    | asterisk         | circle         |             21 |        1031.36 |
|    26 |           0 | Success | cross            | cross          |             36 |        1663.18 |
|    27 |           0 | Success | diamond          | diamond        |             15 |         568.81 |
|    28 |           0 | Success | diamond          | diamond        |             16 |         759.29 |
|    29 |           0 | Fail    | cross            | triangle       |             16 |         795.24 |
|    30 |           0 | Fail    | cross            | circle         |             23 |        1056.96 |
|    31 |           0 | Success | circle           | circle         |             23 |        1028.28 |
|    32 |           0 | Fail    | circle           | square         |             13 |         787.56 |
|    33 |           0 | Fail    | circle           | asterisk       |              9 |         262.30 |
|    34 |           0 | Success | square           | square         |             35 |        1473.13 |
|    35 |           0 | Fail    | cross            | asterisk       |             16 |         753.52 |
|    36 |           0 | Success | cross            | cross          |             16 |         860.04 |
|    37 |           0 | Fail    | cross            | diamond        |             13 |         492.34 |
|    38 |           0 | Fail    | cross            | diamond        |             21 |         789.59 |
|    39 |           0 | Success | square           | square         |             15 |         656.47 |
|    40 |           0 | Fail    | triangle         | cross          |              8 |         340.94 |
|    41 |           0 | Success | cross            | cross          |             10 |         286.06 |
|    42 |           0 | Fail    | cross            | triangle       |             28 |        1316.38 |
|    43 |           0 | Fail    | triangle         | asterisk       |             11 |         556.37 |
|    44 |           0 | Success | cross            | cross          |             25 |        1179.96 |
|    45 |           0 | Fail    | triangle         | diamond        |             19 |         963.36 |
|    46 |           0 | Fail    | square           | cross          |             14 |         614.42 |
|    47 |           0 | Fail    | circle           | cross          |             23 |         955.34 |
|    48 |           0 | Success | square           | square         |             15 |         807.75 |
|    49 |           0 | Success | cross            | cross          |             33 |        1517.14 |
|    50 |           0 | Success | cross            | cross          |             18 |         638.80 |
```

## Timing table

Total trial time measures launch through completion. Experiment time starts with the first valid message. Response time measures the wait after a turn request is sent.

```text
| Trial | Temperature | Total trial (s) | Experiment time (s) | Longest response (s) | Response agent | Response turn |
| ----- | ----------- | --------------- | ------------------- | -------------------- | -------------- | ------------- |
|     1 |           0 |         1145.53 |             1128.02 |               111.77 | Agent4         |            18 |
|     2 |           0 |         1256.04 |             1178.61 |               110.95 | Agent1         |             9 |
|     3 |           0 |          387.80 |              372.52 |                84.70 | Agent5         |             3 |
|     4 |           0 |          778.59 |              764.37 |               119.13 | Agent5         |            13 |
|     5 |           0 |         1580.26 |             1564.94 |               120.26 | Agent2         |            22 |
|     6 |           0 |          973.17 |              956.91 |                93.33 | Agent5         |            23 |
|     7 |           0 |          692.76 |              674.12 |               120.41 | Agent5         |            15 |
|     8 |           0 |          659.92 |              643.95 |                97.23 | Agent3         |            11 |
|     9 |           0 |          868.73 |              796.05 |                96.57 | Agent5         |            16 |
|    10 |           0 |          160.47 |              142.90 |                72.86 | Agent4         |             2 |
|    11 |           0 |          420.92 |              404.27 |                82.04 | Agent3         |             9 |
|    12 |           0 |          692.25 |              672.85 |               113.84 | Agent4         |            12 |
|    13 |           0 |          635.18 |              620.81 |                85.03 | Agent4         |            12 |
|    14 |           0 |          586.11 |              572.74 |                96.55 | Agent1         |            17 |
|    15 |           0 |          817.69 |              800.24 |                85.66 | Agent2         |            21 |
|    16 |           0 |          397.47 |              381.09 |                80.28 | Agent4         |             8 |
|    17 |           0 |          634.54 |              560.34 |               115.94 | Agent4         |            15 |
|    18 |           0 |          255.81 |              241.86 |                79.13 | Agent2         |             4 |
|    19 |           0 |          889.75 |              873.63 |                80.87 | Agent1         |            10 |
|    20 |           0 |          627.82 |              610.50 |               102.01 | Agent2         |            15 |
|    21 |           0 |          459.38 |              441.95 |                57.48 | Agent4         |            15 |
|    22 |           0 |          658.86 |              643.14 |                83.36 | Agent3         |             6 |
|    23 |           0 |          905.81 |              890.64 |                88.42 | Agent1         |            17 |
|    24 |           0 |         1097.07 |             1080.47 |                97.40 | Agent2         |            17 |
|    25 |           0 |         1104.44 |             1031.36 |               113.34 | Agent3         |            12 |
|    26 |           0 |         1736.27 |             1663.18 |                98.96 | Agent5         |            36 |
|    27 |           0 |          642.71 |              568.81 |                85.51 | Agent2         |             9 |
|    28 |           0 |          774.12 |              759.29 |               119.40 | Agent2         |            17 |
|    29 |           0 |          810.22 |              795.24 |               108.47 | Agent4         |            14 |
|    30 |           0 |         1073.70 |             1056.96 |               103.37 | Agent1         |            22 |
|    31 |           0 |         1104.30 |             1028.28 |                93.52 | Agent4         |            24 |
|    32 |           0 |          808.05 |              787.56 |               110.09 | Agent3         |            14 |
|    33 |           0 |          277.58 |              262.30 |                81.41 | Agent2         |             9 |
|    34 |           0 |         1489.50 |             1473.13 |               105.78 | Agent4         |            30 |
|    35 |           0 |          768.42 |              753.52 |                96.40 | Agent1         |            17 |
|    36 |           0 |          876.40 |              860.04 |                98.14 | Agent3         |            10 |
|    37 |           0 |          507.75 |              492.34 |                83.31 | Agent2         |            13 |
|    38 |           0 |          805.81 |              789.59 |                93.36 | Agent5         |            17 |
|    39 |           0 |          672.30 |              656.47 |               114.68 | Agent2         |            16 |
|    40 |           0 |          411.78 |              340.94 |                81.86 | Agent5         |             4 |
|    41 |           0 |          302.37 |              286.06 |                43.75 | Agent4         |            11 |
|    42 |           0 |         1330.97 |             1316.38 |               103.82 | Agent5         |            27 |
|    43 |           0 |          572.95 |              556.37 |                93.61 | Agent3         |            10 |
|    44 |           0 |         1198.62 |             1179.96 |               114.70 | Agent3         |            21 |
|    45 |           0 |          980.38 |              963.36 |               106.12 | Agent2         |            20 |
|    46 |           0 |          633.68 |              614.42 |                89.70 | Agent3         |             9 |
|    47 |           0 |         1026.59 |              955.34 |                88.99 | Agent2         |            24 |
|    48 |           0 |          823.96 |              807.75 |               111.77 | Agent3         |            13 |
|    49 |           0 |         1530.99 |             1517.14 |               109.66 | Agent3         |            33 |
|    50 |           0 |          709.92 |              638.80 |                83.21 | Agent4         |             6 |
```
