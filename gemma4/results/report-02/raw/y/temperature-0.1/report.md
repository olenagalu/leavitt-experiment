# Y topology auto-trial report

## Summary

- Batch: `temperature-0.1`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0.1
- Completed trials: 50/50
- Average time: 1219.48 seconds
- Average total messages: 24.40
- Average Gemma 4 thinking time per response: 46.797 seconds
- Average visible-response generation time: 1.072 seconds
- Average complete generation time: 47.869 seconds
- Success rate: 23/50 (46.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     230 |           230 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     255 |           255 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      62 |           228 |        27.2% (0.272) |                0.333 | 0.816 |                0.272 |
| y        | Agent3 | Agent2    |                  3 |      58 |           228 |        25.4% (0.254) |                0.333 | 0.763 |                0.255 |
| y        | Agent3 | Agent4    |                  3 |     108 |           228 |        47.4% (0.474) |                0.333 | 1.421 |                0.473 |
| y        | Agent4 | Agent3    |                  2 |     227 |           273 |        83.2% (0.832) |                0.500 | 1.663 |                0.830 |
| y        | Agent4 | Agent5    |                  2 |      46 |           273 |        16.8% (0.168) |                0.500 | 0.337 |                0.170 |
| y        | Agent5 | Agent4    |                  1 |     233 |           233 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent2 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |         0.1 | Fail    | square                                      | cross          |             10 |         413.01 |           0 |             0.00 |
|     2 |         0.1 | Success | asterisk                                    | asterisk       |              9 |         596.42 |           0 |             0.00 |
|     3 |         0.1 | Fail    | triangle                                    | asterisk       |             11 |         665.67 |           0 |             0.00 |
|     4 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2563.68 |           0 |             0.00 |
|     5 |         0.1 | Fail    | diamond                                     | cross          |             13 |         596.59 |           0 |             0.00 |
|     6 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2728.24 |           0 |             0.00 |
|     7 |         0.1 | Success | cross                                       | cross          |             40 |        2305.31 |           0 |             0.00 |
|     8 |         0.1 | Success | square                                      | square         |             29 |        1552.44 |           0 |             0.00 |
|     9 |         0.1 | Success | cross                                       | cross          |             17 |         680.08 |           0 |             0.00 |
|    10 |         0.1 | Success | square                                      | square         |             11 |         637.71 |           0 |             0.00 |
|    11 |         0.1 | Success | square                                      | square         |             16 |         975.39 |           0 |             0.00 |
|    12 |         0.1 | Fail    | square                                      | diamond        |             10 |         444.84 |           0 |             0.00 |
|    13 |         0.1 | Fail    | cross                                       | asterisk       |             33 |        1761.97 |           0 |             0.00 |
|    14 |         0.1 | Success | diamond                                     | diamond        |             14 |         443.70 |           0 |             0.00 |
|    15 |         0.1 | Fail    | triangle                                    | cross          |             16 |         560.99 |           0 |             0.00 |
|    16 |         0.1 | Success | cross                                       | cross          |             30 |        1834.77 |           0 |             0.00 |
|    17 |         0.1 | Success | triangle                                    | triangle       |             37 |        2367.45 |           0 |             0.00 |
|    18 |         0.1 | Fail    | circle                                      | triangle       |             26 |        1294.34 |           0 |             0.00 |
|    19 |         0.1 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2951.93 |           0 |             0.00 |
|    20 |         0.1 | Success | cross                                       | cross          |             30 |        1529.87 |           0 |             0.00 |
|    21 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2191.64 |           0 |             0.00 |
|    22 |         0.1 | Success | triangle                                    | triangle       |             23 |        1051.63 |           0 |             0.00 |
|    23 |         0.1 | Success | triangle                                    | triangle       |             18 |         696.30 |           0 |             0.00 |
|    24 |         0.1 | Success | square                                      | square         |              9 |         495.76 |           0 |             0.00 |
|    25 |         0.1 | Success | triangle                                    | triangle       |             17 |         814.28 |           0 |             0.00 |
|    26 |         0.1 | Fail    | triangle                                    | asterisk       |             19 |         621.46 |           0 |             0.00 |
|    27 |         0.1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2611.20 |           0 |             0.00 |
|    28 |         0.1 | Success | circle                                      | circle         |              9 |         449.63 |           0 |             0.00 |
|    29 |         0.1 | Fail    | square                                      | cross          |             21 |         927.34 |           0 |             0.00 |
|    30 |         0.1 | Fail    | square                                      | asterisk       |             23 |         940.18 |           0 |             0.00 |
|    31 |         0.1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2502.66 |           0 |             0.00 |
|    32 |         0.1 | Fail    | triangle                                    | circle         |             35 |        1639.08 |           0 |             0.00 |
|    33 |         0.1 | Success | diamond                                     | diamond        |              9 |         447.58 |           0 |             0.00 |
|    34 |         0.1 | Success | square                                      | square         |              8 |         288.29 |           0 |             0.00 |
|    35 |         0.1 | Fail    | cross                                       | diamond        |             26 |         996.79 |           0 |             0.00 |
|    36 |         0.1 | Fail    | circle                                      | diamond        |              6 |         289.07 |           0 |             0.00 |
|    37 |         0.1 | Fail    | asterisk                                    | diamond        |             10 |         331.03 |           0 |             0.00 |
|    38 |         0.1 | Fail    | square                                      | circle         |             12 |         422.75 |           0 |             0.00 |
|    39 |         0.1 | Success | asterisk                                    | asterisk       |             33 |        1998.88 |           0 |             0.00 |
|    40 |         0.1 | Success | circle                                      | circle         |             27 |        1016.17 |           0 |             0.00 |
|    41 |         0.1 | Fail    | circle                                      | square         |              9 |         641.49 |           0 |             0.00 |
|    42 |         0.1 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2535.23 |           0 |             0.00 |
|    43 |         0.1 | Success | diamond                                     | diamond        |             26 |        1672.70 |           0 |             0.00 |
|    44 |         0.1 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2325.72 |           0 |             0.00 |
|    45 |         0.1 | Success | triangle                                    | triangle       |             33 |        1231.71 |           0 |             0.00 |
|    46 |         0.1 | Fail    | square                                      | triangle       |             22 |        1370.88 |           0 |             0.00 |
|    47 |         0.1 | Success | triangle                                    | triangle       |              8 |         493.35 |           0 |             0.00 |
|    48 |         0.1 | Fail    | triangle                                    | cross          |             15 |         709.39 |           0 |             0.00 |
|    49 |         0.1 | Fail    | circle                                      | diamond        |              9 |         501.71 |           0 |             0.00 |
|    50 |         0.1 | Success | cross                                       | cross          |             41 |        1855.67 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |        430.05 |          430.05 |        12 |            411.355 |                     11.447 |              422.802 |               34.280 |                        0.954 |
|     2 |        609.43 |          609.43 |        11 |            592.989 |                     10.276 |              603.265 |               53.908 |                        0.934 |
|     3 |        686.83 |          686.83 |        12 |            667.741 |                     11.586 |              679.327 |               55.645 |                        0.965 |
|     4 |       2640.58 |         2640.58 |        50 |           2550.658 |                     58.855 |             2609.513 |               51.013 |                        1.177 |
|     5 |        611.11 |          611.11 |        14 |            588.607 |                     14.263 |              602.870 |               42.043 |                        1.019 |
|     6 |       2744.04 |         2744.04 |        51 |           2656.627 |                     55.652 |             2712.280 |               52.091 |                        1.091 |
|     7 |       2376.21 |         2376.21 |        43 |           2125.604 |                     42.799 |             2168.403 |               49.433 |                        0.995 |
|     8 |       1572.30 |         1572.30 |        30 |           1517.699 |                     35.849 |             1553.548 |               50.590 |                        1.195 |
|     9 |        692.99 |          692.99 |        18 |            661.774 |                     20.274 |              682.047 |               36.765 |                        1.126 |
|    10 |        654.32 |          654.32 |        12 |            634.888 |                     12.399 |              647.287 |               52.907 |                        1.033 |
|    11 |        993.92 |          993.92 |        17 |            965.295 |                     18.143 |              983.438 |               56.782 |                        1.067 |
|    12 |        460.11 |          460.11 |        11 |            443.023 |                     10.172 |              453.194 |               40.275 |                        0.925 |
|    13 |       1779.98 |         1779.98 |        34 |           1717.507 |                     41.029 |             1758.537 |               50.515 |                        1.207 |
|    14 |        463.20 |          463.20 |        15 |            438.551 |                     15.117 |              453.667 |               29.237 |                        1.008 |
|    15 |        576.71 |          576.71 |        17 |            550.946 |                     15.261 |              566.207 |               32.409 |                        0.898 |
|    16 |       1851.76 |         1851.76 |        34 |           1802.463 |                     28.503 |             1830.966 |               53.014 |                        0.838 |
|    17 |       2386.30 |         2386.30 |        40 |           2322.462 |                     39.034 |             2361.496 |               58.062 |                        0.976 |
|    18 |       1368.93 |         1368.93 |        27 |           1325.035 |                     26.934 |             1351.969 |               49.075 |                        0.998 |
|    19 |       2972.21 |         2972.21 |        53 |           2881.059 |                     58.930 |             2939.989 |               54.360 |                        1.112 |
|    20 |       1605.27 |         1605.27 |        31 |           1552.812 |                     33.048 |             1585.860 |               50.091 |                        1.066 |
|    21 |       2264.62 |         2264.62 |        50 |           2173.464 |                     59.462 |             2232.926 |               43.469 |                        1.189 |
|    22 |       1067.52 |         1067.52 |        24 |           1029.071 |                     23.873 |             1052.944 |               42.878 |                        0.995 |
|    23 |        711.55 |          711.55 |        19 |            681.347 |                     18.138 |              699.485 |               35.860 |                        0.955 |
|    24 |        510.48 |          510.48 |        10 |            494.992 |                      9.748 |              504.740 |               49.499 |                        0.975 |
|    25 |        833.55 |          833.55 |        18 |            802.006 |                     20.446 |              822.452 |               44.556 |                        1.136 |
|    26 |        637.09 |          637.09 |        20 |            601.066 |                     23.782 |              624.848 |               30.053 |                        1.189 |
|    27 |       2624.67 |         2624.67 |        50 |           2351.659 |                     57.682 |             2409.341 |               47.033 |                        1.154 |
|    28 |        524.29 |          524.29 |        10 |            508.153 |                      9.606 |              517.759 |               50.815 |                        0.961 |
|    29 |       1002.30 |         1002.30 |        22 |            965.195 |                     22.644 |              987.840 |               43.873 |                        1.029 |
|    30 |       1013.96 |         1013.96 |        24 |            971.523 |                     27.571 |              999.094 |               40.480 |                        1.149 |
|    31 |       2572.60 |         2572.60 |        51 |           2487.155 |                     53.590 |             2540.745 |               48.768 |                        1.051 |
|    32 |       1658.24 |         1658.24 |        36 |           1595.829 |                     38.659 |             1634.487 |               44.329 |                        1.074 |
|    33 |        462.93 |          462.93 |        10 |            446.182 |                     10.099 |              456.282 |               44.618 |                        1.010 |
|    34 |        303.66 |          303.66 |         9 |            289.860 |                      8.211 |              298.071 |               32.207 |                        0.912 |
|    35 |       1015.10 |         1015.10 |        27 |            966.153 |                     32.147 |              998.299 |               35.783 |                        1.191 |
|    36 |        304.79 |          304.79 |         7 |            291.740 |                      7.689 |              299.429 |               41.677 |                        1.098 |
|    37 |        346.61 |          346.61 |        11 |            327.720 |                     11.753 |              339.473 |               29.793 |                        1.068 |
|    38 |        440.57 |          440.57 |        13 |            419.716 |                     12.547 |              432.264 |               32.286 |                        0.965 |
|    39 |       2014.51 |         2014.51 |        34 |           1956.027 |                     38.124 |             1994.151 |               57.530 |                        1.121 |
|    40 |       1038.26 |         1038.26 |        28 |            988.446 |                     31.589 |             1020.035 |               35.302 |                        1.128 |
|    41 |        662.27 |          662.27 |        10 |            646.370 |                     10.077 |              656.447 |               64.637 |                        1.008 |
|    42 |       2554.29 |         2554.29 |        51 |           2468.974 |                     53.525 |             2522.500 |               48.411 |                        1.050 |
|    43 |       1745.47 |         1745.47 |        27 |           1519.658 |                     28.610 |             1548.268 |               56.284 |                        1.060 |
|    44 |       2343.01 |         2343.01 |        51 |           2252.854 |                     59.174 |             2312.028 |               44.174 |                        1.160 |
|    45 |       1310.92 |         1310.92 |        34 |           1260.066 |                     29.919 |             1289.984 |               37.061 |                        0.880 |
|    46 |       1445.10 |         1445.10 |        24 |           1403.884 |                     26.502 |             1430.386 |               58.495 |                        1.104 |
|    47 |        564.45 |          564.45 |         9 |            549.373 |                      9.124 |              558.497 |               61.041 |                        1.014 |
|    48 |        727.63 |          727.63 |        16 |            700.439 |                     17.501 |              717.939 |               43.777 |                        1.094 |
|    49 |        517.07 |          517.07 |        10 |            501.217 |                      9.467 |              510.683 |               50.122 |                        0.947 |
|    50 |       1872.67 |         1872.67 |        42 |           1796.469 |                     50.503 |             1846.971 |               42.773 |                        1.202 |
```

## Reconnect details

No Jetson disconnects were recorded.
