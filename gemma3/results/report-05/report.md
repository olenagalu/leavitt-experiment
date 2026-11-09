# Leavitt full study report

## Progress

- Study: `run-8400fecec30c-four-topologies-study`
- Status: complete
- Completed batches: 20/20
- Completed trials: 1000/1000
- Topologies: Circle, Chain, Y topology, Wheel
- Temperatures: 0, 0.05, 0.1, 0.2, 1

## Batch summary

| Topology   | Temperature | Status   | Trials |  Success rate | Average total messages | Average time (seconds) | Detailed report                                                |
| ---------- | ----------: | -------- | -----: | ------------: | ---------------------: | ---------------------: | -------------------------------------------------------------- |
| Circle     |           0 | complete |  50/50 | 24.0% (12/50) |                  15.70 |                 156.92 | [circle / temperature 0](circle/temperature-0/report.md)       |
| Circle     |        0.05 | complete |  50/50 | 24.0% (12/50) |                  15.36 |                 170.52 | [circle / temperature 0.05](circle/temperature-0.05/report.md) |
| Circle     |         0.1 | complete |  50/50 | 34.0% (17/50) |                  15.18 |                 163.34 | [circle / temperature 0.1](circle/temperature-0.1/report.md)   |
| Circle     |         0.2 | complete |  50/50 | 38.0% (19/50) |                  16.00 |                 181.16 | [circle / temperature 0.2](circle/temperature-0.2/report.md)   |
| Circle     |           1 | complete |  50/50 |  16.0% (8/50) |                  14.86 |                 219.01 | [circle / temperature 1](circle/temperature-1/report.md)       |
| Chain      |           0 | complete |  50/50 |  14.0% (7/50) |                  16.18 |                 159.62 | [chain / temperature 0](chain/temperature-0/report.md)         |
| Chain      |        0.05 | complete |  50/50 | 28.0% (14/50) |                  16.24 |                 191.09 | [chain / temperature 0.05](chain/temperature-0.05/report.md)   |
| Chain      |         0.1 | complete |  50/50 | 24.0% (12/50) |                  17.74 |                 206.82 | [chain / temperature 0.1](chain/temperature-0.1/report.md)     |
| Chain      |         0.2 | complete |  50/50 | 38.0% (19/50) |                  16.50 |                 239.68 | [chain / temperature 0.2](chain/temperature-0.2/report.md)     |
| Chain      |           1 | complete |  50/50 | 40.0% (20/50) |                  15.82 |                 197.64 | [chain / temperature 1](chain/temperature-1/report.md)         |
| Y topology |           0 | complete |  50/50 | 24.0% (12/50) |                  18.46 |                 215.52 | [y / temperature 0](y/temperature-0/report.md)                 |
| Y topology |        0.05 | complete |  50/50 | 20.0% (10/50) |                  18.50 |                 178.59 | [y / temperature 0.05](y/temperature-0.05/report.md)           |
| Y topology |         0.1 | complete |  50/50 | 32.0% (16/50) |                  18.30 |                 221.16 | [y / temperature 0.1](y/temperature-0.1/report.md)             |
| Y topology |         0.2 | complete |  50/50 | 30.0% (15/50) |                  17.42 |                 228.75 | [y / temperature 0.2](y/temperature-0.2/report.md)             |
| Y topology |           1 | complete |  50/50 | 26.0% (13/50) |                  17.58 |                 181.72 | [y / temperature 1](y/temperature-1/report.md)                 |
| Wheel      |           0 | complete |  50/50 | 24.0% (12/50) |                  20.68 |                 238.37 | [wheel / temperature 0](wheel/temperature-0/report.md)         |
| Wheel      |        0.05 | complete |  50/50 | 22.0% (11/50) |                  21.18 |                 282.80 | [wheel / temperature 0.05](wheel/temperature-0.05/report.md)   |
| Wheel      |         0.1 | complete |  50/50 | 36.0% (18/50) |                  20.00 |                 279.15 | [wheel / temperature 0.1](wheel/temperature-0.1/report.md)     |
| Wheel      |         0.2 | complete |  50/50 | 20.0% (10/50) |                  18.92 |                 264.94 | [wheel / temperature 0.2](wheel/temperature-0.2/report.md)     |
| Wheel      |           1 | complete |  50/50 | 26.0% (13/50) |                  17.82 |                 248.53 | [wheel / temperature 1](wheel/temperature-1/report.md)         |

## Overall results

- Completed trials: 1000/1000
- Average time: 211.27 seconds
- Average total messages: 17.42
- Success rate: 270/1000 (27.0%)
- Reconnect pauses: 25 across 24 trial(s); 34.07 paused seconds excluded from experiment time

## Topology summary

| Topology   | Trials | Successes | Success rate | Average total messages | Average time (seconds) |
| ---------- | -----: | --------: | -----------: | ---------------------: | ---------------------: |
| Circle     |    250 |        68 |        27.2% |                  15.42 |                 178.19 |
| Chain      |    250 |        72 |        28.8% |                  16.50 |                 198.97 |
| Y topology |    250 |        66 |        26.4% |                  18.05 |                 205.15 |
| Wheel      |    250 |        64 |        25.6% |                  19.72 |                 262.76 |

## Recipient-choice probabilities by temperature

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender at that temperature.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

### Temperature 0

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     152 |                    152 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     160 |                    177 |  90.4% (0.904) |
| Chain      | Agent2 | Agent3    |                  2 |      17 |                    177 |   9.6% (0.096) |
| Chain      | Agent3 | Agent2    |                  2 |     162 |                    169 |  95.9% (0.959) |
| Chain      | Agent3 | Agent4    |                  2 |       7 |                    169 |   4.1% (0.041) |
| Chain      | Agent4 | Agent3    |                  2 |      98 |                    151 |  64.9% (0.649) |
| Chain      | Agent4 | Agent5    |                  2 |      53 |                    151 |  35.1% (0.351) |
| Chain      | Agent5 | Agent4    |                  1 |     160 |                    160 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |      48 |                    157 |  30.6% (0.306) |
| Circle     | Agent1 | Agent5    |                  2 |     109 |                    157 |  69.4% (0.694) |
| Circle     | Agent2 | Agent1    |                  2 |     149 |                    159 |  93.7% (0.937) |
| Circle     | Agent2 | Agent3    |                  2 |      10 |                    159 |   6.3% (0.063) |
| Circle     | Agent3 | Agent2    |                  2 |     155 |                    161 |  96.3% (0.963) |
| Circle     | Agent3 | Agent4    |                  2 |       6 |                    161 |   3.7% (0.037) |
| Circle     | Agent4 | Agent3    |                  2 |     126 |                    151 |  83.4% (0.834) |
| Circle     | Agent4 | Agent5    |                  2 |      25 |                    151 |  16.6% (0.166) |
| Circle     | Agent5 | Agent1    |                  2 |      66 |                    157 |  42.0% (0.420) |
| Circle     | Agent5 | Agent4    |                  2 |      91 |                    157 |  58.0% (0.580) |
| Wheel      | Agent1 | Agent3    |                  1 |     209 |                    209 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     200 |                    200 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     109 |                    180 |  60.6% (0.606) |
| Wheel      | Agent3 | Agent2    |                  4 |      65 |                    180 |  36.1% (0.361) |
| Wheel      | Agent3 | Agent4    |                  4 |       4 |                    180 |   2.2% (0.022) |
| Wheel      | Agent3 | Agent5    |                  4 |       2 |                    180 |   1.1% (0.011) |
| Wheel      | Agent4 | Agent3    |                  1 |     217 |                    217 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     227 |                    227 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     170 |                    170 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     181 |                    181 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      91 |                    185 |  49.2% (0.492) |
| Y topology | Agent3 | Agent2    |                  3 |      74 |                    185 |  40.0% (0.400) |
| Y topology | Agent3 | Agent4    |                  3 |      20 |                    185 |  10.8% (0.108) |
| Y topology | Agent4 | Agent3    |                  2 |     151 |                    167 |  90.4% (0.904) |
| Y topology | Agent4 | Agent5    |                  2 |      16 |                    167 |   9.6% (0.096) |
| Y topology | Agent5 | Agent4    |                  1 |     216 |                    216 | 100.0% (1.000) |
```

### Temperature 0.05

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     151 |                    151 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     148 |                    162 |  91.4% (0.914) |
| Chain      | Agent2 | Agent3    |                  2 |      14 |                    162 |   8.6% (0.086) |
| Chain      | Agent3 | Agent2    |                  2 |     177 |                    182 |  97.3% (0.973) |
| Chain      | Agent3 | Agent4    |                  2 |       5 |                    182 |   2.7% (0.027) |
| Chain      | Agent4 | Agent3    |                  2 |      98 |                    150 |  65.3% (0.653) |
| Chain      | Agent4 | Agent5    |                  2 |      52 |                    150 |  34.7% (0.347) |
| Chain      | Agent5 | Agent4    |                  1 |     167 |                    167 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |      35 |                    141 |  24.8% (0.248) |
| Circle     | Agent1 | Agent5    |                  2 |     106 |                    141 |  75.2% (0.752) |
| Circle     | Agent2 | Agent1    |                  2 |     147 |                    162 |  90.7% (0.907) |
| Circle     | Agent2 | Agent3    |                  2 |      15 |                    162 |   9.3% (0.093) |
| Circle     | Agent3 | Agent2    |                  2 |     149 |                    153 |  97.4% (0.974) |
| Circle     | Agent3 | Agent4    |                  2 |       4 |                    153 |   2.6% (0.026) |
| Circle     | Agent4 | Agent3    |                  2 |     126 |                    146 |  86.3% (0.863) |
| Circle     | Agent4 | Agent5    |                  2 |      20 |                    146 |  13.7% (0.137) |
| Circle     | Agent5 | Agent1    |                  2 |      82 |                    166 |  49.4% (0.494) |
| Circle     | Agent5 | Agent4    |                  2 |      84 |                    166 |  50.6% (0.506) |
| Wheel      | Agent1 | Agent3    |                  1 |     219 |                    219 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     201 |                    201 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     131 |                    210 |  62.4% (0.624) |
| Wheel      | Agent3 | Agent2    |                  4 |      72 |                    210 |  34.3% (0.343) |
| Wheel      | Agent3 | Agent4    |                  4 |       1 |                    210 |   0.5% (0.005) |
| Wheel      | Agent3 | Agent5    |                  4 |       6 |                    210 |   2.9% (0.029) |
| Wheel      | Agent4 | Agent3    |                  1 |     191 |                    191 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     235 |                    235 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     145 |                    145 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     197 |                    197 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      80 |                    200 |  40.0% (0.400) |
| Y topology | Agent3 | Agent2    |                  3 |      79 |                    200 |  39.5% (0.395) |
| Y topology | Agent3 | Agent4    |                  3 |      41 |                    200 |  20.5% (0.205) |
| Y topology | Agent4 | Agent3    |                  2 |     167 |                    184 |  90.8% (0.908) |
| Y topology | Agent4 | Agent5    |                  2 |      17 |                    184 |   9.2% (0.092) |
| Y topology | Agent5 | Agent4    |                  1 |     194 |                    194 | 100.0% (1.000) |
```

### Temperature 0.1

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     189 |                    189 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     151 |                    171 |  88.3% (0.883) |
| Chain      | Agent2 | Agent3    |                  2 |      20 |                    171 |  11.7% (0.117) |
| Chain      | Agent3 | Agent2    |                  2 |     189 |                    193 |  97.9% (0.979) |
| Chain      | Agent3 | Agent4    |                  2 |       4 |                    193 |   2.1% (0.021) |
| Chain      | Agent4 | Agent3    |                  2 |     107 |                    174 |  61.5% (0.615) |
| Chain      | Agent4 | Agent5    |                  2 |      67 |                    174 |  38.5% (0.385) |
| Chain      | Agent5 | Agent4    |                  1 |     160 |                    160 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |      40 |                    145 |  27.6% (0.276) |
| Circle     | Agent1 | Agent5    |                  2 |     105 |                    145 |  72.4% (0.724) |
| Circle     | Agent2 | Agent1    |                  2 |     132 |                    149 |  88.6% (0.886) |
| Circle     | Agent2 | Agent3    |                  2 |      17 |                    149 |  11.4% (0.114) |
| Circle     | Agent3 | Agent2    |                  2 |     142 |                    144 |  98.6% (0.986) |
| Circle     | Agent3 | Agent4    |                  2 |       2 |                    144 |   1.4% (0.014) |
| Circle     | Agent4 | Agent3    |                  2 |     137 |                    167 |  82.0% (0.820) |
| Circle     | Agent4 | Agent5    |                  2 |      30 |                    167 |  18.0% (0.180) |
| Circle     | Agent5 | Agent1    |                  2 |      60 |                    154 |  39.0% (0.390) |
| Circle     | Agent5 | Agent4    |                  2 |      94 |                    154 |  61.0% (0.610) |
| Wheel      | Agent1 | Agent3    |                  1 |     216 |                    216 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     215 |                    215 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     106 |                    186 |  57.0% (0.570) |
| Wheel      | Agent3 | Agent2    |                  4 |      66 |                    186 |  35.5% (0.355) |
| Wheel      | Agent3 | Agent4    |                  4 |       3 |                    186 |   1.6% (0.016) |
| Wheel      | Agent3 | Agent5    |                  4 |      11 |                    186 |   5.9% (0.059) |
| Wheel      | Agent4 | Agent3    |                  1 |     159 |                    159 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     219 |                    219 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     176 |                    176 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     186 |                    186 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      89 |                    198 |  44.9% (0.449) |
| Y topology | Agent3 | Agent2    |                  3 |      76 |                    198 |  38.4% (0.384) |
| Y topology | Agent3 | Agent4    |                  3 |      33 |                    198 |  16.7% (0.167) |
| Y topology | Agent4 | Agent3    |                  2 |     125 |                    144 |  86.8% (0.868) |
| Y topology | Agent4 | Agent5    |                  2 |      19 |                    144 |  13.2% (0.132) |
| Y topology | Agent5 | Agent4    |                  1 |     204 |                    204 | 100.0% (1.000) |
```

### Temperature 0.2

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     159 |                    159 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     154 |                    175 |  88.0% (0.880) |
| Chain      | Agent2 | Agent3    |                  2 |      21 |                    175 |  12.0% (0.120) |
| Chain      | Agent3 | Agent2    |                  2 |     169 |                    182 |  92.9% (0.929) |
| Chain      | Agent3 | Agent4    |                  2 |      13 |                    182 |   7.1% (0.071) |
| Chain      | Agent4 | Agent3    |                  2 |      87 |                    144 |  60.4% (0.604) |
| Chain      | Agent4 | Agent5    |                  2 |      57 |                    144 |  39.6% (0.396) |
| Chain      | Agent5 | Agent4    |                  1 |     164 |                    164 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |      51 |                    163 |  31.3% (0.313) |
| Circle     | Agent1 | Agent5    |                  2 |     112 |                    163 |  68.7% (0.687) |
| Circle     | Agent2 | Agent1    |                  2 |     132 |                    147 |  89.8% (0.898) |
| Circle     | Agent2 | Agent3    |                  2 |      15 |                    147 |  10.2% (0.102) |
| Circle     | Agent3 | Agent2    |                  2 |     176 |                    180 |  97.8% (0.978) |
| Circle     | Agent3 | Agent4    |                  2 |       4 |                    180 |   2.2% (0.022) |
| Circle     | Agent4 | Agent3    |                  2 |     127 |                    159 |  79.9% (0.799) |
| Circle     | Agent4 | Agent5    |                  2 |      32 |                    159 |  20.1% (0.201) |
| Circle     | Agent5 | Agent1    |                  2 |      52 |                    151 |  34.4% (0.344) |
| Circle     | Agent5 | Agent4    |                  2 |      99 |                    151 |  65.6% (0.656) |
| Wheel      | Agent1 | Agent3    |                  1 |     203 |                    203 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     187 |                    187 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     116 |                    183 |  63.4% (0.634) |
| Wheel      | Agent3 | Agent2    |                  4 |      59 |                    183 |  32.2% (0.322) |
| Wheel      | Agent3 | Agent4    |                  4 |       2 |                    183 |   1.1% (0.011) |
| Wheel      | Agent3 | Agent5    |                  4 |       6 |                    183 |   3.3% (0.033) |
| Wheel      | Agent4 | Agent3    |                  1 |     162 |                    162 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     210 |                    210 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     168 |                    168 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     205 |                    205 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      76 |                    171 |  44.4% (0.444) |
| Y topology | Agent3 | Agent2    |                  3 |      68 |                    171 |  39.8% (0.398) |
| Y topology | Agent3 | Agent4    |                  3 |      27 |                    171 |  15.8% (0.158) |
| Y topology | Agent4 | Agent3    |                  2 |     134 |                    158 |  84.8% (0.848) |
| Y topology | Agent4 | Agent5    |                  2 |      24 |                    158 |  15.2% (0.152) |
| Y topology | Agent5 | Agent4    |                  1 |     150 |                    150 | 100.0% (1.000) |
```

### Temperature 1

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     133 |                    133 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     153 |                    168 |  91.1% (0.911) |
| Chain      | Agent2 | Agent3    |                  2 |      15 |                    168 |   8.9% (0.089) |
| Chain      | Agent3 | Agent2    |                  2 |     154 |                    160 |  96.2% (0.963) |
| Chain      | Agent3 | Agent4    |                  2 |       6 |                    160 |   3.8% (0.037) |
| Chain      | Agent4 | Agent3    |                  2 |     107 |                    171 |  62.6% (0.626) |
| Chain      | Agent4 | Agent5    |                  2 |      64 |                    171 |  37.4% (0.374) |
| Chain      | Agent5 | Agent4    |                  1 |     158 |                    158 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |      46 |                    159 |  28.9% (0.289) |
| Circle     | Agent1 | Agent5    |                  2 |     113 |                    159 |  71.1% (0.711) |
| Circle     | Agent2 | Agent1    |                  2 |     131 |                    152 |  86.2% (0.862) |
| Circle     | Agent2 | Agent3    |                  2 |      21 |                    152 |  13.8% (0.138) |
| Circle     | Agent3 | Agent2    |                  2 |     157 |                    162 |  96.9% (0.969) |
| Circle     | Agent3 | Agent4    |                  2 |       5 |                    162 |   3.1% (0.031) |
| Circle     | Agent4 | Agent3    |                  2 |     116 |                    157 |  73.9% (0.739) |
| Circle     | Agent4 | Agent5    |                  2 |      41 |                    157 |  26.1% (0.261) |
| Circle     | Agent5 | Agent1    |                  2 |      45 |                    112 |  40.2% (0.402) |
| Circle     | Agent5 | Agent4    |                  2 |      67 |                    112 |  59.8% (0.598) |
| Wheel      | Agent1 | Agent3    |                  1 |     157 |                    157 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     187 |                    187 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |      98 |                    175 |  56.0% (0.560) |
| Wheel      | Agent3 | Agent2    |                  4 |      59 |                    175 |  33.7% (0.337) |
| Wheel      | Agent3 | Agent4    |                  4 |       9 |                    175 |   5.1% (0.051) |
| Wheel      | Agent3 | Agent5    |                  4 |       9 |                    175 |   5.1% (0.051) |
| Wheel      | Agent4 | Agent3    |                  1 |     185 |                    185 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |     185 |                    185 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     170 |                    170 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     189 |                    189 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |      68 |                    151 |  45.0% (0.450) |
| Y topology | Agent3 | Agent2    |                  3 |      61 |                    151 |  40.4% (0.404) |
| Y topology | Agent3 | Agent4    |                  3 |      22 |                    151 |  14.6% (0.146) |
| Y topology | Agent4 | Agent3    |                  2 |     144 |                    173 |  83.2% (0.832) |
| Y topology | Agent4 | Agent5    |                  2 |      29 |                    173 |  16.8% (0.168) |
| Y topology | Agent5 | Agent4    |                  1 |     193 |                    193 | 100.0% (1.000) |
```

## Overall recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Fallback-assigned routes are excluded from these probabilities.
Observed probability = choices of this recipient / all explicit valid recipient choices by the sender.
Broadcast is not applicable because every broadcast message is delivered to all other agents.

```text
| Topology   | Sender | Recipient | Allowed recipients | Choices | Total explicit choices |    Probability |
| ---------- | ------ | --------- | ------------------ | ------- | ---------------------- | -------------- |
| Chain      | Agent1 | Agent2    |                  1 |     784 |                    784 | 100.0% (1.000) |
| Chain      | Agent2 | Agent1    |                  2 |     766 |                    853 |  89.8% (0.898) |
| Chain      | Agent2 | Agent3    |                  2 |      87 |                    853 |  10.2% (0.102) |
| Chain      | Agent3 | Agent2    |                  2 |     851 |                    886 |  96.0% (0.960) |
| Chain      | Agent3 | Agent4    |                  2 |      35 |                    886 |   4.0% (0.040) |
| Chain      | Agent4 | Agent3    |                  2 |     497 |                    790 |  62.9% (0.629) |
| Chain      | Agent4 | Agent5    |                  2 |     293 |                    790 |  37.1% (0.371) |
| Chain      | Agent5 | Agent4    |                  1 |     809 |                    809 | 100.0% (1.000) |
| Circle     | Agent1 | Agent2    |                  2 |     220 |                    765 |  28.8% (0.288) |
| Circle     | Agent1 | Agent5    |                  2 |     545 |                    765 |  71.2% (0.712) |
| Circle     | Agent2 | Agent1    |                  2 |     691 |                    769 |  89.9% (0.899) |
| Circle     | Agent2 | Agent3    |                  2 |      78 |                    769 |  10.1% (0.101) |
| Circle     | Agent3 | Agent2    |                  2 |     779 |                    800 |  97.4% (0.974) |
| Circle     | Agent3 | Agent4    |                  2 |      21 |                    800 |   2.6% (0.026) |
| Circle     | Agent4 | Agent3    |                  2 |     632 |                    780 |  81.0% (0.810) |
| Circle     | Agent4 | Agent5    |                  2 |     148 |                    780 |  19.0% (0.190) |
| Circle     | Agent5 | Agent1    |                  2 |     305 |                    740 |  41.2% (0.412) |
| Circle     | Agent5 | Agent4    |                  2 |     435 |                    740 |  58.8% (0.588) |
| Wheel      | Agent1 | Agent3    |                  1 |    1004 |                   1004 | 100.0% (1.000) |
| Wheel      | Agent2 | Agent3    |                  1 |     990 |                    990 | 100.0% (1.000) |
| Wheel      | Agent3 | Agent1    |                  4 |     560 |                    934 |  60.0% (0.600) |
| Wheel      | Agent3 | Agent2    |                  4 |     321 |                    934 |  34.4% (0.344) |
| Wheel      | Agent3 | Agent4    |                  4 |      19 |                    934 |   2.0% (0.020) |
| Wheel      | Agent3 | Agent5    |                  4 |      34 |                    934 |   3.6% (0.036) |
| Wheel      | Agent4 | Agent3    |                  1 |     914 |                    914 | 100.0% (1.000) |
| Wheel      | Agent5 | Agent3    |                  1 |    1076 |                   1076 | 100.0% (1.000) |
| Y topology | Agent1 | Agent3    |                  1 |     829 |                    829 | 100.0% (1.000) |
| Y topology | Agent2 | Agent3    |                  1 |     958 |                    958 | 100.0% (1.000) |
| Y topology | Agent3 | Agent1    |                  3 |     404 |                    905 |  44.6% (0.446) |
| Y topology | Agent3 | Agent2    |                  3 |     358 |                    905 |  39.6% (0.396) |
| Y topology | Agent3 | Agent4    |                  3 |     143 |                    905 |  15.8% (0.158) |
| Y topology | Agent4 | Agent3    |                  2 |     721 |                    826 |  87.3% (0.873) |
| Y topology | Agent4 | Agent5    |                  2 |     105 |                    826 |  12.7% (0.127) |
| Y topology | Agent5 | Agent4    |                  1 |     957 |                    957 | 100.0% (1.000) |
```

### Excluded fallback routes

```text
| Topology   | Sender | Target source   | Count |
| ---------- | ------ | --------------- | ----- |
| Chain      | Agent1 | client_assigned |     1 |
| Chain      | Agent2 | client_assigned |     1 |
| Circle     | Agent3 | client_assigned |     1 |
| Wheel      | Agent3 | client_assigned |    12 |
| Y topology | Agent1 | client_assigned |    10 |
| Y topology | Agent2 | client_assigned |     9 |
| Y topology | Agent3 | client_assigned |    15 |
| Y topology | Agent4 | client_assigned |     3 |
| Y topology | Agent5 | client_assigned |     1 |
```

## Cooling pauses

- Pause between temperature batches: 5 minutes
- Pause between topologies: 15 minutes
