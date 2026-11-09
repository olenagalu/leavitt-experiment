# Chain study report

## Progress

- Study: `run-7ab48f7b7ecb-chain-study`
- Status: complete
- Completed batches: 5/5
- Completed trials: 250/250
- Topologies: Chain
- Temperatures: 0, 0.05, 0.1, 0.2, 1

## Batch summary

| Topology | Temperature | Status   | Trials |  Success rate | Average total messages | Average time (seconds) | Detailed report                                              |
| -------- | ----------: | -------- | -----: | ------------: | ---------------------: | ---------------------: | ------------------------------------------------------------ |
| Chain    |           0 | complete |  50/50 | 40.0% (20/50) |                  26.36 |                1248.34 | [chain / temperature 0](chain/temperature-0/report.md)       |
| Chain    |        0.05 | complete |  50/50 | 40.0% (20/50) |                  21.84 |                 972.78 | [chain / temperature 0.05](chain/temperature-0.05/report.md) |
| Chain    |         0.1 | complete |  50/50 | 34.0% (17/50) |                  23.54 |                1087.13 | [chain / temperature 0.1](chain/temperature-0.1/report.md)   |
| Chain    |         0.2 | complete |  50/50 | 38.0% (19/50) |                  26.66 |                1279.57 | [chain / temperature 0.2](chain/temperature-0.2/report.md)   |
| Chain    |           1 | complete |  50/50 | 20.0% (10/50) |                  24.64 |                1306.60 | [chain / temperature 1](chain/temperature-1/report.md)       |

## Overall results

- Completed trials: 250/250
- Average time: 1178.89 seconds
- Average total messages: 24.61
- Success rate: 86/250 (34.4%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities by temperature

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender at that temperature.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

### Temperature 0

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent2    |                  1 |     280 |                    280 | 100.0% (1.000) |
| Agent2 | Agent1    |                  2 |     139 |                    250 |  55.6% (0.556) |
| Agent2 | Agent3    |                  2 |     111 |                    250 |  44.4% (0.444) |
| Agent3 | Agent2    |                  2 |     125 |                    259 |  48.3% (0.483) |
| Agent3 | Agent4    |                  2 |     134 |                    259 |  51.7% (0.517) |
| Agent4 | Agent3    |                  2 |     135 |                    276 |  48.9% (0.489) |
| Agent4 | Agent5    |                  2 |     141 |                    276 |  51.1% (0.511) |
| Agent5 | Agent4    |                  1 |     253 |                    253 | 100.0% (1.000) |
```

### Temperature 0.05

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent2    |                  1 |     222 |                    222 | 100.0% (1.000) |
| Agent2 | Agent1    |                  2 |     123 |                    225 |  54.7% (0.547) |
| Agent2 | Agent3    |                  2 |     102 |                    225 |  45.3% (0.453) |
| Agent3 | Agent2    |                  2 |     110 |                    219 |  50.2% (0.502) |
| Agent3 | Agent4    |                  2 |     109 |                    219 |  49.8% (0.498) |
| Agent4 | Agent3    |                  2 |      92 |                    190 |  48.4% (0.484) |
| Agent4 | Agent5    |                  2 |      98 |                    190 |  51.6% (0.516) |
| Agent5 | Agent4    |                  1 |     236 |                    236 | 100.0% (1.000) |
```

### Temperature 0.1

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent2    |                  1 |     239 |                    239 | 100.0% (1.000) |
| Agent2 | Agent1    |                  2 |     141 |                    259 |  54.4% (0.544) |
| Agent2 | Agent3    |                  2 |     118 |                    259 |  45.6% (0.456) |
| Agent3 | Agent2    |                  2 |     110 |                    232 |  47.4% (0.474) |
| Agent3 | Agent4    |                  2 |     122 |                    232 |  52.6% (0.526) |
| Agent4 | Agent3    |                  2 |     108 |                    222 |  48.6% (0.486) |
| Agent4 | Agent5    |                  2 |     114 |                    222 |  51.4% (0.514) |
| Agent5 | Agent4    |                  1 |     224 |                    224 | 100.0% (1.000) |
```

### Temperature 0.2

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent2    |                  1 |     270 |                    270 | 100.0% (1.000) |
| Agent2 | Agent1    |                  2 |     155 |                    293 |  52.9% (0.529) |
| Agent2 | Agent3    |                  2 |     138 |                    293 |  47.1% (0.471) |
| Agent3 | Agent2    |                  2 |     123 |                    264 |  46.6% (0.466) |
| Agent3 | Agent4    |                  2 |     141 |                    264 |  53.4% (0.534) |
| Agent4 | Agent3    |                  2 |     121 |                    256 |  47.3% (0.473) |
| Agent4 | Agent5    |                  2 |     135 |                    256 |  52.7% (0.527) |
| Agent5 | Agent4    |                  1 |     246 |                    246 | 100.0% (1.000) |
```

### Temperature 1

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent2    |                  1 |     256 |                    256 | 100.0% (1.000) |
| Agent2 | Agent1    |                  2 |     139 |                    256 |  54.3% (0.543) |
| Agent2 | Agent3    |                  2 |     117 |                    256 |  45.7% (0.457) |
| Agent3 | Agent2    |                  2 |     110 |                    218 |  50.5% (0.505) |
| Agent3 | Agent4    |                  2 |     108 |                    218 |  49.5% (0.495) |
| Agent4 | Agent3    |                  2 |     117 |                    247 |  47.4% (0.474) |
| Agent4 | Agent5    |                  2 |     130 |                    247 |  52.6% (0.526) |
| Agent5 | Agent4    |                  1 |     251 |                    251 | 100.0% (1.000) |
```

## Overall recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent2    |                  1 |    1267 |                   1267 | 100.0% (1.000) |
| Agent2 | Agent1    |                  2 |     697 |                   1283 |  54.3% (0.543) |
| Agent2 | Agent3    |                  2 |     586 |                   1283 |  45.7% (0.457) |
| Agent3 | Agent2    |                  2 |     578 |                   1192 |  48.5% (0.485) |
| Agent3 | Agent4    |                  2 |     614 |                   1192 |  51.5% (0.515) |
| Agent4 | Agent3    |                  2 |     573 |                   1191 |  48.1% (0.481) |
| Agent4 | Agent5    |                  2 |     618 |                   1191 |  51.9% (0.519) |
| Agent5 | Agent4    |                  1 |    1210 |                   1210 | 100.0% (1.000) |
```

### Excluded fallback routes

```text
| Sender | Target source   | Count |
| ------ | --------------- | ----- |
| Agent1 | client_assigned |     2 |
| Agent2 | client_assigned |     1 |
| Agent3 | client_assigned |     1 |
| Agent4 | client_assigned |     2 |
| Agent5 | client_assigned |     2 |
| Agent5 | client_default  |     1 |
```

## Cooling pauses

- Pause between temperature batches: 5 minutes
