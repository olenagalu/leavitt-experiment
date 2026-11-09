# Wheel auto-trial report

## Summary

- Batch: `temperature-0.1`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0.1
- Completed trials: 50/50
- Average time: 1563.04 seconds
- Average total messages: 35.36
- Average Gemma 4 thinking time per response: 41.601 seconds
- Average visible-response generation time: 1.008 seconds
- Average complete generation time: 42.609 seconds
- Success rate: 20/50 (40.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     347 |           347 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     380 |           380 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     103 |           324 |        31.8% (0.318) |                0.250 | 1.272 |                0.317 |
| wheel    | Agent3 | Agent2    |                  4 |      98 |           324 |        30.2% (0.302) |                0.250 | 1.210 |                0.302 |
| wheel    | Agent3 | Agent4    |                  4 |      78 |           324 |        24.1% (0.241) |                0.250 | 0.963 |                0.241 |
| wheel    | Agent3 | Agent5    |                  4 |      45 |           324 |        13.9% (0.139) |                0.250 | 0.556 |                0.140 |
| wheel    | Agent4 | Agent3    |                  1 |     356 |           356 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     354 |           354 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source          | Count |
| -------- | ------ | ---------------------- | ----- |
| wheel    | Agent3 | client_default         |     1 |
| wheel    | Agent3 | client_default_invalid |     1 |
| wheel    | Agent4 | client_assigned        |     1 |
| wheel    | Agent4 | client_default         |     2 |
| wheel    | Agent5 | client_default         |     2 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2132.27 |           0 |             0.00 |
|     2 |         0.1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2611.94 |           0 |             0.00 |
|     3 |         0.1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2160.40 |           0 |             0.00 |
|     4 |         0.1 | Fail    | square                                      | circle         |             10 |         320.42 |           0 |             0.00 |
|     5 |         0.1 | Success | cross                                       | cross          |             44 |        2588.51 |           0 |             0.00 |
|     6 |         0.1 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2360.40 |           0 |             0.00 |
|     7 |         0.1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2312.55 |           0 |             0.00 |
|     8 |         0.1 | Success | diamond                                     | diamond        |             22 |         828.52 |           0 |             0.00 |
|     9 |         0.1 | Success | asterisk                                    | asterisk       |             24 |         921.94 |           0 |             0.00 |
|    10 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        1920.11 |           0 |             0.00 |
|    11 |         0.1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2026.96 |           0 |             0.00 |
|    12 |         0.1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        1767.05 |           0 |             0.00 |
|    13 |         0.1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1844.39 |           0 |             0.00 |
|    14 |         0.1 | Success | square                                      | square         |             23 |         923.16 |           0 |             0.00 |
|    15 |         0.1 | Fail    | square                                      | cross          |             34 |        1686.93 |           0 |             0.00 |
|    16 |         0.1 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2435.55 |           0 |             0.00 |
|    17 |         0.1 | Success | diamond                                     | diamond        |              6 |         293.89 |           0 |             0.00 |
|    18 |         0.1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2241.62 |           0 |             0.00 |
|    19 |         0.1 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2408.93 |           0 |             0.00 |
|    20 |         0.1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2463.16 |           0 |             0.00 |
|    21 |         0.1 | Success | diamond                                     | diamond        |             16 |         613.50 |           0 |             0.00 |
|    22 |         0.1 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        1631.42 |           0 |             0.00 |
|    23 |         0.1 | Success | asterisk                                    | asterisk       |             31 |        1475.25 |           0 |             0.00 |
|    24 |         0.1 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2297.92 |           0 |             0.00 |
|    25 |         0.1 | Fail    | square                                      | diamond        |             27 |        1105.95 |           0 |             0.00 |
|    26 |         0.1 | Fail    | square                                      | circle         |             34 |        1517.16 |           0 |             0.00 |
|    27 |         0.1 | Success | circle                                      | circle         |             32 |        1356.29 |           0 |             0.00 |
|    28 |         0.1 | Success | cross                                       | cross          |             36 |        1900.61 |           0 |             0.00 |
|    29 |         0.1 | Success | asterisk                                    | asterisk       |              7 |         267.10 |           0 |             0.00 |
|    30 |         0.1 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        1733.23 |           0 |             0.00 |
|    31 |         0.1 | Success | diamond                                     | diamond        |              8 |         308.34 |           0 |             0.00 |
|    32 |         0.1 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2871.69 |           0 |             0.00 |
|    33 |         0.1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2168.65 |           0 |             0.00 |
|    34 |         0.1 | Fail    | cross                                       | circle         |             31 |        1363.11 |           0 |             0.00 |
|    35 |         0.1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2305.50 |           0 |             0.00 |
|    36 |         0.1 | Fail    | cross                                       | asterisk       |             20 |         915.56 |           0 |             0.00 |
|    37 |         0.1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2365.34 |           0 |             0.00 |
|    38 |         0.1 | Success | cross                                       | cross          |             37 |        1367.97 |           0 |             0.00 |
|    39 |         0.1 | Success | triangle                                    | triangle       |             22 |        1015.22 |           0 |             0.00 |
|    40 |         0.1 | Success | circle                                      | circle         |             27 |        1205.30 |           0 |             0.00 |
|    41 |         0.1 | Fail    | square                                      | asterisk       |             38 |        1807.68 |           0 |             0.00 |
|    42 |         0.1 | Success | circle                                      | circle         |              7 |         242.50 |           0 |             0.00 |
|    43 |         0.1 | Success | cross                                       | cross          |              8 |         212.44 |           0 |             0.00 |
|    44 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2130.18 |           0 |             0.00 |
|    45 |         0.1 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        1949.00 |           0 |             0.00 |
|    46 |         0.1 | Success | asterisk                                    | asterisk       |             39 |        1704.44 |           0 |             0.00 |
|    47 |         0.1 | Success | asterisk                                    | asterisk       |              7 |         391.03 |           0 |             0.00 |
|    48 |         0.1 | Success | circle                                      | circle         |             22 |        1161.87 |           0 |             0.00 |
|    49 |         0.1 | Fail    | square                                      | diamond        |             18 |        1055.72 |           0 |             0.00 |
|    50 |         0.1 | Success | diamond                                     | diamond        |             38 |        1463.17 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |       2151.68 |         2151.68 |        52 |           2069.921 |                     49.580 |             2119.501 |               39.806 |                        0.953 |
|     2 |       2628.95 |         2628.95 |        51 |           2542.371 |                     54.751 |             2597.121 |               49.850 |                        1.074 |
|     3 |       2179.59 |         2179.59 |        50 |           2101.701 |                     47.049 |             2148.751 |               42.034 |                        0.941 |
|     4 |        338.59 |          338.59 |        11 |            321.686 |                     10.303 |              331.989 |               29.244 |                        0.937 |
|     5 |       2606.94 |         2606.94 |        48 |           2530.022 |                     47.776 |             2577.798 |               52.709 |                        0.995 |
|     6 |       2376.42 |         2376.42 |        51 |           2291.702 |                     54.515 |             2346.217 |               44.935 |                        1.069 |
|     7 |       2330.48 |         2330.48 |        50 |           2247.152 |                     51.587 |             2298.739 |               44.943 |                        1.032 |
|     8 |        845.61 |          845.61 |        23 |            806.424 |                     23.486 |              829.910 |               35.062 |                        1.021 |
|     9 |        936.89 |          936.89 |        25 |            896.826 |                     24.628 |              921.454 |               35.873 |                        0.985 |
|    10 |       1939.01 |         1939.01 |        50 |           1858.174 |                     50.572 |             1908.746 |               37.163 |                        1.011 |
|    11 |       2044.86 |         2044.86 |        51 |           1963.033 |                     49.602 |             2012.635 |               38.491 |                        0.973 |
|    12 |       1782.02 |         1782.02 |        50 |           1697.769 |                     51.819 |             1749.588 |               33.955 |                        1.036 |
|    13 |       1860.93 |         1860.93 |        50 |           1775.407 |                     55.262 |             1830.669 |               35.508 |                        1.105 |
|    14 |        939.81 |          939.81 |        24 |            895.798 |                     28.616 |              924.414 |               37.325 |                        1.192 |
|    15 |       1706.55 |         1706.55 |        36 |           1649.582 |                     33.987 |             1683.570 |               45.822 |                        0.944 |
|    16 |       2456.41 |         2456.41 |        50 |           2195.144 |                     49.591 |             2244.735 |               43.903 |                        0.992 |
|    17 |        310.39 |          310.39 |         7 |            300.433 |                      6.075 |              306.508 |               42.919 |                        0.868 |
|    18 |       2261.64 |         2261.64 |        51 |           2179.945 |                     49.033 |             2228.978 |               42.744 |                        0.961 |
|    19 |       2429.36 |         2429.36 |        52 |           2340.621 |                     57.303 |             2397.924 |               45.012 |                        1.102 |
|    20 |       2542.96 |         2542.96 |        51 |           2460.247 |                     49.825 |             2510.072 |               48.240 |                        0.977 |
|    21 |        691.02 |          691.02 |        17 |            663.759 |                     16.782 |              680.541 |               39.045 |                        0.987 |
|    22 |       1648.54 |         1648.54 |        50 |           1564.006 |                     52.423 |             1616.429 |               31.280 |                        1.048 |
|    23 |       1490.67 |         1490.67 |        33 |           1436.908 |                     33.799 |             1470.707 |               43.543 |                        1.024 |
|    24 |       2372.56 |         2372.56 |        50 |           2112.842 |                     48.366 |             2161.208 |               42.257 |                        0.967 |
|    25 |       1121.89 |         1121.89 |        28 |           1076.324 |                     27.350 |             1103.674 |               38.440 |                        0.977 |
|    26 |       1535.08 |         1535.08 |        37 |           1474.839 |                     36.249 |             1511.088 |               39.861 |                        0.980 |
|    27 |       1372.49 |         1372.49 |        33 |           1313.769 |                     37.367 |             1351.136 |               39.811 |                        1.132 |
|    28 |       1919.53 |         1919.53 |        40 |           1856.494 |                     36.777 |             1893.272 |               46.412 |                        0.919 |
|    29 |        283.27 |          283.27 |         8 |            272.148 |                      6.385 |              278.532 |               34.018 |                        0.798 |
|    30 |       1746.49 |         1746.49 |        50 |           1666.608 |                     48.087 |             1714.695 |               33.332 |                        0.962 |
|    31 |        326.01 |          326.01 |         9 |            311.290 |                      9.016 |              320.307 |               34.588 |                        1.002 |
|    32 |       2888.66 |         2888.66 |        52 |           2622.108 |                     53.267 |             2675.375 |               50.425 |                        1.024 |
|    33 |       2184.63 |         2184.63 |        51 |           2103.589 |                     49.362 |             2152.951 |               41.247 |                        0.968 |
|    34 |       1379.64 |         1379.64 |        33 |           1327.825 |                     31.114 |             1358.939 |               40.237 |                        0.943 |
|    35 |       2323.87 |         2323.87 |        50 |           2241.150 |                     49.744 |             2290.893 |               44.823 |                        0.995 |
|    36 |        933.78 |          933.78 |        21 |            900.453 |                     20.189 |              920.641 |               42.879 |                        0.961 |
|    37 |       2382.96 |         2382.96 |        50 |           2304.303 |                     47.123 |             2351.425 |               46.086 |                        0.942 |
|    38 |       1387.24 |         1387.24 |        38 |           1320.550 |                     42.355 |             1362.905 |               34.751 |                        1.115 |
|    39 |       1033.78 |         1033.78 |        23 |            996.642 |                     22.353 |             1018.996 |               43.332 |                        0.972 |
|    40 |       1222.58 |         1222.58 |        28 |           1175.311 |                     29.454 |             1204.765 |               41.975 |                        1.052 |
|    41 |       1824.91 |         1824.91 |        39 |           1754.512 |                     45.671 |             1800.183 |               44.987 |                        1.171 |
|    42 |        317.65 |          317.65 |         8 |            306.172 |                      7.041 |              313.213 |               38.271 |                        0.880 |
|    43 |        230.85 |          230.85 |         9 |            216.233 |                      8.712 |              224.945 |               24.026 |                        0.968 |
|    44 |       2145.99 |         2145.99 |        50 |           2067.996 |                     46.722 |             2114.718 |               41.360 |                        0.934 |
|    45 |       1967.40 |         1967.40 |        50 |           1880.530 |                     53.251 |             1933.782 |               37.611 |                        1.065 |
|    46 |       1721.35 |         1721.35 |        40 |           1656.100 |                     41.099 |             1697.198 |               41.402 |                        1.027 |
|    47 |        468.62 |          468.62 |         8 |            456.955 |                      7.110 |              464.065 |               57.119 |                        0.889 |
|    48 |       1180.04 |         1180.04 |        24 |           1142.717 |                     22.672 |             1165.389 |               47.613 |                        0.945 |
|    49 |       1069.48 |         1069.48 |        21 |           1039.181 |                     16.923 |             1056.104 |               49.485 |                        0.806 |
|    50 |       1481.35 |         1481.35 |        39 |           1412.453 |                     44.545 |             1456.999 |               36.217 |                        1.142 |
```

## Reconnect details

No Jetson disconnects were recorded.
