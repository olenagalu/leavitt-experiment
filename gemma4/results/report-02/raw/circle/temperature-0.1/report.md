# Circle auto-trial report

## Summary

- Batch: `temperature-0.1`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0.1
- Completed trials: 50/50
- Average time: 779.15 seconds
- Average total messages: 16.94
- Average Gemma 4 thinking time per response: 43.163 seconds
- Average visible-response generation time: 1.029 seconds
- Average complete generation time: 44.193 seconds
- Success rate: 22/50 (44.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |     103 |           185 |        55.7% (0.557) |                0.500 | 1.114 |                0.556 |
| circle   | Agent1 | Agent5    |                  2 |      82 |           185 |        44.3% (0.443) |                0.500 | 0.886 |                0.444 |
| circle   | Agent2 | Agent1    |                  2 |      82 |           160 |        51.2% (0.512) |                0.500 | 1.025 |                0.512 |
| circle   | Agent2 | Agent3    |                  2 |      78 |           160 |        48.8% (0.487) |                0.500 | 0.975 |                0.488 |
| circle   | Agent3 | Agent2    |                  2 |      87 |           170 |        51.2% (0.512) |                0.500 | 1.024 |                0.512 |
| circle   | Agent3 | Agent4    |                  2 |      83 |           170 |        48.8% (0.488) |                0.500 | 0.976 |                0.488 |
| circle   | Agent4 | Agent3    |                  2 |      80 |           144 |        55.6% (0.556) |                0.500 | 1.111 |                0.555 |
| circle   | Agent4 | Agent5    |                  2 |      64 |           144 |        44.4% (0.444) |                0.500 | 0.889 |                0.445 |
| circle   | Agent5 | Agent1    |                  2 |      92 |           188 |        48.9% (0.489) |                0.500 | 0.979 |                0.489 |
| circle   | Agent5 | Agent4    |                  2 |      96 |           188 |        51.1% (0.511) |                0.500 | 1.021 |                0.511 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.1 | Fail    | cross            | diamond        |             23 |         959.82 |           0 |             0.00 |
|     2 |         0.1 | Fail    | circle           | triangle       |              9 |         267.35 |           0 |             0.00 |
|     3 |         0.1 | Fail    | asterisk         | diamond        |             13 |         509.99 |           0 |             0.00 |
|     4 |         0.1 | Fail    | square           | triangle       |              9 |         316.65 |           0 |             0.00 |
|     5 |         0.1 | Fail    | cross            | triangle       |             31 |        1303.62 |           0 |             0.00 |
|     6 |         0.1 | Fail    | cross            | diamond        |             27 |        1418.87 |           0 |             0.00 |
|     7 |         0.1 | Fail    | triangle         | cross          |             19 |        1287.18 |           0 |             0.00 |
|     8 |         0.1 | Fail    | cross            | triangle       |             17 |         743.47 |           0 |             0.00 |
|     9 |         0.1 | Success | triangle         | triangle       |              7 |         266.10 |           0 |             0.00 |
|    10 |         0.1 | Success | diamond          | diamond        |             13 |         556.58 |           0 |             0.00 |
|    11 |         0.1 | Success | triangle         | triangle       |             10 |         439.38 |           0 |             0.00 |
|    12 |         0.1 | Fail    | diamond          | circle         |             19 |         904.66 |           0 |             0.00 |
|    13 |         0.1 | Success | asterisk         | asterisk       |             18 |         915.47 |           0 |             0.00 |
|    14 |         0.1 | Fail    | cross            | triangle       |              8 |         342.62 |           0 |             0.00 |
|    15 |         0.1 | Fail    | square           | diamond        |              5 |         134.47 |           0 |             0.00 |
|    16 |         0.1 | Fail    | triangle         | diamond        |              5 |         170.19 |           0 |             0.00 |
|    17 |         0.1 | Fail    | diamond          | asterisk       |             18 |         589.28 |           0 |             0.00 |
|    18 |         0.1 | Success | circle           | circle         |             16 |         785.53 |           0 |             0.00 |
|    19 |         0.1 | Success | asterisk         | asterisk       |             16 |         824.83 |           0 |             0.00 |
|    20 |         0.1 | Success | square           | square         |             33 |        1300.41 |           0 |             0.00 |
|    21 |         0.1 | Fail    | circle           | square         |              6 |         203.85 |           0 |             0.00 |
|    22 |         0.1 | Success | triangle         | triangle       |             12 |         516.54 |           0 |             0.00 |
|    23 |         0.1 | Fail    | cross            | square         |             19 |         776.76 |           0 |             0.00 |
|    24 |         0.1 | Success | circle           | circle         |              8 |         240.37 |           0 |             0.00 |
|    25 |         0.1 | Fail    | cross            | triangle       |             16 |         761.05 |           0 |             0.00 |
|    26 |         0.1 | Success | asterisk         | asterisk       |             19 |         583.24 |           0 |             0.00 |
|    27 |         0.1 | Fail    | diamond          | cross          |             12 |         511.94 |           0 |             0.00 |
|    28 |         0.1 | Fail    | cross            | square         |             17 |        1124.42 |           0 |             0.00 |
|    29 |         0.1 | Fail    | square           | triangle       |             33 |        1899.63 |           0 |             0.00 |
|    30 |         0.1 | Fail    | asterisk         | diamond        |              7 |         209.67 |           0 |             0.00 |
|    31 |         0.1 | Success | circle           | circle         |             35 |        1335.55 |           0 |             0.00 |
|    32 |         0.1 | Success | circle           | circle         |             34 |        1844.09 |           0 |             0.00 |
|    33 |         0.1 | Fail    | diamond          | asterisk       |             25 |        1237.52 |           0 |             0.00 |
|    34 |         0.1 | Success | asterisk         | asterisk       |             22 |         824.25 |           0 |             0.00 |
|    35 |         0.1 | Success | triangle         | triangle       |             24 |        1003.99 |           0 |             0.00 |
|    36 |         0.1 | Fail    | circle           | asterisk       |             12 |         660.79 |           0 |             0.00 |
|    37 |         0.1 | Success | diamond          | diamond        |             20 |         871.24 |           0 |             0.00 |
|    38 |         0.1 | Fail    | cross            | asterisk       |             11 |         483.08 |           0 |             0.00 |
|    39 |         0.1 | Success | cross            | cross          |             16 |         560.96 |           0 |             0.00 |
|    40 |         0.1 | Fail    | triangle         | diamond        |             13 |         724.35 |           0 |             0.00 |
|    41 |         0.1 | Fail    | diamond          | triangle       |              9 |         386.10 |           0 |             0.00 |
|    42 |         0.1 | Success | circle           | circle         |             15 |         729.90 |           0 |             0.00 |
|    43 |         0.1 | Success | triangle         | triangle       |             20 |        1168.81 |           0 |             0.00 |
|    44 |         0.1 | Success | triangle         | triangle       |             25 |        1332.72 |           0 |             0.00 |
|    45 |         0.1 | Fail    | cross            | diamond        |              5 |         104.79 |           0 |             0.00 |
|    46 |         0.1 | Success | diamond          | diamond        |             24 |        1307.62 |           0 |             0.00 |
|    47 |         0.1 | Fail    | cross            | asterisk       |             11 |         396.44 |           0 |             0.00 |
|    48 |         0.1 | Success | square           | square         |             27 |        1473.26 |           0 |             0.00 |
|    49 |         0.1 | Fail    | square           | asterisk       |              9 |         472.05 |           0 |             0.00 |
|    50 |         0.1 | Success | circle           | circle         |             25 |        1176.19 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |        974.17 |          974.17 |        24 |            934.393 |                     24.534 |              958.927 |               38.933 |                        1.022 |
|     2 |        282.79 |          282.79 |        10 |            266.706 |                     10.157 |              276.864 |               26.671 |                        1.016 |
|     3 |        526.78 |          526.78 |        14 |            504.490 |                     13.367 |              517.857 |               36.035 |                        0.955 |
|     4 |        332.85 |          332.85 |        10 |            316.848 |                      9.523 |              326.371 |               31.685 |                        0.952 |
|     5 |       1320.20 |         1320.20 |        32 |           1267.476 |                     33.469 |             1300.946 |               39.609 |                        1.046 |
|     6 |       1435.14 |         1435.14 |        28 |           1385.002 |                     33.081 |             1418.083 |               49.464 |                        1.181 |
|     7 |       1366.45 |         1366.45 |        20 |           1334.728 |                     18.940 |             1353.668 |               66.736 |                        0.947 |
|     8 |        826.15 |          826.15 |        18 |            795.729 |                     18.770 |              814.499 |               44.207 |                        1.043 |
|     9 |        280.04 |          280.04 |         8 |            267.493 |                      7.246 |              274.740 |               33.437 |                        0.906 |
|    10 |        571.51 |          571.51 |        14 |            549.592 |                     13.704 |              563.296 |               39.257 |                        0.979 |
|    11 |        454.62 |          454.62 |        11 |            437.037 |                     11.062 |              448.100 |               39.731 |                        1.006 |
|    12 |        920.98 |          920.98 |        20 |            888.048 |                     21.369 |              909.417 |               44.402 |                        1.068 |
|    13 |        992.84 |          992.84 |        19 |            960.312 |                     20.862 |              981.175 |               50.543 |                        1.098 |
|    14 |        418.48 |          418.48 |         9 |            403.994 |                      7.983 |              411.977 |               44.888 |                        0.887 |
|    15 |        147.53 |          147.53 |         6 |            138.930 |                      4.987 |              143.917 |               23.155 |                        0.831 |
|    16 |        186.37 |          186.37 |         6 |            178.033 |                      5.069 |              183.102 |               29.672 |                        0.845 |
|    17 |        602.39 |          602.39 |        19 |            572.391 |                     18.369 |              590.760 |               30.126 |                        0.967 |
|    18 |        801.72 |          801.72 |        17 |            773.884 |                     18.176 |              792.061 |               45.523 |                        1.069 |
|    19 |        841.26 |          841.26 |        17 |            812.486 |                     18.476 |              830.962 |               47.793 |                        1.087 |
|    20 |       1316.09 |         1316.09 |        34 |           1258.191 |                     35.586 |             1293.777 |               37.006 |                        1.047 |
|    21 |        217.44 |          217.44 |         7 |            207.816 |                      5.592 |              213.407 |               29.688 |                        0.799 |
|    22 |        589.82 |          589.82 |        13 |            568.878 |                     13.014 |              581.892 |               43.760 |                        1.001 |
|    23 |        855.76 |          855.76 |        20 |            822.668 |                     20.991 |              843.659 |               41.133 |                        1.050 |
|    24 |        260.65 |          260.65 |         9 |            244.886 |                      9.493 |              254.378 |               27.210 |                        1.055 |
|    25 |        840.23 |          840.23 |        17 |            812.802 |                     16.552 |              829.354 |               47.812 |                        0.974 |
|    26 |        598.60 |          598.60 |        20 |            565.329 |                     19.937 |              585.267 |               28.266 |                        0.997 |
|    27 |        527.02 |          527.02 |        13 |            503.851 |                     15.310 |              519.161 |               38.758 |                        1.178 |
|    28 |       1139.82 |         1139.82 |        18 |            920.205 |                     17.424 |              937.629 |               51.123 |                        0.968 |
|    29 |       1912.74 |         1912.74 |        34 |           1854.581 |                     37.340 |             1891.922 |               54.547 |                        1.098 |
|    30 |        225.42 |          225.42 |         8 |            213.804 |                      6.436 |              220.239 |               26.725 |                        0.804 |
|    31 |       1351.06 |         1351.06 |        36 |           1292.945 |                     36.880 |             1329.825 |               35.915 |                        1.024 |
|    32 |       1857.23 |         1857.23 |        35 |           1796.281 |                     38.759 |             1835.040 |               51.322 |                        1.107 |
|    33 |       1253.24 |         1253.24 |        26 |           1208.025 |                     30.022 |             1238.046 |               46.462 |                        1.155 |
|    34 |        839.27 |          839.27 |        23 |            802.822 |                     21.745 |              824.567 |               34.905 |                        0.945 |
|    35 |       1020.09 |         1020.09 |        25 |            979.008 |                     25.742 |             1004.751 |               39.160 |                        1.030 |
|    36 |        676.37 |          676.37 |        13 |            655.539 |                     13.048 |              668.587 |               50.426 |                        1.004 |
|    37 |        887.76 |          887.76 |        21 |            850.067 |                     24.027 |              874.093 |               40.479 |                        1.144 |
|    38 |        500.36 |          500.36 |        12 |            483.334 |                      9.990 |              493.324 |               40.278 |                        0.832 |
|    39 |        577.12 |          577.12 |        17 |            551.045 |                     15.583 |              566.628 |               32.414 |                        0.917 |
|    40 |        743.91 |          743.91 |        14 |            720.365 |                     14.937 |              735.302 |               51.455 |                        1.067 |
|    41 |        402.01 |          402.01 |        10 |            385.876 |                      9.715 |              395.591 |               38.588 |                        0.972 |
|    42 |        805.15 |          805.15 |        16 |            779.219 |                     16.361 |              795.580 |               48.701 |                        1.023 |
|    43 |       1254.20 |         1254.20 |        22 |           1218.960 |                     22.072 |             1241.032 |               55.407 |                        1.003 |
|    44 |       1347.64 |         1347.64 |        26 |           1302.724 |                     29.134 |             1331.858 |               50.105 |                        1.121 |
|    45 |        184.05 |          184.05 |         6 |            175.123 |                      5.627 |              180.750 |               29.187 |                        0.938 |
|    46 |       1323.05 |         1323.05 |        25 |           1281.821 |                     26.682 |             1308.503 |               51.273 |                        1.067 |
|    47 |        471.94 |          471.94 |        12 |            451.679 |                     11.793 |              463.472 |               37.640 |                        0.983 |
|    48 |       1490.67 |         1490.67 |        28 |           1444.989 |                     28.642 |             1473.631 |               51.607 |                        1.023 |
|    49 |        489.94 |          489.94 |        10 |            473.584 |                     10.199 |              483.782 |               47.358 |                        1.020 |
|    50 |       1189.66 |         1189.66 |        26 |           1146.801 |                     26.576 |             1173.377 |               44.108 |                        1.022 |
```

## Reconnect details

No Jetson disconnects were recorded.
