# Wheel auto-trial report

## Summary

- Batch: `temperature-0.2`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 1710.46 seconds
- Average total messages: 37.46
- Average Gemma 4 thinking time per response: 43.417 seconds
- Average visible-response generation time: 1.008 seconds
- Average complete generation time: 44.425 seconds
- Success rate: 17/50 (34.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     396 |           396 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     373 |           373 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     103 |           352 |        29.3% (0.293) |                0.250 | 1.170 |                0.292 |
| wheel    | Agent3 | Agent2    |                  4 |     109 |           352 |        31.0% (0.310) |                0.250 | 1.239 |                0.309 |
| wheel    | Agent3 | Agent4    |                  4 |      91 |           352 |        25.9% (0.259) |                0.250 | 1.034 |                0.258 |
| wheel    | Agent3 | Agent5    |                  4 |      49 |           352 |        13.9% (0.139) |                0.250 | 0.557 |                0.140 |
| wheel    | Agent4 | Agent3    |                  1 |     359 |           359 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     393 |           393 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.2 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        1915.02 |           0 |             0.00 |
|     2 |         0.2 | Success | circle                                      | circle         |              7 |         287.42 |           0 |             0.00 |
|     3 |         0.2 | Success | circle                                      | circle         |             49 |        1852.89 |           0 |             0.00 |
|     4 |         0.2 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2358.15 |           0 |             0.00 |
|     5 |         0.2 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2384.74 |           0 |             0.00 |
|     6 |         0.2 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        1801.61 |           0 |             0.00 |
|     7 |         0.2 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        1821.99 |           0 |             0.00 |
|     8 |         0.2 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2087.98 |           0 |             0.00 |
|     9 |         0.2 | Fail    | triangle                                    | asterisk       |             13 |         574.33 |           0 |             0.00 |
|    10 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2691.97 |           0 |             0.00 |
|    11 |         0.2 | Fail    | circle                                      | square         |             47 |        2887.75 |           0 |             0.00 |
|    12 |         0.2 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2340.31 |           0 |             0.00 |
|    13 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             50 |        1853.87 |           0 |             0.00 |
|    14 |         0.2 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2303.74 |           0 |             0.00 |
|    15 |         0.2 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2857.59 |           0 |             0.00 |
|    16 |         0.2 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2928.65 |           0 |             0.00 |
|    17 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2423.20 |           0 |             0.00 |
|    18 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2166.41 |           0 |             0.00 |
|    19 |         0.2 | Success | triangle                                    | triangle       |             40 |        2227.55 |           0 |             0.00 |
|    20 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2428.48 |           0 |             0.00 |
|    21 |         0.2 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2439.30 |           0 |             0.00 |
|    22 |         0.2 | Fail    | circle                                      | triangle       |             37 |        2026.00 |           0 |             0.00 |
|    23 |         0.2 | Success | circle                                      | circle         |             15 |         598.87 |           0 |             0.00 |
|    24 |         0.2 | Success | circle                                      | circle         |             46 |        1786.69 |           0 |             0.00 |
|    25 |         0.2 | Success | square                                      | square         |             42 |        1801.21 |           0 |             0.00 |
|    26 |         0.2 | Success | circle                                      | circle         |             10 |         259.47 |           0 |             0.00 |
|    27 |         0.2 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        1898.99 |           0 |             0.00 |
|    28 |         0.2 | Fail    | asterisk                                    | square         |              9 |         461.09 |           0 |             0.00 |
|    29 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             50 |        1867.95 |           0 |             0.00 |
|    30 |         0.2 | Success | triangle                                    | triangle       |             38 |        2078.18 |           0 |             0.00 |
|    31 |         0.2 | Success | circle                                      | circle         |             34 |        1283.52 |           0 |             0.00 |
|    32 |         0.2 | Fail    | asterisk                                    | square         |             19 |        1032.39 |           0 |             0.00 |
|    33 |         0.2 | Success | square                                      | square         |             18 |         827.49 |           0 |             0.00 |
|    34 |         0.2 | Success | cross                                       | cross          |             12 |         500.83 |           0 |             0.00 |
|    35 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2841.26 |           0 |             0.00 |
|    36 |         0.2 | Fail    | circle                                      | diamond        |             22 |         843.22 |           0 |             0.00 |
|    37 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             50 |        1830.21 |           0 |             0.00 |
|    38 |         0.2 | Fail    | square                                      | asterisk       |             20 |         676.32 |           0 |             0.00 |
|    39 |         0.2 | Success | triangle                                    | triangle       |             15 |         745.67 |           0 |             0.00 |
|    40 |         0.2 | Success | diamond                                     | diamond        |             15 |         567.92 |           0 |             0.00 |
|    41 |         0.2 | Success | cross                                       | cross          |             43 |        1985.63 |           0 |             0.00 |
|    42 |         0.2 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        1864.88 |           0 |             0.00 |
|    43 |         0.2 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2151.86 |           0 |             0.00 |
|    44 |         0.2 | Success | square                                      | square         |              7 |         427.19 |           0 |             0.00 |
|    45 |         0.2 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2162.31 |           0 |             0.00 |
|    46 |         0.2 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2493.29 |           0 |             0.00 |
|    47 |         0.2 | Success | triangle                                    | triangle       |             24 |        1135.38 |           0 |             0.00 |
|    48 |         0.2 | Success | square                                      | square         |             22 |        1338.35 |           0 |             0.00 |
|    49 |         0.2 | Fail    | cross                                       | circle         |             19 |         978.34 |           0 |             0.00 |
|    50 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2425.41 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |       1930.44 |         1930.44 |        51 |           1850.485 |                     48.603 |             1899.089 |               36.284 |                        0.953 |
|     2 |        304.25 |          304.25 |         8 |            291.033 |                      7.640 |              298.672 |               36.379 |                        0.955 |
|     3 |       1871.80 |         1871.80 |        51 |           1786.640 |                     53.647 |             1840.287 |               35.032 |                        1.052 |
|     4 |       2379.15 |         2379.15 |        51 |           2300.181 |                     46.959 |             2347.141 |               45.102 |                        0.921 |
|     5 |       2400.87 |         2400.87 |        50 |           2144.028 |                     45.963 |             2189.991 |               42.881 |                        0.919 |
|     6 |       1820.84 |         1820.84 |        50 |           1739.175 |                     49.254 |             1788.430 |               34.784 |                        0.985 |
|     7 |       1838.75 |         1838.75 |        50 |           1754.632 |                     52.583 |             1807.215 |               35.093 |                        1.052 |
|     8 |       2108.16 |         2108.16 |        50 |           2023.799 |                     51.705 |             2075.505 |               40.476 |                        1.034 |
|     9 |        592.71 |          592.71 |        14 |            571.892 |                     12.229 |              584.122 |               40.849 |                        0.874 |
|    10 |       2705.35 |         2705.35 |        50 |           2617.519 |                     54.782 |             2672.301 |               52.350 |                        1.096 |
|    11 |       2965.29 |         2965.29 |        50 |           2709.366 |                     45.575 |             2754.941 |               54.187 |                        0.911 |
|    12 |       2415.55 |         2415.55 |        51 |           2336.322 |                     47.210 |             2383.532 |               45.810 |                        0.926 |
|    13 |       1876.73 |         1876.73 |        50 |           1798.356 |                     48.421 |             1846.777 |               35.967 |                        0.968 |
|    14 |       2323.79 |         2323.79 |        51 |           2239.126 |                     52.845 |             2291.972 |               43.904 |                        1.036 |
|    15 |       2873.50 |         2873.50 |        51 |           2610.702 |                     51.123 |             2661.824 |               51.190 |                        1.002 |
|    16 |       2944.07 |         2944.07 |        53 |           2859.435 |                     52.098 |             2911.533 |               53.952 |                        0.983 |
|    17 |       2438.69 |         2438.69 |        50 |           2355.224 |                     53.518 |             2408.743 |               47.104 |                        1.070 |
|    18 |       2191.12 |         2191.12 |        52 |           2106.945 |                     50.640 |             2157.585 |               40.518 |                        0.974 |
|    19 |       2246.22 |         2246.22 |        41 |           2178.237 |                     42.262 |             2220.499 |               53.128 |                        1.031 |
|    20 |       2446.09 |         2446.09 |        50 |           2359.871 |                     55.138 |             2415.009 |               47.197 |                        1.103 |
|    21 |       2456.25 |         2456.25 |        51 |           2372.440 |                     50.958 |             2423.397 |               46.518 |                        0.999 |
|    22 |       2103.32 |         2103.32 |        38 |           2038.323 |                     41.507 |             2079.831 |               53.640 |                        1.092 |
|    23 |        677.81 |          677.81 |        16 |            654.373 |                     13.691 |              668.063 |               40.898 |                        0.856 |
|    24 |       1804.74 |         1804.74 |        47 |           1726.153 |                     48.021 |             1774.174 |               36.727 |                        1.022 |
|    25 |       1820.62 |         1820.62 |        43 |           1748.761 |                     44.599 |             1793.359 |               40.669 |                        1.037 |
|    26 |        278.54 |          278.54 |        11 |            262.414 |                      9.675 |              272.089 |               23.856 |                        0.880 |
|    27 |       1914.24 |         1914.24 |        50 |           1828.128 |                     53.426 |             1881.554 |               36.563 |                        1.069 |
|    28 |        478.77 |          478.77 |        10 |            463.371 |                      9.141 |              472.513 |               46.337 |                        0.914 |
|    29 |       1885.47 |         1885.47 |        50 |           1802.913 |                     49.983 |             1852.896 |               36.058 |                        1.000 |
|    30 |       2095.12 |         2095.12 |        39 |           2026.685 |                     42.850 |             2069.535 |               51.966 |                        1.099 |
|    31 |       1301.26 |         1301.26 |        35 |           1237.864 |                     40.104 |             1277.968 |               35.368 |                        1.146 |
|    32 |       1050.61 |         1050.61 |        21 |           1017.604 |                     20.624 |             1038.228 |               48.457 |                        0.982 |
|    33 |        844.26 |          844.26 |        19 |            814.453 |                     17.841 |              832.294 |               42.866 |                        0.939 |
|    34 |        517.78 |          517.78 |        13 |            497.019 |                     12.497 |              509.516 |               38.232 |                        0.961 |
|    35 |       2858.64 |         2858.64 |        52 |           2776.608 |                     48.391 |             2825.000 |               53.396 |                        0.931 |
|    36 |        862.18 |          862.18 |        23 |            826.834 |                     21.763 |              848.597 |               35.949 |                        0.946 |
|    37 |       1849.35 |         1849.35 |        50 |           1761.180 |                     56.583 |             1817.763 |               35.224 |                        1.132 |
|    38 |        752.12 |          752.12 |        21 |            717.283 |                     22.134 |              739.417 |               34.156 |                        1.054 |
|    39 |        830.35 |          830.35 |        16 |            804.851 |                     14.876 |              819.726 |               50.303 |                        0.930 |
|    40 |        584.51 |          584.51 |        16 |            559.580 |                     14.767 |              574.346 |               34.974 |                        0.923 |
|    41 |       2005.67 |         2005.67 |        45 |           1928.949 |                     44.556 |             1973.506 |               42.866 |                        0.990 |
|    42 |       1937.44 |         1937.44 |        50 |           1851.403 |                     51.546 |             1902.949 |               37.028 |                        1.031 |
|    43 |       2169.28 |         2169.28 |        51 |           2084.298 |                     52.435 |             2136.733 |               40.869 |                        1.028 |
|    44 |        447.09 |          447.09 |         8 |            435.161 |                      7.290 |              442.451 |               54.395 |                        0.911 |
|    45 |       2238.51 |         2238.51 |        50 |           2155.819 |                     50.155 |             2205.974 |               43.116 |                        1.003 |
|    46 |       2512.33 |         2512.33 |        51 |           2433.133 |                     47.328 |             2480.461 |               47.708 |                        0.928 |
|    47 |       1150.78 |         1150.78 |        25 |           1107.929 |                     27.600 |             1135.529 |               44.317 |                        1.104 |
|    48 |       1353.76 |         1353.76 |        23 |           1313.467 |                     25.838 |             1339.305 |               57.107 |                        1.123 |
|    49 |       1050.11 |         1050.11 |        20 |           1016.871 |                     21.178 |             1038.049 |               50.844 |                        1.059 |
|    50 |       2504.53 |         2504.53 |        51 |           2419.526 |                     51.372 |             2470.897 |               47.442 |                        1.007 |
```

## Reconnect details

No Jetson disconnects were recorded.
