# Chain auto-trial report

## Summary

- Batch: `temperature-0.2`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 1279.57 seconds
- Average total messages: 26.66
- Average Gemma 4 thinking time per response: 46.058 seconds
- Average visible-response generation time: 1.087 seconds
- Average complete generation time: 47.145 seconds
- Success rate: 19/50 (38.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| chain    | Agent1 | Agent2    |                  1 |     270 |           270 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| chain    | Agent2 | Agent1    |                  2 |     155 |           293 |        52.9% (0.529) |                0.500 | 1.058 |                0.529 |
| chain    | Agent2 | Agent3    |                  2 |     138 |           293 |        47.1% (0.471) |                0.500 | 0.942 |                0.471 |
| chain    | Agent3 | Agent2    |                  2 |     123 |           264 |        46.6% (0.466) |                0.500 | 0.932 |                0.466 |
| chain    | Agent3 | Agent4    |                  2 |     141 |           264 |        53.4% (0.534) |                0.500 | 1.068 |                0.534 |
| chain    | Agent4 | Agent3    |                  2 |     121 |           256 |        47.3% (0.473) |                0.500 | 0.945 |                0.473 |
| chain    | Agent4 | Agent5    |                  2 |     135 |           256 |        52.7% (0.527) |                0.500 | 1.055 |                0.527 |
| chain    | Agent5 | Agent4    |                  1 |     246 |           246 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| chain    | Agent1 | client_assigned |     2 |
| chain    | Agent2 | client_assigned |     1 |
| chain    | Agent4 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.2 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1814.01 |           0 |             0.00 |
|     2 |         0.2 | Success | cross                                       | cross          |             21 |         986.53 |           0 |             0.00 |
|     3 |         0.2 | Fail    | square                                      | triangle       |             28 |        1223.03 |           0 |             0.00 |
|     4 |         0.2 | Fail    | square                                      | circle         |             21 |         908.89 |           0 |             0.00 |
|     5 |         0.2 | Success | square                                      | square         |             25 |        1283.24 |           0 |             0.00 |
|     6 |         0.2 | Fail    | cross                                       | asterisk       |             16 |         555.28 |           0 |             0.00 |
|     7 |         0.2 | Fail    | circle                                      | triangle       |             37 |        1747.51 |           0 |             0.00 |
|     8 |         0.2 | Fail    | cross                                       | triangle       |             47 |        2463.22 |           0 |             0.00 |
|     9 |         0.2 | Fail    | asterisk                                    | circle         |             18 |         720.90 |           0 |             0.00 |
|    10 |         0.2 | Fail    | diamond                                     | triangle       |             20 |         871.21 |           0 |             0.00 |
|    11 |         0.2 | Fail    | square                                      | asterisk       |             14 |         595.45 |           0 |             0.00 |
|    12 |         0.2 | Fail    | triangle                                    | asterisk       |             21 |         877.10 |           0 |             0.00 |
|    13 |         0.2 | Fail    | cross                                       | circle         |             18 |         895.91 |           0 |             0.00 |
|    14 |         0.2 | Success | cross                                       | cross          |             44 |        2232.59 |           0 |             0.00 |
|    15 |         0.2 | Success | triangle                                    | triangle       |             46 |        2540.85 |           0 |             0.00 |
|    16 |         0.2 | Fail    | circle                                      | diamond        |             22 |        1169.31 |           0 |             0.00 |
|    17 |         0.2 | Success | cross                                       | cross          |             11 |         599.04 |           0 |             0.00 |
|    18 |         0.2 | Success | diamond                                     | diamond        |             14 |         519.71 |           0 |             0.00 |
|    19 |         0.2 | Fail    | cross                                       | square         |             21 |         892.59 |           0 |             0.00 |
|    20 |         0.2 | Success | diamond                                     | diamond        |             30 |        1254.87 |           0 |             0.00 |
|    21 |         0.2 | Success | diamond                                     | diamond        |             25 |        1126.48 |           0 |             0.00 |
|    22 |         0.2 | Success | triangle                                    | triangle       |             18 |         864.61 |           0 |             0.00 |
|    23 |         0.2 | Fail    | triangle                                    | square         |             13 |         546.47 |           0 |             0.00 |
|    24 |         0.2 | Fail    | square                                      | triangle       |             22 |         864.97 |           0 |             0.00 |
|    25 |         0.2 | Fail    | circle                                      | cross          |             24 |        1012.22 |           0 |             0.00 |
|    26 |         0.2 | Success | diamond                                     | diamond        |             36 |        1859.13 |           0 |             0.00 |
|    27 |         0.2 | Success | square                                      | square         |             33 |        1413.20 |           0 |             0.00 |
|    28 |         0.2 | Success | cross                                       | cross          |             35 |        1644.58 |           0 |             0.00 |
|    29 |         0.2 | Fail    | square                                      | circle         |             36 |        1975.74 |           0 |             0.00 |
|    30 |         0.2 | Success | triangle                                    | triangle       |             14 |         572.51 |           0 |             0.00 |
|    31 |         0.2 | Fail    | triangle                                    | square         |             29 |        1439.68 |           0 |             0.00 |
|    32 |         0.2 | Success | cross                                       | cross          |             25 |        1585.56 |           0 |             0.00 |
|    33 |         0.2 | Fail    | diamond                                     | asterisk       |              5 |         224.10 |           0 |             0.00 |
|    34 |         0.2 | Fail    | cross                                       | asterisk       |             14 |         506.19 |           0 |             0.00 |
|    35 |         0.2 | Fail    | diamond                                     | asterisk       |             18 |         963.41 |           0 |             0.00 |
|    36 |         0.2 | Fail    | circle                                      | asterisk       |             21 |         982.09 |           0 |             0.00 |
|    37 |         0.2 | Fail    | asterisk                                    | triangle       |             32 |        1619.99 |           0 |             0.00 |
|    38 |         0.2 | Success | triangle                                    | triangle       |             28 |        1539.53 |           0 |             0.00 |
|    39 |         0.2 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2593.87 |           0 |             0.00 |
|    40 |         0.2 | Fail    | square                                      | asterisk       |             24 |        1286.88 |           0 |             0.00 |
|    41 |         0.2 | Fail    | diamond                                     | square         |             11 |         459.35 |           0 |             0.00 |
|    42 |         0.2 | Fail    | triangle                                    | asterisk       |             42 |        2107.36 |           0 |             0.00 |
|    43 |         0.2 | Fail    | circle                                      | square         |             13 |         489.56 |           0 |             0.00 |
|    44 |         0.2 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2474.09 |           0 |             0.00 |
|    45 |         0.2 | Success | cross                                       | cross          |             23 |        1357.49 |           0 |             0.00 |
|    46 |         0.2 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2258.69 |           0 |             0.00 |
|    47 |         0.2 | Success | triangle                                    | triangle       |             34 |        1847.37 |           0 |             0.00 |
|    48 |         0.2 | Success | cross                                       | cross          |             21 |         770.67 |           0 |             0.00 |
|    49 |         0.2 | Fail    | circle                                      | diamond        |             22 |         895.08 |           0 |             0.00 |
|    50 |         0.2 | Success | asterisk                                    | asterisk       |             41 |        2546.46 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |       1829.85 |         1829.85 |        50 |           1738.588 |                     59.125 |             1797.713 |               34.772 |                        1.183 |
|     2 |       1001.82 |         1001.82 |        22 |            961.935 |                     26.308 |              988.243 |               43.724 |                        1.196 |
|     3 |       1236.37 |         1236.37 |        29 |           1188.490 |                     29.113 |             1217.602 |               40.982 |                        1.004 |
|     4 |        927.18 |          927.18 |        22 |            890.914 |                     22.928 |              913.842 |               40.496 |                        1.042 |
|     5 |       1355.84 |         1355.84 |        26 |           1311.278 |                     28.078 |             1339.356 |               50.434 |                        1.080 |
|     6 |        627.71 |          627.71 |        17 |            599.331 |                     16.799 |              616.130 |               35.255 |                        0.988 |
|     7 |       1820.31 |         1820.31 |        39 |           1757.724 |                     39.320 |             1797.044 |               45.070 |                        1.008 |
|     8 |       2476.59 |         2476.59 |        48 |           2395.916 |                     51.313 |             2447.229 |               49.915 |                        1.069 |
|     9 |        735.07 |          735.07 |        19 |            705.007 |                     18.502 |              723.509 |               37.106 |                        0.974 |
|    10 |        884.17 |          884.17 |        21 |            848.240 |                     22.059 |              870.299 |               40.392 |                        1.050 |
|    11 |        610.60 |          610.60 |        15 |            587.468 |                     14.220 |              601.688 |               39.165 |                        0.948 |
|    12 |        952.92 |          952.92 |        22 |            915.742 |                     23.568 |              939.310 |               41.625 |                        1.071 |
|    13 |        913.66 |          913.66 |        19 |            882.750 |                     19.017 |              901.768 |               46.461 |                        1.001 |
|    14 |       2249.01 |         2249.01 |        45 |           2168.118 |                     52.610 |             2220.729 |               48.180 |                        1.169 |
|    15 |       2612.75 |         2612.75 |        48 |           2530.369 |                     53.090 |             2583.459 |               52.716 |                        1.106 |
|    16 |       1242.31 |         1242.31 |        23 |           1204.107 |                     24.482 |             1228.589 |               52.352 |                        1.064 |
|    17 |        616.19 |          616.19 |        12 |            595.670 |                     12.648 |              608.318 |               49.639 |                        1.054 |
|    18 |        592.21 |          592.21 |        15 |            568.007 |                     14.959 |              582.966 |               37.867 |                        0.997 |
|    19 |        905.57 |          905.57 |        22 |            869.797 |                     22.200 |              891.997 |               39.536 |                        1.009 |
|    20 |       1326.35 |         1326.35 |        31 |           1273.256 |                     33.669 |             1306.925 |               41.073 |                        1.086 |
|    21 |       1140.10 |         1140.10 |        26 |           1096.118 |                     27.120 |             1123.238 |               42.158 |                        1.043 |
|    22 |        934.99 |          934.99 |        19 |            902.125 |                     21.009 |              923.135 |               47.480 |                        1.106 |
|    23 |        619.34 |          619.34 |        14 |            594.520 |                     15.682 |              610.202 |               42.466 |                        1.120 |
|    24 |        942.41 |          942.41 |        23 |            902.070 |                     25.372 |              927.442 |               39.220 |                        1.103 |
|    25 |       1027.91 |         1027.91 |        25 |            986.714 |                     25.599 |             1012.313 |               39.469 |                        1.024 |
|    26 |       1874.06 |         1874.06 |        37 |           1806.161 |                     44.053 |             1850.214 |               48.815 |                        1.191 |
|    27 |       1428.92 |         1428.92 |        34 |           1371.142 |                     36.506 |             1407.649 |               40.328 |                        1.074 |
|    28 |       1659.21 |         1659.21 |        36 |           1597.305 |                     39.641 |             1636.947 |               44.370 |                        1.101 |
|    29 |       1991.96 |         1991.96 |        37 |           1928.219 |                     40.103 |             1968.322 |               52.114 |                        1.084 |
|    30 |        646.09 |          646.09 |        15 |            620.941 |                     15.957 |              636.899 |               41.396 |                        1.064 |
|    31 |       1515.03 |         1515.03 |        30 |           1464.200 |                     31.470 |             1495.670 |               48.807 |                        1.049 |
|    32 |       1660.38 |         1660.38 |        26 |           1617.962 |                     26.913 |             1644.875 |               62.229 |                        1.035 |
|    33 |        297.98 |          297.98 |         6 |            288.879 |                      5.543 |              294.421 |               48.146 |                        0.924 |
|    34 |        520.63 |          520.63 |        15 |            494.388 |                     16.609 |              510.997 |               32.959 |                        1.107 |
|    35 |        983.43 |          983.43 |        19 |            953.876 |                     17.158 |              971.034 |               50.204 |                        0.903 |
|    36 |        995.39 |          995.39 |        22 |            960.408 |                     21.749 |              982.157 |               43.655 |                        0.989 |
|    37 |       1634.16 |         1634.16 |        33 |           1581.033 |                     33.368 |             1614.401 |               47.910 |                        1.011 |
|    38 |       1556.42 |         1556.42 |        29 |           1505.889 |                     31.910 |             1537.799 |               51.927 |                        1.100 |
|    39 |       2666.33 |         2666.33 |        50 |           2575.337 |                     59.722 |             2635.059 |               51.507 |                        1.194 |
|    40 |       1368.18 |         1368.18 |        25 |           1325.103 |                     27.784 |             1352.887 |               53.004 |                        1.111 |
|    41 |        532.56 |          532.56 |        12 |            514.397 |                     10.959 |              525.355 |               42.866 |                        0.913 |
|    42 |       2180.72 |         2180.72 |        43 |           2106.776 |                     46.266 |             2153.042 |               48.995 |                        1.076 |
|    43 |        504.40 |          504.40 |        14 |            482.636 |                     13.629 |              496.265 |               34.474 |                        0.973 |
|    44 |       2491.25 |         2491.25 |        50 |           2399.696 |                     59.940 |             2459.636 |               47.994 |                        1.199 |
|    45 |       1370.20 |         1370.20 |        24 |           1330.318 |                     24.046 |             1354.364 |               55.430 |                        1.002 |
|    46 |       2333.80 |         2333.80 |        50 |           2237.339 |                     65.360 |             2302.699 |               44.747 |                        1.307 |
|    47 |       1863.61 |         1863.61 |        35 |           1804.118 |                     37.645 |             1841.763 |               51.546 |                        1.076 |
|    48 |        785.31 |          785.31 |        22 |            748.491 |                     23.046 |              771.537 |               34.022 |                        1.048 |
|    49 |        909.09 |          909.09 |        23 |            869.136 |                     25.462 |              894.598 |               37.789 |                        1.107 |
|    50 |       2622.54 |         2622.54 |        42 |           2548.125 |                     47.535 |             2595.660 |               60.670 |                        1.132 |
```

## Reconnect details

No Jetson disconnects were recorded.
