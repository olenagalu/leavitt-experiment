# Circle study report

## Progress

- Study: `20260513-0017-circle-study`
- Status: complete
- Completed batches: 3/3
- Completed trials: 150/150
- Topologies: Circle
- Temperatures: 0, 0.5, 1

## Batch summary

| Topology | Temperature | Status   | Trials |  Success rate | Average total messages | Average time (seconds) | Detailed report                                              |
| -------- | ----------: | -------- | -----: | ------------: | ---------------------: | ---------------------: | ------------------------------------------------------------ |
| Circle   |           0 | complete |  50/50 | 20.0% (10/50) |                  12.36 |                  57.35 | [circle / temperature 0](circle/temperature-0/report.md)     |
| Circle   |         0.5 | complete |  50/50 | 34.0% (17/50) |                  12.00 |                  56.44 | [circle / temperature 0.5](circle/temperature-0.5/report.md) |
| Circle   |           1 | complete |  50/50 | 40.0% (20/50) |                  10.96 |                  51.49 | [circle / temperature 1](circle/temperature-1/report.md)     |

## Overall results

- Completed trials: 150/150
- Average time: 55.09 seconds
- Average total messages: 11.77
- Success rate: 47/150 (31.3%)

## Overall recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender.

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |   Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | ------------- |
| Agent1 | Agent2    |                  2 |      46 |                    390 | 11.8% (0.118) |
| Agent1 | Agent5    |                  2 |     344 |                    390 | 88.2% (0.882) |
| Agent2 | Agent1    |                  2 |     295 |                    373 | 79.1% (0.791) |
| Agent2 | Agent3    |                  2 |      78 |                    373 | 20.9% (0.209) |
| Agent3 | Agent2    |                  2 |     311 |                    322 | 96.6% (0.966) |
| Agent3 | Agent4    |                  2 |      11 |                    322 |  3.4% (0.034) |
| Agent4 | Agent3    |                  2 |     245 |                    335 | 73.1% (0.731) |
| Agent4 | Agent5    |                  2 |      90 |                    335 | 26.9% (0.269) |
| Agent5 | Agent1    |                  2 |     253 |                    346 | 73.1% (0.731) |
| Agent5 | Agent4    |                  2 |      93 |                    346 | 26.9% (0.269) |
```

### Excluded fallback routes

No fallback routes were recorded.

## Full success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- |
|     1 |           0 | Fail    | circle                                      | cross          |              7 |         214.90 |
|     2 |           0 | Success | circle                                      | circle         |             16 |          68.28 |
|     3 |           0 | Fail    | asterisk                                    | square         |             15 |          62.76 |
|     4 |           0 | Fail    | square                                      | circle         |             18 |          76.22 |
|     5 |           0 | Fail    | asterisk                                    | square         |              5 |          23.34 |
|     6 |           0 | Fail    | triangle                                    | circle         |             14 |          60.69 |
|     7 |           0 | Success | square                                      | square         |             19 |          82.48 |
|     8 |           0 | Success | diamond                                     | diamond        |              5 |          23.55 |
|     9 |           0 | Fail    | triangle                                    | square         |             13 |          56.96 |
|    10 |           0 | Success | cross                                       | cross          |             10 |          42.93 |
|    11 |           0 | Fail    | diamond                                     | triangle       |             10 |          44.96 |
|    12 |           0 | Fail    | circle                                      | triangle       |             10 |          43.01 |
|    13 |           0 | Fail    | diamond                                     | cross          |              7 |          30.62 |
|    14 |           0 | Fail    | triangle                                    | cross          |             19 |          83.48 |
|    15 |           0 | Fail    | cross                                       | asterisk       |             11 |          48.39 |
|    16 |           0 | Fail    | cross                                       | diamond        |             10 |          46.03 |
|    17 |           0 | Fail    | circle                                      | asterisk       |              5 |          23.63 |
|    18 |           0 | Fail    | cross                                       | triangle       |             10 |          42.42 |
|    19 |           0 | Fail    | cross                                       | diamond        |              7 |          31.57 |
|    20 |           0 | Success | cross                                       | cross          |             18 |          79.82 |
|    21 |           0 | Fail    | cross                                       | triangle       |             12 |          52.24 |
|    22 |           0 | Fail    | square                                      | asterisk       |             15 |          64.82 |
|    23 |           0 | Fail    | cross                                       | triangle       |             12 |          50.85 |
|    24 |           0 | Fail    | circle                                      | cross          |             14 |          64.87 |
|    25 |           0 | Fail    | diamond                                     | triangle       |              7 |          30.48 |
|    26 |           0 | Fail    | circle                                      | asterisk       |             18 |          76.17 |
|    27 |           0 | Fail    | diamond                                     | square         |             21 |          88.33 |
|    28 |           0 | Fail    | diamond                                     | triangle       |             14 |          59.38 |
|    29 |           0 | Fail    | square                                      | diamond        |             14 |          60.59 |
|    30 |           0 | Success | diamond                                     | diamond        |              5 |          23.67 |
|    31 |           0 | Fail    | asterisk                                    | circle         |             10 |          45.01 |
|    32 |           0 | Fail    | No figure submitted (message limit reached) | diamond        |             40 |         158.60 |
|    33 |           0 | Fail    | diamond                                     | asterisk       |             11 |          47.53 |
|    34 |           0 | Success | circle                                      | circle         |              5 |          23.84 |
|    35 |           0 | Fail    | cross                                       | circle         |             23 |          97.77 |
|    36 |           0 | Fail    | circle                                      | cross          |              7 |          30.96 |
|    37 |           0 | Fail    | triangle                                    | diamond        |              7 |          32.20 |
|    38 |           0 | Fail    | square                                      | triangle       |              5 |          23.11 |
|    39 |           0 | Fail    | cross                                       | diamond        |             11 |          47.33 |
|    40 |           0 | Fail    | square                                      | triangle       |             10 |          44.86 |
|    41 |           0 | Fail    | triangle                                    | asterisk       |             10 |          44.66 |
|    42 |           0 | Fail    | square                                      | diamond        |             15 |          68.01 |
|    43 |           0 | Fail    | circle                                      | asterisk       |              5 |          23.61 |
|    44 |           0 | Fail    | cross                                       | circle         |             15 |          63.14 |
|    45 |           0 | Success | square                                      | square         |             10 |          45.38 |
|    46 |           0 | Fail    | circle                                      | square         |             11 |          47.51 |
|    47 |           0 | Success | circle                                      | circle         |             10 |          43.48 |
|    48 |           0 | Fail    | square                                      | circle         |             22 |          94.44 |
|    49 |           0 | Success | triangle                                    | triangle       |             16 |          64.94 |
|    50 |           0 | Fail    | square                                      | diamond        |             14 |          63.82 |
|    51 |         0.5 | Fail    | cross                                       | asterisk       |              7 |         216.51 |
|    52 |         0.5 | Fail    | diamond                                     | square         |             14 |          62.22 |
|    53 |         0.5 | Success | circle                                      | circle         |             15 |          67.34 |
|    54 |         0.5 | Fail    | circle                                      | diamond        |              9 |          40.85 |
|    55 |         0.5 | Fail    | circle                                      | cross          |             10 |          43.82 |
|    56 |         0.5 | Fail    | cross                                       | triangle       |             14 |          59.31 |
|    57 |         0.5 | Fail    | circle                                      | triangle       |             10 |          45.20 |
|    58 |         0.5 | Success | triangle                                    | triangle       |             10 |          46.15 |
|    59 |         0.5 | Success | circle                                      | circle         |             10 |          43.16 |
|    60 |         0.5 | Fail    | cross                                       | triangle       |             11 |          48.03 |
|    61 |         0.5 | Success | circle                                      | circle         |              5 |          23.94 |
|    62 |         0.5 | Fail    | cross                                       | triangle       |              5 |          24.31 |
|    63 |         0.5 | Success | cross                                       | cross          |             19 |          83.28 |
|    64 |         0.5 | Success | circle                                      | circle         |              5 |          23.40 |
|    65 |         0.5 | Fail    | circle                                      | cross          |             10 |          44.61 |
|    66 |         0.5 | Success | triangle                                    | triangle       |             10 |          44.75 |
|    67 |         0.5 | Fail    | triangle                                    | asterisk       |             10 |          44.38 |
|    68 |         0.5 | Fail    | square                                      | circle         |             10 |          45.38 |
|    69 |         0.5 | Fail    | square                                      | asterisk       |             14 |          62.18 |
|    70 |         0.5 | Success | diamond                                     | diamond        |              5 |          23.00 |
|    71 |         0.5 | Fail    | circle                                      | asterisk       |              5 |          23.50 |
|    72 |         0.5 | Success | square                                      | square         |              5 |          22.97 |
|    73 |         0.5 | Fail    | cross                                       | triangle       |             10 |          44.22 |
|    74 |         0.5 | Fail    | circle                                      | diamond        |             18 |          73.97 |
|    75 |         0.5 | Fail    | square                                      | triangle       |             19 |          82.79 |
|    76 |         0.5 | Success | square                                      | square         |              7 |          31.34 |
|    77 |         0.5 | Success | square                                      | square         |             10 |          44.78 |
|    78 |         0.5 | Fail    | circle                                      | asterisk       |             10 |          43.19 |
|    79 |         0.5 | Success | square                                      | square         |             19 |          79.96 |
|    80 |         0.5 | Success | square                                      | square         |             10 |          45.14 |
|    81 |         0.5 | Fail    | circle                                      | asterisk       |             16 |          71.15 |
|    82 |         0.5 | Success | triangle                                    | triangle       |             11 |          49.92 |
|    83 |         0.5 | Fail    | square                                      | diamond        |             15 |          63.10 |
|    84 |         0.5 | Fail    | square                                      | diamond        |             18 |          77.07 |
|    85 |         0.5 | Fail    | square                                      | asterisk       |              5 |          23.76 |
|    86 |         0.5 | Fail    | square                                      | triangle       |             15 |          67.13 |
|    87 |         0.5 | Success | asterisk                                    | asterisk       |             25 |         104.81 |
|    88 |         0.5 | Fail    | square                                      | diamond        |              5 |          24.63 |
|    89 |         0.5 | Fail    | square                                      | triangle       |              5 |          23.68 |
|    90 |         0.5 | Fail    | circle                                      | square         |             10 |          45.90 |
|    91 |         0.5 | Fail    | triangle                                    | cross          |             15 |          65.06 |
|    92 |         0.5 | Fail    | cross                                       | asterisk       |              7 |          32.36 |
|    93 |         0.5 | Fail    | triangle                                    | asterisk       |             10 |          44.81 |
|    94 |         0.5 | Fail    | asterisk                                    | circle         |             35 |         145.30 |
|    95 |         0.5 | Fail    | square                                      | cross          |             20 |          83.31 |
|    96 |         0.5 | Fail    | triangle                                    | circle         |             10 |          46.79 |
|    97 |         0.5 | Fail    | triangle                                    | circle         |             23 |          98.96 |
|    98 |         0.5 | Success | circle                                      | circle         |             10 |          44.39 |
|    99 |         0.5 | Success | square                                      | square         |             11 |          51.04 |
|   100 |         0.5 | Fail    | triangle                                    | asterisk       |             18 |          75.31 |
|   101 |           1 | Fail    | asterisk                                    | circle         |             11 |         232.83 |
|   102 |           1 | Success | diamond                                     | diamond        |              8 |          35.48 |
|   103 |           1 | Fail    | square                                      | asterisk       |             11 |          48.18 |
|   104 |           1 | Fail    | asterisk                                    | diamond        |              7 |          30.67 |
|   105 |           1 | Success | square                                      | square         |             10 |          44.55 |
|   106 |           1 | Success | asterisk                                    | asterisk       |              7 |          32.38 |
|   107 |           1 | Fail    | triangle                                    | circle         |             11 |          47.18 |
|   108 |           1 | Fail    | circle                                      | triangle       |              5 |          23.67 |
|   109 |           1 | Success | circle                                      | circle         |             10 |          44.79 |
|   110 |           1 | Success | square                                      | square         |              7 |          30.78 |
|   111 |           1 | Fail    | diamond                                     | circle         |             10 |          42.24 |
|   112 |           1 | Success | circle                                      | circle         |              7 |          30.65 |
|   113 |           1 | Success | triangle                                    | triangle       |              7 |          30.56 |
|   114 |           1 | Fail    | cross                                       | asterisk       |             10 |          45.17 |
|   115 |           1 | Fail    | No figure submitted (message limit reached) | asterisk       |             40 |         161.38 |
|   116 |           1 | Fail    | cross                                       | asterisk       |             10 |          45.58 |
|   117 |           1 | Fail    | diamond                                     | square         |             37 |         152.69 |
|   118 |           1 | Fail    | diamond                                     | square         |             11 |          49.08 |
|   119 |           1 | Success | diamond                                     | diamond        |              5 |          23.00 |
|   120 |           1 | Success | cross                                       | cross          |             10 |          44.58 |
|   121 |           1 | Success | diamond                                     | diamond        |             14 |          60.06 |
|   122 |           1 | Fail    | cross                                       | square         |              7 |          32.76 |
|   123 |           1 | Fail    | triangle                                    | square         |             14 |          59.92 |
|   124 |           1 | Success | triangle                                    | triangle       |              5 |          24.16 |
|   125 |           1 | Fail    | square                                      | cross          |             14 |          58.27 |
|   126 |           1 | Fail    | asterisk                                    | triangle       |             18 |          76.91 |
|   127 |           1 | Fail    | circle                                      | diamond        |             15 |          65.04 |
|   128 |           1 | Success | diamond                                     | diamond        |              7 |          30.78 |
|   129 |           1 | Fail    | asterisk                                    | circle         |              8 |          35.71 |
|   130 |           1 | Fail    | asterisk                                    | circle         |             10 |          45.36 |
|   131 |           1 | Fail    | cross                                       | circle         |              5 |          22.86 |
|   132 |           1 | Success | square                                      | square         |             10 |          45.73 |
|   133 |           1 | Success | triangle                                    | triangle       |             12 |          51.38 |
|   134 |           1 | Fail    | diamond                                     | cross          |              7 |          30.54 |
|   135 |           1 | Fail    | triangle                                    | asterisk       |              5 |          23.93 |
|   136 |           1 | Success | diamond                                     | diamond        |             10 |          44.08 |
|   137 |           1 | Fail    | square                                      | asterisk       |              7 |          32.27 |
|   138 |           1 | Fail    | circle                                      | asterisk       |              5 |          24.14 |
|   139 |           1 | Fail    | triangle                                    | circle         |             10 |          44.04 |
|   140 |           1 | Fail    | diamond                                     | square         |              8 |          37.32 |
|   141 |           1 | Fail    | square                                      | asterisk       |             18 |          74.94 |
|   142 |           1 | Success | diamond                                     | diamond        |             10 |          42.94 |
|   143 |           1 | Fail    | cross                                       | diamond        |             10 |          44.49 |
|   144 |           1 | Success | square                                      | square         |             15 |          64.30 |
|   145 |           1 | Fail    | triangle                                    | square         |             10 |          44.50 |
|   146 |           1 | Success | circle                                      | circle         |              5 |          24.58 |
|   147 |           1 | Success | diamond                                     | diamond        |              8 |          36.39 |
|   148 |           1 | Success | square                                      | square         |             24 |         103.25 |
|   149 |           1 | Fail    | cross                                       | triangle       |              7 |          31.21 |
|   150 |           1 | Fail    | cross                                       | square         |             16 |          67.14 |
```

## Cooling and Jetson temperatures

- Pause between temperature batches: 5 minutes
- Temperature snapshots recorded: 12
- Raw temperature data: `temperatures.jsonl`

```text
| Recorded (UTC)                   | Phase            | Pause       | Agent1 C | Agent2 C | Agent3 C | Agent4 C | Agent5 C | Maximum C |
| -------------------------------- | ---------------- | ----------- | -------- | -------- | -------- | -------- | -------- | --------- |
| 2026-05-13T01:11:29.555476+00:00 | cooling_start    | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T01:12:30.073379+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T01:13:30.311794+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T01:14:30.732039+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T01:15:31.099274+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T01:16:29.898040+00:00 | cooling_end      | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:10:00.428269+00:00 | cooling_start    | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:11:00.843253+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:12:01.371503+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:13:02.040486+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:14:02.628504+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:15:00.757781+00:00 | cooling_end      | temperature |        - |        - |        - |        - |        - |         - |
```
