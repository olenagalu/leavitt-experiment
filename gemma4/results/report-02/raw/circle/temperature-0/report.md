# Circle auto-trial report

## Summary

- Batch: `temperature-0`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0
- Completed trials: 50/50
- Average time: 744.64 seconds
- Average total messages: 16.58
- Average Gemma 4 thinking time per response: 42.240 seconds
- Average visible-response generation time: 1.019 seconds
- Average complete generation time: 43.260 seconds
- Success rate: 20/50 (40.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      71 |           154 |        46.1% (0.461) |                0.500 | 0.922 |                0.461 |
| circle   | Agent1 | Agent5    |                  2 |      83 |           154 |        53.9% (0.539) |                0.500 | 1.078 |                0.539 |
| circle   | Agent2 | Agent1    |                  2 |      95 |           167 |        56.9% (0.569) |                0.500 | 1.138 |                0.568 |
| circle   | Agent2 | Agent3    |                  2 |      72 |           167 |        43.1% (0.431) |                0.500 | 0.862 |                0.432 |
| circle   | Agent3 | Agent2    |                  2 |      85 |           172 |        49.4% (0.494) |                0.500 | 0.988 |                0.494 |
| circle   | Agent3 | Agent4    |                  2 |      87 |           172 |        50.6% (0.506) |                0.500 | 1.012 |                0.506 |
| circle   | Agent4 | Agent3    |                  2 |      99 |           176 |        56.2% (0.562) |                0.500 | 1.125 |                0.562 |
| circle   | Agent4 | Agent5    |                  2 |      77 |           176 |        43.8% (0.438) |                0.500 | 0.875 |                0.438 |
| circle   | Agent5 | Agent1    |                  2 |      73 |           160 |        45.6% (0.456) |                0.500 | 0.912 |                0.457 |
| circle   | Agent5 | Agent4    |                  2 |      87 |           160 |        54.4% (0.544) |                0.500 | 1.087 |                0.543 |
```

### Excluded fallback routes

No fallback routes were recorded.

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Success | circle           | circle         |             13 |         468.34 |           0 |             0.00 |
|     2 |           0 | Fail    | square           | triangle       |             25 |         997.99 |           0 |             0.00 |
|     3 |           0 | Fail    | diamond          | cross          |             17 |         660.58 |           0 |             0.00 |
|     4 |           0 | Fail    | cross            | circle         |              9 |         445.05 |           0 |             0.00 |
|     5 |           0 | Success | cross            | cross          |             23 |        1383.03 |           0 |             0.00 |
|     6 |           0 | Fail    | cross            | asterisk       |             20 |        1019.03 |           0 |             0.00 |
|     7 |           0 | Success | square           | square         |             23 |         917.09 |           0 |             0.00 |
|     8 |           0 | Fail    | square           | circle         |             30 |        1388.21 |           0 |             0.00 |
|     9 |           0 | Fail    | cross            | triangle       |             13 |         441.77 |           0 |             0.00 |
|    10 |           0 | Fail    | circle           | square         |             21 |         920.43 |           0 |             0.00 |
|    11 |           0 | Fail    | diamond          | cross          |              9 |         256.81 |           0 |             0.00 |
|    12 |           0 | Success | circle           | circle         |             33 |        1650.16 |           0 |             0.00 |
|    13 |           0 | Fail    | cross            | square         |             11 |         423.75 |           0 |             0.00 |
|    14 |           0 | Fail    | circle           | square         |             26 |        1239.55 |           0 |             0.00 |
|    15 |           0 | Success | triangle         | triangle       |             14 |         509.16 |           0 |             0.00 |
|    16 |           0 | Success | triangle         | triangle       |             31 |        1365.05 |           0 |             0.00 |
|    17 |           0 | Fail    | circle           | square         |             17 |         683.54 |           0 |             0.00 |
|    18 |           0 | Fail    | square           | diamond        |             21 |        1259.65 |           0 |             0.00 |
|    19 |           0 | Success | triangle         | triangle       |             17 |        1015.53 |           0 |             0.00 |
|    20 |           0 | Fail    | cross            | square         |             16 |         757.83 |           0 |             0.00 |
|    21 |           0 | Success | cross            | cross          |             20 |         797.64 |           0 |             0.00 |
|    22 |           0 | Success | circle           | circle         |             13 |         525.07 |           0 |             0.00 |
|    23 |           0 | Success | asterisk         | asterisk       |             17 |         973.42 |           0 |             0.00 |
|    24 |           0 | Success | asterisk         | asterisk       |             24 |        1151.65 |           0 |             0.00 |
|    25 |           0 | Fail    | cross            | triangle       |             14 |         467.81 |           0 |             0.00 |
|    26 |           0 | Success | cross            | cross          |             18 |         560.56 |           0 |             0.00 |
|    27 |           0 | Success | triangle         | triangle       |             18 |        1106.48 |           0 |             0.00 |
|    28 |           0 | Fail    | cross            | circle         |              6 |         273.03 |           0 |             0.00 |
|    29 |           0 | Fail    | cross            | triangle       |              9 |         290.50 |           0 |             0.00 |
|    30 |           0 | Success | cross            | cross          |             18 |         694.17 |           0 |             0.00 |
|    31 |           0 | Fail    | square           | triangle       |             12 |         425.27 |           0 |             0.00 |
|    32 |           0 | Fail    | square           | circle         |             13 |         492.12 |           0 |             0.00 |
|    33 |           0 | Fail    | cross            | triangle       |             17 |         769.76 |           0 |             0.00 |
|    34 |           0 | Fail    | circle           | square         |             10 |         393.02 |           0 |             0.00 |
|    35 |           0 | Fail    | diamond          | circle         |              7 |         201.57 |           0 |             0.00 |
|    36 |           0 | Success | diamond          | diamond        |             10 |         351.61 |           0 |             0.00 |
|    37 |           0 | Success | cross            | cross          |             25 |        1233.85 |           0 |             0.00 |
|    38 |           0 | Success | cross            | cross          |             24 |        1139.98 |           0 |             0.00 |
|    39 |           0 | Fail    | square           | diamond        |              9 |         331.49 |           0 |             0.00 |
|    40 |           0 | Fail    | square           | cross          |              9 |         282.32 |           0 |             0.00 |
|    41 |           0 | Success | square           | square         |             15 |         608.75 |           0 |             0.00 |
|    42 |           0 | Fail    | cross            | square         |             16 |         875.56 |           0 |             0.00 |
|    43 |           0 | Fail    | asterisk         | square         |             17 |         647.26 |           0 |             0.00 |
|    44 |           0 | Fail    | circle           | cross          |              8 |         376.38 |           0 |             0.00 |
|    45 |           0 | Success | circle           | circle         |             10 |         507.15 |           0 |             0.00 |
|    46 |           0 | Fail    | circle           | asterisk       |             12 |         506.93 |           0 |             0.00 |
|    47 |           0 | Fail    | cross            | asterisk       |             36 |        1882.91 |           0 |             0.00 |
|    48 |           0 | Fail    | cross            | triangle       |              8 |         252.45 |           0 |             0.00 |
|    49 |           0 | Success | triangle         | triangle       |             16 |         912.18 |           0 |             0.00 |
|    50 |           0 | Fail    | circle           | asterisk       |              9 |         398.37 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |        486.15 |          486.15 |        14 |            464.104 |                     13.566 |              477.670 |               33.150 |                        0.969 |
|     2 |       1011.99 |         1011.99 |        26 |            969.655 |                     26.453 |              996.109 |               37.294 |                        1.017 |
|     3 |        674.23 |          674.23 |        18 |            645.620 |                     17.634 |              663.255 |               35.868 |                        0.980 |
|     4 |        458.70 |          458.70 |        10 |            443.590 |                      8.990 |              452.581 |               44.359 |                        0.899 |
|     5 |       1399.49 |         1399.49 |        24 |           1360.798 |                     23.588 |             1384.385 |               56.700 |                        0.983 |
|     6 |       1033.31 |         1033.31 |        21 |            997.441 |                     22.535 |             1019.976 |               47.497 |                        1.073 |
|     7 |        990.07 |          990.07 |        24 |            949.723 |                     25.479 |              975.201 |               39.572 |                        1.062 |
|     8 |       1405.32 |         1405.32 |        31 |           1353.385 |                     33.080 |             1386.465 |               43.658 |                        1.067 |
|     9 |        456.67 |          456.67 |        14 |            434.720 |                     13.312 |              448.032 |               31.051 |                        0.951 |
|    10 |        993.75 |          993.75 |        22 |            955.065 |                     25.583 |              980.648 |               43.412 |                        1.163 |
|    11 |        271.86 |          271.86 |        10 |            256.277 |                      9.180 |              265.457 |               25.628 |                        0.918 |
|    12 |       1666.85 |         1666.85 |        34 |           1606.869 |                     38.699 |             1645.567 |               47.261 |                        1.138 |
|    13 |        499.96 |          499.96 |        12 |            482.099 |                     11.010 |              493.109 |               40.175 |                        0.917 |
|    14 |       1326.18 |         1326.18 |        27 |           1281.563 |                     27.975 |             1309.539 |               47.465 |                        1.036 |
|    15 |        526.45 |          526.45 |        15 |            503.442 |                     13.932 |              517.374 |               33.563 |                        0.929 |
|    16 |       1379.28 |         1379.28 |        32 |           1324.911 |                     34.252 |             1359.163 |               41.403 |                        1.070 |
|    17 |        755.02 |          755.02 |        18 |            725.184 |                     18.448 |              743.632 |               40.288 |                        1.025 |
|    18 |       1278.12 |         1278.12 |        22 |           1243.207 |                     21.776 |             1264.983 |               56.509 |                        0.990 |
|    19 |       1030.80 |         1030.80 |        18 |           1002.837 |                     16.855 |             1019.692 |               55.713 |                        0.936 |
|    20 |        833.01 |          833.01 |        17 |            804.516 |                     17.389 |              821.905 |               47.324 |                        1.023 |
|    21 |        813.41 |          813.41 |        21 |            778.190 |                     22.867 |              801.057 |               37.057 |                        1.089 |
|    22 |        540.57 |          540.57 |        14 |            519.080 |                     13.293 |              532.372 |               37.077 |                        0.949 |
|    23 |       1049.73 |         1049.73 |        19 |           1020.974 |                     18.086 |             1039.059 |               53.735 |                        0.952 |
|    24 |       1169.02 |         1169.02 |        25 |           1126.656 |                     26.994 |             1153.650 |               45.066 |                        1.080 |
|    25 |        482.34 |          482.34 |        15 |            459.269 |                     13.517 |              472.786 |               30.618 |                        0.901 |
|    26 |        577.38 |          577.38 |        19 |            546.576 |                     19.690 |              566.267 |               28.767 |                        1.036 |
|    27 |       1122.89 |         1122.89 |        19 |           1090.245 |                     20.782 |             1111.027 |               57.381 |                        1.094 |
|    28 |        287.46 |          287.46 |         7 |            277.470 |                      5.949 |              283.419 |               39.639 |                        0.850 |
|    29 |        306.34 |          306.34 |        10 |            289.878 |                     10.044 |              299.922 |               28.988 |                        1.004 |
|    30 |        710.77 |          710.77 |        19 |            679.649 |                     19.066 |              698.715 |               35.771 |                        1.003 |
|    31 |        440.20 |          440.20 |        13 |            421.734 |                     10.977 |              432.711 |               32.441 |                        0.844 |
|    32 |        505.79 |          505.79 |        14 |            483.168 |                     13.800 |              496.968 |               34.512 |                        0.986 |
|    33 |        786.40 |          786.40 |        18 |            756.747 |                     18.183 |              774.930 |               42.041 |                        1.010 |
|    34 |        467.49 |          467.49 |        11 |            451.081 |                      9.429 |              460.510 |               41.007 |                        0.857 |
|    35 |        217.12 |          217.12 |         8 |            205.354 |                      7.354 |              212.708 |               25.669 |                        0.919 |
|    36 |        364.87 |          364.87 |        11 |            348.694 |                      9.982 |              358.676 |               31.699 |                        0.907 |
|    37 |       1249.88 |         1249.88 |        26 |           1206.782 |                     26.847 |             1233.629 |               46.415 |                        1.033 |
|    38 |       1154.22 |         1154.22 |        25 |           1112.855 |                     26.060 |             1138.915 |               44.514 |                        1.042 |
|    39 |        405.11 |          405.11 |        10 |            390.900 |                      8.383 |              399.283 |               39.090 |                        0.838 |
|    40 |        299.16 |          299.16 |        10 |            284.173 |                      8.741 |              292.914 |               28.417 |                        0.874 |
|    41 |        625.11 |          625.11 |        16 |            600.821 |                     15.077 |              615.898 |               37.551 |                        0.942 |
|    42 |        891.27 |          891.27 |        17 |            860.613 |                     20.086 |              880.699 |               50.624 |                        1.182 |
|    43 |        665.17 |          665.17 |        18 |            634.458 |                     19.442 |              653.900 |               35.248 |                        1.080 |
|    44 |        389.90 |          389.90 |         9 |            376.536 |                      7.626 |              384.162 |               41.837 |                        0.847 |
|    45 |        523.01 |          523.01 |        11 |            504.870 |                     11.794 |              516.664 |               45.897 |                        1.072 |
|    46 |        519.30 |          519.30 |        13 |            499.067 |                     12.244 |              511.311 |               38.390 |                        0.942 |
|    47 |       1896.52 |         1896.52 |        37 |           1831.728 |                     42.379 |             1874.106 |               49.506 |                        1.145 |
|    48 |        327.03 |          327.03 |         9 |            313.595 |                      8.149 |              321.744 |               34.844 |                        0.905 |
|    49 |        929.12 |          929.12 |        17 |            897.897 |                     19.973 |              917.870 |               52.817 |                        1.175 |
|    50 |        413.97 |          413.97 |        10 |            397.329 |                     10.604 |              407.933 |               39.733 |                        1.060 |
```

## Reconnect details

No Jetson disconnects were recorded.
