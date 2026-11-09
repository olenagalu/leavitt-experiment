# Leavitt full study report

## Progress

- Study: `run-2ff44b7bef35-four-topologies-study`
- Status: complete
- Completed batches: 20/20
- Completed trials: 1000/1000
- Topologies: Circle, Chain, Y topology, Wheel
- Temperatures: 0, 0.05, 0.1, 0.2, 1

## Batch summary

| Topology   | Temperature | Status   | Trials |  Success rate | Average total messages | Average time (seconds) | Detailed report                                                |
| ---------- | ----------: | -------- | -----: | ------------: | ---------------------: | ---------------------: | -------------------------------------------------------------- |
| Circle     |           0 | complete |  50/50 | 34.0% (17/50) |                  14.30 |                 172.76 | [circle / temperature 0](circle/temperature-0/report.md)       |
| Circle     |        0.05 | complete |  50/50 | 22.0% (11/50) |                  19.00 |                 195.25 | [circle / temperature 0.05](circle/temperature-0.05/report.md) |
| Circle     |         0.1 | complete |  50/50 | 28.0% (14/50) |                  16.28 |                 173.60 | [circle / temperature 0.1](circle/temperature-0.1/report.md)   |
| Circle     |         0.2 | complete |  50/50 | 26.0% (13/50) |                  14.24 |                 158.73 | [circle / temperature 0.2](circle/temperature-0.2/report.md)   |
| Circle     |           1 | complete |  50/50 |  16.0% (8/50) |                  14.44 |                 159.27 | [circle / temperature 1](circle/temperature-1/report.md)       |
| Chain      |           0 | complete |  50/50 |  18.0% (9/50) |                  16.90 |                 221.85 | [chain / temperature 0](chain/temperature-0/report.md)         |
| Chain      |        0.05 | complete |  50/50 |  18.0% (9/50) |                  16.42 |                 206.12 | [chain / temperature 0.05](chain/temperature-0.05/report.md)   |
| Chain      |         0.1 | complete |  50/50 | 20.0% (10/50) |                  18.76 |                 202.54 | [chain / temperature 0.1](chain/temperature-0.1/report.md)     |
| Chain      |         0.2 | complete |  50/50 | 26.0% (13/50) |                  17.12 |                 203.26 | [chain / temperature 0.2](chain/temperature-0.2/report.md)     |
| Chain      |           1 | complete |  50/50 | 32.0% (16/50) |                  16.48 |                 177.91 | [chain / temperature 1](chain/temperature-1/report.md)         |
| Y topology |           0 | complete |  50/50 | 28.0% (14/50) |                  18.48 |                 245.22 | [y / temperature 0](y/temperature-0/report.md)                 |
| Y topology |        0.05 | complete |  50/50 | 32.0% (16/50) |                  18.62 |                 212.86 | [y / temperature 0.05](y/temperature-0.05/report.md)           |
| Y topology |         0.1 | complete |  50/50 | 34.0% (17/50) |                  17.00 |                 194.69 | [y / temperature 0.1](y/temperature-0.1/report.md)             |
| Y topology |         0.2 | complete |  50/50 | 22.0% (11/50) |                  19.56 |                 302.10 | [y / temperature 0.2](y/temperature-0.2/report.md)             |
| Y topology |           1 | complete |  50/50 | 24.0% (12/50) |                  20.22 |                 246.11 | [y / temperature 1](y/temperature-1/report.md)                 |
| Wheel      |           0 | complete |  50/50 | 26.0% (13/50) |                  20.56 |                 268.77 | [wheel / temperature 0](wheel/temperature-0/report.md)         |
| Wheel      |        0.05 | complete |  50/50 | 40.0% (20/50) |                  17.56 |                 199.91 | [wheel / temperature 0.05](wheel/temperature-0.05/report.md)   |
| Wheel      |         0.1 | complete |  50/50 | 22.0% (11/50) |                  18.32 |                 218.88 | [wheel / temperature 0.1](wheel/temperature-0.1/report.md)     |
| Wheel      |         0.2 | complete |  50/50 | 30.0% (15/50) |                  18.46 |                 257.79 | [wheel / temperature 0.2](wheel/temperature-0.2/report.md)     |
| Wheel      |           1 | complete |  50/50 |  18.0% (9/50) |                  18.24 |                 214.09 | [wheel / temperature 1](wheel/temperature-1/report.md)         |

## Overall results

- Completed trials: 1000/1000
- Average time: 211.59 seconds
- Average total messages: 17.55
- Success rate: 258/1000 (25.8%)
- Reconnect pauses: 29 across 29 trial(s); 1152.33 paused seconds excluded from experiment time

## Topology summary

| Topology   | Trials | Successes | Success rate | Average total messages | Average time (seconds) |
| ---------- | -----: | --------: | -----------: | ---------------------: | ---------------------: |
| Circle     |    250 |        63 |        25.2% |                  15.65 |                 171.92 |
| Chain      |    250 |        57 |        22.8% |                  17.14 |                 202.34 |
| Y topology |    250 |        70 |        28.0% |                  18.78 |                 240.20 |
| Wheel      |    250 |        68 |        27.2% |                  18.63 |                 231.89 |

## Recipient-choice probabilities by temperature

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender at that temperature.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

### Temperature 0

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     194 |                    194 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     155 |                    170 |  91.2% (0.912) |
| Chain      | Agent2 | Agent3    |                  2 |      15 |                    170 |   8.8% (0.088) |
| Chain      | Agent3 | Agent2    |                  2 |     185 |                    197 |  93.9% (0.939) |
| Chain      | Agent3 | Agent4    |                  2 |      12 |                    197 |   6.1% (0.061) |
| Chain      | Agent4 | Agent3    |                  2 |      85 |                    167 |  50.9% (0.509) |
| Chain      | Agent4 | Agent5    |                  2 |      82 |                    167 |  49.1% (0.491) |
| Chain      | Agent5 | Agent4    |                  1 |     116 |                    116 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |      40 |                    135 |  29.6% (0.296) |
| Circle     | Agent1 | Agent5    |                  2 |      95 |                    135 |  70.4% (0.704) |
| Circle     | Agent2 | Agent1    |                  2 |     122 |                    136 |  89.7% (0.897) |
| Circle     | Agent2 | Agent3    |                  2 |      14 |                    136 |  10.3% (0.103) |
| Circle     | Agent3 | Agent2    |                  2 |     146 |                    151 |  96.7% (0.967) |
| Circle     | Agent3 | Agent4    |                  2 |       5 |                    151 |   3.3% (0.033) |
| Circle     | Agent4 | Agent3    |                  2 |     135 |                    156 |  86.5% (0.865) |
| Circle     | Agent4 | Agent5    |                  2 |      21 |                    156 |  13.5% (0.135) |
| Circle     | Agent5 | Agent1    |                  2 |      61 |                    137 |  44.5% (0.445) |
| Circle     | Agent5 | Agent4    |                  2 |      76 |                    137 |  55.5% (0.555) |
| Wheel      | Agent1 | Agent3    |                  1 |     204 |                    204 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     195 |                    195 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     143 |                    243 |  58.8% (0.588) |
| Wheel      | Agent3 | Agent2    |                  4 |      91 |                    243 |  37.4% (0.374) |
| Wheel      | Agent3 | Agent4    |                  4 |       4 |                    243 |   1.6% (0.016) |
| Wheel      | Agent3 | Agent5    |                  4 |       5 |                    243 |   2.1% (0.021) |
| Wheel      | Agent4 | Agent3    |                  1 |     203 |                    203 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     181 |                    181 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     176 |                    176 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     174 |                    174 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      92 |                    181 |  50.8% (0.508) |
| Y topology | Agent3 | Agent2    |                  3 |      63 |                    181 |  34.8% (0.348) |
| Y topology | Agent3 | Agent4    |                  3 |      26 |                    181 |  14.4% (0.144) |
| Y topology | Agent4 | Agent3    |                  2 |     153 |                    173 |  88.4% (0.884) |
| Y topology | Agent4 | Agent5    |                  2 |      20 |                    173 |  11.6% (0.116) |
| Y topology | Agent5 | Agent4    |                  1 |     211 |                    211 | 100.0% (1.000) |
```

### Temperature 0.05

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     169 |                    169 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     115 |                    127 |  90.6% (0.906) |
| Chain      | Agent2 | Agent3    |                  2 |      12 |                    127 |   9.4% (0.094) |
| Chain      | Agent3 | Agent2    |                  2 |     168 |                    174 |  96.6% (0.966) |
| Chain      | Agent3 | Agent4    |                  2 |       6 |                    174 |   3.4% (0.034) |
| Chain      | Agent4 | Agent3    |                  2 |     131 |                    175 |  74.9% (0.749) |
| Chain      | Agent4 | Agent5    |                  2 |      44 |                    175 |  25.1% (0.251) |
| Chain      | Agent5 | Agent4    |                  1 |     176 |                    176 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |      45 |                    176 |  25.6% (0.256) |
| Circle     | Agent1 | Agent5    |                  2 |     131 |                    176 |  74.4% (0.744) |
| Circle     | Agent2 | Agent1    |                  2 |     193 |                    211 |  91.5% (0.915) |
| Circle     | Agent2 | Agent3    |                  2 |      18 |                    211 |   8.5% (0.085) |
| Circle     | Agent3 | Agent2    |                  2 |     187 |                    198 |  94.4% (0.944) |
| Circle     | Agent3 | Agent4    |                  2 |      11 |                    198 |   5.6% (0.056) |
| Circle     | Agent4 | Agent3    |                  2 |     168 |                    186 |  90.3% (0.903) |
| Circle     | Agent4 | Agent5    |                  2 |      18 |                    186 |   9.7% (0.097) |
| Circle     | Agent5 | Agent1    |                  2 |      84 |                    179 |  46.9% (0.469) |
| Circle     | Agent5 | Agent4    |                  2 |      95 |                    179 |  53.1% (0.531) |
| Wheel      | Agent1 | Agent3    |                  1 |     187 |                    187 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     178 |                    178 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     108 |                    180 |  60.0% (0.600) |
| Wheel      | Agent3 | Agent2    |                  4 |      61 |                    180 |  33.9% (0.339) |
| Wheel      | Agent3 | Agent4    |                  4 |       3 |                    180 |   1.7% (0.017) |
| Wheel      | Agent3 | Agent5    |                  4 |       8 |                    180 |   4.4% (0.044) |
| Wheel      | Agent4 | Agent3    |                  1 |     153 |                    153 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     178 |                    178 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     177 |                    177 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     169 |                    169 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      80 |                    180 |  44.4% (0.444) |
| Y topology | Agent3 | Agent2    |                  3 |      67 |                    180 |  37.2% (0.372) |
| Y topology | Agent3 | Agent4    |                  3 |      33 |                    180 |  18.3% (0.183) |
| Y topology | Agent4 | Agent3    |                  2 |     158 |                    175 |  90.3% (0.903) |
| Y topology | Agent4 | Agent5    |                  2 |      17 |                    175 |   9.7% (0.097) |
| Y topology | Agent5 | Agent4    |                  1 |     208 |                    208 | 100.0% (1.000) |
```

### Temperature 0.1

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     165 |                    165 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     140 |                    159 |  88.1% (0.881) |
| Chain      | Agent2 | Agent3    |                  2 |      19 |                    159 |  11.9% (0.119) |
| Chain      | Agent3 | Agent2    |                  2 |     204 |                    210 |  97.1% (0.971) |
| Chain      | Agent3 | Agent4    |                  2 |       6 |                    210 |   2.9% (0.029) |
| Chain      | Agent4 | Agent3    |                  2 |     152 |                    188 |  80.9% (0.809) |
| Chain      | Agent4 | Agent5    |                  2 |      36 |                    188 |  19.1% (0.191) |
| Chain      | Agent5 | Agent4    |                  1 |     209 |                    209 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |      61 |                    158 |  38.6% (0.386) |
| Circle     | Agent1 | Agent5    |                  2 |      97 |                    158 |  61.4% (0.614) |
| Circle     | Agent2 | Agent1    |                  2 |     158 |                    167 |  94.6% (0.946) |
| Circle     | Agent2 | Agent3    |                  2 |       9 |                    167 |   5.4% (0.054) |
| Circle     | Agent3 | Agent2    |                  2 |     154 |                    162 |  95.1% (0.951) |
| Circle     | Agent3 | Agent4    |                  2 |       8 |                    162 |   4.9% (0.049) |
| Circle     | Agent4 | Agent3    |                  2 |     144 |                    169 |  85.2% (0.852) |
| Circle     | Agent4 | Agent5    |                  2 |      25 |                    169 |  14.8% (0.148) |
| Circle     | Agent5 | Agent1    |                  2 |      53 |                    158 |  33.5% (0.335) |
| Circle     | Agent5 | Agent4    |                  2 |     105 |                    158 |  66.5% (0.665) |
| Wheel      | Agent1 | Agent3    |                  1 |     165 |                    165 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     184 |                    184 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     105 |                    186 |  56.5% (0.565) |
| Wheel      | Agent3 | Agent2    |                  4 |      70 |                    186 |  37.6% (0.376) |
| Wheel      | Agent3 | Agent4    |                  4 |       5 |                    186 |   2.7% (0.027) |
| Wheel      | Agent3 | Agent5    |                  4 |       6 |                    186 |   3.2% (0.032) |
| Wheel      | Agent4 | Agent3    |                  1 |     190 |                    190 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     191 |                    191 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     174 |                    174 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     160 |                    160 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      82 |                    170 |  48.2% (0.482) |
| Y topology | Agent3 | Agent2    |                  3 |      61 |                    170 |  35.9% (0.359) |
| Y topology | Agent3 | Agent4    |                  3 |      27 |                    170 |  15.9% (0.159) |
| Y topology | Agent4 | Agent3    |                  2 |     141 |                    160 |  88.1% (0.881) |
| Y topology | Agent4 | Agent5    |                  2 |      19 |                    160 |  11.9% (0.119) |
| Y topology | Agent5 | Agent4    |                  1 |     165 |                    165 | 100.0% (1.000) |
```

### Temperature 0.2

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     167 |                    167 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     148 |                    166 |  89.2% (0.892) |
| Chain      | Agent2 | Agent3    |                  2 |      18 |                    166 |  10.8% (0.108) |
| Chain      | Agent3 | Agent2    |                  2 |     170 |                    179 |  95.0% (0.950) |
| Chain      | Agent3 | Agent4    |                  2 |       9 |                    179 |   5.0% (0.050) |
| Chain      | Agent4 | Agent3    |                  2 |     118 |                    157 |  75.2% (0.752) |
| Chain      | Agent4 | Agent5    |                  2 |      39 |                    157 |  24.8% (0.248) |
| Chain      | Agent5 | Agent4    |                  1 |     187 |                    187 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |      42 |                    139 |  30.2% (0.302) |
| Circle     | Agent1 | Agent5    |                  2 |      97 |                    139 |  69.8% (0.698) |
| Circle     | Agent2 | Agent1    |                  2 |     124 |                    136 |  91.2% (0.912) |
| Circle     | Agent2 | Agent3    |                  2 |      12 |                    136 |   8.8% (0.088) |
| Circle     | Agent3 | Agent2    |                  2 |     146 |                    148 |  98.6% (0.986) |
| Circle     | Agent3 | Agent4    |                  2 |       2 |                    148 |   1.4% (0.014) |
| Circle     | Agent4 | Agent3    |                  2 |     122 |                    150 |  81.3% (0.813) |
| Circle     | Agent4 | Agent5    |                  2 |      28 |                    150 |  18.7% (0.187) |
| Circle     | Agent5 | Agent1    |                  2 |      64 |                    139 |  46.0% (0.460) |
| Circle     | Agent5 | Agent4    |                  2 |      75 |                    139 |  54.0% (0.540) |
| Wheel      | Agent1 | Agent3    |                  1 |     166 |                    166 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     181 |                    181 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     100 |                    179 |  55.9% (0.559) |
| Wheel      | Agent3 | Agent2    |                  4 |      67 |                    179 |  37.4% (0.374) |
| Wheel      | Agent3 | Agent4    |                  4 |       5 |                    179 |   2.8% (0.028) |
| Wheel      | Agent3 | Agent5    |                  4 |       7 |                    179 |   3.9% (0.039) |
| Wheel      | Agent4 | Agent3    |                  1 |     181 |                    181 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     203 |                    203 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     209 |                    209 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     203 |                    203 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |     100 |                    185 |  54.1% (0.541) |
| Y topology | Agent3 | Agent2    |                  3 |      65 |                    185 |  35.1% (0.351) |
| Y topology | Agent3 | Agent4    |                  3 |      20 |                    185 |  10.8% (0.108) |
| Y topology | Agent4 | Agent3    |                  2 |     119 |                    143 |  83.2% (0.832) |
| Y topology | Agent4 | Agent5    |                  2 |      24 |                    143 |  16.8% (0.168) |
| Y topology | Agent5 | Agent4    |                  1 |     229 |                    229 | 100.0% (1.000) |
```

### Temperature 1

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     155 |                    155 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     154 |                    185 |  83.2% (0.832) |
| Chain      | Agent2 | Agent3    |                  2 |      31 |                    185 |  16.8% (0.168) |
| Chain      | Agent3 | Agent2    |                  2 |     151 |                    163 |  92.6% (0.926) |
| Chain      | Agent3 | Agent4    |                  2 |      12 |                    163 |   7.4% (0.074) |
| Chain      | Agent4 | Agent3    |                  2 |     103 |                    158 |  65.2% (0.652) |
| Chain      | Agent4 | Agent5    |                  2 |      55 |                    158 |  34.8% (0.348) |
| Chain      | Agent5 | Agent4    |                  1 |     162 |                    162 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |      33 |                    121 |  27.3% (0.273) |
| Circle     | Agent1 | Agent5    |                  2 |      88 |                    121 |  72.7% (0.727) |
| Circle     | Agent2 | Agent1    |                  2 |     142 |                    159 |  89.3% (0.893) |
| Circle     | Agent2 | Agent3    |                  2 |      17 |                    159 |  10.7% (0.107) |
| Circle     | Agent3 | Agent2    |                  2 |     132 |                    139 |  95.0% (0.950) |
| Circle     | Agent3 | Agent4    |                  2 |       7 |                    139 |   5.0% (0.050) |
| Circle     | Agent4 | Agent3    |                  2 |     122 |                    158 |  77.2% (0.772) |
| Circle     | Agent4 | Agent5    |                  2 |      36 |                    158 |  22.8% (0.228) |
| Circle     | Agent5 | Agent1    |                  2 |      57 |                    145 |  39.3% (0.393) |
| Circle     | Agent5 | Agent4    |                  2 |      88 |                    145 |  60.7% (0.607) |
| Wheel      | Agent1 | Agent3    |                  1 |     187 |                    187 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     177 |                    177 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |      90 |                    169 |  53.3% (0.533) |
| Wheel      | Agent3 | Agent2    |                  4 |      57 |                    169 |  33.7% (0.337) |
| Wheel      | Agent3 | Agent4    |                  4 |      14 |                    169 |   8.3% (0.083) |
| Wheel      | Agent3 | Agent5    |                  4 |       8 |                    169 |   4.7% (0.047) |
| Wheel      | Agent4 | Agent3    |                  1 |     191 |                    191 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     179 |                    179 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     199 |                    199 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     221 |                    221 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      86 |                    195 |  44.1% (0.441) |
| Y topology | Agent3 | Agent2    |                  3 |      74 |                    195 |  37.9% (0.379) |
| Y topology | Agent3 | Agent4    |                  3 |      35 |                    195 |  17.9% (0.179) |
| Y topology | Agent4 | Agent3    |                  2 |     148 |                    176 |  84.1% (0.841) |
| Y topology | Agent4 | Agent5    |                  2 |      28 |                    176 |  15.9% (0.159) |
| Y topology | Agent5 | Agent4    |                  1 |     213 |                    213 | 100.0% (1.000) |
```

## Overall recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     850 |                    850 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     712 |                    807 |  88.2% (0.882) |
| Chain      | Agent2 | Agent3    |                  2 |      95 |                    807 |  11.8% (0.118) |
| Chain      | Agent3 | Agent2    |                  2 |     878 |                    923 |  95.1% (0.951) |
| Chain      | Agent3 | Agent4    |                  2 |      45 |                    923 |   4.9% (0.049) |
| Chain      | Agent4 | Agent3    |                  2 |     589 |                    845 |  69.7% (0.697) |
| Chain      | Agent4 | Agent5    |                  2 |     256 |                    845 |  30.3% (0.303) |
| Chain      | Agent5 | Agent4    |                  1 |     850 |                    850 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |     221 |                    729 |  30.3% (0.303) |
| Circle     | Agent1 | Agent5    |                  2 |     508 |                    729 |  69.7% (0.697) |
| Circle     | Agent2 | Agent1    |                  2 |     739 |                    809 |  91.3% (0.913) |
| Circle     | Agent2 | Agent3    |                  2 |      70 |                    809 |   8.7% (0.087) |
| Circle     | Agent3 | Agent2    |                  2 |     765 |                    798 |  95.9% (0.959) |
| Circle     | Agent3 | Agent4    |                  2 |      33 |                    798 |   4.1% (0.041) |
| Circle     | Agent4 | Agent3    |                  2 |     691 |                    819 |  84.4% (0.844) |
| Circle     | Agent4 | Agent5    |                  2 |     128 |                    819 |  15.6% (0.156) |
| Circle     | Agent5 | Agent1    |                  2 |     319 |                    758 |  42.1% (0.421) |
| Circle     | Agent5 | Agent4    |                  2 |     439 |                    758 |  57.9% (0.579) |
| Wheel      | Agent1 | Agent3    |                  1 |     909 |                    909 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     915 |                    915 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     546 |                    957 |  57.1% (0.571) |
| Wheel      | Agent3 | Agent2    |                  4 |     346 |                    957 |  36.2% (0.362) |
| Wheel      | Agent3 | Agent4    |                  4 |      31 |                    957 |   3.2% (0.032) |
| Wheel      | Agent3 | Agent5    |                  4 |      34 |                    957 |   3.6% (0.036) |
| Wheel      | Agent4 | Agent3    |                  1 |     918 |                    918 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     932 |                    932 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     935 |                    935 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     927 |                    927 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |     440 |                    911 |  48.3% (0.483) |
| Y topology | Agent3 | Agent2    |                  3 |     330 |                    911 |  36.2% (0.362) |
| Y topology | Agent3 | Agent4    |                  3 |     141 |                    911 |  15.5% (0.155) |
| Y topology | Agent4 | Agent3    |                  2 |     719 |                    827 |  86.9% (0.869) |
| Y topology | Agent4 | Agent5    |                  2 |     108 |                    827 |  13.1% (0.131) |
| Y topology | Agent5 | Agent4    |                  1 |    1026 |                   1026 | 100.0% (1.000) |
```

### Excluded fallback routes

```text
| Topology   | Sender | Target source   | Count |
| ---------- | ------ | --------------- | ----- |
| Chain      | Agent2 | client_assigned |     2 |
| Chain      | Agent3 | client_assigned |     3 |
| Chain      | Agent4 | client_assigned |     2 |
| Chain      | Agent5 | client_assigned |     2 |
| Wheel      | Agent1 | client_assigned |     5 |
| Wheel      | Agent3 | client_assigned |    21 |
| Y topology | Agent1 | client_assigned |    22 |
| Y topology | Agent2 | client_assigned |    13 |
| Y topology | Agent3 | client_assigned |    22 |
| Y topology | Agent4 | client_assigned |     8 |
| Y topology | Agent5 | client_assigned |     3 |
```

## Cooling pauses

- Pause between temperature batches: 5 minutes
- Pause between topologies: 15 minutes
