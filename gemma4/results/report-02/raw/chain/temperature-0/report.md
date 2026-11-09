# Chain auto-trial report

## Summary

- Batch: `temperature-0`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0
- Completed trials: 50/50
- Average time: 1248.34 seconds
- Average total messages: 26.36
- Average Gemma 4 thinking time per response: 44.815 seconds
- Average visible-response generation time: 1.073 seconds
- Average complete generation time: 45.888 seconds
- Success rate: 20/50 (40.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     280 |           280 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     139 |           250 |        55.6% (0.556) |                0.500 | 1.112 |                0.556 |
| chain    | Agent2 | Agent3    |                  2 |     111 |           250 |        44.4% (0.444) |                0.500 | 0.888 |                0.444 |
| chain    | Agent3 | Agent2    |                  2 |     125 |           259 |        48.3% (0.483) |                0.500 | 0.965 |                0.483 |
| chain    | Agent3 | Agent4    |                  2 |     134 |           259 |        51.7% (0.517) |                0.500 | 1.035 |                0.517 |
| chain    | Agent4 | Agent3    |                  2 |     135 |           276 |        48.9% (0.489) |                0.500 | 0.978 |                0.489 |
| chain    | Agent4 | Agent5    |                  2 |     141 |           276 |        51.1% (0.511) |                0.500 | 1.022 |                0.511 |
| chain    | Agent5 | Agent4    |                  1 |     253 |           253 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Fail    | circle                                      | diamond        |             31 |        1108.43 |           0 |             0.00 |
|     2 |           0 | Fail    | square                                      | diamond        |             43 |        1791.72 |           0 |             0.00 |
|     3 |           0 | Fail    | circle                                      | diamond        |             17 |         821.26 |           0 |             0.00 |
|     4 |           0 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2378.28 |           0 |             0.00 |
|     5 |           0 | Fail    | square                                      | asterisk       |             29 |        1341.75 |           0 |             0.00 |
|     6 |           0 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2694.91 |           0 |             0.00 |
|     7 |           0 | Success | square                                      | square         |              7 |         300.37 |           0 |             0.00 |
|     8 |           0 | Success | triangle                                    | triangle       |              9 |         246.43 |           0 |             0.00 |
|     9 |           0 | Success | cross                                       | cross          |             37 |        1602.36 |           0 |             0.00 |
|    10 |           0 | Fail    | cross                                       | diamond        |             21 |         939.64 |           0 |             0.00 |
|    11 |           0 | Fail    | square                                      | asterisk       |             27 |        1550.21 |           0 |             0.00 |
|    12 |           0 | Success | square                                      | square         |             12 |         486.09 |           0 |             0.00 |
|    13 |           0 | Fail    | cross                                       | circle         |             35 |        1325.03 |           0 |             0.00 |
|    14 |           0 | Success | triangle                                    | triangle       |             23 |         846.39 |           0 |             0.00 |
|    15 |           0 | Fail    | triangle                                    | circle         |             23 |         941.12 |           0 |             0.00 |
|    16 |           0 | Fail    | cross                                       | triangle       |             41 |        1838.15 |           0 |             0.00 |
|    17 |           0 | Success | square                                      | square         |             22 |        1241.77 |           0 |             0.00 |
|    18 |           0 | Fail    | cross                                       | diamond        |             37 |        1788.58 |           0 |             0.00 |
|    19 |           0 | Success | cross                                       | cross          |             22 |        1037.02 |           0 |             0.00 |
|    20 |           0 | Fail    | asterisk                                    | cross          |             33 |        1669.19 |           0 |             0.00 |
|    21 |           0 | Fail    | diamond                                     | circle         |              9 |         382.50 |           0 |             0.00 |
|    22 |           0 | Fail    | triangle                                    | asterisk       |             15 |         582.96 |           0 |             0.00 |
|    23 |           0 | Fail    | cross                                       | square         |             37 |        1660.14 |           0 |             0.00 |
|    24 |           0 | Fail    | square                                      | diamond        |             35 |        2327.33 |           0 |             0.00 |
|    25 |           0 | Success | square                                      | square         |             23 |        1093.30 |           0 |             0.00 |
|    26 |           0 | Success | square                                      | square         |             45 |        2384.00 |           0 |             0.00 |
|    27 |           0 | Success | circle                                      | circle         |             41 |        2374.13 |           0 |             0.00 |
|    28 |           0 | Fail    | circle                                      | triangle       |             21 |         851.43 |           0 |             0.00 |
|    29 |           0 | Fail    | cross                                       | asterisk       |             15 |         554.27 |           0 |             0.00 |
|    30 |           0 | Fail    | circle                                      | square         |             42 |        2150.41 |           0 |             0.00 |
|    31 |           0 | Success | cross                                       | cross          |             27 |        1071.47 |           0 |             0.00 |
|    32 |           0 | Success | square                                      | square         |             34 |        1845.64 |           0 |             0.00 |
|    33 |           0 | Fail    | triangle                                    | asterisk       |             25 |        1054.23 |           0 |             0.00 |
|    34 |           0 | Success | circle                                      | circle         |             17 |         894.02 |           0 |             0.00 |
|    35 |           0 | Fail    | cross                                       | circle         |             22 |         813.36 |           0 |             0.00 |
|    36 |           0 | Fail    | diamond                                     | circle         |             22 |         902.83 |           0 |             0.00 |
|    37 |           0 | Success | triangle                                    | triangle       |             23 |         834.78 |           0 |             0.00 |
|    38 |           0 | Fail    | cross                                       | asterisk       |             39 |        2454.14 |           0 |             0.00 |
|    39 |           0 | Success | cross                                       | cross          |             22 |        1142.11 |           0 |             0.00 |
|    40 |           0 | Fail    | circle                                      | asterisk       |             18 |         912.53 |           0 |             0.00 |
|    41 |           0 | Fail    | cross                                       | triangle       |             26 |        1457.33 |           0 |             0.00 |
|    42 |           0 | Success | square                                      | square         |             29 |        1448.67 |           0 |             0.00 |
|    43 |           0 | Success | circle                                      | circle         |             16 |         705.13 |           0 |             0.00 |
|    44 |           0 | Fail    | square                                      | asterisk       |             20 |         809.70 |           0 |             0.00 |
|    45 |           0 | Fail    | cross                                       | square         |             18 |         580.05 |           0 |             0.00 |
|    46 |           0 | Success | square                                      | square         |             28 |        1257.33 |           0 |             0.00 |
|    47 |           0 | Success | square                                      | square         |             17 |         909.51 |           0 |             0.00 |
|    48 |           0 | Success | asterisk                                    | asterisk       |             21 |         905.33 |           0 |             0.00 |
|    49 |           0 | Fail    | cross                                       | circle         |             22 |        1147.04 |           0 |             0.00 |
|    50 |           0 | Fail    | asterisk                                    | triangle       |             20 |         962.70 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |       1125.37 |         1125.37 |        32 |           1071.465 |                     34.448 |             1105.913 |               33.483 |                        1.076 |
|     2 |       1805.98 |         1805.98 |        44 |           1729.896 |                     48.111 |             1778.008 |               39.316 |                        1.093 |
|     3 |        837.65 |          837.65 |        18 |            805.751 |                     20.912 |              826.664 |               44.764 |                        1.162 |
|     4 |       2393.11 |         2393.11 |        50 |           2305.649 |                     56.641 |             2362.290 |               46.113 |                        1.133 |
|     5 |       1416.18 |         1416.18 |        30 |           1364.777 |                     33.844 |             1398.621 |               45.493 |                        1.128 |
|     6 |       2767.13 |         2767.13 |        50 |           2679.750 |                     55.659 |             2735.409 |               53.595 |                        1.113 |
|     7 |        315.90 |          315.90 |         8 |            304.767 |                      6.620 |              311.387 |               38.096 |                        0.827 |
|     8 |        260.74 |          260.74 |        10 |            244.553 |                      9.503 |              254.056 |               24.455 |                        0.950 |
|     9 |       1616.39 |         1616.39 |        38 |           1551.329 |                     41.449 |             1592.778 |               40.824 |                        1.091 |
|    10 |        953.80 |          953.80 |        22 |            917.354 |                     22.283 |              939.637 |               41.698 |                        1.013 |
|    11 |       1566.50 |         1566.50 |        28 |           1519.325 |                     29.804 |             1549.129 |               54.262 |                        1.064 |
|    12 |        501.01 |          501.01 |        13 |            480.878 |                     12.204 |              493.082 |               36.991 |                        0.939 |
|    13 |       1340.21 |         1340.21 |        36 |           1279.004 |                     38.147 |             1317.151 |               35.528 |                        1.060 |
|    14 |        862.94 |          862.94 |        24 |            821.166 |                     27.012 |              848.177 |               34.215 |                        1.125 |
|    15 |       1016.27 |         1016.27 |        24 |            974.139 |                     26.764 |             1000.902 |               40.589 |                        1.115 |
|    16 |       1855.80 |         1855.80 |        42 |           1778.727 |                     49.414 |             1828.141 |               42.351 |                        1.177 |
|    17 |       1258.26 |         1258.26 |        23 |           1220.446 |                     22.330 |             1242.776 |               53.063 |                        0.971 |
|    18 |       1803.75 |         1803.75 |        38 |           1737.636 |                     43.134 |             1780.770 |               45.727 |                        1.135 |
|    19 |       1050.79 |         1050.79 |        23 |           1012.852 |                     23.894 |             1036.746 |               44.037 |                        1.039 |
|    20 |       1686.00 |         1686.00 |        34 |           1624.575 |                     41.176 |             1665.750 |               47.782 |                        1.211 |
|    21 |        398.09 |          398.09 |        10 |            382.514 |                      9.335 |              391.849 |               38.251 |                        0.933 |
|    22 |        596.04 |          596.04 |        16 |            570.170 |                     16.018 |              586.188 |               35.636 |                        1.001 |
|    23 |       1676.05 |         1676.05 |        38 |           1606.884 |                     44.312 |             1651.196 |               42.286 |                        1.166 |
|    24 |       2342.38 |         2342.38 |        36 |           2280.120 |                     39.526 |             2319.646 |               63.337 |                        1.098 |
|    25 |       1110.29 |         1110.29 |        24 |           1071.509 |                     24.630 |             1096.139 |               44.646 |                        1.026 |
|    26 |       2399.13 |         2399.13 |        46 |           2319.061 |                     50.867 |             2369.928 |               50.414 |                        1.106 |
|    27 |       2389.48 |         2389.48 |        42 |           2313.679 |                     49.123 |             2362.803 |               55.088 |                        1.170 |
|    28 |        865.28 |          865.28 |        22 |            828.041 |                     22.982 |              851.023 |               37.638 |                        1.045 |
|    29 |        570.49 |          570.49 |        16 |            545.863 |                     15.020 |              560.883 |               34.116 |                        0.939 |
|    30 |       2166.91 |         2166.91 |        44 |           2096.053 |                     43.786 |             2139.839 |               47.638 |                        0.995 |
|    31 |       1086.52 |         1086.52 |        28 |           1039.001 |                     29.872 |             1068.872 |               37.107 |                        1.067 |
|    32 |       1861.61 |         1861.61 |        37 |           1801.416 |                     37.705 |             1839.122 |               48.687 |                        1.019 |
|    33 |       1068.21 |         1068.21 |        26 |           1025.079 |                     25.846 |             1050.926 |               39.426 |                        0.994 |
|    34 |        908.41 |          908.41 |        18 |            875.586 |                     21.823 |              897.409 |               48.644 |                        1.212 |
|    35 |        888.31 |          888.31 |        23 |            847.967 |                     25.530 |              873.498 |               36.868 |                        1.110 |
|    36 |        918.08 |          918.08 |        23 |            880.485 |                     22.932 |              903.418 |               38.282 |                        0.997 |
|    37 |        851.57 |          851.57 |        24 |            811.060 |                     25.266 |              836.326 |               33.794 |                        1.053 |
|    38 |       2529.84 |         2529.84 |        42 |           2465.277 |                     38.462 |             2503.740 |               58.697 |                        0.916 |
|    39 |       1216.95 |         1216.95 |        23 |           1178.581 |                     24.224 |             1202.805 |               51.243 |                        1.053 |
|    40 |        984.23 |          984.23 |        19 |            951.876 |                     20.469 |              972.345 |               50.099 |                        1.077 |
|    41 |       1531.46 |         1531.46 |        27 |           1485.939 |                     28.839 |             1514.778 |               55.035 |                        1.068 |
|    42 |       1525.34 |         1525.34 |        30 |           1473.392 |                     33.106 |             1506.498 |               49.113 |                        1.104 |
|    43 |        718.13 |          718.13 |        17 |            688.982 |                     18.745 |              707.727 |               40.528 |                        1.103 |
|    44 |        881.02 |          881.02 |        21 |            845.472 |                     22.836 |              868.309 |               40.261 |                        1.087 |
|    45 |        595.42 |          595.42 |        19 |            563.846 |                     19.965 |              583.811 |               29.676 |                        1.051 |
|    46 |       1271.96 |         1271.96 |        29 |           1222.674 |                     30.723 |             1253.398 |               42.161 |                        1.059 |
|    47 |        925.34 |          925.34 |        18 |            895.713 |                     18.436 |              914.149 |               49.762 |                        1.024 |
|    48 |        918.64 |          918.64 |        22 |            882.880 |                     22.580 |              905.461 |               40.131 |                        1.026 |
|    49 |       1163.11 |         1163.11 |        23 |           1126.295 |                     22.245 |             1148.540 |               48.969 |                        0.967 |
|    50 |        978.25 |          978.25 |        21 |            941.932 |                     23.075 |              965.007 |               44.854 |                        1.099 |
```

## Reconnect details

No Jetson disconnects were recorded.
