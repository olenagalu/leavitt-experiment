# Circle auto-trial report

## Summary

- Batch: `temperature-1`
- Model: `gemma4:e2b-it-qat`
- Temperature: 1
- Completed trials: 50/50
- Average time: 1030.52 seconds
- Average total messages: 18.02
- Average Gemma 4 thinking time per response: 51.461 seconds
- Average visible-response generation time: 1.138 seconds
- Average complete generation time: 52.599 seconds
- Success rate: 24/50 (48.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| circle   | Agent1 | Agent2    |                  2 |      80 |           182 |        44.0% (0.440) |                0.500 | 0.879 |                0.440 |
| circle   | Agent1 | Agent5    |                  2 |     102 |           182 |        56.0% (0.560) |                0.500 | 1.121 |                0.560 |
| circle   | Agent2 | Agent1    |                  2 |      93 |           186 |        50.0% (0.500) |                0.500 | 1.000 |                0.500 |
| circle   | Agent2 | Agent3    |                  2 |      93 |           186 |        50.0% (0.500) |                0.500 | 1.000 |                0.500 |
| circle   | Agent3 | Agent2    |                  2 |      88 |           172 |        51.2% (0.512) |                0.500 | 1.023 |                0.512 |
| circle   | Agent3 | Agent4    |                  2 |      84 |           172 |        48.8% (0.488) |                0.500 | 0.977 |                0.488 |
| circle   | Agent4 | Agent3    |                  2 |     104 |           183 |        56.8% (0.568) |                0.500 | 1.137 |                0.568 |
| circle   | Agent4 | Agent5    |                  2 |      79 |           183 |        43.2% (0.432) |                0.500 | 0.863 |                0.432 |
| circle   | Agent5 | Agent1    |                  2 |      78 |           176 |        44.3% (0.443) |                0.500 | 0.886 |                0.444 |
| circle   | Agent5 | Agent4    |                  2 |      98 |           176 |        55.7% (0.557) |                0.500 | 1.114 |                0.556 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source          | Count |
| -------- | ------ | ---------------------- | ----- |
| circle   | Agent1 | client_default_invalid |     1 |
| circle   | Agent3 | client_default         |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           1 | Fail    | square           | diamond        |             12 |         340.82 |           0 |             0.00 |
|     2 |           1 | Fail    | circle           | diamond        |             13 |         629.95 |           0 |             0.00 |
|     3 |           1 | Fail    | circle           | cross          |             11 |         430.00 |           0 |             0.00 |
|     4 |           1 | Success | asterisk         | asterisk       |             27 |        1785.69 |           0 |             0.00 |
|     5 |           1 | Fail    | circle           | triangle       |             25 |        1206.22 |           0 |             0.00 |
|     6 |           1 | Fail    | diamond          | triangle       |             14 |         672.78 |           0 |             0.00 |
|     7 |           1 | Success | diamond          | diamond        |             21 |        1227.38 |           0 |             0.00 |
|     8 |           1 | Fail    | diamond          | triangle       |             13 |         563.90 |           0 |             0.00 |
|     9 |           1 | Success | cross            | cross          |             18 |         965.55 |           0 |             0.00 |
|    10 |           1 | Success | cross            | cross          |             17 |         812.98 |           0 |             0.00 |
|    11 |           1 | Success | triangle         | triangle       |             14 |         496.34 |           0 |             0.00 |
|    12 |           1 | Fail    | cross            | circle         |             36 |        2062.85 |           0 |             0.00 |
|    13 |           1 | Success | triangle         | triangle       |             10 |         426.89 |           0 |             0.00 |
|    14 |           1 | Success | cross            | cross          |             18 |         746.92 |           0 |             0.00 |
|    15 |           1 | Fail    | diamond          | asterisk       |             12 |         604.46 |           0 |             0.00 |
|    16 |           1 | Success | square           | square         |             24 |        1092.06 |           0 |             0.00 |
|    17 |           1 | Success | asterisk         | asterisk       |             11 |         562.08 |           0 |             0.00 |
|    18 |           1 | Success | cross            | cross          |             20 |        1282.81 |           0 |             0.00 |
|    19 |           1 | Fail    | triangle         | circle         |              9 |         523.86 |           0 |             0.00 |
|    20 |           1 | Fail    | diamond          | triangle       |             15 |         699.85 |           0 |             0.00 |
|    21 |           1 | Fail    | cross            | circle         |             13 |         876.44 |           0 |             0.00 |
|    22 |           1 | Success | cross            | cross          |             24 |        1388.60 |           0 |             0.00 |
|    23 |           1 | Success | cross            | cross          |              5 |         274.52 |           0 |             0.00 |
|    24 |           1 | Fail    | diamond          | triangle       |              6 |         278.68 |           0 |             0.00 |
|    25 |           1 | Fail    | cross            | asterisk       |             34 |        1690.35 |           0 |             0.00 |
|    26 |           1 | Success | square           | square         |             15 |         848.93 |           0 |             0.00 |
|    27 |           1 | Success | cross            | cross          |             21 |        1362.59 |           0 |             0.00 |
|    28 |           1 | Fail    | triangle         | diamond        |             13 |         671.40 |           0 |             0.00 |
|    29 |           1 | Success | circle           | circle         |             15 |         853.86 |           0 |             0.00 |
|    30 |           1 | Fail    | asterisk         | circle         |             30 |        1635.19 |           0 |             0.00 |
|    31 |           1 | Fail    | circle           | cross          |             23 |        1345.34 |           0 |             0.00 |
|    32 |           1 | Success | diamond          | diamond        |             25 |        1703.54 |           0 |             0.00 |
|    33 |           1 | Fail    | circle           | square         |              9 |         827.76 |           0 |             0.00 |
|    34 |           1 | Fail    | square           | diamond        |             16 |         779.15 |           0 |             0.00 |
|    35 |           1 | Fail    | circle           | diamond        |             29 |        1486.71 |           0 |             0.00 |
|    36 |           1 | Success | square           | square         |             19 |        1567.19 |           0 |             0.00 |
|    37 |           1 | Success | square           | square         |             24 |        1355.21 |           0 |             0.00 |
|    38 |           1 | Fail    | asterisk         | cross          |             18 |        1169.12 |           0 |             0.00 |
|    39 |           1 | Success | diamond          | diamond        |             20 |        1111.56 |           0 |             0.00 |
|    40 |           1 | Success | cross            | cross          |             16 |         806.14 |           0 |             0.00 |
|    41 |           1 | Success | triangle         | triangle       |             13 |         801.12 |           0 |             0.00 |
|    42 |           1 | Fail    | square           | asterisk       |             19 |        1402.93 |           0 |             0.00 |
|    43 |           1 | Fail    | square           | cross          |             11 |         809.20 |           0 |             0.00 |
|    44 |           1 | Fail    | triangle         | cross          |             13 |         546.76 |           0 |             0.00 |
|    45 |           1 | Fail    | cross            | triangle       |             27 |        1705.68 |           0 |             0.00 |
|    46 |           1 | Success | triangle         | triangle       |             27 |        1803.65 |           0 |             0.00 |
|    47 |           1 | Success | asterisk         | asterisk       |             15 |         720.21 |           0 |             0.00 |
|    48 |           1 | Success | square           | square         |             32 |        2652.29 |           0 |             0.00 |
|    49 |           1 | Fail    | cross            | triangle       |             19 |        1375.14 |           0 |             0.00 |
|    50 |           1 | Fail    | asterisk         | triangle       |             10 |         543.36 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |        389.85 |          389.85 |        14 |            363.170 |                     17.682 |              380.852 |               25.941 |                        1.263 |
|     2 |        646.12 |          646.12 |        14 |            622.369 |                     15.365 |              637.735 |               44.455 |                        1.098 |
|     3 |        446.13 |          446.13 |        12 |            427.358 |                     10.839 |              438.196 |               35.613 |                        0.903 |
|     4 |       1801.59 |         1801.59 |        28 |           1748.784 |                     35.224 |             1784.009 |               62.457 |                        1.258 |
|     5 |       1221.33 |         1221.33 |        26 |           1173.913 |                     30.705 |             1204.618 |               45.150 |                        1.181 |
|     6 |        746.18 |          746.18 |        15 |            722.464 |                     14.884 |              737.348 |               48.164 |                        0.992 |
|     7 |       1243.39 |         1243.39 |        22 |           1204.851 |                     25.098 |             1229.949 |               54.766 |                        1.141 |
|     8 |        638.58 |          638.58 |        14 |            612.883 |                     16.005 |              628.888 |               43.777 |                        1.143 |
|     9 |        988.27 |          988.27 |        19 |            953.895 |                     21.016 |              974.911 |               50.205 |                        1.106 |
|    10 |        827.28 |          827.28 |        18 |            796.794 |                     18.508 |              815.302 |               44.266 |                        1.028 |
|    11 |        511.80 |          511.80 |        15 |            485.296 |                     16.972 |              502.268 |               32.353 |                        1.131 |
|    12 |       2079.35 |         2079.35 |        37 |           2009.452 |                     46.993 |             2056.445 |               54.310 |                        1.270 |
|    13 |        495.23 |          495.23 |        11 |            476.674 |                     11.206 |              487.879 |               43.334 |                        1.019 |
|    14 |        761.54 |          761.54 |        19 |            727.235 |                     22.627 |              749.861 |               38.276 |                        1.191 |
|    15 |        620.59 |          620.59 |        13 |            598.169 |                     14.435 |              612.604 |               46.013 |                        1.110 |
|    16 |       1106.70 |         1106.70 |        25 |           1063.466 |                     26.482 |             1089.947 |               42.539 |                        1.059 |
|    17 |        582.02 |          582.02 |        12 |            562.446 |                     12.776 |              575.222 |               46.870 |                        1.065 |
|    18 |       1364.97 |         1364.97 |        21 |           1327.275 |                     24.470 |             1351.745 |               63.204 |                        1.165 |
|    19 |        542.23 |          542.23 |        10 |            525.445 |                     10.517 |              535.962 |               52.545 |                        1.052 |
|    20 |        714.05 |          714.05 |        16 |            689.638 |                     14.161 |              703.799 |               43.102 |                        0.885 |
|    21 |        892.57 |          892.57 |        15 |            862.843 |                     19.949 |              882.792 |               57.523 |                        1.330 |
|    22 |       1473.25 |         1473.25 |        25 |           1425.894 |                     30.537 |             1456.431 |               57.036 |                        1.221 |
|    23 |        291.74 |          291.74 |         6 |            282.700 |                      5.404 |              288.104 |               47.117 |                        0.901 |
|    24 |        288.51 |          288.51 |         7 |            277.655 |                      6.682 |              284.337 |               39.665 |                        0.955 |
|    25 |       1706.34 |         1706.34 |        35 |           1642.574 |                     41.799 |             1684.373 |               46.931 |                        1.194 |
|    26 |        868.86 |          868.86 |        16 |            688.979 |                     18.666 |              707.645 |               43.061 |                        1.167 |
|    27 |       1416.52 |         1416.52 |        22 |            969.831 |                     25.197 |              995.028 |               44.083 |                        1.145 |
|    28 |        686.56 |          686.56 |        14 |            663.687 |                     14.346 |              678.033 |               47.406 |                        1.025 |
|    29 |        933.58 |          933.58 |        16 |            895.797 |                     16.276 |              912.073 |               55.987 |                        1.017 |
|    30 |       1646.80 |         1646.80 |        31 |           1573.478 |                     36.246 |             1609.724 |               50.757 |                        1.169 |
|    31 |       1420.43 |         1420.43 |        24 |           1192.530 |                     27.408 |             1219.938 |               49.689 |                        1.142 |
|    32 |       1776.65 |         1776.65 |        26 |           1732.851 |                     27.724 |             1760.574 |               66.648 |                        1.066 |
|    33 |        901.61 |          901.61 |        10 |            698.557 |                     10.361 |              708.918 |               69.856 |                        1.036 |
|    34 |        791.84 |          791.84 |        17 |            762.096 |                     19.426 |              781.522 |               44.829 |                        1.143 |
|    35 |       1505.26 |         1505.26 |        30 |           1393.730 |                     35.637 |             1429.367 |               46.458 |                        1.188 |
|    36 |       1582.83 |         1582.83 |        20 |           1336.114 |                     24.451 |             1360.565 |               66.806 |                        1.223 |
|    37 |       1434.17 |         1434.17 |        25 |           1201.459 |                     30.334 |             1231.794 |               48.058 |                        1.213 |
|    38 |       1243.09 |         1243.09 |        19 |           1121.182 |                     20.981 |             1142.163 |               59.010 |                        1.104 |
|    39 |       1198.27 |         1198.27 |        21 |           1160.877 |                     24.833 |             1185.710 |               55.280 |                        1.183 |
|    40 |        826.69 |          826.69 |        17 |            795.925 |                     20.138 |              816.063 |               46.819 |                        1.185 |
|    41 |        816.50 |          816.50 |        14 |            691.771 |                     15.005 |              706.776 |               49.412 |                        1.072 |
|    42 |       1419.77 |         1419.77 |        20 |           1109.026 |                     22.701 |             1131.727 |               55.451 |                        1.135 |
|    43 |        830.04 |          830.04 |        12 |            690.147 |                     10.786 |              700.934 |               57.512 |                        0.899 |
|    44 |        623.68 |          623.68 |        14 |            598.737 |                     15.538 |              614.275 |               42.767 |                        1.110 |
|    45 |       1904.17 |         1904.17 |        28 |           1656.908 |                     33.626 |             1690.534 |               59.175 |                        1.201 |
|    46 |       1817.99 |         1817.99 |        28 |           1707.196 |                     31.400 |             1738.597 |               60.971 |                        1.121 |
|    47 |        734.25 |          734.25 |        16 |            660.388 |                     17.804 |              678.192 |               41.274 |                        1.113 |
|    48 |       2667.78 |         2667.78 |        33 |           2474.321 |                     39.772 |             2514.093 |               74.979 |                        1.205 |
|    49 |       1385.58 |         1385.58 |        20 |           1139.897 |                     23.862 |             1163.759 |               56.995 |                        1.193 |
|    50 |        748.83 |          748.83 |        11 |            543.815 |                     11.537 |              555.353 |               49.438 |                        1.049 |
```

## Reconnect details

No Jetson disconnects were recorded.
