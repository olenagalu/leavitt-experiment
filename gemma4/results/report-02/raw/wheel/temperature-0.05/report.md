# Wheel auto-trial report

## Summary

- Batch: `temperature-0.05`
- Model: `gemma4:e2b-it-qat`
- Temperature: 0.05
- Completed trials: 50/50
- Average time: 1663.13 seconds
- Average total messages: 35.28
- Average Gemma 4 thinking time per response: 43.642 seconds
- Average visible-response generation time: 0.999 seconds
- Average complete generation time: 44.641 seconds
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
| wheel    | Agent2 | Agent3    |                  1 |     341 |           341 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |      95 |           330 |        28.8% (0.288) |                0.250 | 1.152 |                0.288 |
| wheel    | Agent3 | Agent2    |                  4 |      94 |           330 |        28.5% (0.285) |                0.250 | 1.139 |                0.285 |
| wheel    | Agent3 | Agent4    |                  4 |      93 |           330 |        28.2% (0.282) |                0.250 | 1.127 |                0.282 |
| wheel    | Agent3 | Agent5    |                  4 |      48 |           330 |        14.5% (0.145) |                0.250 | 0.582 |                0.146 |
| wheel    | Agent4 | Agent3    |                  1 |     366 |           366 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     377 |           377 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| wheel    | Agent3 | client_assigned |     1 |
| wheel    | Agent5 | client_assigned |     1 |
| wheel    | Agent5 | client_default  |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |        0.05 | Fail    | diamond                                     | circle         |             41 |        1777.83 |           0 |             0.00 |
|     2 |        0.05 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2141.69 |           0 |             0.00 |
|     3 |        0.05 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2836.98 |           0 |             0.00 |
|     4 |        0.05 | Success | diamond                                     | diamond        |             35 |        1237.29 |           0 |             0.00 |
|     5 |        0.05 | Fail    | asterisk                                    | circle         |             23 |         892.24 |           0 |             0.00 |
|     6 |        0.05 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2092.04 |           0 |             0.00 |
|     7 |        0.05 | Success | square                                      | square         |              5 |         161.75 |           0 |             0.00 |
|     8 |        0.05 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2810.02 |           0 |             0.00 |
|     9 |        0.05 | Success | circle                                      | circle         |             46 |        2515.84 |           0 |             0.00 |
|    10 |        0.05 | Fail    | cross                                       | triangle       |             46 |        2198.30 |           0 |             0.00 |
|    11 |        0.05 | Success | asterisk                                    | asterisk       |              8 |         199.40 |           0 |             0.00 |
|    12 |        0.05 | Success | circle                                      | circle         |             44 |        1882.82 |           0 |             0.00 |
|    13 |        0.05 | Fail    | No figure submitted (message limit reached) | square         |             50 |        2202.03 |           0 |             0.00 |
|    14 |        0.05 | Success | circle                                      | circle         |              6 |         314.00 |           0 |             0.00 |
|    15 |        0.05 | Success | square                                      | square         |             20 |         800.54 |           0 |             0.00 |
|    16 |        0.05 | Success | diamond                                     | diamond        |              9 |         510.96 |           0 |             0.00 |
|    17 |        0.05 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2091.16 |           0 |             0.00 |
|    18 |        0.05 | Success | cross                                       | cross          |             37 |        1182.77 |           0 |             0.00 |
|    19 |        0.05 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        1775.90 |           0 |             0.00 |
|    20 |        0.05 | Fail    | asterisk                                    | cross          |             48 |        2224.91 |           0 |             0.00 |
|    21 |        0.05 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2226.83 |           0 |             0.00 |
|    22 |        0.05 | Success | square                                      | square         |             32 |        1705.16 |           0 |             0.00 |
|    23 |        0.05 | Fail    | triangle                                    | circle         |             37 |        1748.53 |           0 |             0.00 |
|    24 |        0.05 | Success | diamond                                     | diamond        |             35 |        1504.59 |           0 |             0.00 |
|    25 |        0.05 | Success | triangle                                    | triangle       |             16 |         825.91 |           0 |             0.00 |
|    26 |        0.05 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2660.63 |           0 |             0.00 |
|    27 |        0.05 | Fail    | circle                                      | cross          |             31 |        1922.52 |           0 |             0.00 |
|    28 |        0.05 | Success | asterisk                                    | asterisk       |             28 |         989.71 |           0 |             0.00 |
|    29 |        0.05 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2197.52 |           0 |             0.00 |
|    30 |        0.05 | Success | triangle                                    | triangle       |             30 |        1558.89 |           0 |             0.00 |
|    31 |        0.05 | Fail    | asterisk                                    | cross          |             12 |         745.91 |           0 |             0.00 |
|    32 |        0.05 | Success | triangle                                    | triangle       |             17 |         686.19 |           0 |             0.00 |
|    33 |        0.05 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2373.22 |           0 |             0.00 |
|    34 |        0.05 | Fail    | triangle                                    | diamond        |             30 |        1061.43 |           0 |             0.00 |
|    35 |        0.05 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2998.27 |           0 |             0.00 |
|    36 |        0.05 | Fail    | triangle                                    | circle         |             33 |        2327.80 |           0 |             0.00 |
|    37 |        0.05 | Fail    | diamond                                     | cross          |             20 |         809.57 |           0 |             0.00 |
|    38 |        0.05 | Success | square                                      | square         |             43 |        2122.42 |           0 |             0.00 |
|    39 |        0.05 | Success | cross                                       | cross          |              6 |         239.67 |           0 |             0.00 |
|    40 |        0.05 | Fail    | square                                      | triangle       |             40 |        1707.67 |           0 |             0.00 |
|    41 |        0.05 | Success | square                                      | square         |             37 |        1758.99 |           0 |             0.00 |
|    42 |        0.05 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        2718.06 |           0 |             0.00 |
|    43 |        0.05 | Success | circle                                      | circle         |             21 |        1049.15 |           0 |             0.00 |
|    44 |        0.05 | Fail    | No figure submitted (message limit reached) | cross          |             50 |        2453.95 |           0 |             0.00 |
|    45 |        0.05 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2447.75 |           0 |             0.00 |
|    46 |        0.05 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2163.31 |           0 |             0.00 |
|    47 |        0.05 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2684.25 |           0 |             0.00 |
|    48 |        0.05 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        1990.69 |           0 |             0.00 |
|    49 |        0.05 | Success | diamond                                     | diamond        |             21 |         993.16 |           0 |             0.00 |
|    50 |        0.05 | Fail    | asterisk                                    | circle         |              7 |         636.34 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |       1796.01 |         1796.01 |        43 |           1724.655 |                     44.876 |             1769.531 |               40.108 |                        1.044 |
|     2 |       2162.00 |         2162.00 |        52 |           2081.701 |                     49.304 |             2131.004 |               40.033 |                        0.948 |
|     3 |       2856.19 |         2856.19 |        54 |           2769.770 |                     51.968 |             2821.739 |               51.292 |                        0.962 |
|     4 |       1254.04 |         1254.04 |        36 |           1199.217 |                     32.490 |             1231.707 |               33.312 |                        0.902 |
|     5 |        912.14 |          912.14 |        24 |            875.979 |                     21.456 |              897.435 |               36.499 |                        0.894 |
|     6 |       2105.05 |         2105.05 |        52 |           2023.998 |                     49.175 |             2073.173 |               38.923 |                        0.946 |
|     7 |        180.16 |          180.16 |         6 |            171.076 |                      5.080 |              176.156 |               28.513 |                        0.847 |
|     8 |       2826.91 |         2826.91 |        51 |           2742.126 |                     53.748 |             2795.874 |               53.767 |                        1.054 |
|     9 |       2533.43 |         2533.43 |        47 |           2446.007 |                     57.161 |             2503.169 |               52.043 |                        1.216 |
|    10 |       2215.57 |         2215.57 |        48 |           1958.078 |                     46.972 |             2005.049 |               40.793 |                        0.979 |
|    11 |        276.63 |          276.63 |         9 |            263.564 |                      7.700 |              271.264 |               29.285 |                        0.856 |
|    12 |       1900.89 |         1900.89 |        45 |           1824.352 |                     49.068 |             1873.420 |               40.541 |                        1.090 |
|    13 |       2276.11 |         2276.11 |        50 |           2187.487 |                     56.994 |             2244.481 |               43.750 |                        1.140 |
|    14 |        330.82 |          330.82 |         7 |            320.023 |                      6.626 |              326.649 |               45.718 |                        0.947 |
|    15 |        877.68 |          877.68 |        21 |            842.722 |                     22.070 |              864.792 |               40.130 |                        1.051 |
|    16 |        527.31 |          527.31 |        11 |            512.052 |                      8.723 |              520.774 |               46.550 |                        0.793 |
|    17 |       2108.63 |         2108.63 |        50 |           2027.298 |                     50.769 |             2078.068 |               40.546 |                        1.015 |
|    18 |       1199.51 |         1199.51 |        38 |           1139.008 |                     36.634 |             1175.642 |               29.974 |                        0.964 |
|    19 |       1794.75 |         1794.75 |        50 |           1711.330 |                     52.302 |             1763.632 |               34.227 |                        1.046 |
|    20 |       2244.90 |         2244.90 |        49 |           2162.444 |                     52.496 |             2214.940 |               44.132 |                        1.071 |
|    21 |       2247.04 |         2247.04 |        51 |           2166.882 |                     48.631 |             2215.512 |               42.488 |                        0.954 |
|    22 |       1725.33 |         1725.33 |        33 |           1488.218 |                     36.122 |             1524.340 |               45.098 |                        1.095 |
|    23 |       1765.81 |         1765.81 |        38 |           1703.189 |                     38.450 |             1741.639 |               44.821 |                        1.012 |
|    24 |       1584.59 |         1584.59 |        36 |           1525.101 |                     37.495 |             1562.596 |               42.364 |                        1.042 |
|    25 |        901.83 |          901.83 |        17 |            873.185 |                     18.558 |              891.743 |               51.364 |                        1.092 |
|    26 |       2676.28 |         2676.28 |        53 |           2591.050 |                     52.708 |             2643.758 |               48.888 |                        0.995 |
|    27 |       1998.28 |         1998.28 |        34 |           1945.842 |                     30.890 |             1976.732 |               57.231 |                        0.909 |
|    28 |       1009.59 |         1009.59 |        29 |            962.433 |                     29.061 |              991.494 |               33.187 |                        1.002 |
|    29 |       2216.49 |         2216.49 |        51 |           2130.093 |                     54.889 |             2184.982 |               41.767 |                        1.076 |
|    30 |       1635.89 |         1635.89 |        31 |           1582.026 |                     34.736 |             1616.762 |               51.033 |                        1.121 |
|    31 |        764.63 |          764.63 |        15 |            743.813 |                     11.535 |              755.348 |               49.588 |                        0.769 |
|    32 |        765.29 |          765.29 |        18 |            737.809 |                     16.280 |              754.089 |               40.989 |                        0.904 |
|    33 |       2391.20 |         2391.20 |        50 |           2130.395 |                     48.909 |             2179.304 |               42.608 |                        0.978 |
|    34 |       1077.72 |         1077.72 |        31 |           1026.728 |                     30.899 |             1057.627 |               33.120 |                        0.997 |
|    35 |       3073.56 |         3073.56 |        52 |           2635.020 |                     45.951 |             2680.971 |               50.673 |                        0.884 |
|    36 |       2347.22 |         2347.22 |        36 |           2108.627 |                     35.902 |             2144.529 |               58.573 |                        0.997 |
|    37 |        827.37 |          827.37 |        21 |            793.014 |                     20.909 |              813.923 |               37.763 |                        0.996 |
|    38 |       2138.26 |         2138.26 |        44 |           2067.732 |                     43.193 |             2110.924 |               46.994 |                        0.982 |
|    39 |        317.99 |          317.99 |         7 |            307.606 |                      6.209 |              313.814 |               43.944 |                        0.887 |
|    40 |       1724.85 |         1724.85 |        41 |           1653.309 |                     46.041 |             1699.350 |               40.325 |                        1.123 |
|    41 |       1775.42 |         1775.42 |        39 |           1713.590 |                     37.111 |             1750.701 |               43.938 |                        0.952 |
|    42 |       2733.97 |         2733.97 |        51 |           2468.976 |                     52.878 |             2521.854 |               48.411 |                        1.037 |
|    43 |       1068.17 |         1068.17 |        22 |           1033.799 |                     20.018 |             1053.818 |               46.991 |                        0.910 |
|    44 |       2469.84 |         2469.84 |        51 |           2210.074 |                     46.818 |             2256.892 |               43.335 |                        0.918 |
|    45 |       2467.01 |         2467.01 |        52 |           2382.363 |                     52.355 |             2434.719 |               45.815 |                        1.007 |
|    46 |       2179.63 |         2179.63 |        50 |           2093.956 |                     52.819 |             2146.774 |               41.879 |                        1.056 |
|    47 |       2701.09 |         2701.09 |        51 |           2438.441 |                     48.736 |             2487.176 |               47.813 |                        0.956 |
|    48 |       2009.65 |         2009.65 |        51 |           1930.958 |                     46.646 |             1977.604 |               37.862 |                        0.915 |
|    49 |       1012.42 |         1012.42 |        23 |            976.782 |                     21.171 |              997.953 |               42.469 |                        0.920 |
|    50 |        654.10 |          654.10 |         9 |            460.747 |                      6.344 |              467.091 |               51.194 |                        0.705 |
```

## Reconnect details

No Jetson disconnects were recorded.
