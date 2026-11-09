# Leavitt full study report

## Progress

- Study: `20260513-0027-remaining-topologies-study`
- Status: complete
- Completed batches: 9/9
- Completed trials: 450/450
- Topologies: Y topology, Chain, Wheel
- Temperatures: 0, 0.5, 1

## Batch summary

| Topology   | Temperature | Status   | Trials |  Success rate | Average total messages | Average time (seconds) | Detailed report                                            |
| ---------- | ----------: | -------- | -----: | ------------: | ---------------------: | ---------------------: | ---------------------------------------------------------- |
| Y topology |           0 | complete |  50/50 | 26.0% (13/50) |                  17.04 |                  74.31 | [y / temperature 0](y/temperature-0/report.md)             |
| Y topology |         0.5 | complete |  50/50 | 34.0% (17/50) |                  17.36 |                  75.87 | [y / temperature 0.5](y/temperature-0.5/report.md)         |
| Y topology |           1 | complete |  50/50 | 38.0% (19/50) |                  18.78 |                  81.41 | [y / temperature 1](y/temperature-1/report.md)             |
| Chain      |           0 | complete |  50/50 | 22.0% (11/50) |                  13.92 |                  63.02 | [chain / temperature 0](chain/temperature-0/report.md)     |
| Chain      |         0.5 | complete |  50/50 | 30.0% (15/50) |                  15.24 |                  66.85 | [chain / temperature 0.5](chain/temperature-0.5/report.md) |
| Chain      |           1 | complete |  50/50 | 30.0% (15/50) |                  15.64 |                  67.86 | [chain / temperature 1](chain/temperature-1/report.md)     |
| Wheel      |           0 | complete |  50/50 | 26.0% (13/50) |                  16.04 |                  75.82 | [wheel / temperature 0](wheel/temperature-0/report.md)     |
| Wheel      |         0.5 | complete |  50/50 | 22.0% (11/50) |                  17.06 |                  81.32 | [wheel / temperature 0.5](wheel/temperature-0.5/report.md) |
| Wheel      |           1 | complete |  50/50 | 36.0% (18/50) |                  18.00 |                  84.72 | [wheel / temperature 1](wheel/temperature-1/report.md)     |

## Overall results

- Completed trials: 450/450
- Average time: 74.57 seconds
- Average total messages: 16.56
- Success rate: 132/450 (29.3%)

## Topology summary

| Topology   | Trials | Successes | Success rate | Average total messages | Average time (seconds) |
| ---------- | -----: | --------: | -----------: | ---------------------: | ---------------------: |
| Y topology |    150 |        49 |        32.7% |                  17.73 |                  77.19 |
| Chain      |    150 |        41 |        27.3% |                  14.93 |                  65.91 |
| Wheel      |    150 |        42 |        28.0% |                  17.03 |                  80.62 |

## Recipient-choice probabilities by temperature

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender at that temperature.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

### Temperature 0

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     126 |                    126 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     121 |                    137 |  88.3% (0.883) |
| Chain      | Agent2 | Agent3    |                  2 |      16 |                    137 |  11.7% (0.117) |
| Chain      | Agent3 | Agent2    |                  2 |     130 |                    134 |  97.0% (0.970) |
| Chain      | Agent3 | Agent4    |                  2 |       4 |                    134 |   3.0% (0.030) |
| Chain      | Agent4 | Agent3    |                  2 |      97 |                    158 |  61.4% (0.614) |
| Chain      | Agent4 | Agent5    |                  2 |      61 |                    158 |  38.6% (0.386) |
| Chain      | Agent5 | Agent4    |                  1 |     141 |                    141 | 100.0% (1.000) |
| Wheel      | Agent1 | Agent3    |                  1 |     145 |                    145 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     169 |                    169 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     102 |                    170 |  60.0% (0.600) |
| Wheel      | Agent3 | Agent2    |                  4 |      64 |                    170 |  37.6% (0.376) |
| Wheel      | Agent3 | Agent4    |                  4 |       2 |                    170 |   1.2% (0.012) |
| Wheel      | Agent3 | Agent5    |                  4 |       2 |                    170 |   1.2% (0.012) |
| Wheel      | Agent4 | Agent3    |                  1 |     163 |                    163 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     155 |                    155 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     168 |                    168 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     164 |                    164 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      71 |                    167 |  42.5% (0.425) |
| Y topology | Agent3 | Agent2    |                  3 |      63 |                    167 |  37.7% (0.377) |
| Y topology | Agent3 | Agent4    |                  3 |      33 |                    167 |  19.8% (0.198) |
| Y topology | Agent4 | Agent3    |                  2 |     128 |                    168 |  76.2% (0.762) |
| Y topology | Agent4 | Agent5    |                  2 |      40 |                    168 |  23.8% (0.238) |
| Y topology | Agent5 | Agent4    |                  1 |     184 |                    184 | 100.0% (1.000) |
```

### Temperature 0.5

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     134 |                    134 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     124 |                    145 |  85.5% (0.855) |
| Chain      | Agent2 | Agent3    |                  2 |      21 |                    145 |  14.5% (0.145) |
| Chain      | Agent3 | Agent2    |                  2 |     145 |                    153 |  94.8% (0.948) |
| Chain      | Agent3 | Agent4    |                  2 |       8 |                    153 |   5.2% (0.052) |
| Chain      | Agent4 | Agent3    |                  2 |     114 |                    170 |  67.1% (0.671) |
| Chain      | Agent4 | Agent5    |                  2 |      56 |                    170 |  32.9% (0.329) |
| Chain      | Agent5 | Agent4    |                  1 |     160 |                    160 | 100.0% (1.000) |
| Wheel      | Agent1 | Agent3    |                  1 |     175 |                    175 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     180 |                    180 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |      91 |                    166 |  54.8% (0.548) |
| Wheel      | Agent3 | Agent2    |                  4 |      67 |                    166 |  40.4% (0.404) |
| Wheel      | Agent3 | Agent4    |                  4 |       4 |                    166 |   2.4% (0.024) |
| Wheel      | Agent3 | Agent5    |                  4 |       4 |                    166 |   2.4% (0.024) |
| Wheel      | Agent4 | Agent3    |                  1 |     159 |                    159 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     173 |                    173 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     144 |                    144 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     183 |                    183 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      80 |                    185 |  43.2% (0.432) |
| Y topology | Agent3 | Agent2    |                  3 |      79 |                    185 |  42.7% (0.427) |
| Y topology | Agent3 | Agent4    |                  3 |      26 |                    185 |  14.1% (0.141) |
| Y topology | Agent4 | Agent3    |                  2 |     154 |                    189 |  81.5% (0.815) |
| Y topology | Agent4 | Agent5    |                  2 |      35 |                    189 |  18.5% (0.185) |
| Y topology | Agent5 | Agent4    |                  1 |     165 |                    165 | 100.0% (1.000) |
```

### Temperature 1

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     125 |                    125 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     150 |                    177 |  84.7% (0.847) |
| Chain      | Agent2 | Agent3    |                  2 |      27 |                    177 |  15.3% (0.153) |
| Chain      | Agent3 | Agent2    |                  2 |     162 |                    166 |  97.6% (0.976) |
| Chain      | Agent3 | Agent4    |                  2 |       4 |                    166 |   2.4% (0.024) |
| Chain      | Agent4 | Agent3    |                  2 |     104 |                    159 |  65.4% (0.654) |
| Chain      | Agent4 | Agent5    |                  2 |      55 |                    159 |  34.6% (0.346) |
| Chain      | Agent5 | Agent4    |                  1 |     155 |                    155 | 100.0% (1.000) |
| Wheel      | Agent1 | Agent3    |                  1 |     174 |                    174 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     168 |                    168 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |      96 |                    180 |  53.3% (0.533) |
| Wheel      | Agent3 | Agent2    |                  4 |      69 |                    180 |  38.3% (0.383) |
| Wheel      | Agent3 | Agent4    |                  4 |       6 |                    180 |   3.3% (0.033) |
| Wheel      | Agent3 | Agent5    |                  4 |       9 |                    180 |   5.0% (0.050) |
| Wheel      | Agent4 | Agent3    |                  1 |     197 |                    197 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     181 |                    181 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     205 |                    205 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     181 |                    181 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      83 |                    195 |  42.6% (0.426) |
| Y topology | Agent3 | Agent2    |                  3 |      75 |                    195 |  38.5% (0.385) |
| Y topology | Agent3 | Agent4    |                  3 |      37 |                    195 |  19.0% (0.190) |
| Y topology | Agent4 | Agent3    |                  2 |     151 |                    183 |  82.5% (0.825) |
| Y topology | Agent4 | Agent5    |                  2 |      32 |                    183 |  17.5% (0.175) |
| Y topology | Agent5 | Agent4    |                  1 |     175 |                    175 | 100.0% (1.000) |
```

## Overall recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     385 |                    385 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     395 |                    459 |  86.1% (0.861) |
| Chain      | Agent2 | Agent3    |                  2 |      64 |                    459 |  13.9% (0.139) |
| Chain      | Agent3 | Agent2    |                  2 |     437 |                    453 |  96.5% (0.965) |
| Chain      | Agent3 | Agent4    |                  2 |      16 |                    453 |   3.5% (0.035) |
| Chain      | Agent4 | Agent3    |                  2 |     315 |                    487 |  64.7% (0.647) |
| Chain      | Agent4 | Agent5    |                  2 |     172 |                    487 |  35.3% (0.353) |
| Chain      | Agent5 | Agent4    |                  1 |     456 |                    456 | 100.0% (1.000) |
| Wheel      | Agent1 | Agent3    |                  1 |     494 |                    494 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     517 |                    517 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     289 |                    516 |  56.0% (0.560) |
| Wheel      | Agent3 | Agent2    |                  4 |     200 |                    516 |  38.8% (0.388) |
| Wheel      | Agent3 | Agent4    |                  4 |      12 |                    516 |   2.3% (0.023) |
| Wheel      | Agent3 | Agent5    |                  4 |      15 |                    516 |   2.9% (0.029) |
| Wheel      | Agent4 | Agent3    |                  1 |     519 |                    519 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     509 |                    509 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     517 |                    517 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     528 |                    528 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |     234 |                    547 |  42.8% (0.428) |
| Y topology | Agent3 | Agent2    |                  3 |     217 |                    547 |  39.7% (0.397) |
| Y topology | Agent3 | Agent4    |                  3 |      96 |                    547 |  17.6% (0.176) |
| Y topology | Agent4 | Agent3    |                  2 |     433 |                    540 |  80.2% (0.802) |
| Y topology | Agent4 | Agent5    |                  2 |     107 |                    540 |  19.8% (0.198) |
| Y topology | Agent5 | Agent4    |                  1 |     524 |                    524 | 100.0% (1.000) |
```

### Excluded fallback routes

```text
| Topology   | Sender | Target source   | Count |
| ---------- | ------ | --------------- | ----- |
| Y topology | Agent1 | client_assigned |     1 |
| Y topology | Agent2 | client_assigned |     1 |
| Y topology | Agent3 | client_assigned |     1 |
```

## Y topology full success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- |
|     1 |           0 | Fail    | circle                                      | triangle       |             21 |         275.27 |
|     2 |           0 | Success | square                                      | square         |              9 |          37.87 |
|     3 |           0 | Success | diamond                                     | diamond        |             17 |          74.09 |
|     4 |           0 | Fail    | circle                                      | triangle       |             34 |         140.39 |
|     5 |           0 | Fail    | circle                                      | square         |             12 |          50.16 |
|     6 |           0 | Fail    | circle                                      | triangle       |             15 |          61.36 |
|     7 |           0 | Fail    | diamond                                     | square         |             15 |          64.29 |
|     8 |           0 | Fail    | triangle                                    | diamond        |             14 |          66.06 |
|     9 |           0 | Fail    | cross                                       | diamond        |             10 |          43.12 |
|    10 |           0 | Success | circle                                      | circle         |             18 |          75.44 |
|    11 |           0 | Fail    | circle                                      | cross          |             23 |          98.31 |
|    12 |           0 | Success | cross                                       | cross          |              8 |          34.66 |
|    13 |           0 | Fail    | square                                      | triangle       |             16 |          59.37 |
|    14 |           0 | Fail    | square                                      | cross          |             11 |          49.23 |
|    15 |           0 | Fail    | No figure submitted (message limit reached) | asterisk       |             50 |         201.89 |
|    16 |           0 | Fail    | triangle                                    | diamond        |             12 |          51.13 |
|    17 |           0 | Fail    | cross                                       | circle         |             23 |          98.70 |
|    18 |           0 | Fail    | diamond                                     | cross          |             13 |          47.97 |
|    19 |           0 | Fail    | asterisk                                    | circle         |             14 |          57.90 |
|    20 |           0 | Success | cross                                       | cross          |             10 |          44.02 |
|    21 |           0 | Fail    | diamond                                     | cross          |              9 |          38.00 |
|    22 |           0 | Success | asterisk                                    | asterisk       |             22 |          94.25 |
|    23 |           0 | Fail    | asterisk                                    | triangle       |             20 |          79.21 |
|    24 |           0 | Fail    | diamond                                     | square         |             16 |          62.83 |
|    25 |           0 | Fail    | cross                                       | triangle       |             16 |          68.13 |
|    26 |           0 | Fail    | square                                      | circle         |             13 |          56.14 |
|    27 |           0 | Fail    | square                                      | diamond        |             12 |          49.51 |
|    28 |           0 | Fail    | cross                                       | asterisk       |             16 |          67.74 |
|    29 |           0 | Success | square                                      | square         |             26 |         100.99 |
|    30 |           0 | Fail    | diamond                                     | circle         |             17 |          75.49 |
|    31 |           0 | Success | circle                                      | circle         |             19 |          82.11 |
|    32 |           0 | Fail    | asterisk                                    | diamond        |             11 |          44.68 |
|    33 |           0 | Fail    | diamond                                     | asterisk       |             14 |          60.12 |
|    34 |           0 | Success | triangle                                    | triangle       |              8 |          34.37 |
|    35 |           0 | Fail    | triangle                                    | circle         |             20 |          79.62 |
|    36 |           0 | Fail    | square                                      | triangle       |             20 |          80.76 |
|    37 |           0 | Success | square                                      | square         |              8 |          34.17 |
|    38 |           0 | Fail    | circle                                      | square         |             21 |          84.38 |
|    39 |           0 | Fail    | diamond                                     | asterisk       |             10 |          44.49 |
|    40 |           0 | Fail    | No figure submitted (message limit reached) | cross          |             50 |         186.35 |
|    41 |           0 | Success | diamond                                     | diamond        |             25 |         101.60 |
|    42 |           0 | Fail    | triangle                                    | circle         |             12 |          53.50 |
|    43 |           0 | Fail    | circle                                      | cross          |             26 |         100.08 |
|    44 |           0 | Fail    | square                                      | triangle       |             21 |          89.59 |
|    45 |           0 | Fail    | diamond                                     | cross          |             14 |          55.64 |
|    46 |           0 | Success | diamond                                     | diamond        |              7 |          29.57 |
|    47 |           0 | Fail    | cross                                       | diamond        |             13 |          56.81 |
|    48 |           0 | Fail    | cross                                       | asterisk       |              8 |          36.90 |
|    49 |           0 | Fail    | circle                                      | cross          |             24 |          96.87 |
|    50 |           0 | Success | circle                                      | circle         |              9 |          40.14 |
|    51 |         0.5 | Success | circle                                      | circle         |             24 |         284.95 |
|    52 |         0.5 | Fail    | triangle                                    | square         |             26 |         111.03 |
|    53 |         0.5 | Fail    | diamond                                     | cross          |             22 |          91.65 |
|    54 |         0.5 | Fail    | cross                                       | asterisk       |              6 |          25.84 |
|    55 |         0.5 | Fail    | square                                      | cross          |             11 |          45.58 |
|    56 |         0.5 | Success | square                                      | square         |             22 |          87.97 |
|    57 |         0.5 | Success | asterisk                                    | asterisk       |             21 |          93.25 |
|    58 |         0.5 | Success | asterisk                                    | asterisk       |             39 |         149.26 |
|    59 |         0.5 | Fail    | asterisk                                    | triangle       |             15 |          61.35 |
|    60 |         0.5 | Success | triangle                                    | triangle       |             16 |          63.43 |
|    61 |         0.5 | Fail    | square                                      | triangle       |             11 |          48.91 |
|    62 |         0.5 | Success | diamond                                     | diamond        |             23 |          97.03 |
|    63 |         0.5 | Fail    | circle                                      | triangle       |             15 |          64.07 |
|    64 |         0.5 | Fail    | diamond                                     | triangle       |             16 |          68.32 |
|    65 |         0.5 | Fail    | cross                                       | triangle       |             17 |          69.68 |
|    66 |         0.5 | Success | asterisk                                    | asterisk       |             10 |          43.03 |
|    67 |         0.5 | Fail    | square                                      | triangle       |             17 |          74.57 |
|    68 |         0.5 | Success | cross                                       | cross          |             17 |          70.24 |
|    69 |         0.5 | Fail    | diamond                                     | square         |             18 |          76.04 |
|    70 |         0.5 | Fail    | square                                      | diamond        |             10 |          42.03 |
|    71 |         0.5 | Success | square                                      | square         |             14 |          58.60 |
|    72 |         0.5 | Success | square                                      | square         |             20 |          81.78 |
|    73 |         0.5 | Success | circle                                      | circle         |             20 |          84.58 |
|    74 |         0.5 | Fail    | cross                                       | asterisk       |              9 |          41.69 |
|    75 |         0.5 | Fail    | cross                                       | asterisk       |             19 |          75.98 |
|    76 |         0.5 | Fail    | diamond                                     | cross          |              7 |          30.46 |
|    77 |         0.5 | Fail    | circle                                      | triangle       |             11 |          43.68 |
|    78 |         0.5 | Success | cross                                       | cross          |             19 |          81.07 |
|    79 |         0.5 | Fail    | diamond                                     | cross          |             36 |         138.07 |
|    80 |         0.5 | Fail    | square                                      | diamond        |             29 |         126.45 |
|    81 |         0.5 | Fail    | cross                                       | diamond        |             19 |          78.03 |
|    82 |         0.5 | Fail    | diamond                                     | asterisk       |             13 |          54.08 |
|    83 |         0.5 | Fail    | triangle                                    | square         |             15 |          63.33 |
|    84 |         0.5 | Fail    | triangle                                    | diamond        |             14 |          58.61 |
|    85 |         0.5 | Fail    | circle                                      | cross          |             19 |          78.69 |
|    86 |         0.5 | Fail    | triangle                                    | diamond        |             12 |          51.48 |
|    87 |         0.5 | Fail    | square                                      | triangle       |             14 |          57.57 |
|    88 |         0.5 | Fail    | asterisk                                    | diamond        |             12 |          50.49 |
|    89 |         0.5 | Fail    | diamond                                     | square         |             27 |         109.53 |
|    90 |         0.5 | Fail    | circle                                      | cross          |             12 |          51.50 |
|    91 |         0.5 | Success | square                                      | square         |              7 |          32.95 |
|    92 |         0.5 | Success | triangle                                    | triangle       |             36 |         139.89 |
|    93 |         0.5 | Success | asterisk                                    | asterisk       |             18 |          69.94 |
|    94 |         0.5 | Fail    | cross                                       | diamond        |             10 |          46.58 |
|    95 |         0.5 | Fail    | circle                                      | square         |             14 |          62.60 |
|    96 |         0.5 | Fail    | square                                      | diamond        |             15 |          57.15 |
|    97 |         0.5 | Success | asterisk                                    | asterisk       |             18 |          72.38 |
|    98 |         0.5 | Success | circle                                      | circle         |             13 |          55.00 |
|    99 |         0.5 | Fail    | cross                                       | circle         |             23 |          97.71 |
|   100 |         0.5 | Fail    | diamond                                     | triangle       |             17 |          75.41 |
|   101 |           1 | Fail    | diamond                                     | circle         |             21 |         259.12 |
|   102 |           1 | Success | diamond                                     | diamond        |             14 |          56.03 |
|   103 |           1 | Success | diamond                                     | diamond        |             11 |          48.61 |
|   104 |           1 | Success | circle                                      | circle         |             24 |          96.17 |
|   105 |           1 | Fail    | triangle                                    | diamond        |             27 |         103.16 |
|   106 |           1 | Success | triangle                                    | triangle       |             13 |          57.66 |
|   107 |           1 | Fail    | diamond                                     | cross          |             24 |          99.15 |
|   108 |           1 | Fail    | cross                                       | diamond        |             10 |          45.30 |
|   109 |           1 | Fail    | cross                                       | asterisk       |             22 |          89.97 |
|   110 |           1 | Fail    | asterisk                                    | triangle       |             30 |         124.83 |
|   111 |           1 | Success | cross                                       | cross          |             14 |          57.23 |
|   112 |           1 | Fail    | triangle                                    | cross          |             32 |         131.68 |
|   113 |           1 | Fail    | square                                      | circle         |             30 |         121.06 |
|   114 |           1 | Fail    | square                                      | asterisk       |             11 |          46.91 |
|   115 |           1 | Fail    | circle                                      | square         |             11 |          46.40 |
|   116 |           1 | Fail    | triangle                                    | circle         |             16 |          68.69 |
|   117 |           1 | Fail    | circle                                      | diamond        |             22 |          86.53 |
|   118 |           1 | Fail    | No figure submitted (message limit reached) | diamond        |             50 |         193.23 |
|   119 |           1 | Success | circle                                      | circle         |             13 |          59.28 |
|   120 |           1 | Success | asterisk                                    | asterisk       |             22 |          96.34 |
|   121 |           1 | Success | triangle                                    | triangle       |             12 |          56.64 |
|   122 |           1 | Fail    | circle                                      | triangle       |             13 |          59.61 |
|   123 |           1 | Fail    | square                                      | asterisk       |             22 |          88.81 |
|   124 |           1 | Success | cross                                       | cross          |             20 |          87.47 |
|   125 |           1 | Fail    | cross                                       | square         |             24 |          99.31 |
|   126 |           1 | Fail    | circle                                      | square         |             14 |          60.07 |
|   127 |           1 | Success | circle                                      | circle         |             14 |          54.35 |
|   128 |           1 | Fail    | circle                                      | diamond        |             26 |         110.94 |
|   129 |           1 | Success | circle                                      | circle         |             14 |          59.97 |
|   130 |           1 | Success | square                                      | square         |             10 |          44.21 |
|   131 |           1 | Fail    | triangle                                    | cross          |              8 |          34.82 |
|   132 |           1 | Success | cross                                       | cross          |             13 |          56.09 |
|   133 |           1 | Success | diamond                                     | diamond        |             16 |          67.50 |
|   134 |           1 | Fail    | square                                      | diamond        |             17 |          69.52 |
|   135 |           1 | Fail    | triangle                                    | circle         |             12 |          50.97 |
|   136 |           1 | Fail    | cross                                       | diamond        |             13 |          56.98 |
|   137 |           1 | Fail    | No figure submitted (message limit reached) | square         |             50 |         187.14 |
|   138 |           1 | Success | circle                                      | circle         |             15 |          67.12 |
|   139 |           1 | Fail    | cross                                       | asterisk       |             32 |         133.56 |
|   140 |           1 | Success | square                                      | square         |             16 |          65.05 |
|   141 |           1 | Success | diamond                                     | diamond        |             10 |          41.82 |
|   142 |           1 | Success | cross                                       | cross          |             21 |          87.03 |
|   143 |           1 | Fail    | triangle                                    | cross          |             18 |          72.87 |
|   144 |           1 | Fail    | cross                                       | triangle       |              6 |          26.84 |
|   145 |           1 | Fail    | square                                      | circle         |             18 |          76.32 |
|   146 |           1 | Fail    | asterisk                                    | triangle       |             15 |          65.05 |
|   147 |           1 | Fail    | triangle                                    | asterisk       |             40 |         160.47 |
|   148 |           1 | Fail    | circle                                      | asterisk       |              8 |          37.17 |
|   149 |           1 | Success | cross                                       | cross          |             10 |          44.43 |
|   150 |           1 | Fail    | diamond                                     | cross          |             15 |          60.98 |
```

## Chain full success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- |
|     1 |           0 | Success | asterisk         | asterisk       |             21 |         264.69 |
|     2 |           0 | Fail    | cross            | circle         |             21 |          82.74 |
|     3 |           0 | Fail    | diamond          | cross          |              9 |          36.30 |
|     4 |           0 | Success | diamond          | diamond        |              8 |          35.34 |
|     5 |           0 | Fail    | cross            | circle         |             16 |          66.36 |
|     6 |           0 | Fail    | square           | diamond        |              9 |          40.04 |
|     7 |           0 | Fail    | asterisk         | diamond        |             18 |          71.44 |
|     8 |           0 | Fail    | cross            | square         |             20 |          88.96 |
|     9 |           0 | Fail    | triangle         | square         |             15 |          64.58 |
|    10 |           0 | Fail    | asterisk         | triangle       |             14 |          60.42 |
|    11 |           0 | Success | diamond          | diamond        |              6 |          25.96 |
|    12 |           0 | Fail    | square           | cross          |             11 |          47.92 |
|    13 |           0 | Fail    | triangle         | square         |             24 |         101.67 |
|    14 |           0 | Fail    | diamond          | circle         |             11 |          46.20 |
|    15 |           0 | Fail    | cross            | diamond        |              9 |          39.02 |
|    16 |           0 | Fail    | triangle         | circle         |             11 |          45.03 |
|    17 |           0 | Fail    | square           | cross          |             10 |          42.70 |
|    18 |           0 | Success | asterisk         | asterisk       |             11 |          46.34 |
|    19 |           0 | Fail    | circle           | asterisk       |             19 |          84.51 |
|    20 |           0 | Fail    | asterisk         | square         |             12 |          50.48 |
|    21 |           0 | Fail    | triangle         | square         |              8 |          34.58 |
|    22 |           0 | Fail    | diamond          | circle         |             12 |          53.90 |
|    23 |           0 | Fail    | circle           | cross          |             20 |          83.57 |
|    24 |           0 | Fail    | triangle         | square         |             13 |          57.58 |
|    25 |           0 | Fail    | asterisk         | diamond        |             20 |          80.53 |
|    26 |           0 | Fail    | triangle         | asterisk       |             12 |          53.56 |
|    27 |           0 | Fail    | square           | asterisk       |              9 |          39.83 |
|    28 |           0 | Fail    | cross            | triangle       |             11 |          44.63 |
|    29 |           0 | Success | triangle         | triangle       |             13 |          56.13 |
|    30 |           0 | Success | triangle         | triangle       |             10 |          44.39 |
|    31 |           0 | Success | diamond          | diamond        |             16 |          67.70 |
|    32 |           0 | Fail    | diamond          | triangle       |             38 |         158.89 |
|    33 |           0 | Fail    | triangle         | circle         |             10 |          44.15 |
|    34 |           0 | Fail    | cross            | diamond        |             10 |          43.33 |
|    35 |           0 | Fail    | circle           | square         |             14 |          60.55 |
|    36 |           0 | Success | asterisk         | asterisk       |             18 |          78.20 |
|    37 |           0 | Fail    | diamond          | square         |             11 |          47.67 |
|    38 |           0 | Fail    | circle           | square         |             12 |          51.37 |
|    39 |           0 | Fail    | diamond          | asterisk       |             16 |          72.20 |
|    40 |           0 | Fail    | cross            | asterisk       |             13 |          52.91 |
|    41 |           0 | Success | triangle         | triangle       |             12 |          52.33 |
|    42 |           0 | Fail    | triangle         | cross          |             13 |          58.20 |
|    43 |           0 | Fail    | triangle         | circle         |             10 |          42.20 |
|    44 |           0 | Fail    | circle           | cross          |             13 |          58.11 |
|    45 |           0 | Fail    | diamond          | square         |             13 |          56.18 |
|    46 |           0 | Fail    | circle           | triangle       |             22 |          92.75 |
|    47 |           0 | Fail    | square           | asterisk       |             19 |          78.59 |
|    48 |           0 | Fail    | asterisk         | cross          |             15 |          65.10 |
|    49 |           0 | Success | diamond          | diamond        |              9 |          40.42 |
|    50 |           0 | Success | asterisk         | asterisk       |              9 |          40.73 |
|    51 |         0.5 | Fail    | diamond          | square         |             10 |         197.80 |
|    52 |         0.5 | Fail    | triangle         | cross          |              7 |          30.47 |
|    53 |         0.5 | Success | cross            | cross          |             19 |          74.51 |
|    54 |         0.5 | Fail    | square           | asterisk       |             17 |          70.56 |
|    55 |         0.5 | Fail    | triangle         | asterisk       |             11 |          46.87 |
|    56 |         0.5 | Success | circle           | circle         |             20 |          81.10 |
|    57 |         0.5 | Success | diamond          | diamond        |             22 |          93.59 |
|    58 |         0.5 | Success | circle           | circle         |             10 |          45.33 |
|    59 |         0.5 | Fail    | cross            | square         |             14 |          57.64 |
|    60 |         0.5 | Fail    | cross            | circle         |             15 |          65.83 |
|    61 |         0.5 | Fail    | cross            | diamond        |             11 |          46.57 |
|    62 |         0.5 | Fail    | circle           | square         |             24 |          94.93 |
|    63 |         0.5 | Fail    | triangle         | diamond        |             18 |          68.13 |
|    64 |         0.5 | Success | asterisk         | asterisk       |             11 |          48.24 |
|    65 |         0.5 | Fail    | cross            | diamond        |             23 |          94.23 |
|    66 |         0.5 | Fail    | triangle         | diamond        |              6 |          26.64 |
|    67 |         0.5 | Fail    | diamond          | circle         |             12 |          52.90 |
|    68 |         0.5 | Fail    | square           | triangle       |             10 |          45.33 |
|    69 |         0.5 | Fail    | diamond          | circle         |             31 |         119.82 |
|    70 |         0.5 | Fail    | square           | asterisk       |             16 |          69.47 |
|    71 |         0.5 | Fail    | diamond          | triangle       |             22 |          86.04 |
|    72 |         0.5 | Fail    | circle           | cross          |             14 |          59.44 |
|    73 |         0.5 | Fail    | asterisk         | diamond        |             15 |          62.11 |
|    74 |         0.5 | Fail    | square           | triangle       |             17 |          70.62 |
|    75 |         0.5 | Success | circle           | circle         |             15 |          60.33 |
|    76 |         0.5 | Fail    | cross            | square         |             16 |          64.71 |
|    77 |         0.5 | Success | cross            | cross          |             27 |         113.66 |
|    78 |         0.5 | Fail    | asterisk         | cross          |             11 |          45.76 |
|    79 |         0.5 | Fail    | cross            | asterisk       |             17 |          71.68 |
|    80 |         0.5 | Fail    | triangle         | square         |             14 |          56.66 |
|    81 |         0.5 | Fail    | diamond          | cross          |             32 |         135.80 |
|    82 |         0.5 | Success | square           | square         |             11 |          48.66 |
|    83 |         0.5 | Success | diamond          | diamond        |              7 |          31.35 |
|    84 |         0.5 | Fail    | circle           | cross          |             23 |          95.12 |
|    85 |         0.5 | Success | cross            | cross          |             16 |          70.41 |
|    86 |         0.5 | Success | asterisk         | asterisk       |             22 |          98.99 |
|    87 |         0.5 | Fail    | triangle         | cross          |              6 |          26.10 |
|    88 |         0.5 | Fail    | diamond          | square         |             13 |          56.48 |
|    89 |         0.5 | Fail    | square           | cross          |             10 |          43.71 |
|    90 |         0.5 | Fail    | square           | diamond        |             13 |          49.08 |
|    91 |         0.5 | Fail    | square           | diamond        |              9 |          39.13 |
|    92 |         0.5 | Fail    | diamond          | cross          |             18 |          74.71 |
|    93 |         0.5 | Success | diamond          | diamond        |             12 |          53.63 |
|    94 |         0.5 | Fail    | circle           | triangle       |             18 |          79.75 |
|    95 |         0.5 | Fail    | square           | diamond        |             12 |          53.43 |
|    96 |         0.5 | Success | square           | square         |             18 |          71.74 |
|    97 |         0.5 | Fail    | diamond          | triangle       |              9 |          37.34 |
|    98 |         0.5 | Fail    | cross            | triangle       |              9 |          37.43 |
|    99 |         0.5 | Success | triangle         | triangle       |             13 |          57.69 |
|   100 |         0.5 | Success | cross            | cross          |             16 |          60.77 |
|   101 |           1 | Fail    | cross            | diamond        |             17 |         224.14 |
|   102 |           1 | Fail    | cross            | asterisk       |             16 |          65.30 |
|   103 |           1 | Fail    | cross            | square         |             20 |          81.56 |
|   104 |           1 | Fail    | square           | asterisk       |             16 |          68.60 |
|   105 |           1 | Fail    | circle           | triangle       |             18 |          78.03 |
|   106 |           1 | Fail    | triangle         | square         |              9 |          35.68 |
|   107 |           1 | Success | triangle         | triangle       |              8 |          35.64 |
|   108 |           1 | Fail    | circle           | cross          |             21 |          79.78 |
|   109 |           1 | Fail    | cross            | asterisk       |             13 |          53.34 |
|   110 |           1 | Success | asterisk         | asterisk       |             19 |          77.70 |
|   111 |           1 | Success | cross            | cross          |             11 |          44.02 |
|   112 |           1 | Fail    | triangle         | cross          |             16 |          65.93 |
|   113 |           1 | Success | circle           | circle         |             11 |          45.89 |
|   114 |           1 | Success | diamond          | diamond        |              9 |          38.93 |
|   115 |           1 | Success | square           | square         |              9 |          38.26 |
|   116 |           1 | Fail    | cross            | square         |             27 |         108.62 |
|   117 |           1 | Fail    | triangle         | square         |             17 |          70.42 |
|   118 |           1 | Success | square           | square         |             27 |         105.96 |
|   119 |           1 | Fail    | asterisk         | cross          |             16 |          65.91 |
|   120 |           1 | Fail    | cross            | diamond        |             17 |          68.05 |
|   121 |           1 | Success | cross            | cross          |             31 |         130.08 |
|   122 |           1 | Fail    | cross            | circle         |             13 |          53.95 |
|   123 |           1 | Fail    | asterisk         | diamond        |             10 |          43.91 |
|   124 |           1 | Success | asterisk         | asterisk       |              6 |          25.87 |
|   125 |           1 | Fail    | cross            | square         |              8 |          35.30 |
|   126 |           1 | Fail    | circle           | square         |              9 |          36.87 |
|   127 |           1 | Fail    | circle           | square         |             15 |          65.66 |
|   128 |           1 | Fail    | asterisk         | circle         |             13 |          61.06 |
|   129 |           1 | Fail    | diamond          | asterisk       |             13 |          49.84 |
|   130 |           1 | Fail    | circle           | diamond        |             11 |          48.26 |
|   131 |           1 | Fail    | square           | cross          |             15 |          66.05 |
|   132 |           1 | Success | cross            | cross          |             43 |         161.66 |
|   133 |           1 | Fail    | circle           | cross          |             16 |          68.71 |
|   134 |           1 | Fail    | triangle         | circle         |             19 |          77.67 |
|   135 |           1 | Success | asterisk         | asterisk       |             10 |          44.40 |
|   136 |           1 | Fail    | cross            | triangle       |             14 |          59.14 |
|   137 |           1 | Fail    | triangle         | circle         |             19 |          79.42 |
|   138 |           1 | Fail    | triangle         | asterisk       |              8 |          33.58 |
|   139 |           1 | Fail    | cross            | circle         |             19 |          81.27 |
|   140 |           1 | Success | square           | square         |             26 |         101.54 |
|   141 |           1 | Fail    | cross            | circle         |             13 |          54.85 |
|   142 |           1 | Fail    | triangle         | asterisk       |             18 |          77.55 |
|   143 |           1 | Fail    | circle           | diamond        |             15 |          56.37 |
|   144 |           1 | Success | diamond          | diamond        |             13 |          59.18 |
|   145 |           1 | Fail    | circle           | diamond        |             15 |          62.92 |
|   146 |           1 | Fail    | cross            | triangle       |              9 |          40.70 |
|   147 |           1 | Success | square           | square         |             27 |         108.66 |
|   148 |           1 | Success | square           | square         |             18 |          74.76 |
|   149 |           1 | Fail    | cross            | circle         |              7 |          31.30 |
|   150 |           1 | Fail    | cross            | asterisk       |             12 |          50.69 |
```

## Wheel full success table

```text
| Round | Temperature | Result  | Submitted figure                            | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ------------------------------------------- | -------------- | -------------- | -------------- |
|     1 |           0 | Fail    | circle                                      | diamond        |             16 |         240.36 |
|     2 |           0 | Success | circle                                      | circle         |             19 |          87.20 |
|     3 |           0 | Fail    | square                                      | circle         |             14 |          61.46 |
|     4 |           0 | Fail    | asterisk                                    | circle         |             12 |          58.47 |
|     5 |           0 | Fail    | diamond                                     | triangle       |             12 |          52.64 |
|     6 |           0 | Fail    | circle                                      | square         |             25 |         115.83 |
|     7 |           0 | Success | triangle                                    | triangle       |             10 |          50.40 |
|     8 |           0 | Fail    | square                                      | triangle       |             12 |          54.27 |
|     9 |           0 | Fail    | cross                                       | square         |             10 |          47.47 |
|    10 |           0 | Fail    | circle                                      | square         |             21 |          88.55 |
|    11 |           0 | Fail    | cross                                       | circle         |             13 |          58.94 |
|    12 |           0 | Fail    | asterisk                                    | diamond        |             14 |          63.29 |
|    13 |           0 | Fail    | diamond                                     | triangle       |             13 |          60.05 |
|    14 |           0 | Fail    | circle                                      | cross          |             13 |          61.35 |
|    15 |           0 | Fail    | diamond                                     | asterisk       |             19 |          86.57 |
|    16 |           0 | Fail    | circle                                      | asterisk       |             16 |          70.11 |
|    17 |           0 | Fail    | diamond                                     | circle         |             33 |         142.05 |
|    18 |           0 | Fail    | diamond                                     | circle         |             16 |          74.83 |
|    19 |           0 | Fail    | cross                                       | triangle       |              9 |          43.57 |
|    20 |           0 | Fail    | triangle                                    | circle         |             24 |         105.13 |
|    21 |           0 | Success | square                                      | square         |             22 |          97.50 |
|    22 |           0 | Fail    | diamond                                     | asterisk       |             12 |          56.10 |
|    23 |           0 | Fail    | circle                                      | square         |             19 |          79.93 |
|    24 |           0 | Fail    | diamond                                     | triangle       |             10 |          45.51 |
|    25 |           0 | Success | diamond                                     | diamond        |             47 |         192.83 |
|    26 |           0 | Success | cross                                       | cross          |             10 |          42.47 |
|    27 |           0 | Fail    | square                                      | diamond        |             18 |          86.41 |
|    28 |           0 | Fail    | circle                                      | diamond        |             14 |          63.78 |
|    29 |           0 | Success | circle                                      | circle         |              7 |          35.25 |
|    30 |           0 | Success | square                                      | square         |              8 |          38.58 |
|    31 |           0 | Fail    | cross                                       | diamond        |             18 |          79.69 |
|    32 |           0 | Success | diamond                                     | diamond        |             21 |          93.39 |
|    33 |           0 | Fail    | asterisk                                    | triangle       |             24 |         107.03 |
|    34 |           0 | Success | triangle                                    | triangle       |             18 |          84.31 |
|    35 |           0 | Fail    | diamond                                     | asterisk       |             10 |          44.77 |
|    36 |           0 | Fail    | circle                                      | cross          |             10 |          45.90 |
|    37 |           0 | Fail    | cross                                       | diamond        |             19 |          82.44 |
|    38 |           0 | Fail    | triangle                                    | square         |             18 |          77.68 |
|    39 |           0 | Fail    | triangle                                    | asterisk       |             14 |          61.66 |
|    40 |           0 | Fail    | circle                                      | cross          |             21 |          91.14 |
|    41 |           0 | Fail    | triangle                                    | circle         |              9 |          44.33 |
|    42 |           0 | Success | triangle                                    | triangle       |             13 |          57.66 |
|    43 |           0 | Success | cross                                       | cross          |             11 |          54.14 |
|    44 |           0 | Fail    | circle                                      | triangle       |             14 |          69.16 |
|    45 |           0 | Success | diamond                                     | diamond        |             12 |          55.51 |
|    46 |           0 | Fail    | diamond                                     | circle         |             13 |          64.10 |
|    47 |           0 | Fail    | diamond                                     | square         |             15 |          67.43 |
|    48 |           0 | Success | square                                      | square         |             13 |          59.34 |
|    49 |           0 | Fail    | circle                                      | diamond        |             15 |          70.15 |
|    50 |           0 | Fail    | asterisk                                    | square         |             26 |         120.24 |
|    51 |         0.5 | Success | diamond                                     | diamond        |             14 |         219.80 |
|    52 |         0.5 | Success | circle                                      | circle         |             21 |          96.75 |
|    53 |         0.5 | Fail    | square                                      | diamond        |             23 |         109.34 |
|    54 |         0.5 | Fail    | diamond                                     | square         |              8 |          34.35 |
|    55 |         0.5 | Fail    | cross                                       | asterisk       |             19 |          81.03 |
|    56 |         0.5 | Fail    | square                                      | circle         |             10 |          48.96 |
|    57 |         0.5 | Fail    | cross                                       | circle         |             16 |          72.21 |
|    58 |         0.5 | Success | diamond                                     | diamond        |             17 |          80.96 |
|    59 |         0.5 | Fail    | asterisk                                    | circle         |             23 |          97.98 |
|    60 |         0.5 | Fail    | circle                                      | diamond        |             27 |         123.57 |
|    61 |         0.5 | Fail    | triangle                                    | diamond        |             17 |          83.95 |
|    62 |         0.5 | Fail    | asterisk                                    | cross          |             12 |          50.82 |
|    63 |         0.5 | Fail    | cross                                       | diamond        |             22 |         100.01 |
|    64 |         0.5 | Fail    | cross                                       | square         |             12 |          57.30 |
|    65 |         0.5 | Fail    | circle                                      | diamond        |             19 |          88.14 |
|    66 |         0.5 | Fail    | cross                                       | circle         |             12 |          58.19 |
|    67 |         0.5 | Fail    | circle                                      | cross          |             25 |         119.25 |
|    68 |         0.5 | Fail    | cross                                       | triangle       |             17 |          71.09 |
|    69 |         0.5 | Fail    | circle                                      | square         |             11 |          51.64 |
|    70 |         0.5 | Fail    | cross                                       | triangle       |             27 |         123.35 |
|    71 |         0.5 | Success | circle                                      | circle         |             39 |         173.85 |
|    72 |         0.5 | Fail    | triangle                                    | asterisk       |             13 |          63.57 |
|    73 |         0.5 | Success | circle                                      | circle         |             25 |         114.09 |
|    74 |         0.5 | Fail    | triangle                                    | asterisk       |             24 |          99.24 |
|    75 |         0.5 | Success | triangle                                    | triangle       |             13 |          64.55 |
|    76 |         0.5 | Success | cross                                       | cross          |             11 |          54.72 |
|    77 |         0.5 | Fail    | circle                                      | square         |             22 |          94.35 |
|    78 |         0.5 | Fail    | circle                                      | diamond        |             12 |          54.90 |
|    79 |         0.5 | Fail    | diamond                                     | square         |             16 |          71.08 |
|    80 |         0.5 | Fail    | asterisk                                    | triangle       |              9 |          44.69 |
|    81 |         0.5 | Fail    | asterisk                                    | square         |             10 |          46.78 |
|    82 |         0.5 | Success | asterisk                                    | asterisk       |             15 |          68.57 |
|    83 |         0.5 | Fail    | circle                                      | square         |             14 |          63.63 |
|    84 |         0.5 | Fail    | cross                                       | circle         |             12 |          55.69 |
|    85 |         0.5 | Fail    | cross                                       | diamond        |             20 |          91.13 |
|    86 |         0.5 | Fail    | circle                                      | cross          |             12 |          59.16 |
|    87 |         0.5 | Fail    | diamond                                     | asterisk       |             10 |          44.02 |
|    88 |         0.5 | Fail    | circle                                      | asterisk       |             24 |         101.97 |
|    89 |         0.5 | Fail    | cross                                       | triangle       |             12 |          56.00 |
|    90 |         0.5 | Success | circle                                      | circle         |             18 |          84.75 |
|    91 |         0.5 | Fail    | circle                                      | diamond        |             15 |          67.04 |
|    92 |         0.5 | Fail    | square                                      | diamond        |             21 |         107.66 |
|    93 |         0.5 | Fail    | cross                                       | circle         |              7 |          30.93 |
|    94 |         0.5 | Fail    | square                                      | cross          |             25 |         106.88 |
|    95 |         0.5 | Success | circle                                      | circle         |             13 |          57.92 |
|    96 |         0.5 | Success | diamond                                     | diamond        |             10 |          47.39 |
|    97 |         0.5 | Fail    | circle                                      | triangle       |             18 |          91.29 |
|    98 |         0.5 | Fail    | cross                                       | square         |             14 |          63.27 |
|    99 |         0.5 | Fail    | square                                      | diamond        |             23 |         109.56 |
|   100 |         0.5 | Fail    | triangle                                    | diamond        |             24 |         108.79 |
|   101 |           1 | Fail    | diamond                                     | triangle       |             17 |         235.69 |
|   102 |           1 | Success | triangle                                    | triangle       |             24 |          94.84 |
|   103 |           1 | Fail    | square                                      | asterisk       |             17 |          72.18 |
|   104 |           1 | Fail    | triangle                                    | diamond        |             15 |          68.35 |
|   105 |           1 | Fail    | circle                                      | triangle       |             13 |          57.94 |
|   106 |           1 | Fail    | circle                                      | triangle       |             16 |          75.65 |
|   107 |           1 | Fail    | square                                      | cross          |             24 |         114.69 |
|   108 |           1 | Fail    | circle                                      | triangle       |             12 |          58.88 |
|   109 |           1 | Success | circle                                      | circle         |             15 |          70.65 |
|   110 |           1 | Fail    | triangle                                    | square         |             19 |          80.80 |
|   111 |           1 | Success | asterisk                                    | asterisk       |             19 |          89.60 |
|   112 |           1 | Success | square                                      | square         |             18 |          79.95 |
|   113 |           1 | Fail    | circle                                      | square         |              8 |          36.52 |
|   114 |           1 | Fail    | No figure submitted (message limit reached) | square         |             50 |         236.75 |
|   115 |           1 | Success | circle                                      | circle         |             24 |         107.58 |
|   116 |           1 | Fail    | circle                                      | triangle       |             14 |          59.94 |
|   117 |           1 | Success | circle                                      | circle         |             19 |          96.84 |
|   118 |           1 | Fail    | circle                                      | diamond        |             12 |          52.66 |
|   119 |           1 | Success | diamond                                     | diamond        |             42 |         177.14 |
|   120 |           1 | Fail    | diamond                                     | square         |             20 |          90.61 |
|   121 |           1 | Fail    | asterisk                                    | square         |             11 |          49.81 |
|   122 |           1 | Fail    | circle                                      | cross          |             13 |          59.36 |
|   123 |           1 | Success | square                                      | square         |             12 |          57.18 |
|   124 |           1 | Fail    | square                                      | asterisk       |             22 |         100.65 |
|   125 |           1 | Success | circle                                      | circle         |              9 |          42.74 |
|   126 |           1 | Success | circle                                      | circle         |              9 |          41.43 |
|   127 |           1 | Fail    | diamond                                     | square         |              7 |          32.96 |
|   128 |           1 | Fail    | square                                      | asterisk       |              8 |          37.54 |
|   129 |           1 | Fail    | circle                                      | asterisk       |              7 |          35.24 |
|   130 |           1 | Fail    | circle                                      | cross          |             33 |         144.30 |
|   131 |           1 | Success | cross                                       | cross          |             14 |          59.82 |
|   132 |           1 | Fail    | square                                      | asterisk       |             29 |         121.43 |
|   133 |           1 | Fail    | cross                                       | diamond        |             12 |          54.71 |
|   134 |           1 | Success | diamond                                     | diamond        |             22 |         112.82 |
|   135 |           1 | Success | cross                                       | cross          |             19 |          87.41 |
|   136 |           1 | Fail    | asterisk                                    | triangle       |             27 |         128.00 |
|   137 |           1 | Fail    | cross                                       | diamond        |             32 |         131.07 |
|   138 |           1 | Fail    | square                                      | asterisk       |             23 |         102.14 |
|   139 |           1 | Fail    | circle                                      | cross          |             21 |          92.13 |
|   140 |           1 | Fail    | square                                      | circle         |              7 |          34.17 |
|   141 |           1 | Fail    | diamond                                     | triangle       |             14 |          65.56 |
|   142 |           1 | Success | triangle                                    | triangle       |             11 |          51.15 |
|   143 |           1 | Fail    | triangle                                    | cross          |             16 |          80.12 |
|   144 |           1 | Fail    | cross                                       | diamond        |             19 |          78.49 |
|   145 |           1 | Success | diamond                                     | diamond        |             20 |          88.81 |
|   146 |           1 | Fail    | triangle                                    | square         |             18 |          81.41 |
|   147 |           1 | Success | square                                      | square         |             11 |          52.71 |
|   148 |           1 | Success | square                                      | square         |             18 |          90.41 |
|   149 |           1 | Success | circle                                      | circle         |             20 |          86.06 |
|   150 |           1 | Fail    | diamond                                     | square         |             18 |          79.00 |
```

## Cooling and Jetson temperatures

- Pause between temperature batches: 5 minutes
- Pause between topologies: 15 minutes
- Temperature snapshots recorded: 68
- Raw temperature data: `temperatures.jsonl`

```text
| Recorded (UTC)                   | Phase            | Pause       | Agent1 C | Agent2 C | Agent3 C | Agent4 C | Agent5 C | Maximum C |
| -------------------------------- | ---------------- | ----------- | -------- | -------- | -------- | -------- | -------- | --------- |
| 2026-05-13T01:35:46.560054+00:00 | cooling_start    | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T01:36:46.938980+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T01:37:47.318565+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T01:38:47.797075+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T01:39:48.325354+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T01:40:47.004031+00:00 | cooling_end      | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:50:22.000304+00:00 | cooling_start    | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:51:22.529161+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:52:22.868120+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:53:23.326159+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:54:23.705541+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T02:55:22.754302+00:00 | cooling_end      | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:09:43.965448+00:00 | cooling_start    | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:10:44.525395+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:11:44.972523+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:12:45.351100+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:13:45.870864+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:14:46.299036+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:15:46.827858+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:16:47.426625+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:17:47.935546+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:18:48.364486+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:19:48.793755+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:20:49.521926+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:21:49.858061+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:22:50.225617+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:23:50.549504+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T04:24:44.353984+00:00 | cooling_end      | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T05:23:45.836527+00:00 | cooling_start    | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T05:24:46.415490+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T05:25:46.861491+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T05:26:47.634553+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T05:27:48.052443+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T05:28:46.490806+00:00 | cooling_end      | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T06:30:54.496336+00:00 | cooling_start    | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T06:31:55.134949+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T06:32:55.719710+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T06:33:56.392603+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T06:34:56.921887+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T06:35:54.911096+00:00 | cooling_end      | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:38:51.055525+00:00 | cooling_start    | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:39:51.883955+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:40:52.572582+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:41:53.184106+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:42:53.865034+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:43:54.408808+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:44:55.050301+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:45:55.626925+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:46:56.355814+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:47:56.842452+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:48:57.363732+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:49:57.942250+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:50:58.520356+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:51:59.181439+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:52:59.838748+00:00 | cooling_interval | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T07:53:51.717073+00:00 | cooling_end      | topology    |        - |        - |        - |        - |        - |         - |
| 2026-05-13T09:03:41.904423+00:00 | cooling_start    | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T09:04:42.592823+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T09:05:43.271390+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T09:06:43.959901+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T09:07:44.489220+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T09:08:42.557772+00:00 | cooling_end      | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T10:23:15.446157+00:00 | cooling_start    | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T10:24:16.317880+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T10:25:17.014766+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T10:26:17.837463+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T10:27:18.426158+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T10:28:16.242656+00:00 | cooling_end      | temperature |        - |        - |        - |        - |        - |         - |
```
