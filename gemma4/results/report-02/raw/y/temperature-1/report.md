# Y topology auto-trial report

## Summary

- Batch: `temperature-1`
- Model: `gemma4:e2b-it-qat`
- Temperature: 1
- Completed trials: 50/50
- Average time: 1679.70 seconds
- Average total messages: 28.18
- Average Gemma 4 thinking time per response: 53.342 seconds
- Average visible-response generation time: 1.136 seconds
- Average complete generation time: 54.478 seconds
- Success rate: 14/50 (28.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     282 |           282 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     311 |           311 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      51 |           233 |        21.9% (0.219) |                0.333 | 0.657 |                0.220 |
| y        | Agent3 | Agent2    |                  3 |      67 |           233 |        28.8% (0.288) |                0.333 | 0.863 |                0.288 |
| y        | Agent3 | Agent4    |                  3 |     115 |           233 |        49.4% (0.494) |                0.333 | 1.481 |                0.493 |
| y        | Agent4 | Agent3    |                  2 |     197 |           248 |        79.4% (0.794) |                0.500 | 1.589 |                0.793 |
| y        | Agent4 | Agent5    |                  2 |      51 |           248 |        20.6% (0.206) |                0.500 | 0.411 |                0.207 |
| y        | Agent5 | Agent4    |                  1 |     331 |           331 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent1 | client_default  |     1 |
| y        | Agent2 | client_default  |     1 |
| y        | Agent3 | client_assigned |     1 |
| y        | Agent5 | client_default  |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           1 | Fail    | cross                                       | asterisk       |             36 |        2252.29 |           0 |             0.00 |
|     2 |           1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2558.68 |           0 |             0.00 |
|     3 |           1 | Fail    | cross                                       | square         |             35 |        2210.29 |           0 |             0.00 |
|     4 |           1 | Success | cross                                       | cross          |              8 |         331.70 |           0 |             0.00 |
|     5 |           1 | Fail    | cross                                       | triangle       |             17 |        1100.67 |           0 |             0.00 |
|     6 |           1 | Fail    | cross                                       | asterisk       |             15 |        1042.84 |           0 |             0.00 |
|     7 |           1 | Success | diamond                                     | diamond        |             11 |         898.13 |           0 |             0.00 |
|     8 |           1 | Fail    | diamond                                     | triangle       |             17 |        1099.35 |           0 |             0.00 |
|     9 |           1 | Fail    | triangle                                    | asterisk       |             48 |        2631.39 |           0 |             0.00 |
|    10 |           1 | Fail    | cross                                       | asterisk       |             47 |        2078.19 |           0 |             0.00 |
|    11 |           1 | Fail    | asterisk                                    | diamond        |             27 |        1712.49 |           0 |             0.00 |
|    12 |           1 | Fail    | triangle                                    | cross          |             42 |        1762.40 |           0 |             0.00 |
|    13 |           1 | Success | cross                                       | cross          |             17 |        1229.78 |           0 |             0.00 |
|    14 |           1 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2624.76 |           0 |             0.00 |
|    15 |           1 | Success | asterisk                                    | asterisk       |             10 |         399.89 |           0 |             0.00 |
|    16 |           1 | Fail    | circle                                      | triangle       |             21 |        1125.71 |           0 |             0.00 |
|    17 |           1 | Fail    | square                                      | asterisk       |             48 |        2952.70 |           0 |             0.00 |
|    18 |           1 | Fail    | cross                                       | diamond        |             11 |         754.91 |           0 |             0.00 |
|    19 |           1 | Success | square                                      | square         |             22 |        1475.90 |           0 |             0.00 |
|    20 |           1 | Fail    | cross                                       | square         |             45 |        2540.12 |           0 |             0.00 |
|    21 |           1 | Fail    | circle                                      | cross          |             48 |        2269.76 |           0 |             0.00 |
|    22 |           1 | Fail    | diamond                                     | square         |             16 |        1120.43 |           0 |             0.00 |
|    23 |           1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        3032.80 |           0 |             0.00 |
|    24 |           1 | Fail    | asterisk                                    | triangle       |             18 |        1381.15 |           0 |             0.00 |
|    25 |           1 | Fail    | square                                      | asterisk       |             20 |        1016.97 |           0 |             0.00 |
|    26 |           1 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2045.92 |           0 |             0.00 |
|    27 |           1 | Success | cross                                       | cross          |             23 |        1220.12 |           0 |             0.00 |
|    28 |           1 | Fail    | asterisk                                    | square         |             22 |        1384.23 |           0 |             0.00 |
|    29 |           1 | Fail    | square                                      | circle         |             18 |        1260.96 |           0 |             0.00 |
|    30 |           1 | Success | circle                                      | circle         |             25 |        1298.51 |           0 |             0.00 |
|    31 |           1 | Fail    | triangle                                    | cross          |             23 |        1137.45 |           0 |             0.00 |
|    32 |           1 | Success | triangle                                    | triangle       |             17 |        1049.96 |           0 |             0.00 |
|    33 |           1 | Success | cross                                       | cross          |             21 |        2062.42 |           0 |             0.00 |
|    34 |           1 | Success | square                                      | square         |             23 |        1939.53 |           0 |             0.00 |
|    35 |           1 | Fail    | cross                                       | square         |             42 |        2459.17 |           0 |             0.00 |
|    36 |           1 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2856.65 |           0 |             0.00 |
|    37 |           1 | Success | asterisk                                    | asterisk       |             17 |         782.67 |           0 |             0.00 |
|    38 |           1 | Fail    | diamond                                     | triangle       |             14 |         760.90 |           0 |             0.00 |
|    39 |           1 | Fail    | square                                      | asterisk       |             32 |        2251.44 |           0 |             0.00 |
|    40 |           1 | Fail    | diamond                                     | circle         |             10 |         775.02 |           0 |             0.00 |
|    41 |           1 | Success | diamond                                     | diamond        |             13 |         795.18 |           0 |             0.00 |
|    42 |           1 | Success | asterisk                                    | asterisk       |             34 |        2439.69 |           0 |             0.00 |
|    43 |           1 | Fail    | square                                      | circle         |              7 |        1110.79 |           0 |             0.00 |
|    44 |           1 | Fail    | triangle                                    | diamond        |             13 |         897.56 |           0 |             0.00 |
|    45 |           1 | Success | diamond                                     | diamond        |             40 |        2647.47 |           0 |             0.00 |
|    46 |           1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2264.25 |           0 |             0.00 |
|    47 |           1 | Fail    | triangle                                    | square         |             49 |        3018.95 |           0 |             0.00 |
|    48 |           1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        3177.31 |           0 |             0.00 |
|    49 |           1 | Fail    | cross                                       | triangle       |             27 |        2061.66 |           0 |             0.00 |
|    50 |           1 | Fail    | cross                                       | circle         |             10 |         684.06 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |       2272.73 |         2272.73 |        37 |           1841.205 |                     45.559 |             1886.764 |               49.762 |                        1.231 |
|     2 |       2577.39 |         2577.39 |        50 |           2442.590 |                     54.294 |             2496.884 |               48.852 |                        1.086 |
|     3 |       2228.46 |         2228.46 |        36 |           1857.476 |                     43.000 |             1900.476 |               51.597 |                        1.194 |
|     4 |        592.43 |          592.43 |         9 |            475.772 |                      9.537 |              485.308 |               52.864 |                        1.060 |
|     5 |       1114.85 |         1114.85 |        18 |            853.811 |                     21.307 |              875.119 |               47.434 |                        1.184 |
|     6 |       1206.81 |         1206.81 |        16 |           1041.588 |                     16.345 |             1057.933 |               65.099 |                        1.022 |
|     7 |        915.33 |          915.33 |        12 |            708.301 |                     12.977 |              721.278 |               59.025 |                        1.081 |
|     8 |       1183.70 |         1183.70 |        18 |            967.538 |                     18.842 |              986.380 |               53.752 |                        1.047 |
|     9 |       2713.02 |         2713.02 |        49 |           2475.186 |                     53.684 |             2528.870 |               50.514 |                        1.096 |
|    10 |       2087.76 |         2087.76 |        48 |           2083.762 |                     53.933 |             2137.695 |               43.412 |                        1.124 |
|    11 |       1727.79 |         1727.79 |        28 |           1313.141 |                     30.745 |             1343.886 |               46.898 |                        1.098 |
|    12 |       2022.73 |         2022.73 |        43 |           1950.559 |                     50.736 |             2001.296 |               45.362 |                        1.180 |
|    13 |       1246.01 |         1246.01 |        18 |           1214.683 |                     19.376 |             1234.060 |               67.482 |                        1.076 |
|    14 |       2641.29 |         2641.29 |        50 |           2679.258 |                     59.419 |             2738.677 |               53.585 |                        1.188 |
|    15 |        424.67 |          424.67 |        11 |            405.491 |                     12.046 |              417.536 |               36.863 |                        1.095 |
|    16 |       1202.85 |         1202.85 |        22 |           1165.864 |                     23.070 |             1188.933 |               52.994 |                        1.049 |
|    17 |       3028.06 |         3028.06 |        50 |           3000.330 |                     53.829 |             3054.159 |               60.007 |                        1.077 |
|    18 |        832.40 |          832.40 |        12 |            790.813 |                     11.888 |              802.701 |               65.901 |                        0.991 |
|    19 |       1557.60 |         1557.60 |        23 |           1374.639 |                     26.021 |             1400.660 |               59.767 |                        1.131 |
|    20 |       2552.54 |         2552.54 |        46 |           2283.279 |                     52.374 |             2335.652 |               49.636 |                        1.139 |
|    21 |       2284.33 |         2284.33 |        49 |           2309.028 |                     57.765 |             2366.793 |               47.123 |                        1.179 |
|    22 |       1201.42 |         1201.42 |        17 |           1040.775 |                     18.243 |             1059.019 |               61.222 |                        1.073 |
|    23 |       3174.58 |         3174.58 |        50 |           2748.855 |                     62.629 |             2811.484 |               54.977 |                        1.253 |
|    24 |       1401.24 |         1401.24 |        19 |           1084.664 |                     19.607 |             1104.271 |               57.088 |                        1.032 |
|    25 |       1036.31 |         1036.31 |        21 |            982.557 |                     25.021 |             1007.578 |               46.788 |                        1.191 |
|    26 |       2062.92 |         2062.92 |        50 |           2092.681 |                     57.807 |             2150.489 |               41.854 |                        1.156 |
|    27 |       1436.23 |         1436.23 |        24 |           1202.821 |                     25.640 |             1228.462 |               50.118 |                        1.068 |
|    28 |       1468.91 |         1468.91 |        23 |           1200.588 |                     23.170 |             1223.758 |               52.199 |                        1.007 |
|    29 |       1278.38 |         1278.38 |        19 |           1006.436 |                     22.776 |             1029.213 |               52.970 |                        1.199 |
|    30 |       1314.46 |         1314.46 |        26 |           1276.815 |                     25.919 |             1302.734 |               49.108 |                        0.997 |
|    31 |       1147.72 |         1147.72 |        24 |           1077.734 |                     29.168 |             1106.902 |               44.906 |                        1.215 |
|    32 |       1122.46 |         1122.46 |        18 |           1059.551 |                     22.500 |             1082.051 |               58.864 |                        1.250 |
|    33 |       2078.97 |         2078.97 |        22 |           1409.218 |                     27.133 |             1436.351 |               64.055 |                        1.233 |
|    34 |       2021.03 |         2021.03 |        24 |           1192.684 |                     26.109 |             1218.792 |               49.695 |                        1.088 |
|    35 |       2534.45 |         2534.45 |        43 |           2441.144 |                     51.412 |             2492.556 |               56.771 |                        1.196 |
|    36 |       2932.84 |         2932.84 |        50 |           2897.778 |                     57.778 |             2955.556 |               57.956 |                        1.156 |
|    37 |        801.53 |          801.53 |        18 |            770.428 |                     19.301 |              789.729 |               42.802 |                        1.072 |
|    38 |        777.42 |          777.42 |        15 |            752.322 |                     15.325 |              767.646 |               50.155 |                        1.022 |
|    39 |       2266.85 |         2266.85 |        33 |           1954.211 |                     35.944 |             1990.155 |               59.219 |                        1.089 |
|    40 |        793.57 |          793.57 |        11 |            775.665 |                     10.319 |              785.984 |               70.515 |                        0.938 |
|    41 |        880.22 |          880.22 |        14 |            855.444 |                     16.070 |              871.514 |               61.103 |                        1.148 |
|    42 |       2457.42 |         2457.42 |        35 |           2201.886 |                     37.133 |             2239.019 |               62.911 |                        1.061 |
|    43 |       1129.84 |         1129.84 |         8 |            621.878 |                      8.011 |              629.889 |               77.735 |                        1.001 |
|    44 |        915.40 |          915.40 |        14 |            667.240 |                     15.036 |              682.276 |               47.660 |                        1.074 |
|    45 |       2673.07 |         2673.07 |        41 |           2381.838 |                     47.500 |             2429.338 |               58.094 |                        1.159 |
|    46 |       2471.97 |         2471.97 |        50 |           2639.539 |                     58.204 |             2697.744 |               52.791 |                        1.164 |
|    47 |       3144.86 |         3144.86 |        50 |           2725.876 |                     61.763 |             2787.639 |               54.518 |                        1.235 |
|    48 |       3191.94 |         3191.94 |        50 |           2805.888 |                     58.170 |             2864.058 |               56.118 |                        1.163 |
|    49 |       2156.24 |         2156.24 |        28 |           1795.757 |                     32.763 |             1828.520 |               64.134 |                        1.170 |
|    50 |        948.48 |          948.48 |        11 |            608.840 |                     13.864 |              622.704 |               55.349 |                        1.260 |
```

## Reconnect details

No Jetson disconnects were recorded.
