# Y topology auto-trial report

## Summary

- Batch: `temperature-0.2`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 1435.46 seconds
- Average total messages: 27.82
- Average Gemma 4 thinking time per response: 47.618 seconds
- Average visible-response generation time: 1.074 seconds
- Average complete generation time: 48.692 seconds
- Success rate: 27/50 (54.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     277 |           277 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     297 |           297 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      67 |           287 |        23.3% (0.233) |                0.333 | 0.700 |                0.234 |
| y        | Agent3 | Agent2    |                  3 |      72 |           287 |        25.1% (0.251) |                0.333 | 0.753 |                0.251 |
| y        | Agent3 | Agent4    |                  3 |     148 |           287 |        51.6% (0.516) |                0.333 | 1.547 |                0.515 |
| y        | Agent4 | Agent3    |                  2 |     193 |           242 |        79.8% (0.798) |                0.500 | 1.595 |                0.796 |
| y        | Agent4 | Agent5    |                  2 |      49 |           242 |        20.2% (0.202) |                0.500 | 0.405 |                0.204 |
| y        | Agent5 | Agent4    |                  1 |     285 |           285 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent3 | client_assigned |     1 |
| y        | Agent4 | client_assigned |     1 |
| y        | Agent5 | client_default  |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.2 | Success | cross                                       | cross          |             13 |         407.98 |           0 |             0.00 |
|     2 |         0.2 | Fail    | triangle                                    | circle         |              9 |         442.78 |           0 |             0.00 |
|     3 |         0.2 | Success | circle                                      | circle         |             28 |        1242.50 |           0 |             0.00 |
|     4 |         0.2 | Success | circle                                      | circle         |             23 |        1409.80 |           0 |             0.00 |
|     5 |         0.2 | Success | triangle                                    | triangle       |             30 |        1362.33 |           0 |             0.00 |
|     6 |         0.2 | Fail    | cross                                       | asterisk       |             19 |         847.91 |           0 |             0.00 |
|     7 |         0.2 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2390.62 |           0 |             0.00 |
|     8 |         0.2 | Success | cross                                       | cross          |             33 |        1542.90 |           0 |             0.00 |
|     9 |         0.2 | Success | diamond                                     | diamond        |             15 |         758.55 |           0 |             0.00 |
|    10 |         0.2 | Fail    | square                                      | circle         |             47 |        2576.35 |           0 |             0.00 |
|    11 |         0.2 | Success | triangle                                    | triangle       |             30 |        1529.40 |           0 |             0.00 |
|    12 |         0.2 | Success | square                                      | square         |             22 |        1180.70 |           0 |             0.00 |
|    13 |         0.2 | Success | circle                                      | circle         |             30 |        1464.59 |           0 |             0.00 |
|    14 |         0.2 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2128.28 |           0 |             0.00 |
|    15 |         0.2 | Success | cross                                       | cross          |             19 |         927.57 |           0 |             0.00 |
|    16 |         0.2 | Success | cross                                       | cross          |             16 |         881.49 |           0 |             0.00 |
|    17 |         0.2 | Fail    | square                                      | triangle       |             26 |        1122.01 |           0 |             0.00 |
|    18 |         0.2 | Success | diamond                                     | diamond        |             12 |         549.57 |           0 |             0.00 |
|    19 |         0.2 | Success | square                                      | square         |             37 |        2098.14 |           0 |             0.00 |
|    20 |         0.2 | Fail    | cross                                       | asterisk       |             32 |        1769.97 |           0 |             0.00 |
|    21 |         0.2 | Fail    | asterisk                                    | diamond        |             26 |        1134.07 |           0 |             0.00 |
|    22 |         0.2 | Fail    | circle                                      | triangle       |             49 |        2124.29 |           0 |             0.00 |
|    23 |         0.2 | Success | asterisk                                    | asterisk       |             45 |        2316.68 |           0 |             0.00 |
|    24 |         0.2 | Fail    | asterisk                                    | triangle       |             15 |         683.99 |           0 |             0.00 |
|    25 |         0.2 | Success | square                                      | square         |             18 |        1162.25 |           0 |             0.00 |
|    26 |         0.2 | Success | square                                      | square         |             34 |        2057.38 |           0 |             0.00 |
|    27 |         0.2 | Success | triangle                                    | triangle       |             11 |         534.44 |           0 |             0.00 |
|    28 |         0.2 | Success | circle                                      | circle         |             25 |        1006.58 |           0 |             0.00 |
|    29 |         0.2 | Fail    | cross                                       | square         |              9 |         408.50 |           0 |             0.00 |
|    30 |         0.2 | Fail    | square                                      | triangle       |             13 |         622.78 |           0 |             0.00 |
|    31 |         0.2 | Success | cross                                       | cross          |             22 |        1038.80 |           0 |             0.00 |
|    32 |         0.2 | Fail    | square                                      | circle         |              9 |         713.56 |           0 |             0.00 |
|    33 |         0.2 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2209.95 |           0 |             0.00 |
|    34 |         0.2 | Fail    | circle                                      | asterisk       |             17 |         569.91 |           0 |             0.00 |
|    35 |         0.2 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2641.52 |           0 |             0.00 |
|    36 |         0.2 | Success | asterisk                                    | asterisk       |             10 |         447.27 |           0 |             0.00 |
|    37 |         0.2 | Fail    | cross                                       | asterisk       |             19 |        1205.84 |           0 |             0.00 |
|    38 |         0.2 | Fail    | triangle                                    | diamond        |             23 |        1099.09 |           0 |             0.00 |
|    39 |         0.2 | Success | square                                      | square         |             18 |         967.79 |           0 |             0.00 |
|    40 |         0.2 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2475.10 |           0 |             0.00 |
|    41 |         0.2 | Success | diamond                                     | diamond        |             26 |        1415.53 |           0 |             0.00 |
|    42 |         0.2 | Success | cross                                       | cross          |             21 |        1573.22 |           0 |             0.00 |
|    43 |         0.2 | Fail    | cross                                       | square         |             40 |        2019.57 |           0 |             0.00 |
|    44 |         0.2 | Success | cross                                       | cross          |             22 |        1234.02 |           0 |             0.00 |
|    45 |         0.2 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2882.71 |           0 |             0.00 |
|    46 |         0.2 | Fail    | circle                                      | square         |             30 |        1597.65 |           0 |             0.00 |
|    47 |         0.2 | Success | diamond                                     | diamond        |             44 |        2360.02 |           0 |             0.00 |
|    48 |         0.2 | Fail    | diamond                                     | square         |             38 |        2050.67 |           0 |             0.00 |
|    49 |         0.2 | Success | asterisk                                    | asterisk       |             47 |        3432.19 |           0 |             0.00 |
|    50 |         0.2 | Success | diamond                                     | diamond        |             19 |        1154.20 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |        427.16 |          427.16 |        14 |            406.095 |                     12.779 |              418.874 |               29.007 |                        0.913 |
|     2 |        463.96 |          463.96 |        10 |            449.484 |                      8.830 |              458.314 |               44.948 |                        0.883 |
|     3 |       1260.00 |         1260.00 |        29 |           1209.040 |                     33.092 |             1242.132 |               41.691 |                        1.141 |
|     4 |       1424.18 |         1424.18 |        24 |           1382.031 |                     26.397 |             1408.428 |               57.585 |                        1.100 |
|     5 |       1447.09 |         1447.09 |        31 |           1398.334 |                     29.633 |             1427.967 |               45.108 |                        0.956 |
|     6 |        861.57 |          861.57 |        21 |            825.907 |                     22.332 |              848.239 |               39.329 |                        1.063 |
|     7 |       2408.63 |         2408.63 |        50 |           2317.528 |                     59.531 |             2377.059 |               46.351 |                        1.191 |
|     8 |       1560.65 |         1560.65 |        34 |           1502.822 |                     37.080 |             1539.902 |               44.201 |                        1.091 |
|     9 |        840.88 |          840.88 |        16 |            815.795 |                     15.739 |              831.534 |               50.987 |                        0.984 |
|    10 |       2652.97 |         2652.97 |        48 |           2566.174 |                     55.254 |             2621.429 |               53.462 |                        1.151 |
|    11 |       1548.48 |         1548.48 |        31 |           1494.378 |                     34.592 |             1528.970 |               48.206 |                        1.116 |
|    12 |       1195.86 |         1195.86 |        23 |           1156.551 |                     24.997 |             1181.548 |               50.285 |                        1.087 |
|    13 |       1484.13 |         1484.13 |        31 |           1433.363 |                     31.281 |             1464.644 |               46.238 |                        1.009 |
|    14 |       2143.80 |         2143.80 |        50 |           2054.350 |                     57.705 |             2112.055 |               41.087 |                        1.154 |
|    15 |        945.15 |          945.15 |        20 |            911.651 |                     20.644 |              932.295 |               45.583 |                        1.032 |
|    16 |        964.06 |          964.06 |        17 |            937.371 |                     15.873 |              953.245 |               55.139 |                        0.934 |
|    17 |       1135.71 |         1135.71 |        27 |           1092.634 |                     25.617 |             1118.251 |               40.468 |                        0.949 |
|    18 |        564.09 |          564.09 |        13 |            542.888 |                     13.331 |              556.219 |               41.761 |                        1.025 |
|    19 |       2113.60 |         2113.60 |        39 |           2044.153 |                     45.859 |             2090.012 |               52.414 |                        1.176 |
|    20 |       1853.07 |         1853.07 |        33 |           1584.507 |                     34.631 |             1619.138 |               48.015 |                        1.049 |
|    21 |       1157.33 |         1157.33 |        27 |            959.899 |                     31.125 |              991.024 |               35.552 |                        1.153 |
|    22 |       2198.29 |         2198.29 |        50 |           2136.789 |                     54.020 |             2190.808 |               42.736 |                        1.080 |
|    23 |       2331.59 |         2331.59 |        46 |           2245.674 |                     57.048 |             2302.722 |               48.819 |                        1.240 |
|    24 |        702.44 |          702.44 |        16 |            673.591 |                     18.078 |              691.669 |               42.099 |                        1.130 |
|    25 |       1184.58 |         1184.58 |        20 |           1151.149 |                     21.101 |             1172.250 |               57.557 |                        1.055 |
|    26 |       2073.62 |         2073.62 |        35 |           2013.772 |                     37.532 |             2051.305 |               57.536 |                        1.072 |
|    27 |        548.23 |          548.23 |        12 |            528.083 |                     12.335 |              540.418 |               44.007 |                        1.028 |
|    28 |       1023.61 |         1023.61 |        26 |            980.895 |                     25.556 |             1006.451 |               37.727 |                        0.983 |
|    29 |        422.32 |          422.32 |        10 |            404.821 |                     10.669 |              415.491 |               40.482 |                        1.067 |
|    30 |        640.67 |          640.67 |        14 |            617.354 |                     14.259 |              631.613 |               44.097 |                        1.018 |
|    31 |       1116.13 |         1116.13 |        23 |           1075.707 |                     24.803 |             1100.510 |               46.770 |                        1.078 |
|    32 |        727.80 |          727.80 |        10 |            584.066 |                      9.481 |              593.547 |               58.407 |                        0.948 |
|    33 |       2294.21 |         2294.21 |        50 |           2260.558 |                     51.279 |             2311.837 |               45.211 |                        1.026 |
|    34 |        583.79 |          583.79 |        18 |            525.803 |                     20.538 |              546.341 |               29.211 |                        1.141 |
|    35 |       2657.80 |         2657.80 |        50 |           2639.588 |                     48.650 |             2688.238 |               52.792 |                        0.973 |
|    36 |        460.47 |          460.47 |        11 |            441.565 |                     12.059 |              453.624 |               40.142 |                        1.096 |
|    37 |       1220.88 |         1220.88 |        20 |           1152.478 |                     20.233 |             1172.711 |               57.624 |                        1.012 |
|    38 |       1174.64 |         1174.64 |        24 |           1135.448 |                     24.722 |             1160.170 |               47.310 |                        1.030 |
|    39 |        980.87 |          980.87 |        19 |            947.638 |                     20.307 |              967.945 |               49.876 |                        1.069 |
|    40 |       2495.73 |         2495.73 |        51 |           2408.925 |                     54.335 |             2463.261 |               47.234 |                        1.065 |
|    41 |       1436.01 |         1436.01 |        27 |           1295.620 |                     29.845 |             1325.465 |               47.986 |                        1.105 |
|    42 |       1589.00 |         1589.00 |        22 |           1252.738 |                     21.081 |             1273.819 |               56.943 |                        0.958 |
|    43 |       2037.13 |         2037.13 |        41 |           1965.179 |                     42.768 |             2007.947 |               47.931 |                        1.043 |
|    44 |       1251.21 |         1251.21 |        23 |           1020.240 |                     24.868 |             1045.108 |               44.358 |                        1.081 |
|    45 |       2898.00 |         2898.00 |        50 |           2522.053 |                     57.984 |             2580.037 |               50.441 |                        1.160 |
|    46 |       1615.28 |         1615.28 |        31 |           1373.328 |                     32.789 |             1406.117 |               44.301 |                        1.058 |
|    47 |       2375.75 |         2375.75 |        45 |           2297.636 |                     48.587 |             2346.223 |               51.059 |                        1.080 |
|    48 |       2071.24 |         2071.24 |        39 |           1929.440 |                     44.580 |             1974.021 |               49.473 |                        1.143 |
|    49 |       3454.74 |         3454.74 |        48 |           2897.852 |                     49.104 |             2946.956 |               60.372 |                        1.023 |
|    50 |       1222.42 |         1222.42 |        20 |            959.051 |                     20.551 |              979.602 |               47.953 |                        1.028 |
```

## Reconnect details

No Jetson disconnects were recorded.
