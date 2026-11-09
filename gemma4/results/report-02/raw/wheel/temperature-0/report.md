# Wheel auto-trial report

## Summary

- Batch: `temperature-0`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0
- Completed trials: 50/50
- Average time: 1592.64 seconds
- Average total messages: 35.64
- Average Gemma 4 thinking time per response: 42.021 seconds
- Average visible-response generation time: 0.994 seconds
- Average complete generation time: 43.015 seconds
- Success rate: 17/50 (34.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     334 |           334 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     344 |           344 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |     100 |           373 |        26.8% (0.268) |                0.250 | 1.072 |                0.268 |
| wheel    | Agent3 | Agent2    |                  4 |     115 |           373 |        30.8% (0.308) |                0.250 | 1.233 |                0.308 |
| wheel    | Agent3 | Agent4    |                  4 |     100 |           373 |        26.8% (0.268) |                0.250 | 1.072 |                0.268 |
| wheel    | Agent3 | Agent5    |                  4 |      58 |           373 |        15.5% (0.155) |                0.250 | 0.622 |                0.156 |
| wheel    | Agent4 | Agent3    |                  1 |     361 |           361 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     366 |           366 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source  | Count |
| -------- | ------ | -------------- | ----- |
| wheel    | Agent1 | client_default |     3 |
| wheel    | Agent5 | client_default |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           0 | Success | asterisk                                    | asterisk       |              6 |         151.97 |           0 |             0.00 |
|     2 |           0 | Fail    | square                                      | triangle       |             20 |         765.77 |           0 |             0.00 |
|     3 |           0 | Success | square                                      | square         |             22 |        1170.00 |           0 |             0.00 |
|     4 |           0 | Success | triangle                                    | triangle       |             34 |        1693.25 |           0 |             0.00 |
|     5 |           0 | Fail    | triangle                                    | circle         |             31 |        1130.59 |           0 |             0.00 |
|     6 |           0 | Fail    | cross                                       | diamond        |             42 |        1772.99 |           0 |             0.00 |
|     7 |           0 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2645.44 |           0 |             0.00 |
|     8 |           0 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        1897.08 |           0 |             0.00 |
|     9 |           0 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2065.01 |           0 |             0.00 |
|    10 |           0 | Success | cross                                       | cross          |             26 |         946.46 |           0 |             0.00 |
|    11 |           0 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        1902.27 |           0 |             0.00 |
|    12 |           0 | Success | triangle                                    | triangle       |              6 |         262.13 |           0 |             0.00 |
|    13 |           0 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2019.27 |           0 |             0.00 |
|    14 |           0 | Fail    | cross                                       | circle         |             48 |        2458.25 |           0 |             0.00 |
|    15 |           0 | Success | triangle                                    | triangle       |             12 |         554.94 |           0 |             0.00 |
|    16 |           0 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2736.81 |           0 |             0.00 |
|    17 |           0 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        1979.13 |           0 |             0.00 |
|    18 |           0 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        1908.91 |           0 |             0.00 |
|    19 |           0 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2338.16 |           0 |             0.00 |
|    20 |           0 | Success | circle                                      | circle         |             42 |        2306.55 |           0 |             0.00 |
|    21 |           0 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2720.67 |           0 |             0.00 |
|    22 |           0 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        1833.55 |           0 |             0.00 |
|    23 |           0 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2074.35 |           0 |             0.00 |
|    24 |           0 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2556.41 |           0 |             0.00 |
|    25 |           0 | Fail    | cross                                       | triangle       |              6 |         204.62 |           0 |             0.00 |
|    26 |           0 | Success | triangle                                    | triangle       |             12 |         320.83 |           0 |             0.00 |
|    27 |           0 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1991.22 |           0 |             0.00 |
|    28 |           0 | Success | triangle                                    | triangle       |              7 |         309.28 |           0 |             0.00 |
|    29 |           0 | Success | asterisk                                    | asterisk       |             24 |         757.02 |           0 |             0.00 |
|    30 |           0 | Success | asterisk                                    | asterisk       |             17 |         677.01 |           0 |             0.00 |
|    31 |           0 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2145.42 |           0 |             0.00 |
|    32 |           0 | Success | cross                                       | cross          |             18 |        1095.26 |           0 |             0.00 |
|    33 |           0 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2807.64 |           0 |             0.00 |
|    34 |           0 | Fail    | circle                                      | diamond        |             22 |        1079.31 |           0 |             0.00 |
|    35 |           0 | Fail    | square                                      | diamond        |             35 |        1546.97 |           0 |             0.00 |
|    36 |           0 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2137.57 |           0 |             0.00 |
|    37 |           0 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2610.28 |           0 |             0.00 |
|    38 |           0 | Success | diamond                                     | diamond        |              9 |         321.10 |           0 |             0.00 |
|    39 |           0 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2470.98 |           0 |             0.00 |
|    40 |           0 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2027.38 |           0 |             0.00 |
|    41 |           0 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2039.18 |           0 |             0.00 |
|    42 |           0 | Fail    | square                                      | circle         |             17 |         735.96 |           0 |             0.00 |
|    43 |           0 | Success | triangle                                    | triangle       |             37 |        1764.59 |           0 |             0.00 |
|    44 |           0 | Success | square                                      | square         |             38 |        1800.80 |           0 |             0.00 |
|    45 |           0 | Success | cross                                       | cross          |              6 |         237.13 |           0 |             0.00 |
|    46 |           0 | Success | circle                                      | circle         |             34 |        1593.66 |           0 |             0.00 |
|    47 |           0 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2322.35 |           0 |             0.00 |
|    48 |           0 | Fail    | circle                                      | triangle       |             22 |        1128.82 |           0 |             0.00 |
|    49 |           0 | Fail    | asterisk                                    | circle         |             39 |        2025.63 |           0 |             0.00 |
|    50 |           0 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1591.89 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |        169.58 |          169.58 |         7 |            158.599 |                      6.345 |              164.945 |               22.657 |                        0.906 |
|     2 |        782.29 |          782.29 |        21 |            748.742 |                     20.971 |              769.713 |               35.654 |                        0.999 |
|     3 |       1189.44 |         1189.44 |        23 |           1152.672 |                     22.845 |             1175.517 |               50.116 |                        0.993 |
|     4 |       1709.93 |         1709.93 |        35 |           1652.273 |                     37.240 |             1689.514 |               47.208 |                        1.064 |
|     5 |       1149.40 |         1149.40 |        32 |           1096.707 |                     32.643 |             1129.351 |               34.272 |                        1.020 |
|     6 |       1791.55 |         1791.55 |        43 |           1718.783 |                     47.138 |             1765.921 |               39.972 |                        1.096 |
|     7 |       2665.51 |         2665.51 |        53 |           2580.789 |                     51.956 |             2632.744 |               48.694 |                        0.980 |
|     8 |       1973.22 |         1973.22 |        51 |           1892.936 |                     48.388 |             1941.323 |               37.116 |                        0.949 |
|     9 |       2080.27 |         2080.27 |        50 |           1998.612 |                     51.255 |             2049.867 |               39.972 |                        1.025 |
|    10 |        965.68 |          965.68 |        27 |            922.137 |                     26.201 |              948.339 |               34.153 |                        0.970 |
|    11 |       1916.21 |         1916.21 |        50 |           1839.561 |                     45.875 |             1885.435 |               36.791 |                        0.917 |
|    12 |        277.12 |          277.12 |         7 |            266.825 |                      5.916 |              272.740 |               38.118 |                        0.845 |
|    13 |       2032.19 |         2032.19 |        51 |           1944.119 |                     55.396 |             1999.515 |               38.120 |                        1.086 |
|    14 |       2474.35 |         2474.35 |        51 |           2391.720 |                     51.072 |             2442.792 |               46.896 |                        1.001 |
|    15 |        572.63 |          572.63 |        13 |            550.815 |                     13.225 |              564.040 |               42.370 |                        1.017 |
|    16 |       2755.36 |         2755.36 |        52 |           2671.593 |                     52.052 |             2723.645 |               51.377 |                        1.001 |
|    17 |       1993.64 |         1993.64 |        50 |           1912.227 |                     50.010 |             1962.237 |               38.245 |                        1.000 |
|    18 |       1927.25 |         1927.25 |        50 |           1847.426 |                     47.544 |             1894.969 |               36.949 |                        0.951 |
|    19 |       2354.29 |         2354.29 |        51 |           2273.243 |                     49.931 |             2323.174 |               44.573 |                        0.979 |
|    20 |       2320.17 |         2320.17 |        44 |           2245.241 |                     48.118 |             2293.359 |               51.028 |                        1.094 |
|    21 |       2736.44 |         2736.44 |        52 |           2652.333 |                     50.050 |             2702.383 |               51.006 |                        0.963 |
|    22 |       1850.48 |         1850.48 |        51 |           1762.603 |                     57.553 |             1820.156 |               34.561 |                        1.128 |
|    23 |       2090.56 |         2090.56 |        50 |           2008.534 |                     51.020 |             2059.555 |               40.171 |                        1.020 |
|    24 |       2575.70 |         2575.70 |        53 |           2489.316 |                     53.425 |             2542.741 |               46.968 |                        1.008 |
|    25 |        221.04 |          221.04 |         7 |            210.578 |                      6.112 |              216.689 |               30.083 |                        0.873 |
|    26 |        341.62 |          341.62 |        13 |            320.486 |                     13.268 |              333.754 |               24.653 |                        1.021 |
|    27 |       2008.99 |         2008.99 |        50 |           1925.203 |                     52.812 |             1978.016 |               38.504 |                        1.056 |
|    28 |        327.16 |          327.16 |         8 |            313.880 |                      7.684 |              321.564 |               39.235 |                        0.960 |
|    29 |        773.23 |          773.23 |        25 |            733.813 |                     23.390 |              757.202 |               29.353 |                        0.936 |
|    30 |        692.29 |          692.29 |        18 |            663.927 |                     17.129 |              681.056 |               36.885 |                        0.952 |
|    31 |       2163.04 |         2163.04 |        51 |           2079.748 |                     50.417 |             2130.164 |               40.779 |                        0.989 |
|    32 |       1115.83 |         1115.83 |        21 |           1085.899 |                     16.368 |             1102.267 |               51.709 |                        0.779 |
|    33 |       2824.76 |         2824.76 |        51 |           2378.158 |                     52.616 |             2430.774 |               46.631 |                        1.032 |
|    34 |       1096.03 |         1096.03 |        23 |           1061.010 |                     20.394 |             1081.404 |               46.131 |                        0.887 |
|    35 |       1620.36 |         1620.36 |        36 |           1562.916 |                     34.358 |             1597.274 |               43.414 |                        0.954 |
|    36 |       2154.29 |         2154.29 |        52 |           2071.695 |                     50.615 |             2122.310 |               39.840 |                        0.973 |
|    37 |       2686.73 |         2686.73 |        52 |           2601.254 |                     52.506 |             2653.759 |               50.024 |                        1.010 |
|    38 |        338.95 |          338.95 |        10 |            323.526 |                      9.139 |              332.665 |               32.353 |                        0.914 |
|    39 |       2489.83 |         2489.83 |        50 |           2408.690 |                     50.844 |             2459.534 |               48.174 |                        1.017 |
|    40 |       2102.73 |         2102.73 |        50 |           2025.697 |                     45.562 |             2071.259 |               40.514 |                        0.911 |
|    41 |       2056.48 |         2056.48 |        50 |           1977.087 |                     47.735 |             2024.822 |               39.542 |                        0.955 |
|    42 |        753.58 |          753.58 |        19 |            725.094 |                     17.213 |              742.306 |               38.163 |                        0.906 |
|    43 |       1781.08 |         1781.08 |        40 |           1715.941 |                     40.269 |             1756.210 |               42.899 |                        1.007 |
|    44 |       1818.38 |         1818.38 |        40 |           1753.968 |                     39.215 |             1793.183 |               43.849 |                        0.980 |
|    45 |        255.75 |          255.75 |         7 |            245.920 |                      5.661 |              251.581 |               35.131 |                        0.809 |
|    46 |       1612.27 |         1612.27 |        36 |           1553.878 |                     35.451 |             1589.328 |               43.163 |                        0.985 |
|    47 |       2398.85 |         2398.85 |        50 |           2135.195 |                     50.545 |             2185.740 |               42.704 |                        1.011 |
|    48 |       1201.10 |         1201.10 |        24 |           1161.223 |                     23.826 |             1185.049 |               48.384 |                        0.993 |
|    49 |       2044.27 |         2044.27 |        40 |           1980.412 |                     38.796 |             2019.208 |               49.510 |                        0.970 |
|    50 |       1606.85 |         1606.85 |        50 |           1525.761 |                     49.953 |             1575.713 |               30.515 |                        0.999 |
```

## Reconnect details

No Jetson disconnects were recorded.
