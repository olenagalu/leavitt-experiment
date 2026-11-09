# Circle study report

## Progress

- Study: `run-a364a9198797-circle-study`
- Status: complete
- Completed batches: 5/5
- Completed trials: 250/250
- Topologies: Circle
- Temperatures: 0, 0.05, 0.1, 0.2, 1

## Batch summary

| Topology | Temperature | Status   | Trials |  Success rate | Average total messages | Average time (seconds) | Detailed report                                                |
| -------- | ----------: | -------- | -----: | ------------: | ---------------------: | ---------------------: | -------------------------------------------------------------- |
| Circle   |           0 | complete |  50/50 | 40.0% (20/50) |                  16.58 |                 744.64 | [circle / temperature 0](circle/temperature-0/report.md)       |
| Circle   |        0.05 | complete |  50/50 | 50.0% (25/50) |                  16.34 |                 722.20 | [circle / temperature 0.05](circle/temperature-0.05/report.md) |
| Circle   |         0.1 | complete |  50/50 | 44.0% (22/50) |                  16.94 |                 779.15 | [circle / temperature 0.1](circle/temperature-0.1/report.md)   |
| Circle   |         0.2 | complete |  50/50 | 40.0% (20/50) |                  17.58 |                 794.79 | [circle / temperature 0.2](circle/temperature-0.2/report.md)   |
| Circle   |           1 | complete |  50/50 | 48.0% (24/50) |                  18.02 |                1030.52 | [circle / temperature 1](circle/temperature-1/report.md)       |

## Overall results

- Completed trials: 250/250
- Average time: 814.26 seconds
- Average total messages: 17.09
- Success rate: 111/250 (44.4%)
- Reconnect pauses: 1 across 1 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities by temperature

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender at that temperature.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

### Temperature 0

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |   Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | ------------- |
| Agent1 | Agent2    |                  2 |      71 |                    154 | 46.1% (0.461) |
| Agent1 | Agent5    |                  2 |      83 |                    154 | 53.9% (0.539) |
| Agent2 | Agent1    |                  2 |      95 |                    167 | 56.9% (0.569) |
| Agent2 | Agent3    |                  2 |      72 |                    167 | 43.1% (0.431) |
| Agent3 | Agent2    |                  2 |      85 |                    172 | 49.4% (0.494) |
| Agent3 | Agent4    |                  2 |      87 |                    172 | 50.6% (0.506) |
| Agent4 | Agent3    |                  2 |      99 |                    176 | 56.2% (0.562) |
| Agent4 | Agent5    |                  2 |      77 |                    176 | 43.8% (0.438) |
| Agent5 | Agent1    |                  2 |      73 |                    160 | 45.6% (0.456) |
| Agent5 | Agent4    |                  2 |      87 |                    160 | 54.4% (0.544) |
```

### Temperature 0.05

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |   Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | ------------- |
| Agent1 | Agent2    |                  2 |      97 |                    199 | 48.7% (0.487) |
| Agent1 | Agent5    |                  2 |     102 |                    199 | 51.3% (0.513) |
| Agent2 | Agent1    |                  2 |      74 |                    145 | 51.0% (0.510) |
| Agent2 | Agent3    |                  2 |      71 |                    145 | 49.0% (0.490) |
| Agent3 | Agent2    |                  2 |      88 |                    159 | 55.3% (0.553) |
| Agent3 | Agent4    |                  2 |      71 |                    159 | 44.7% (0.447) |
| Agent4 | Agent3    |                  2 |      82 |                    149 | 55.0% (0.550) |
| Agent4 | Agent5    |                  2 |      67 |                    149 | 45.0% (0.450) |
| Agent5 | Agent1    |                  2 |      82 |                    165 | 49.7% (0.497) |
| Agent5 | Agent4    |                  2 |      83 |                    165 | 50.3% (0.503) |
```

### Temperature 0.1

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |   Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | ------------- |
| Agent1 | Agent2    |                  2 |     103 |                    185 | 55.7% (0.557) |
| Agent1 | Agent5    |                  2 |      82 |                    185 | 44.3% (0.443) |
| Agent2 | Agent1    |                  2 |      82 |                    160 | 51.2% (0.512) |
| Agent2 | Agent3    |                  2 |      78 |                    160 | 48.8% (0.487) |
| Agent3 | Agent2    |                  2 |      87 |                    170 | 51.2% (0.512) |
| Agent3 | Agent4    |                  2 |      83 |                    170 | 48.8% (0.488) |
| Agent4 | Agent3    |                  2 |      80 |                    144 | 55.6% (0.556) |
| Agent4 | Agent5    |                  2 |      64 |                    144 | 44.4% (0.444) |
| Agent5 | Agent1    |                  2 |      92 |                    188 | 48.9% (0.489) |
| Agent5 | Agent4    |                  2 |      96 |                    188 | 51.1% (0.511) |
```

### Temperature 0.2

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |   Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | ------------- |
| Agent1 | Agent2    |                  2 |      89 |                    180 | 49.4% (0.494) |
| Agent1 | Agent5    |                  2 |      91 |                    180 | 50.6% (0.506) |
| Agent2 | Agent1    |                  2 |      92 |                    169 | 54.4% (0.544) |
| Agent2 | Agent3    |                  2 |      77 |                    169 | 45.6% (0.456) |
| Agent3 | Agent2    |                  2 |      94 |                    161 | 58.4% (0.584) |
| Agent3 | Agent4    |                  2 |      67 |                    161 | 41.6% (0.416) |
| Agent4 | Agent3    |                  2 |     100 |                    200 | 50.0% (0.500) |
| Agent4 | Agent5    |                  2 |     100 |                    200 | 50.0% (0.500) |
| Agent5 | Agent1    |                  2 |      76 |                    169 | 45.0% (0.450) |
| Agent5 | Agent4    |                  2 |      93 |                    169 | 55.0% (0.550) |
```

### Temperature 1

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |   Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | ------------- |
| Agent1 | Agent2    |                  2 |      80 |                    182 | 44.0% (0.440) |
| Agent1 | Agent5    |                  2 |     102 |                    182 | 56.0% (0.560) |
| Agent2 | Agent1    |                  2 |      93 |                    186 | 50.0% (0.500) |
| Agent2 | Agent3    |                  2 |      93 |                    186 | 50.0% (0.500) |
| Agent3 | Agent2    |                  2 |      88 |                    172 | 51.2% (0.512) |
| Agent3 | Agent4    |                  2 |      84 |                    172 | 48.8% (0.488) |
| Agent4 | Agent3    |                  2 |     104 |                    183 | 56.8% (0.568) |
| Agent4 | Agent5    |                  2 |      79 |                    183 | 43.2% (0.432) |
| Agent5 | Agent1    |                  2 |      78 |                    176 | 44.3% (0.443) |
| Agent5 | Agent4    |                  2 |      98 |                    176 | 55.7% (0.557) |
```

## Overall recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |   Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | ------------- |
| Agent1 | Agent2    |                  2 |     440 |                    900 | 48.9% (0.489) |
| Agent1 | Agent5    |                  2 |     460 |                    900 | 51.1% (0.511) |
| Agent2 | Agent1    |                  2 |     436 |                    827 | 52.7% (0.527) |
| Agent2 | Agent3    |                  2 |     391 |                    827 | 47.3% (0.473) |
| Agent3 | Agent2    |                  2 |     442 |                    834 | 53.0% (0.530) |
| Agent3 | Agent4    |                  2 |     392 |                    834 | 47.0% (0.470) |
| Agent4 | Agent3    |                  2 |     465 |                    852 | 54.6% (0.546) |
| Agent4 | Agent5    |                  2 |     387 |                    852 | 45.4% (0.454) |
| Agent5 | Agent1    |                  2 |     401 |                    858 | 46.7% (0.467) |
| Agent5 | Agent4    |                  2 |     457 |                    858 | 53.3% (0.533) |
```

### Excluded fallback routes

```text
| Sender | Target source          | Count |
| ------ | ---------------------- | ----- |
| Agent1 | client_default_invalid |     1 |
| Agent3 | client_default         |     1 |
```

## Cooling pauses

- Pause between temperature batches: 5 minutes
