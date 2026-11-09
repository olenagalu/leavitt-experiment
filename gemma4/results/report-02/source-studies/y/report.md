# Y topology study report

## Progress

- Study: `run-de35e52effd2-y-study`
- Status: complete
- Completed batches: 5/5
- Completed trials: 250/250
- Topologies: Y topology
- Temperatures: 0, 0.05, 0.1, 0.2, 1

## Batch summary

| Topology   | Temperature | Status   | Trials |  Success rate | Average total messages | Average time (seconds) | Detailed report                                      |
| ---------- | ----------: | -------- | -----: | ------------: | ---------------------: | ---------------------: | ---------------------------------------------------- |
| Y topology |           0 | complete |  50/50 | 48.0% (24/50) |                  25.46 |                1266.01 | [y / temperature 0](y/temperature-0/report.md)       |
| Y topology |        0.05 | complete |  50/50 | 48.0% (24/50) |                  25.42 |                1245.95 | [y / temperature 0.05](y/temperature-0.05/report.md) |
| Y topology |         0.1 | complete |  50/50 | 46.0% (23/50) |                  24.40 |                1219.48 | [y / temperature 0.1](y/temperature-0.1/report.md)   |
| Y topology |         0.2 | complete |  50/50 | 54.0% (27/50) |                  27.82 |                1435.46 | [y / temperature 0.2](y/temperature-0.2/report.md)   |
| Y topology |           1 | complete |  50/50 | 28.0% (14/50) |                  28.18 |                1679.70 | [y / temperature 1](y/temperature-1/report.md)       |

## Overall results

- Completed trials: 250/250
- Average time: 1369.32 seconds
- Average total messages: 26.26
- Success rate: 112/250 (44.8%)
- Reconnect pauses: 0 across 0 trial(s); 0.00 paused seconds excluded from experiment time

## Recipient-choice probabilities by temperature

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender at that temperature.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

### Temperature 0

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent3    |                  1 |     244 |                    244 | 100.0% (1.000) |
| Agent2 | Agent3    |                  1 |     263 |                    263 | 100.0% (1.000) |
| Agent3 | Agent1    |                  3 |      58 |                    237 |  24.5% (0.245) |
| Agent3 | Agent2    |                  3 |      54 |                    237 |  22.8% (0.228) |
| Agent3 | Agent4    |                  3 |     125 |                    237 |  52.7% (0.527) |
| Agent4 | Agent3    |                  2 |     197 |                    250 |  78.8% (0.788) |
| Agent4 | Agent5    |                  2 |      53 |                    250 |  21.2% (0.212) |
| Agent5 | Agent4    |                  1 |     278 |                    278 | 100.0% (1.000) |
```

### Temperature 0.05

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent3    |                  1 |     269 |                    269 | 100.0% (1.000) |
| Agent2 | Agent3    |                  1 |     267 |                    267 | 100.0% (1.000) |
| Agent3 | Agent1    |                  3 |      60 |                    234 |  25.6% (0.256) |
| Agent3 | Agent2    |                  3 |      62 |                    234 |  26.5% (0.265) |
| Agent3 | Agent4    |                  3 |     112 |                    234 |  47.9% (0.479) |
| Agent4 | Agent3    |                  2 |     197 |                    260 |  75.8% (0.758) |
| Agent4 | Agent5    |                  2 |      63 |                    260 |  24.2% (0.242) |
| Agent5 | Agent4    |                  1 |     240 |                    240 | 100.0% (1.000) |
```

### Temperature 0.1

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent3    |                  1 |     230 |                    230 | 100.0% (1.000) |
| Agent2 | Agent3    |                  1 |     255 |                    255 | 100.0% (1.000) |
| Agent3 | Agent1    |                  3 |      62 |                    228 |  27.2% (0.272) |
| Agent3 | Agent2    |                  3 |      58 |                    228 |  25.4% (0.254) |
| Agent3 | Agent4    |                  3 |     108 |                    228 |  47.4% (0.474) |
| Agent4 | Agent3    |                  2 |     227 |                    273 |  83.2% (0.832) |
| Agent4 | Agent5    |                  2 |      46 |                    273 |  16.8% (0.168) |
| Agent5 | Agent4    |                  1 |     233 |                    233 | 100.0% (1.000) |
```

### Temperature 0.2

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent3    |                  1 |     277 |                    277 | 100.0% (1.000) |
| Agent2 | Agent3    |                  1 |     297 |                    297 | 100.0% (1.000) |
| Agent3 | Agent1    |                  3 |      67 |                    287 |  23.3% (0.233) |
| Agent3 | Agent2    |                  3 |      72 |                    287 |  25.1% (0.251) |
| Agent3 | Agent4    |                  3 |     148 |                    287 |  51.6% (0.516) |
| Agent4 | Agent3    |                  2 |     193 |                    242 |  79.8% (0.798) |
| Agent4 | Agent5    |                  2 |      49 |                    242 |  20.2% (0.202) |
| Agent5 | Agent4    |                  1 |     285 |                    285 | 100.0% (1.000) |
```

### Temperature 1

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent3    |                  1 |     282 |                    282 | 100.0% (1.000) |
| Agent2 | Agent3    |                  1 |     311 |                    311 | 100.0% (1.000) |
| Agent3 | Agent1    |                  3 |      51 |                    233 |  21.9% (0.219) |
| Agent3 | Agent2    |                  3 |      67 |                    233 |  28.8% (0.288) |
| Agent3 | Agent4    |                  3 |     115 |                    233 |  49.4% (0.494) |
| Agent4 | Agent3    |                  2 |     197 |                    248 |  79.4% (0.794) |
| Agent4 | Agent5    |                  2 |      51 |                    248 |  20.6% (0.206) |
| Agent5 | Agent4    |                  1 |     331 |                    331 | 100.0% (1.000) |
```

## Overall recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

```text
| Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Agent1 | Agent3    |                  1 |    1302 |                   1302 | 100.0% (1.000) |
| Agent2 | Agent3    |                  1 |    1393 |                   1393 | 100.0% (1.000) |
| Agent3 | Agent1    |                  3 |     298 |                   1219 |  24.4% (0.244) |
| Agent3 | Agent2    |                  3 |     313 |                   1219 |  25.7% (0.257) |
| Agent3 | Agent4    |                  3 |     608 |                   1219 |  49.9% (0.499) |
| Agent4 | Agent3    |                  2 |    1011 |                   1273 |  79.4% (0.794) |
| Agent4 | Agent5    |                  2 |     262 |                   1273 |  20.6% (0.206) |
| Agent5 | Agent4    |                  1 |    1367 |                   1367 | 100.0% (1.000) |
```

### Excluded fallback routes

```text
| Sender | Target source   | Count |
| ------ | --------------- | ----- |
| Agent1 | client_default  |     2 |
| Agent2 | client_assigned |     1 |
| Agent2 | client_default  |     1 |
| Agent3 | client_assigned |     3 |
| Agent4 | client_assigned |     1 |
| Agent5 | client_default  |     2 |
```

## Cooling pauses

- Pause between temperature batches: 5 minutes
