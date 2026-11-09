# Circle auto-trial report

## Summary

- Batch: `temperature-0.2`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0.2
- Completed trials: 50/50
- Average time: 794.79 seconds
- Average total messages: 17.58
- Average Gemma 4 thinking time per response: 41.746 seconds
- Average visible-response generation time: 1.039 seconds
- Average complete generation time: 42.785 seconds
- Success rate: 20/50 (40.0%)
- Reconnect pauses: 1 across 1 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      89 |           180 |        49.4% (0.494) |                0.500 | 0.989 |                0.494 |
| circle   | Agent1 | Agent5    |                  2 |      91 |           180 |        50.6% (0.506) |                0.500 | 1.011 |                0.506 |
| circle   | Agent2 | Agent1    |                  2 |      92 |           169 |        54.4% (0.544) |                0.500 | 1.089 |                0.544 |
| circle   | Agent2 | Agent3    |                  2 |      77 |           169 |        45.6% (0.456) |                0.500 | 0.911 |                0.456 |
| circle   | Agent3 | Agent2    |                  2 |      94 |           161 |        58.4% (0.584) |                0.500 | 1.168 |                0.583 |
| circle   | Agent3 | Agent4    |                  2 |      67 |           161 |        41.6% (0.416) |                0.500 | 0.832 |                0.417 |
| circle   | Agent4 | Agent3    |                  2 |     100 |           200 |        50.0% (0.500) |                0.500 | 1.000 |                0.500 |
| circle   | Agent4 | Agent5    |                  2 |     100 |           200 |        50.0% (0.500) |                0.500 | 1.000 |                0.500 |
| circle   | Agent5 | Agent1    |                  2 |      76 |           169 |        45.0% (0.450) |                0.500 | 0.899 |                0.450 |
| circle   | Agent5 | Agent4    |                  2 |      93 |           169 |        55.0% (0.550) |                0.500 | 1.101 |                0.550 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.2 | Fail    | square                                      | asterisk       |              8 |         215.16 |           0 |             0.00 |
|     2 |         0.2 | Fail    | triangle                                    | asterisk       |             17 |         733.28 |           0 |             0.00 |
|     3 |         0.2 | Success | cross                                       | cross          |             10 |         495.06 |           0 |             0.00 |
|     4 |         0.2 | Fail    | cross                                       | triangle       |             13 |         610.04 |           0 |             0.00 |
|     5 |         0.2 | Success | cross                                       | cross          |             23 |        1144.84 |           0 |             0.00 |
|     6 |         0.2 | Fail    | diamond                                     | circle         |             26 |        1265.35 |           0 |             0.00 |
|     7 |         0.2 | Fail    | square                                      | triangle       |             15 |         728.35 |           0 |             0.00 |
|     8 |         0.2 | Fail    | cross                                       | triangle       |             16 |         651.96 |           0 |             0.00 |
|     9 |         0.2 | Fail    | triangle                                    | asterisk       |             14 |         674.43 |           0 |             0.00 |
|    10 |         0.2 | Fail    | No figure submitted (message limit reached) | asterisk       |             40 |        1546.23 |           0 |             0.00 |
|    11 |         0.2 | Fail    | asterisk                                    | diamond        |             16 |         893.21 |           0 |             0.00 |
|    12 |         0.2 | Fail    | triangle                                    | circle         |              4 |         138.27 |           0 |             0.00 |
|    13 |         0.2 | Success | diamond                                     | diamond        |             19 |         898.59 |           0 |             0.00 |
|    14 |         0.2 | Fail    | asterisk                                    | diamond        |             20 |         826.16 |           0 |             0.00 |
|    15 |         0.2 | Fail    | cross                                       | diamond        |             10 |         325.53 |           0 |             0.00 |
|    16 |         0.2 | Fail    | square                                      | triangle       |             13 |         654.17 |           0 |             0.00 |
|    17 |         0.2 | Fail    | circle                                      | asterisk       |             15 |         717.12 |           0 |             0.00 |
|    18 |         0.2 | Fail    | triangle                                    | cross          |             16 |         713.34 |           0 |             0.00 |
|    19 |         0.2 | Success | diamond                                     | diamond        |             11 |         475.72 |           0 |             0.00 |
|    20 |         0.2 | Success | circle                                      | circle         |             21 |        1185.99 |           0 |             0.00 |
|    21 |         0.2 | Success | triangle                                    | triangle       |              8 |         397.95 |           0 |             0.00 |
|    22 |         0.2 | Success | circle                                      | circle         |             15 |         499.08 |           0 |             0.00 |
|    23 |         0.2 | Success | cross                                       | cross          |              9 |         324.08 |           0 |             0.00 |
|    24 |         0.2 | Fail    | cross                                       | square         |             23 |         899.44 |           0 |             0.00 |
|    25 |         0.2 | Success | circle                                      | circle         |             15 |         563.25 |           0 |             0.00 |
|    26 |         0.2 | Fail    | No figure submitted (message limit reached) | asterisk       |             40 |        1427.62 |           0 |             0.00 |
|    27 |         0.2 | Fail    | triangle                                    | diamond        |             11 |         350.78 |           0 |             0.00 |
|    28 |         0.2 | Fail    | diamond                                     | square         |              4 |          89.27 |           0 |             0.00 |
|    29 |         0.2 | Fail    | cross                                       | asterisk       |             22 |        1081.10 |           0 |             0.00 |
|    30 |         0.2 | Success | square                                      | square         |             17 |        1120.29 |           0 |             0.00 |
|    31 |         0.2 | Fail    | No figure submitted (message limit reached) | square         |             40 |        2523.89 |           0 |             0.00 |
|    32 |         0.2 | Fail    | cross                                       | diamond        |             12 |         288.25 |           0 |             0.00 |
|    33 |         0.2 | Success | triangle                                    | triangle       |             37 |        2287.75 |           1 |             0.00 |
|    34 |         0.2 | Fail    | circle                                      | diamond        |             13 |         481.68 |           0 |             0.00 |
|    35 |         0.2 | Fail    | asterisk                                    | triangle       |             20 |         690.41 |           0 |             0.00 |
|    36 |         0.2 | Success | cross                                       | cross          |             17 |         714.78 |           0 |             0.00 |
|    37 |         0.2 | Success | circle                                      | circle         |             16 |         559.45 |           0 |             0.00 |
|    38 |         0.2 | Fail    | circle                                      | triangle       |             10 |         436.69 |           0 |             0.00 |
|    39 |         0.2 | Fail    | circle                                      | square         |             24 |         994.69 |           0 |             0.00 |
|    40 |         0.2 | Fail    | square                                      | asterisk       |              9 |         468.03 |           0 |             0.00 |
|    41 |         0.2 | Success | asterisk                                    | asterisk       |             22 |         906.34 |           0 |             0.00 |
|    42 |         0.2 | Success | cross                                       | cross          |             10 |         312.15 |           0 |             0.00 |
|    43 |         0.2 | Success | cross                                       | cross          |             39 |        1819.34 |           0 |             0.00 |
|    44 |         0.2 | Fail    | circle                                      | asterisk       |              3 |          91.26 |           0 |             0.00 |
|    45 |         0.2 | Success | diamond                                     | diamond        |             14 |         655.25 |           0 |             0.00 |
|    46 |         0.2 | Success | asterisk                                    | asterisk       |             21 |         825.03 |           0 |             0.00 |
|    47 |         0.2 | Success | diamond                                     | diamond        |             21 |        1137.90 |           0 |             0.00 |
|    48 |         0.2 | Fail    | circle                                      | asterisk       |             18 |         802.56 |           0 |             0.00 |
|    49 |         0.2 | Success | triangle                                    | triangle       |             28 |        1568.49 |           0 |             0.00 |
|    50 |         0.2 | Fail    | circle                                      | square         |             14 |         529.69 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |        234.11 |          234.11 |         9 |            220.416 |                      7.655 |              228.070 |               24.491 |                        0.851 |
|     2 |        746.88 |          746.88 |        18 |            717.916 |                     16.821 |              734.737 |               39.884 |                        0.934 |
|     3 |        569.86 |          569.86 |        11 |            551.953 |                     11.011 |              562.964 |               50.178 |                        1.001 |
|     4 |        624.22 |          624.22 |        14 |            601.114 |                     14.052 |              615.166 |               42.937 |                        1.004 |
|     5 |       1158.08 |         1158.08 |        24 |           1118.812 |                     24.971 |             1143.782 |               46.617 |                        1.040 |
|     6 |       1352.93 |         1352.93 |        27 |           1306.212 |                     30.757 |             1336.969 |               48.378 |                        1.139 |
|     7 |        741.85 |          741.85 |        16 |            713.057 |                     19.204 |              732.261 |               44.566 |                        1.200 |
|     8 |        666.29 |          666.29 |        17 |            638.295 |                     16.656 |              654.951 |               37.547 |                        0.980 |
|     9 |        760.31 |          760.31 |        15 |            737.045 |                     14.083 |              751.128 |               49.136 |                        0.939 |
|    10 |       1561.15 |         1561.15 |        40 |           1492.691 |                     43.858 |             1536.549 |               37.317 |                        1.096 |
|    11 |        907.44 |          907.44 |        17 |            878.599 |                     18.257 |              896.856 |               51.682 |                        1.074 |
|    12 |        154.53 |          154.53 |         5 |            147.686 |                      4.170 |              151.856 |               29.537 |                        0.834 |
|    13 |        915.08 |          915.08 |        20 |            884.302 |                     19.050 |              903.352 |               44.215 |                        0.953 |
|    14 |        916.02 |          916.02 |        21 |            882.282 |                     21.649 |              903.931 |               42.013 |                        1.031 |
|    15 |        339.60 |          339.60 |        11 |            320.820 |                     11.772 |              332.593 |               29.165 |                        1.070 |
|    16 |        668.11 |          668.11 |        14 |            645.042 |                     13.462 |              658.504 |               46.074 |                        0.962 |
|    17 |        804.03 |          804.03 |        16 |            778.346 |                     15.295 |              793.641 |               48.647 |                        0.956 |
|    18 |        786.45 |          786.45 |        17 |            758.341 |                     17.725 |              776.066 |               44.608 |                        1.043 |
|    19 |        491.35 |          491.35 |        12 |            472.527 |                     11.349 |              483.876 |               39.377 |                        0.946 |
|    20 |       1200.83 |         1200.83 |        22 |           1163.140 |                     24.206 |             1187.347 |               52.870 |                        1.100 |
|    21 |        414.17 |          414.17 |         9 |            400.598 |                      7.899 |              408.496 |               44.511 |                        0.878 |
|    22 |        511.95 |          511.95 |        16 |            485.633 |                     16.285 |              501.918 |               30.352 |                        1.018 |
|    23 |        340.95 |          340.95 |        10 |            324.271 |                     10.688 |              334.959 |               32.427 |                        1.069 |
|    24 |        920.43 |          920.43 |        24 |            879.410 |                     25.835 |              905.246 |               36.642 |                        1.076 |
|    25 |        579.55 |          579.55 |        16 |            553.855 |                     15.951 |              569.806 |               34.616 |                        0.997 |
|    26 |       1442.61 |         1442.61 |        40 |           1371.935 |                     45.364 |             1417.300 |               34.298 |                        1.134 |
|    27 |        367.49 |          367.49 |        12 |            349.229 |                     10.698 |              359.927 |               29.102 |                        0.891 |
|    28 |        102.68 |          102.68 |         5 |             95.528 |                      4.075 |               99.602 |               19.106 |                        0.815 |
|    29 |       1095.19 |         1095.19 |        23 |           1055.963 |                     24.602 |             1080.565 |               45.911 |                        1.070 |
|    30 |       1136.55 |         1136.55 |        18 |           1106.150 |                     19.072 |             1125.222 |               61.453 |                        1.060 |
|    31 |       2540.14 |         2540.14 |        40 |           1915.618 |                     46.551 |             1962.169 |               47.890 |                        1.164 |
|    32 |        306.17 |          306.17 |        13 |            285.729 |                     11.762 |              297.490 |               21.979 |                        0.905 |
|    33 |       2302.61 |         2302.61 |        38 |           1863.307 |                     43.414 |             1906.721 |               49.034 |                        1.142 |
|    34 |        501.01 |          501.01 |        14 |            479.222 |                     13.221 |              492.443 |               34.230 |                        0.944 |
|    35 |        703.89 |          703.89 |        21 |            668.463 |                     21.464 |              689.927 |               31.832 |                        1.022 |
|    36 |        729.69 |          729.69 |        18 |            696.858 |                     21.399 |              718.257 |               38.714 |                        1.189 |
|    37 |        576.07 |          576.07 |        17 |            548.164 |                     16.994 |              565.157 |               32.245 |                        1.000 |
|    38 |        450.05 |          450.05 |        11 |            433.010 |                     10.053 |              443.063 |               39.365 |                        0.914 |
|    39 |       1065.77 |         1065.77 |        25 |           1025.481 |                     24.041 |             1049.523 |               41.019 |                        0.962 |
|    40 |        483.18 |          483.18 |        10 |            466.892 |                     10.364 |              477.256 |               46.689 |                        1.036 |
|    41 |        919.88 |          919.88 |        23 |            879.537 |                     26.408 |              905.945 |               38.241 |                        1.148 |
|    42 |        328.15 |          328.15 |        11 |            311.176 |                     10.543 |              321.719 |               28.289 |                        0.958 |
|    43 |       1839.71 |         1839.71 |        40 |           1773.815 |                     41.171 |             1814.986 |               44.345 |                        1.029 |
|    44 |        106.15 |          106.15 |         4 |            100.664 |                      2.926 |              103.590 |               25.166 |                        0.731 |
|    45 |        729.68 |          729.68 |        15 |            705.047 |                     15.407 |              720.454 |               47.003 |                        1.027 |
|    46 |        843.51 |          843.51 |        22 |            808.873 |                     20.998 |              829.871 |               36.767 |                        0.954 |
|    47 |       1152.26 |         1152.26 |        23 |           1113.579 |                     23.946 |             1137.525 |               48.416 |                        1.041 |
|    48 |        885.38 |          885.38 |        19 |            853.873 |                     19.866 |              873.739 |               44.941 |                        1.046 |
|    49 |       1581.43 |         1581.43 |        29 |           1532.022 |                     31.639 |             1563.661 |               52.828 |                        1.091 |
|    50 |        610.75 |          610.75 |        15 |            586.033 |                     14.839 |              600.873 |               39.069 |                        0.989 |
```

## Reconnect details

Paused time is excluded from the trial's experiment-time measurement.

```text
| Round | Disconnected Jetsons | Paused at (UTC)                  | Resumed at (UTC)                 | Paused (seconds) |
| ----- | -------------------- | -------------------------------- | -------------------------------- | ---------------- |
|    33 | Agent2               | 2026-05-14T18:18:41.996564+00:00 | 2026-05-14T18:18:41.998981+00:00 |             0.00 |
```
