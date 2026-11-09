# Y topology auto-trial report

## Summary

- Batch: `temperature-0`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0
- Completed trials: 50/50
- Average time: 1266.01 seconds
- Average total messages: 25.46
- Average Gemma 4 thinking time per response: 46.344 seconds
- Average visible-response generation time: 1.069 seconds
- Average complete generation time: 47.414 seconds
- Success rate: 24/50 (48.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     244 |           244 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     263 |           263 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      58 |           237 |        24.5% (0.245) |                0.333 | 0.734 |                0.245 |
| y        | Agent3 | Agent2    |                  3 |      54 |           237 |        22.8% (0.228) |                0.333 | 0.684 |                0.229 |
| y        | Agent3 | Agent4    |                  3 |     125 |           237 |        52.7% (0.527) |                0.333 | 1.582 |                0.526 |
| y        | Agent4 | Agent3    |                  2 |     197 |           250 |        78.8% (0.788) |                0.500 | 1.576 |                0.787 |
| y        | Agent4 | Agent5    |                  2 |      53 |           250 |        21.2% (0.212) |                0.500 | 0.424 |                0.213 |
| y        | Agent5 | Agent4    |                  1 |     278 |           278 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source  | Count |
| -------- | ------ | -------------- | ----- |
| y        | Agent1 | client_default |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Success | cross                                       | cross          |             12 |         547.95 |           0 |             0.00 |
|     2 |           0 | Fail    | asterisk                                    | circle         |             11 |         551.43 |           0 |             0.00 |
|     3 |           0 | Fail    | cross                                       | square         |             30 |        1367.62 |           0 |             0.00 |
|     4 |           0 | Success | asterisk                                    | asterisk       |             27 |        1367.73 |           0 |             0.00 |
|     5 |           0 | Success | triangle                                    | triangle       |             11 |         594.41 |           0 |             0.00 |
|     6 |           0 | Fail    | circle                                      | cross          |             33 |        2679.13 |           0 |             0.00 |
|     7 |           0 | Fail    | triangle                                    | cross          |             28 |        1061.38 |           0 |             0.00 |
|     8 |           0 | Fail    | cross                                       | square         |             26 |        1394.06 |           0 |             0.00 |
|     9 |           0 | Fail    | asterisk                                    | diamond        |             18 |         956.54 |           0 |             0.00 |
|    10 |           0 | Success | asterisk                                    | asterisk       |             39 |        1873.96 |           0 |             0.00 |
|    11 |           0 | Success | asterisk                                    | asterisk       |              8 |         448.36 |           0 |             0.00 |
|    12 |           0 | Fail    | circle                                      | diamond        |             35 |        2083.23 |           0 |             0.00 |
|    13 |           0 | Fail    | circle                                      | diamond        |             11 |         699.33 |           0 |             0.00 |
|    14 |           0 | Success | cross                                       | cross          |              8 |         288.69 |           0 |             0.00 |
|    15 |           0 | Success | triangle                                    | triangle       |             24 |        1075.47 |           0 |             0.00 |
|    16 |           0 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2289.80 |           0 |             0.00 |
|    17 |           0 | Fail    | cross                                       | square         |             16 |         842.22 |           0 |             0.00 |
|    18 |           0 | Success | circle                                      | circle         |             22 |        1273.13 |           0 |             0.00 |
|    19 |           0 | Success | diamond                                     | diamond        |             26 |        1576.33 |           0 |             0.00 |
|    20 |           0 | Fail    | square                                      | triangle       |             22 |         934.10 |           0 |             0.00 |
|    21 |           0 | Success | diamond                                     | diamond        |             25 |         993.52 |           0 |             0.00 |
|    22 |           0 | Success | asterisk                                    | asterisk       |              9 |         513.94 |           0 |             0.00 |
|    23 |           0 | Fail    | cross                                       | diamond        |             44 |        1736.93 |           0 |             0.00 |
|    24 |           0 | Success | triangle                                    | triangle       |             22 |        1053.23 |           0 |             0.00 |
|    25 |           0 | Fail    | diamond                                     | triangle       |             24 |         944.52 |           0 |             0.00 |
|    26 |           0 | Success | asterisk                                    | asterisk       |             18 |        1002.88 |           0 |             0.00 |
|    27 |           0 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2736.30 |           0 |             0.00 |
|    28 |           0 | Fail    | square                                      | cross          |             31 |        1581.12 |           0 |             0.00 |
|    29 |           0 | Success | diamond                                     | diamond        |             13 |         707.72 |           0 |             0.00 |
|    30 |           0 | Success | cross                                       | cross          |             47 |        2301.36 |           0 |             0.00 |
|    31 |           0 | Success | triangle                                    | triangle       |             48 |        2692.59 |           0 |             0.00 |
|    32 |           0 | Success | circle                                      | circle         |              7 |         383.00 |           0 |             0.00 |
|    33 |           0 | Fail    | diamond                                     | triangle       |             13 |         517.05 |           0 |             0.00 |
|    34 |           0 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2643.94 |           0 |             0.00 |
|    35 |           0 | Fail    | square                                      | circle         |             15 |         866.37 |           0 |             0.00 |
|    36 |           0 | Success | circle                                      | circle         |              7 |         354.51 |           0 |             0.00 |
|    37 |           0 | Fail    | diamond                                     | triangle       |              9 |         377.74 |           0 |             0.00 |
|    38 |           0 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2246.97 |           0 |             0.00 |
|    39 |           0 | Fail    | cross                                       | triangle       |             48 |        2432.80 |           0 |             0.00 |
|    40 |           0 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2234.60 |           0 |             0.00 |
|    41 |           0 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2265.93 |           0 |             0.00 |
|    42 |           0 | Success | square                                      | square         |             18 |         823.20 |           0 |             0.00 |
|    43 |           0 | Fail    | triangle                                    | asterisk       |             13 |         739.24 |           0 |             0.00 |
|    44 |           0 | Success | asterisk                                    | asterisk       |             17 |         648.15 |           0 |             0.00 |
|    45 |           0 | Fail    | diamond                                     | circle         |              9 |         256.07 |           0 |             0.00 |
|    46 |           0 | Success | asterisk                                    | asterisk       |             43 |        1886.99 |           0 |             0.00 |
|    47 |           0 | Success | circle                                      | circle         |             12 |         388.01 |           0 |             0.00 |
|    48 |           0 | Fail    | square                                      | cross          |             17 |         752.97 |           0 |             0.00 |
|    49 |           0 | Success | circle                                      | circle         |             35 |        2093.79 |           0 |             0.00 |
|    50 |           0 | Success | square                                      | square         |             22 |        1220.23 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |        567.33 |          567.33 |        14 |            546.888 |                     12.155 |              559.043 |               39.063 |                        0.868 |
|     2 |        566.36 |          566.36 |        12 |            547.109 |                     12.194 |              559.303 |               45.592 |                        1.016 |
|     3 |       1383.49 |         1383.49 |        32 |           1331.979 |                     31.719 |             1363.698 |               41.624 |                        0.991 |
|     4 |       1383.66 |         1383.66 |        28 |           1339.426 |                     27.007 |             1366.433 |               47.837 |                        0.965 |
|     5 |        616.14 |          616.14 |        12 |            597.412 |                     11.651 |              609.063 |               49.784 |                        0.971 |
|     6 |       2753.06 |         2753.06 |        40 |           2510.098 |                     37.636 |             2547.734 |               62.752 |                        0.941 |
|     7 |       1080.01 |         1080.01 |        29 |           1028.424 |                     33.242 |             1061.666 |               35.463 |                        1.146 |
|     8 |       1409.12 |         1409.12 |        29 |           1363.799 |                     28.121 |             1391.920 |               47.028 |                        0.970 |
|     9 |       1033.33 |         1033.33 |        19 |           1003.401 |                     18.789 |             1022.190 |               52.811 |                        0.989 |
|    10 |       1979.97 |         1979.97 |        40 |           1907.774 |                     47.910 |             1955.683 |               47.694 |                        1.198 |
|    11 |        462.25 |          462.25 |         9 |            448.267 |                      8.497 |              456.763 |               49.807 |                        0.944 |
|    12 |       2160.56 |         2160.56 |        36 |           2100.133 |                     38.600 |             2138.733 |               58.337 |                        1.072 |
|    13 |        714.20 |          714.20 |        13 |            693.476 |                     12.641 |              706.117 |               53.344 |                        0.972 |
|    14 |        301.96 |          301.96 |         9 |            288.747 |                      7.619 |              296.367 |               32.083 |                        0.847 |
|    15 |       1091.35 |         1091.35 |        26 |           1049.433 |                     24.365 |             1073.798 |               40.363 |                        0.937 |
|    16 |       2302.90 |         2302.90 |        50 |           2211.469 |                     58.289 |             2269.759 |               44.229 |                        1.166 |
|    17 |        859.06 |          859.06 |        18 |            830.310 |                     17.135 |              847.445 |               46.128 |                        0.952 |
|    18 |       1292.47 |         1292.47 |        23 |           1253.309 |                     25.237 |             1278.546 |               54.492 |                        1.097 |
|    19 |       1592.41 |         1592.41 |        28 |           1544.060 |                     30.773 |             1574.832 |               55.145 |                        1.099 |
|    20 |        950.08 |          950.08 |        23 |            913.708 |                     22.503 |              936.211 |               39.726 |                        0.978 |
|    21 |       1010.69 |         1010.69 |        26 |            968.995 |                     25.332 |              994.327 |               37.269 |                        0.974 |
|    22 |        530.64 |          530.64 |        10 |            514.165 |                      9.777 |              523.942 |               51.416 |                        0.978 |
|    23 |       1752.44 |         1752.44 |        45 |           1670.776 |                     53.223 |             1724.000 |               37.128 |                        1.183 |
|    24 |       1068.73 |         1068.73 |        24 |           1029.217 |                     25.093 |             1054.311 |               42.884 |                        1.046 |
|    25 |       1019.55 |         1019.55 |        25 |            975.958 |                     26.979 |             1002.937 |               39.038 |                        1.079 |
|    26 |       1017.72 |         1017.72 |        21 |            983.860 |                     21.021 |             1004.881 |               46.850 |                        1.001 |
|    27 |       2755.96 |         2755.96 |        50 |           2668.288 |                     56.328 |             2724.616 |               53.366 |                        1.127 |
|    28 |       1596.09 |         1596.09 |        33 |           1541.834 |                     33.215 |             1575.049 |               46.722 |                        1.007 |
|    29 |        782.29 |          782.29 |        14 |            759.288 |                     14.201 |              773.489 |               54.235 |                        1.014 |
|    30 |       2318.76 |         2318.76 |        48 |           2231.213 |                     56.843 |             2288.056 |               46.484 |                        1.184 |
|    31 |       2765.79 |         2765.79 |        49 |           2495.986 |                     59.277 |             2555.264 |               50.938 |                        1.210 |
|    32 |        456.85 |          456.85 |         8 |            444.568 |                      6.940 |              451.508 |               55.571 |                        0.867 |
|    33 |        536.77 |          536.77 |        14 |            514.899 |                     12.999 |              527.898 |               36.778 |                        0.929 |
|    34 |       2658.27 |         2658.27 |        50 |           2566.668 |                     60.334 |             2627.002 |               51.333 |                        1.207 |
|    35 |        945.14 |          945.14 |        17 |            920.556 |                     14.026 |              934.583 |               54.150 |                        0.825 |
|    36 |        430.49 |          430.49 |         8 |            418.366 |                      7.035 |              425.401 |               52.296 |                        0.879 |
|    37 |        392.30 |          392.30 |        10 |            376.295 |                      9.505 |              385.800 |               37.629 |                        0.951 |
|    38 |       2266.75 |         2266.75 |        52 |           2172.248 |                     62.356 |             2234.605 |               41.774 |                        1.199 |
|    39 |       2506.65 |         2506.65 |        50 |           2420.274 |                     54.712 |             2474.986 |               48.405 |                        1.094 |
|    40 |       2305.09 |         2305.09 |        51 |           2215.022 |                     57.749 |             2272.771 |               43.432 |                        1.132 |
|    41 |       2280.47 |         2280.47 |        51 |           2191.700 |                     56.952 |             2248.652 |               42.975 |                        1.117 |
|    42 |        839.37 |          839.37 |        19 |            807.324 |                     20.245 |              827.569 |               42.491 |                        1.066 |
|    43 |        755.09 |          755.09 |        14 |            730.002 |                     16.631 |              746.633 |               52.143 |                        1.188 |
|    44 |        724.63 |          724.63 |        18 |            694.384 |                     18.901 |              713.285 |               38.577 |                        1.050 |
|    45 |        277.63 |          277.63 |        10 |            262.231 |                      9.144 |              271.375 |               26.223 |                        0.914 |
|    46 |       1902.84 |         1902.84 |        44 |           1825.477 |                     50.466 |             1875.943 |               41.488 |                        1.147 |
|    47 |        406.65 |          406.65 |        13 |            386.622 |                     11.952 |              398.574 |               29.740 |                        0.919 |
|    48 |        772.05 |          772.05 |        18 |            740.426 |                     19.814 |              760.240 |               41.135 |                        1.101 |
|    49 |       2107.58 |         2107.58 |        38 |           2048.986 |                     35.928 |             2084.914 |               53.921 |                        0.945 |
|    50 |       1241.10 |         1241.10 |        24 |           1202.108 |                     23.931 |             1226.039 |               50.088 |                        0.997 |
```

## Reconnect details

No Jetson disconnects were recorded.
