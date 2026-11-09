# Y topology auto-trial report

## Summary

- Batch: `temperature-0.05`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0.05
- Completed trials: 50/50
- Average time: 1245.95 seconds
- Average total messages: 25.42
- Average Gemma 4 thinking time per response: 45.986 seconds
- Average visible-response generation time: 1.062 seconds
- Average complete generation time: 47.048 seconds
- Success rate: 24/50 (48.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     269 |           269 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     267 |           267 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      60 |           234 |        25.6% (0.256) |                0.333 | 0.769 |                0.257 |
| y        | Agent3 | Agent2    |                  3 |      62 |           234 |        26.5% (0.265) |                0.333 | 0.795 |                0.265 |
| y        | Agent3 | Agent4    |                  3 |     112 |           234 |        47.9% (0.479) |                0.333 | 1.436 |                0.478 |
| y        | Agent4 | Agent3    |                  2 |     197 |           260 |        75.8% (0.758) |                0.500 | 1.515 |                0.757 |
| y        | Agent4 | Agent5    |                  2 |      63 |           260 |        24.2% (0.242) |                0.500 | 0.485 |                0.243 |
| y        | Agent5 | Agent4    |                  1 |     240 |           240 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent3 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |        0.05 | Success | circle                                      | circle         |             20 |         806.33 |           0 |             0.00 |
|     2 |        0.05 | Fail    | diamond                                     | square         |             11 |         544.37 |           0 |             0.00 |
|     3 |        0.05 | Success | asterisk                                    | asterisk       |             14 |         827.31 |           0 |             0.00 |
|     4 |        0.05 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2818.48 |           0 |             0.00 |
|     5 |        0.05 | Fail    | cross                                       | asterisk       |             10 |         446.46 |           0 |             0.00 |
|     6 |        0.05 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        3106.64 |           0 |             0.00 |
|     7 |        0.05 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2070.11 |           0 |             0.00 |
|     8 |        0.05 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2384.81 |           0 |             0.00 |
|     9 |        0.05 | Success | square                                      | square         |             28 |        1269.10 |           0 |             0.00 |
|    10 |        0.05 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2710.11 |           0 |             0.00 |
|    11 |        0.05 | Fail    | cross                                       | square         |             20 |         949.76 |           0 |             0.00 |
|    12 |        0.05 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2280.50 |           0 |             0.00 |
|    13 |        0.05 | Success | square                                      | square         |             12 |         574.46 |           0 |             0.00 |
|    14 |        0.05 | Fail    | circle                                      | diamond        |             28 |        1199.59 |           0 |             0.00 |
|    15 |        0.05 | Success | circle                                      | circle         |             17 |         812.16 |           0 |             0.00 |
|    16 |        0.05 | Fail    | cross                                       | square         |             17 |        1001.80 |           0 |             0.00 |
|    17 |        0.05 | Success | circle                                      | circle         |             28 |        1282.87 |           0 |             0.00 |
|    18 |        0.05 | Fail    | circle                                      | cross          |             19 |         780.76 |           0 |             0.00 |
|    19 |        0.05 | Success | triangle                                    | triangle       |             10 |         442.20 |           0 |             0.00 |
|    20 |        0.05 | Fail    | circle                                      | triangle       |             33 |        1824.15 |           0 |             0.00 |
|    21 |        0.05 | Fail    | square                                      | asterisk       |             38 |        1807.65 |           0 |             0.00 |
|    22 |        0.05 | Success | triangle                                    | triangle       |              7 |         353.42 |           0 |             0.00 |
|    23 |        0.05 | Success | triangle                                    | triangle       |             43 |        2849.96 |           0 |             0.00 |
|    24 |        0.05 | Success | diamond                                     | diamond        |             37 |        1791.14 |           0 |             0.00 |
|    25 |        0.05 | Fail    | circle                                      | asterisk       |             17 |         849.49 |           0 |             0.00 |
|    26 |        0.05 | Fail    | diamond                                     | cross          |             26 |        1150.87 |           0 |             0.00 |
|    27 |        0.05 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2217.21 |           0 |             0.00 |
|    28 |        0.05 | Success | triangle                                    | triangle       |             15 |         503.66 |           0 |             0.00 |
|    29 |        0.05 | Success | asterisk                                    | asterisk       |             10 |         687.80 |           0 |             0.00 |
|    30 |        0.05 | Success | cross                                       | cross          |             14 |         713.87 |           0 |             0.00 |
|    31 |        0.05 | Fail    | square                                      | cross          |             15 |         725.95 |           0 |             0.00 |
|    32 |        0.05 | Fail    | asterisk                                    | diamond        |             28 |        1264.78 |           0 |             0.00 |
|    33 |        0.05 | Success | square                                      | square         |             23 |        1084.29 |           0 |             0.00 |
|    34 |        0.05 | Success | square                                      | square         |             42 |        2261.55 |           0 |             0.00 |
|    35 |        0.05 | Success | diamond                                     | diamond        |             26 |        1308.91 |           0 |             0.00 |
|    36 |        0.05 | Success | triangle                                    | triangle       |             28 |        1165.97 |           0 |             0.00 |
|    37 |        0.05 | Success | circle                                      | circle         |             16 |         721.52 |           0 |             0.00 |
|    38 |        0.05 | Fail    | cross                                       | diamond        |             11 |         510.91 |           0 |             0.00 |
|    39 |        0.05 | Fail    | triangle                                    | asterisk       |             22 |        1029.44 |           0 |             0.00 |
|    40 |        0.05 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2512.71 |           0 |             0.00 |
|    41 |        0.05 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2097.62 |           0 |             0.00 |
|    42 |        0.05 | Success | asterisk                                    | asterisk       |             18 |         800.82 |           0 |             0.00 |
|    43 |        0.05 | Fail    | diamond                                     | asterisk       |             18 |         919.63 |           0 |             0.00 |
|    44 |        0.05 | Success | square                                      | square         |              8 |         432.95 |           0 |             0.00 |
|    45 |        0.05 | Success | triangle                                    | triangle       |             18 |         967.79 |           0 |             0.00 |
|    46 |        0.05 | Success | cross                                       | cross          |             39 |        1811.38 |           0 |             0.00 |
|    47 |        0.05 | Fail    | square                                      | diamond        |             12 |         494.05 |           0 |             0.00 |
|    48 |        0.05 | Success | diamond                                     | diamond        |              7 |         593.32 |           0 |             0.00 |
|    49 |        0.05 | Fail    | triangle                                    | diamond        |             10 |         390.76 |           0 |             0.00 |
|    50 |        0.05 | Success | square                                      | square         |              6 |         146.04 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |        830.04 |          830.04 |        21 |            794.527 |                     23.200 |              817.727 |               37.835 |                        1.105 |
|     2 |        560.97 |          560.97 |        12 |            541.833 |                     11.958 |              553.791 |               45.153 |                        0.997 |
|     3 |        843.13 |          843.13 |        16 |            819.397 |                     13.901 |              833.298 |               51.212 |                        0.869 |
|     4 |       2893.56 |         2893.56 |        52 |           2806.713 |                     53.407 |             2860.120 |               53.975 |                        1.027 |
|     5 |        524.63 |          524.63 |        11 |            507.103 |                     11.303 |              518.406 |               46.100 |                        1.028 |
|     6 |       3121.22 |         3121.22 |        51 |           3027.001 |                     62.177 |             3089.178 |               59.353 |                        1.219 |
|     7 |       2085.32 |         2085.32 |        50 |           2001.248 |                     52.961 |             2054.209 |               40.025 |                        1.059 |
|     8 |       2403.07 |         2403.07 |        50 |           2315.253 |                     56.913 |             2372.166 |               46.305 |                        1.138 |
|     9 |       1351.40 |         1351.40 |        29 |           1301.337 |                     32.459 |             1333.797 |               44.874 |                        1.119 |
|    10 |       2724.75 |         2724.75 |        52 |           2450.874 |                     60.370 |             2511.245 |               47.132 |                        1.161 |
|    11 |        965.13 |          965.13 |        21 |            928.364 |                     22.018 |              950.382 |               44.208 |                        1.048 |
|    12 |       2298.71 |         2298.71 |        51 |           2218.637 |                     47.325 |             2265.962 |               43.503 |                        0.928 |
|    13 |        590.16 |          590.16 |        13 |            568.689 |                     13.227 |              581.916 |               43.745 |                        1.017 |
|    14 |       1216.42 |         1216.42 |        29 |           1161.784 |                     36.149 |             1197.933 |               40.062 |                        1.247 |
|    15 |        889.65 |          889.65 |        18 |            859.594 |                     18.956 |              878.550 |               47.755 |                        1.053 |
|    16 |       1075.60 |         1075.60 |        19 |           1046.633 |                     17.788 |             1064.422 |               55.086 |                        0.936 |
|    17 |       1298.35 |         1298.35 |        29 |           1248.077 |                     32.969 |             1281.046 |               43.037 |                        1.137 |
|    18 |        795.34 |          795.34 |        20 |            757.398 |                     24.992 |              782.390 |               37.870 |                        1.250 |
|    19 |        457.73 |          457.73 |        11 |            441.293 |                      9.587 |              450.880 |               40.118 |                        0.872 |
|    20 |       1839.75 |         1839.75 |        35 |           1777.824 |                     39.045 |             1816.868 |               50.795 |                        1.116 |
|    21 |       1823.74 |         1823.74 |        39 |           1750.100 |                     49.237 |             1799.337 |               44.874 |                        1.262 |
|    22 |        373.75 |          373.75 |         8 |            361.341 |                      7.759 |              369.101 |               45.168 |                        0.970 |
|    23 |       2862.97 |         2862.97 |        48 |           2788.487 |                     44.908 |             2833.395 |               58.093 |                        0.936 |
|    24 |       1811.27 |         1811.27 |        38 |           1749.684 |                     38.668 |             1788.352 |               46.044 |                        1.018 |
|    25 |        925.00 |          925.00 |        19 |            892.121 |                     20.116 |              912.237 |               46.954 |                        1.059 |
|    26 |       1167.92 |         1167.92 |        27 |           1119.738 |                     31.834 |             1151.572 |               41.472 |                        1.179 |
|    27 |       2296.97 |         2296.97 |        51 |           2207.459 |                     56.794 |             2264.254 |               43.284 |                        1.114 |
|    28 |        523.03 |          523.03 |        16 |            496.421 |                     16.733 |              513.154 |               31.026 |                        1.046 |
|    29 |        704.58 |          704.58 |        12 |            687.319 |                     10.793 |              698.111 |               57.277 |                        0.899 |
|    30 |        733.42 |          733.42 |        15 |            705.811 |                     17.745 |              723.556 |               47.054 |                        1.183 |
|    31 |        745.36 |          745.36 |        16 |            721.505 |                     14.169 |              735.674 |               45.094 |                        0.886 |
|    32 |       1346.00 |         1346.00 |        30 |           1298.548 |                     27.982 |             1326.530 |               43.285 |                        0.933 |
|    33 |       1160.50 |         1160.50 |        24 |           1122.528 |                     22.962 |             1145.490 |               46.772 |                        0.957 |
|    34 |       2277.04 |         2277.04 |        44 |           2204.430 |                     44.505 |             2248.935 |               50.101 |                        1.011 |
|    35 |       1325.62 |         1325.62 |        28 |           1281.767 |                     25.831 |             1307.598 |               45.777 |                        0.923 |
|    36 |       1180.81 |         1180.81 |        29 |           1129.053 |                     32.819 |             1161.872 |               38.933 |                        1.132 |
|    37 |        735.60 |          735.60 |        17 |            708.009 |                     17.067 |              725.076 |               41.648 |                        1.004 |
|    38 |        526.33 |          526.33 |        13 |            506.088 |                     12.300 |              518.388 |               38.930 |                        0.946 |
|    39 |       1051.82 |         1051.82 |        23 |           1012.189 |                     24.842 |             1037.031 |               44.008 |                        1.080 |
|    40 |       2525.59 |         2525.59 |        51 |           2446.175 |                     48.304 |             2494.480 |               47.964 |                        0.947 |
|    41 |       2112.71 |         2112.71 |        50 |           2027.681 |                     55.554 |             2083.235 |               40.554 |                        1.111 |
|    42 |        818.11 |          818.11 |        19 |            787.064 |                     19.730 |              806.793 |               41.424 |                        1.038 |
|    43 |        991.01 |          991.01 |        19 |            775.924 |                     22.441 |              798.364 |               40.838 |                        1.181 |
|    44 |        505.09 |          505.09 |         9 |            489.427 |                      9.935 |              499.362 |               54.381 |                        1.104 |
|    45 |        988.76 |          988.76 |        19 |            956.110 |                     21.163 |              977.273 |               50.322 |                        1.114 |
|    46 |       1824.54 |         1824.54 |        40 |           1758.826 |                     40.036 |             1798.863 |               43.971 |                        1.001 |
|    47 |        570.06 |          570.06 |        13 |            547.889 |                     13.237 |              561.126 |               42.145 |                        1.018 |
|    48 |        608.71 |          608.71 |         8 |            596.244 |                      7.797 |              604.042 |               74.531 |                        0.975 |
|    49 |        466.55 |          466.55 |        11 |            446.584 |                     13.268 |              459.852 |               40.599 |                        1.206 |
|    50 |        161.89 |          161.89 |         7 |            150.721 |                      6.657 |              157.379 |               21.532 |                        0.951 |
```

## Reconnect details

No Jetson disconnects were recorded.
