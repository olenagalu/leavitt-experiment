# Wheel auto-trial report

## Summary

- Batch: `temperature-1`
- Model: `gemma4:e2b-it-qat`
- Temperature: 1
- Completed trials: 25/50
- Average time: 1483.69 seconds
- Average total messages: 31.60
- Average Gemma 4 thinking time per response: 44.327 seconds
- Average visible-response generation time: 1.125 seconds
- Average complete generation time: 45.452 seconds
- Success rate: 12/25 (48.0%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| wheel    | Agent1 | Agent3    |                  1 |     160 |           160 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent2 | Agent3    |                  1 |     148 |           148 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent3 | Agent1    |                  4 |      48 |           149 |        32.2% (0.322) |                0.250 | 1.289 |                0.321 |
| wheel    | Agent3 | Agent2    |                  4 |      36 |           149 |        24.2% (0.242) |                0.250 | 0.966 |                0.242 |
| wheel    | Agent3 | Agent4    |                  4 |      34 |           149 |        22.8% (0.228) |                0.250 | 0.913 |                0.228 |
| wheel    | Agent3 | Agent5    |                  4 |      31 |           149 |        20.8% (0.208) |                0.250 | 0.832 |                0.209 |
| wheel    | Agent4 | Agent3    |                  1 |     169 |           169 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| wheel    | Agent5 | Agent3    |                  1 |     160 |           160 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source          | Count |
| -------- | ------ | ---------------------- | ----- |
| wheel    | Agent2 | client_default         |     1 |
| wheel    | Agent3 | client_default_invalid |     1 |
| wheel    | Agent4 | client_assigned        |     2 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) | Disconnects | Paused (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- | ----------- | ---------------- |
|     1 |           1 | Success | cross                                       | cross          |              9 |         314.30 |           0 |             0.00 |
|     2 |           1 | Fail    | diamond                                     | circle         |             35 |        1502.17 |           0 |             0.00 |
|     3 |           1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2527.37 |           0 |             0.00 |
|     4 |           1 | Success | triangle                                    | triangle       |             31 |        1683.37 |           0 |             0.00 |
|     5 |           1 | Success | cross                                       | cross          |             20 |         907.59 |           0 |             0.00 |
|     6 |           1 | Success | triangle                                    | triangle       |              9 |         415.09 |           0 |             0.00 |
|     7 |           1 | Fail    | asterisk                                    | square         |             10 |         520.33 |           0 |             0.00 |
|     8 |           1 | Fail    | triangle                                    | square         |             10 |         525.52 |           0 |             0.00 |
|     9 |           1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        1731.80 |           0 |             0.00 |
|    10 |           1 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |        3007.90 |           0 |             0.00 |
|    11 |           1 | Success | triangle                                    | triangle       |             29 |        1433.41 |           0 |             0.00 |
|    12 |           1 | Fail    | No figure submitted (message limit reached) | triangle       |             50 |        2680.30 |           0 |             0.00 |
|    13 |           1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2149.18 |           0 |             0.00 |
|    14 |           1 | Success | diamond                                     | diamond        |             12 |         617.95 |           0 |             0.00 |
|    15 |           1 | Success | square                                      | square         |             39 |        1938.50 |           0 |             0.00 |
|    16 |           1 | Success | cross                                       | cross          |             25 |        1243.88 |           0 |             0.00 |
|    17 |           1 | Success | asterisk                                    | asterisk       |             29 |        1404.33 |           0 |             0.00 |
|    18 |           1 | Fail    | circle                                      | diamond        |             36 |        1203.14 |           0 |             0.00 |
|    19 |           1 | Success | diamond                                     | diamond        |             35 |        1352.30 |           0 |             0.00 |
|    20 |           1 | Fail    | square                                      | triangle       |             46 |        1997.39 |           0 |             0.00 |
|    21 |           1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |        2502.84 |           0 |             0.00 |
|    22 |           1 | Success | cross                                       | cross          |             24 |        1158.14 |           0 |             0.00 |
|    23 |           1 | Fail    | No figure submitted (message limit reached) | circle         |             50 |        2127.07 |           0 |             0.00 |
|    24 |           1 | Success | circle                                      | circle         |             12 |         537.23 |           0 |             0.00 |
|    25 |           1 | Fail    | diamond                                     | circle         |             29 |        1611.10 |           0 |             0.00 |
```

## Gemma 4 timing by trial

Thinking and visible-response times are measured independently from streamed Ollama chunks.

```text
| Trial | Wall time (s) | Active time (s) | Responses | Total thinking (s) | Total visible response (s) | Total generation (s) | Average thinking (s) | Average visible response (s) |
| ----- | ------------- | --------------- | --------- | ------------------ | -------------------------- | -------------------- | -------------------- | ---------------------------- |
|     1 |        335.70 |          335.70 |        10 |            318.315 |                     11.131 |              329.445 |               31.831 |                        1.113 |
|     2 |       1513.32 |         1513.32 |        36 |           1450.950 |                     39.981 |             1490.931 |               40.304 |                        1.111 |
|     3 |       2541.53 |         2541.53 |        50 |           2455.463 |                     55.387 |             2510.850 |               49.109 |                        1.108 |
|     4 |       1700.22 |         1700.22 |        32 |           1517.949 |                     35.519 |             1553.468 |               47.436 |                        1.110 |
|     5 |        924.30 |          924.30 |        21 |            890.689 |                     19.867 |              910.556 |               42.414 |                        0.946 |
|     6 |        431.52 |          431.52 |        10 |            414.239 |                     11.230 |              425.469 |               41.424 |                        1.123 |
|     7 |        597.91 |          597.91 |        11 |            580.548 |                     10.470 |              591.018 |               52.777 |                        0.952 |
|     8 |        544.77 |          544.77 |        11 |            526.970 |                     10.983 |              537.953 |               47.906 |                        0.998 |
|     9 |       1745.30 |         1745.30 |        50 |           1658.973 |                     54.986 |             1713.958 |               33.179 |                        1.100 |
|    10 |       3023.43 |         3023.43 |        50 |           2800.789 |                     57.432 |             2858.222 |               56.016 |                        1.149 |
|    11 |       1589.84 |         1589.84 |        30 |           1393.484 |                     37.532 |             1431.015 |               46.449 |                        1.251 |
|    12 |       2697.45 |         2697.45 |        50 |           2610.010 |                     56.460 |             2666.469 |               52.200 |                        1.129 |
|    13 |       2222.57 |         2222.57 |        50 |           2128.742 |                     62.407 |             2191.149 |               42.575 |                        1.248 |
|    14 |        630.90 |          630.90 |        13 |            609.161 |                     12.914 |              622.076 |               46.859 |                        0.993 |
|    15 |       1956.47 |         1956.47 |        40 |           1783.459 |                     49.582 |             1833.041 |               44.586 |                        1.240 |
|    16 |       1280.93 |         1280.93 |        26 |           1202.866 |                     29.303 |             1232.169 |               46.264 |                        1.127 |
|    17 |       1419.74 |         1419.74 |        30 |           1337.132 |                     33.879 |             1371.012 |               44.571 |                        1.129 |
|    18 |       1222.18 |         1222.18 |        37 |           1210.851 |                     37.043 |             1247.893 |               32.726 |                        1.001 |
|    19 |       1370.88 |         1370.88 |        37 |           1301.851 |                     46.415 |             1348.267 |               35.185 |                        1.254 |
|    20 |       2073.43 |         2073.43 |        47 |           1987.318 |                     55.718 |             2043.036 |               42.283 |                        1.185 |
|    21 |       2522.23 |         2522.23 |        50 |           2438.338 |                     52.335 |             2490.673 |               48.767 |                        1.047 |
|    22 |       1174.80 |         1174.80 |        25 |           1078.147 |                     30.034 |             1108.181 |               43.126 |                        1.201 |
|    23 |       2138.74 |         2138.74 |        50 |           2053.288 |                     53.977 |             2107.265 |               41.066 |                        1.080 |
|    24 |        554.12 |          554.12 |        13 |            532.194 |                     13.544 |              545.738 |               40.938 |                        1.042 |
|    25 |       1629.68 |         1629.68 |        30 |           1578.767 |                     31.709 |             1610.476 |               52.626 |                        1.057 |
```

## Reconnect details

No Jetson disconnects were recorded.

## Curation note

Only source trials 1-25 are included. Source trials 26-30 were excluded after the reported Jetson filesystem failure.
