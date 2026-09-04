# gemma4:e2b-it-qat — Leavitt full study report

## Progress

- Model: `gemma4:e2b-it-qat`
- Study: `20260513-0157-leavitt-study`
- Status: running
- Completed batches: 1/12
- Completed trials: 50/600
- Topologies: Circle, Y topology, Wheel, Chain
- Temperatures: 0, 0.5, 1

## Batch summary

| Topology   | Temperature | Status   | Trials |  Success rate | Average total messages | Average time (seconds) | Detailed report                                              |
| ---------- | ----------: | -------- | -----: | ------------: | ---------------------: | ---------------------: | ------------------------------------------------------------ |
| Circle     |           0 | complete |  50/50 | 38.0% (19/50) |                  17.44 |                 783.43 | [circle / temperature 0](circle/temperature-0/report.md)     |
| Circle     |         0.5 | running  |   0/50 |    0.0% (0/0) |                   0.00 |                   0.00 | [circle / temperature 0.5](circle/temperature-0.5/report.md) |
| Circle     |           1 | pending  |   0/50 |    0.0% (0/0) |                   0.00 |                   0.00 | -                                                            |
| Y topology |           0 | pending  |   0/50 |    0.0% (0/0) |                   0.00 |                   0.00 | -                                                            |
| Y topology |         0.5 | pending  |   0/50 |    0.0% (0/0) |                   0.00 |                   0.00 | -                                                            |
| Y topology |           1 | pending  |   0/50 |    0.0% (0/0) |                   0.00 |                   0.00 | -                                                            |
| Wheel      |           0 | pending  |   0/50 |    0.0% (0/0) |                   0.00 |                   0.00 | -                                                            |
| Wheel      |         0.5 | pending  |   0/50 |    0.0% (0/0) |                   0.00 |                   0.00 | -                                                            |
| Wheel      |           1 | pending  |   0/50 |    0.0% (0/0) |                   0.00 |                   0.00 | -                                                            |
| Chain      |           0 | pending  |   0/50 |    0.0% (0/0) |                   0.00 |                   0.00 | -                                                            |
| Chain      |         0.5 | pending  |   0/50 |    0.0% (0/0) |                   0.00 |                   0.00 | -                                                            |
| Chain      |           1 | pending  |   0/50 |    0.0% (0/0) |                   0.00 |                   0.00 | -                                                            |

## Overall results

- Completed trials: 50/600
- Average time: 783.43 seconds
- Average total messages: 17.44
- Success rate: 19/50 (38.0%)

## Topology summary

| Topology   | Trials | Successes | Success rate | Average total messages | Average time (seconds) |
| ---------- | -----: | --------: | -----------: | ---------------------: | ---------------------: |
| Circle     |     50 |        19 |        38.0% |                  17.44 |                 783.43 |
| Y topology |      0 |         0 |         0.0% |                   0.00 |                   0.00 |
| Wheel      |      0 |         0 |         0.0% |                   0.00 |                   0.00 |
| Chain      |      0 |         0 |         0.0% |                   0.00 |                   0.00 |

## Timing

Total trial time measures each trial from launch through completion. Full topology span measures the first trial start through the last trial completion for that topology, including cooling pauses between its temperature batches. Response time measures the server wait after sending a turn request.

- Longest trial: 1736.27 seconds (Circle, temperature 0, trial 26)
- Longest response: 120.41 seconds (Agent5, Circle, temperature 0, trial 7)

### Time by topology

```text
| Topology | Trials | Summed trial time (s) | Full topology span (s) | Average trial (s) | Longest trial (s) | Longest trial ID | Longest response (s) | Response agent |
| -------- | ------ | --------------------- | ---------------------- | ----------------- | ----------------- | ---------------- | -------------------- | -------------- |
| Circle   |     50 |              40555.71 |               40663.89 |            811.11 |           1736.27 | 26               |               120.41 | Agent5         |
```

### Time for every trial

```text
| Topology | Temperature | Trial | Total trial (s) | Experiment time (s) | Longest response (s) | Response agent | Response turn |
| -------- | ----------- | ----- | --------------- | ------------------- | -------------------- | -------------- | ------------- |
| Circle   |           0 |     1 |         1145.53 |             1128.02 |               111.77 | Agent4         |            18 |
| Circle   |           0 |     2 |         1256.04 |             1178.61 |               110.95 | Agent1         |             9 |
| Circle   |           0 |     3 |          387.80 |              372.52 |                84.70 | Agent5         |             3 |
| Circle   |           0 |     4 |          778.59 |              764.37 |               119.13 | Agent5         |            13 |
| Circle   |           0 |     5 |         1580.26 |             1564.94 |               120.26 | Agent2         |            22 |
| Circle   |           0 |     6 |          973.17 |              956.91 |                93.33 | Agent5         |            23 |
| Circle   |           0 |     7 |          692.76 |              674.12 |               120.41 | Agent5         |            15 |
| Circle   |           0 |     8 |          659.92 |              643.95 |                97.23 | Agent3         |            11 |
| Circle   |           0 |     9 |          868.73 |              796.05 |                96.57 | Agent5         |            16 |
| Circle   |           0 |    10 |          160.47 |              142.90 |                72.86 | Agent4         |             2 |
| Circle   |           0 |    11 |          420.92 |              404.27 |                82.04 | Agent3         |             9 |
| Circle   |           0 |    12 |          692.25 |              672.85 |               113.84 | Agent4         |            12 |
| Circle   |           0 |    13 |          635.18 |              620.81 |                85.03 | Agent4         |            12 |
| Circle   |           0 |    14 |          586.11 |              572.74 |                96.55 | Agent1         |            17 |
| Circle   |           0 |    15 |          817.69 |              800.24 |                85.66 | Agent2         |            21 |
| Circle   |           0 |    16 |          397.47 |              381.09 |                80.28 | Agent4         |             8 |
| Circle   |           0 |    17 |          634.54 |              560.34 |               115.94 | Agent4         |            15 |
| Circle   |           0 |    18 |          255.81 |              241.86 |                79.13 | Agent2         |             4 |
| Circle   |           0 |    19 |          889.75 |              873.63 |                80.87 | Agent1         |            10 |
| Circle   |           0 |    20 |          627.82 |              610.50 |               102.01 | Agent2         |            15 |
| Circle   |           0 |    21 |          459.38 |              441.95 |                57.48 | Agent4         |            15 |
| Circle   |           0 |    22 |          658.86 |              643.14 |                83.36 | Agent3         |             6 |
| Circle   |           0 |    23 |          905.81 |              890.64 |                88.42 | Agent1         |            17 |
| Circle   |           0 |    24 |         1097.07 |             1080.47 |                97.40 | Agent2         |            17 |
| Circle   |           0 |    25 |         1104.44 |             1031.36 |               113.34 | Agent3         |            12 |
| Circle   |           0 |    26 |         1736.27 |             1663.18 |                98.96 | Agent5         |            36 |
| Circle   |           0 |    27 |          642.71 |              568.81 |                85.51 | Agent2         |             9 |
| Circle   |           0 |    28 |          774.12 |              759.29 |               119.40 | Agent2         |            17 |
| Circle   |           0 |    29 |          810.22 |              795.24 |               108.47 | Agent4         |            14 |
| Circle   |           0 |    30 |         1073.70 |             1056.96 |               103.37 | Agent1         |            22 |
| Circle   |           0 |    31 |         1104.30 |             1028.28 |                93.52 | Agent4         |            24 |
| Circle   |           0 |    32 |          808.05 |              787.56 |               110.09 | Agent3         |            14 |
| Circle   |           0 |    33 |          277.58 |              262.30 |                81.41 | Agent2         |             9 |
| Circle   |           0 |    34 |         1489.50 |             1473.13 |               105.78 | Agent4         |            30 |
| Circle   |           0 |    35 |          768.42 |              753.52 |                96.40 | Agent1         |            17 |
| Circle   |           0 |    36 |          876.40 |              860.04 |                98.14 | Agent3         |            10 |
| Circle   |           0 |    37 |          507.75 |              492.34 |                83.31 | Agent2         |            13 |
| Circle   |           0 |    38 |          805.81 |              789.59 |                93.36 | Agent5         |            17 |
| Circle   |           0 |    39 |          672.30 |              656.47 |               114.68 | Agent2         |            16 |
| Circle   |           0 |    40 |          411.78 |              340.94 |                81.86 | Agent5         |             4 |
| Circle   |           0 |    41 |          302.37 |              286.06 |                43.75 | Agent4         |            11 |
| Circle   |           0 |    42 |         1330.97 |             1316.38 |               103.82 | Agent5         |            27 |
| Circle   |           0 |    43 |          572.95 |              556.37 |                93.61 | Agent3         |            10 |
| Circle   |           0 |    44 |         1198.62 |             1179.96 |               114.70 | Agent3         |            21 |
| Circle   |           0 |    45 |          980.38 |              963.36 |               106.12 | Agent2         |            20 |
| Circle   |           0 |    46 |          633.68 |              614.42 |                89.70 | Agent3         |             9 |
| Circle   |           0 |    47 |         1026.59 |              955.34 |                88.99 | Agent2         |            24 |
| Circle   |           0 |    48 |          823.96 |              807.75 |               111.77 | Agent3         |            13 |
| Circle   |           0 |    49 |         1530.99 |             1517.14 |               109.66 | Agent3         |            33 |
| Circle   |           0 |    50 |          709.92 |              638.80 |                83.21 | Agent4         |             6 |
```

## Recipient-choice probabilities by temperature

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender at that temperature.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

### Temperature 0

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |   Probability |
| -------- | ------ | --------- | ------------------ | ------- | ---------------------- | ------------- |
| Circle   | Agent1 | Agent2    |                  2 |      95 |                    188 | 50.5% (0.505) |
| Circle   | Agent1 | Agent5    |                  2 |      93 |                    188 | 49.5% (0.495) |
| Circle   | Agent2 | Agent1    |                  2 |      87 |                    172 | 50.6% (0.506) |
| Circle   | Agent2 | Agent3    |                  2 |      85 |                    172 | 49.4% (0.494) |
| Circle   | Agent3 | Agent2    |                  2 |      78 |                    166 | 47.0% (0.470) |
| Circle   | Agent3 | Agent4    |                  2 |      88 |                    166 | 53.0% (0.530) |
| Circle   | Agent4 | Agent3    |                  2 |     104 |                    180 | 57.8% (0.578) |
| Circle   | Agent4 | Agent5    |                  2 |      76 |                    180 | 42.2% (0.422) |
| Circle   | Agent5 | Agent1    |                  2 |      76 |                    164 | 46.3% (0.463) |
| Circle   | Agent5 | Agent4    |                  2 |      88 |                    164 | 53.7% (0.537) |
```

### Temperature 0.5

No explicit valid recipient choices were recorded at this temperature.

### Temperature 1

No explicit valid recipient choices were recorded at this temperature.

## Overall recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |   Probability |
| -------- | ------ | --------- | ------------------ | ------- | ---------------------- | ------------- |
| Circle   | Agent1 | Agent2    |                  2 |      95 |                    188 | 50.5% (0.505) |
| Circle   | Agent1 | Agent5    |                  2 |      93 |                    188 | 49.5% (0.495) |
| Circle   | Agent2 | Agent1    |                  2 |      87 |                    172 | 50.6% (0.506) |
| Circle   | Agent2 | Agent3    |                  2 |      85 |                    172 | 49.4% (0.494) |
| Circle   | Agent3 | Agent2    |                  2 |      78 |                    166 | 47.0% (0.470) |
| Circle   | Agent3 | Agent4    |                  2 |      88 |                    166 | 53.0% (0.530) |
| Circle   | Agent4 | Agent3    |                  2 |     104 |                    180 | 57.8% (0.578) |
| Circle   | Agent4 | Agent5    |                  2 |      76 |                    180 | 42.2% (0.422) |
| Circle   | Agent5 | Agent1    |                  2 |      76 |                    164 | 46.3% (0.463) |
| Circle   | Agent5 | Agent4    |                  2 |      88 |                    164 | 53.7% (0.537) |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| Circle   | Agent2 | server_assigned |     1 |
| Circle   | Agent5 | server_assigned |     1 |
```

## Cooling and Jetson temperatures

- Pause between temperature batches: 5 minutes
- Pause between topologies: 15 minutes
- Temperature snapshots recorded: 6
- Raw temperature data: `temperatures.jsonl`

```text
| Recorded (UTC)                   | Phase            | Pause       | Agent1 C | Agent2 C | Agent3 C | Agent4 C | Agent5 C | Maximum C |
| -------------------------------- | ---------------- | ----------- | -------- | -------- | -------- | -------- | -------- | --------- |
| 2026-05-13T13:15:10.858359+00:00 | cooling_start    | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T13:16:11.516870+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T13:17:12.030287+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T13:18:12.374974+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T13:19:13.057762+00:00 | cooling_interval | temperature |        - |        - |        - |        - |        - |         - |
| 2026-05-13T13:20:11.318309+00:00 | cooling_end      | temperature |        - |        - |        - |        - |        - |         - |
```
