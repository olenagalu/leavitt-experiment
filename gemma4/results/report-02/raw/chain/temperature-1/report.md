# Chain auto-trial report

## Summary

- Batch: `temperature-1`
- Model: `gemma4:e2b-it-qat`
- Temperature: 1
- Completed trials: 50/50
- Average time: 1306.60 seconds
- Average total messages: 24.64
- Average Gemma 4 thinking time per response: 50.347 seconds
- Average visible-response generation time: 1.174 seconds
- Average complete generation time: 51.521 seconds
- Success rate: 10/50 (20.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     256 |           256 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     139 |           256 |        54.3% (0.543) |                0.500 | 1.086 |                0.543 |
| chain    | Agent2 | Agent3    |                  2 |     117 |           256 |        45.7% (0.457) |                0.500 | 0.914 |                0.457 |
| chain    | Agent3 | Agent2    |                  2 |     110 |           218 |        50.5% (0.505) |                0.500 | 1.009 |                0.505 |
| chain    | Agent3 | Agent4    |                  2 |     108 |           218 |        49.5% (0.495) |                0.500 | 0.991 |                0.495 |
| chain    | Agent4 | Agent3    |                  2 |     117 |           247 |        47.4% (0.474) |                0.500 | 0.947 |                0.474 |
| chain    | Agent4 | Agent5    |                  2 |     130 |           247 |        52.6% (0.526) |                0.500 | 1.053 |                0.526 |
| chain    | Agent5 | Agent4    |                  1 |     251 |           251 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| chain    | Agent3 | client_assigned |     1 |
| chain    | Agent4 | client_assigned |     1 |
| chain    | Agent5 | client_assigned |     1 |
| chain    | Agent5 | client_default  |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           1 | Fail    | cross                                       | asterisk       |             22 |         784.28 |           0 |             0.00 |
|     2 |           1 | Fail    | asterisk                                    | cross          |             20 |        1097.19 |           0 |             0.00 |
|     3 |           1 | Fail    | diamond                                     | triangle       |             41 |        2249.97 |           0 |             0.00 |
|     4 |           1 | Fail    | circle                                      | asterisk       |             15 |         824.56 |           0 |             0.00 |
|     5 |           1 | Success | circle                                      | circle         |             31 |        1578.89 |           0 |             0.00 |
|     6 |           1 | Fail    | cross                                       | circle         |             20 |         934.06 |           0 |             0.00 |
|     7 |           1 | Fail    | square                                      | cross          |             20 |        1285.18 |           0 |             0.00 |
|     8 |           1 | Fail    | circle                                      | triangle       |             16 |         828.97 |           0 |             0.00 |
|     9 |           1 | Fail    | cross                                       | triangle       |             37 |        2332.13 |           0 |             0.00 |
|    10 |           1 | Fail    | triangle                                    | cross          |             26 |        1318.27 |           0 |             0.00 |
|    11 |           1 | Success | diamond                                     | diamond        |             21 |         938.03 |           0 |             0.00 |
|    12 |           1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2726.87 |           0 |             0.00 |
|    13 |           1 | Fail    | asterisk                                    | circle         |             29 |        1752.78 |           0 |             0.00 |
|    14 |           1 | Success | triangle                                    | triangle       |             21 |         790.93 |           0 |             0.00 |
|    15 |           1 | Fail    | diamond                                     | triangle       |             11 |         562.37 |           0 |             0.00 |
|    16 |           1 | Fail    | cross                                       | square         |             14 |         673.34 |           0 |             0.00 |
|    17 |           1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2667.85 |           0 |             0.00 |
|    18 |           1 | Fail    | circle                                      | cross          |             24 |        1530.45 |           0 |             0.00 |
|    19 |           1 | Fail    | cross                                       | circle         |             33 |        2073.55 |           0 |             0.00 |
|    20 |           1 | Success | asterisk                                    | asterisk       |             48 |        2820.27 |           0 |             0.00 |
|    21 |           1 | Fail    | asterisk                                    | circle         |             24 |        1532.54 |           0 |             0.00 |
|    22 |           1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2655.64 |           0 |             0.00 |
|    23 |           1 | Fail    | cross                                       | asterisk       |             28 |        1605.66 |           0 |             0.00 |
|    24 |           1 | Fail    | cross                                       | circle         |             17 |         987.51 |           0 |             0.00 |
|    25 |           1 | Fail    | diamond                                     | square         |              9 |         420.26 |           0 |             0.00 |
|    26 |           1 | Success | cross                                       | cross          |             15 |         604.35 |           0 |             0.00 |
|    27 |           1 | Success | asterisk                                    | asterisk       |             11 |         684.56 |           0 |             0.00 |
|    28 |           1 | Fail    | asterisk                                    | circle         |             19 |         775.51 |           0 |             0.00 |
|    29 |           1 | Fail    | circle                                      | square         |             42 |        2570.89 |           0 |             0.00 |
|    30 |           1 | Fail    | triangle                                    | square         |             11 |         511.49 |           0 |             0.00 |
|    31 |           1 | Fail    | diamond                                     | asterisk       |             29 |        1745.23 |           0 |             0.00 |
|    32 |           1 | Fail    | diamond                                     | square         |             27 |        1411.36 |           0 |             0.00 |
|    33 |           1 | Fail    | triangle                                    | circle         |             13 |         576.62 |           0 |             0.00 |
|    34 |           1 | Success | diamond                                     | diamond        |             19 |         912.00 |           0 |             0.00 |
|    35 |           1 | Fail    | square                                      | circle         |             20 |         955.07 |           0 |             0.00 |
|    36 |           1 | Fail    | cross                                       | triangle       |             17 |         718.83 |           0 |             0.00 |
|    37 |           1 | Fail    | square                                      | triangle       |             33 |        2164.68 |           0 |             0.00 |
|    38 |           1 | Fail    | square                                      | diamond        |             45 |        1801.99 |           0 |             0.00 |
|    39 |           1 | Fail    | circle                                      | square         |             20 |        1155.72 |           0 |             0.00 |
|    40 |           1 | Fail    | cross                                       | circle         |             38 |        2295.93 |           0 |             0.00 |
|    41 |           1 | Fail    | cross                                       | circle         |             33 |        1862.75 |           0 |             0.00 |
|    42 |           1 | Fail    | cross                                       | square         |             16 |         665.44 |           0 |             0.00 |
|    43 |           1 | Success | square                                      | square         |             18 |         608.26 |           0 |             0.00 |
|    44 |           1 | Fail    | cross                                       | diamond        |             10 |         342.09 |           0 |             0.00 |
|    45 |           1 | Fail    | square                                      | diamond        |             33 |        1887.77 |           0 |             0.00 |
|    46 |           1 | Success | circle                                      | circle         |             23 |        1192.95 |           0 |             0.00 |
|    47 |           1 | Fail    | square                                      | asterisk       |             12 |         421.20 |           0 |             0.00 |
|    48 |           1 | Success | cross                                       | cross          |             12 |         659.74 |           0 |             0.00 |
|    49 |           1 | Fail    | cross                                       | square         |             15 |         689.89 |           0 |             0.00 |
|    50 |           1 | Fail    | circle                                      | triangle       |             24 |        1144.25 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |        799.83 |          799.83 |        23 |            762.252 |                     23.875 |              786.128 |               33.141 |                        1.038 |
|     2 |       1114.82 |         1114.82 |        21 |           1076.533 |                     25.407 |             1101.941 |               51.263 |                        1.210 |
|     3 |       2323.95 |         2323.95 |        42 |           2238.803 |                     57.487 |             2296.290 |               53.305 |                        1.369 |
|     4 |        842.08 |          842.08 |        16 |            813.246 |                     18.667 |              831.913 |               50.828 |                        1.167 |
|     5 |       1599.64 |         1599.64 |        32 |           1541.192 |                     36.988 |             1578.180 |               48.162 |                        1.156 |
|     6 |        945.23 |          945.23 |        21 |            907.495 |                     25.029 |              932.524 |               43.214 |                        1.192 |
|     7 |       1361.68 |         1361.68 |        22 |           1324.495 |                     23.048 |             1347.543 |               60.204 |                        1.048 |
|     8 |        904.23 |          904.23 |        17 |            876.246 |                     17.320 |              893.566 |               51.544 |                        1.019 |
|     9 |       2402.69 |         2402.69 |        38 |           2334.793 |                     45.690 |             2380.483 |               61.442 |                        1.202 |
|    10 |       1332.18 |         1332.18 |        27 |           1284.854 |                     31.127 |             1315.981 |               47.587 |                        1.153 |
|    11 |       1017.89 |         1017.89 |        22 |            978.097 |                     26.639 |             1004.736 |               44.459 |                        1.211 |
|    12 |       2800.41 |         2800.41 |        50 |           2703.857 |                     65.709 |             2769.566 |               54.077 |                        1.314 |
|    13 |       1768.29 |         1768.29 |        30 |           1712.651 |                     36.432 |             1749.083 |               57.088 |                        1.214 |
|    14 |        805.99 |          805.99 |        22 |            769.167 |                     23.423 |              792.590 |               34.962 |                        1.065 |
|    15 |        576.52 |          576.52 |        12 |            558.041 |                     11.056 |              569.097 |               46.503 |                        0.921 |
|    16 |        686.86 |          686.86 |        15 |            662.099 |                     15.668 |              677.767 |               44.140 |                        1.045 |
|    17 |       2682.13 |         2682.13 |        50 |           2585.867 |                     65.489 |             2651.356 |               51.717 |                        1.310 |
|    18 |       1542.77 |         1542.77 |        25 |           1498.193 |                     29.147 |             1527.340 |               59.928 |                        1.166 |
|    19 |       2089.32 |         2089.32 |        34 |           2025.527 |                     41.455 |             2066.981 |               59.574 |                        1.219 |
|    20 |       2832.07 |         2832.07 |        49 |           2742.475 |                     58.210 |             2800.685 |               55.969 |                        1.188 |
|    21 |       1540.83 |         1540.83 |        25 |           1496.652 |                     28.671 |             1525.322 |               59.866 |                        1.147 |
|    22 |       2674.42 |         2674.42 |        50 |           2577.426 |                     65.899 |             2643.325 |               51.549 |                        1.318 |
|    23 |       1623.00 |         1623.00 |        29 |           1569.698 |                     34.835 |             1604.534 |               54.128 |                        1.201 |
|    24 |       1002.40 |         1002.40 |        18 |            971.170 |                     19.695 |              990.865 |               53.954 |                        1.094 |
|    25 |        435.92 |          435.92 |        10 |            418.806 |                     11.205 |              430.011 |               41.881 |                        1.121 |
|    26 |        623.10 |          623.10 |        16 |            595.124 |                     18.320 |              613.444 |               37.195 |                        1.145 |
|    27 |        699.07 |          699.07 |        13 |            679.203 |                     11.857 |              691.059 |               52.246 |                        0.912 |
|    28 |        848.75 |          848.75 |        20 |            814.672 |                     21.232 |              835.904 |               40.734 |                        1.062 |
|    29 |       2589.24 |         2589.24 |        43 |           2508.259 |                     54.104 |             2562.363 |               58.332 |                        1.258 |
|    30 |        585.46 |          585.46 |        12 |            565.911 |                     12.147 |              578.058 |               47.159 |                        1.012 |
|    31 |       1762.03 |         1762.03 |        30 |           1708.396 |                     35.363 |             1743.759 |               56.947 |                        1.179 |
|    32 |       1486.08 |         1486.08 |        28 |           1431.696 |                     35.830 |             1467.526 |               51.132 |                        1.280 |
|    33 |        595.19 |          595.19 |        14 |            573.711 |                     13.609 |              587.320 |               40.979 |                        0.972 |
|    34 |        978.43 |          978.43 |        20 |            943.835 |                     22.424 |              966.259 |               47.192 |                        1.121 |
|    35 |        971.14 |          971.14 |        21 |            933.831 |                     24.422 |              958.253 |               44.468 |                        1.163 |
|    36 |        730.16 |          730.16 |        18 |            701.122 |                     17.597 |              718.719 |               38.951 |                        0.978 |
|    37 |       2176.73 |         2176.73 |        34 |           2115.450 |                     39.455 |             2154.905 |               62.219 |                        1.160 |
|    38 |       1819.14 |         1819.14 |        46 |           1736.089 |                     53.195 |             1789.284 |               37.741 |                        1.156 |
|    39 |       1172.54 |         1172.54 |        21 |           1136.282 |                     23.798 |             1160.080 |               54.109 |                        1.133 |
|    40 |       2366.80 |         2366.80 |        39 |           2298.027 |                     44.266 |             2342.294 |               58.924 |                        1.135 |
|    41 |       1877.08 |         1877.08 |        34 |           1811.925 |                     44.039 |             1855.964 |               53.292 |                        1.295 |
|    42 |        681.63 |          681.63 |        17 |            654.135 |                     17.160 |              671.295 |               38.479 |                        1.009 |
|    43 |        619.69 |          619.69 |        19 |            586.879 |                     21.169 |              608.048 |               30.888 |                        1.114 |
|    44 |        356.62 |          356.62 |        11 |            339.248 |                     11.136 |              350.384 |               30.841 |                        1.012 |
|    45 |       1899.71 |         1899.71 |        34 |           1838.471 |                     38.786 |             1877.257 |               54.073 |                        1.141 |
|    46 |       1269.62 |         1269.62 |        24 |           1226.232 |                     29.496 |             1255.727 |               51.093 |                        1.229 |
|    47 |        441.14 |          441.14 |        13 |            417.773 |                     15.029 |              432.802 |               32.136 |                        1.156 |
|    48 |        680.43 |          680.43 |        13 |            657.582 |                     14.291 |              671.873 |               50.583 |                        1.099 |
|    49 |        699.07 |          699.07 |        16 |            669.966 |                     18.672 |              688.638 |               41.873 |                        1.167 |
|    50 |       1164.47 |         1164.47 |        25 |           1120.639 |                     28.109 |             1148.748 |               44.826 |                        1.124 |
```

## Reconnect details

No Jetson disconnects were recorded.
