# Y topology auto-trial report

## Summary

- Batch: `temperature-0.5`
- Temperature: 0.5
- Completed trials: 50/50
- Average time: 75.87 seconds
- Average total messages: 17.36
- Success rate: 17/50 (34.0%)

## Recipient-choice probabilities

Only valid recipients explicitly selected by the model (`target_source = agent`) are included. Broadcast messages and fallback-assigned recipients are excluded.
Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.
Uniform expected probability = 1 / number of recipients that sender is allowed to contact.

```text
| Topology | Sender | Recipient | Allowed recipients | Choices | Total choices | Observed probability | Expected probability |  Lift | Smoothed probability |
| -------- | ------ | --------- | ------------------ | ------- | ------------- | -------------------- | -------------------- | ----- | -------------------- |
| y        | Agent1 | Agent3    |                  1 |     144 |           144 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent2 | Agent3    |                  1 |     183 |           183 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
| y        | Agent3 | Agent1    |                  3 |      80 |           185 |        43.2% (0.432) |                0.333 | 1.297 |                0.432 |
| y        | Agent3 | Agent2    |                  3 |      79 |           185 |        42.7% (0.427) |                0.333 | 1.281 |                0.426 |
| y        | Agent3 | Agent4    |                  3 |      26 |           185 |        14.1% (0.141) |                0.333 | 0.422 |                0.142 |
| y        | Agent4 | Agent3    |                  2 |     154 |           189 |        81.5% (0.815) |                0.500 | 1.630 |                0.813 |
| y        | Agent4 | Agent5    |                  2 |      35 |           189 |        18.5% (0.185) |                0.500 | 0.370 |                0.187 |
| y        | Agent5 | Agent4    |                  1 |     165 |           165 |       100.0% (1.000) |                1.000 | 1.000 |                1.000 |
```

### Excluded fallback routes

```text
| Topology | Sender | Target source   | Count |
| -------- | ------ | --------------- | ----- |
| y        | Agent1 | client_assigned |     1 |
| y        | Agent2 | client_assigned |     1 |
```

## Success table

```text
| Round | Temperature | Result  | Submitted figure | Correct figure | Total messages | Time (seconds) |
| ----- | ----------- | ------- | ---------------- | -------------- | -------------- | -------------- |
|     1 |         0.5 | Success | circle           | circle         |             24 |         284.95 |
|     2 |         0.5 | Fail    | triangle         | square         |             26 |         111.03 |
|     3 |         0.5 | Fail    | diamond          | cross          |             22 |          91.65 |
|     4 |         0.5 | Fail    | cross            | asterisk       |              6 |          25.84 |
|     5 |         0.5 | Fail    | square           | cross          |             11 |          45.58 |
|     6 |         0.5 | Success | square           | square         |             22 |          87.97 |
|     7 |         0.5 | Success | asterisk         | asterisk       |             21 |          93.25 |
|     8 |         0.5 | Success | asterisk         | asterisk       |             39 |         149.26 |
|     9 |         0.5 | Fail    | asterisk         | triangle       |             15 |          61.35 |
|    10 |         0.5 | Success | triangle         | triangle       |             16 |          63.43 |
|    11 |         0.5 | Fail    | square           | triangle       |             11 |          48.91 |
|    12 |         0.5 | Success | diamond          | diamond        |             23 |          97.03 |
|    13 |         0.5 | Fail    | circle           | triangle       |             15 |          64.07 |
|    14 |         0.5 | Fail    | diamond          | triangle       |             16 |          68.32 |
|    15 |         0.5 | Fail    | cross            | triangle       |             17 |          69.68 |
|    16 |         0.5 | Success | asterisk         | asterisk       |             10 |          43.03 |
|    17 |         0.5 | Fail    | square           | triangle       |             17 |          74.57 |
|    18 |         0.5 | Success | cross            | cross          |             17 |          70.24 |
|    19 |         0.5 | Fail    | diamond          | square         |             18 |          76.04 |
|    20 |         0.5 | Fail    | square           | diamond        |             10 |          42.03 |
|    21 |         0.5 | Success | square           | square         |             14 |          58.60 |
|    22 |         0.5 | Success | square           | square         |             20 |          81.78 |
|    23 |         0.5 | Success | circle           | circle         |             20 |          84.58 |
|    24 |         0.5 | Fail    | cross            | asterisk       |              9 |          41.69 |
|    25 |         0.5 | Fail    | cross            | asterisk       |             19 |          75.98 |
|    26 |         0.5 | Fail    | diamond          | cross          |              7 |          30.46 |
|    27 |         0.5 | Fail    | circle           | triangle       |             11 |          43.68 |
|    28 |         0.5 | Success | cross            | cross          |             19 |          81.07 |
|    29 |         0.5 | Fail    | diamond          | cross          |             36 |         138.07 |
|    30 |         0.5 | Fail    | square           | diamond        |             29 |         126.45 |
|    31 |         0.5 | Fail    | cross            | diamond        |             19 |          78.03 |
|    32 |         0.5 | Fail    | diamond          | asterisk       |             13 |          54.08 |
|    33 |         0.5 | Fail    | triangle         | square         |             15 |          63.33 |
|    34 |         0.5 | Fail    | triangle         | diamond        |             14 |          58.61 |
|    35 |         0.5 | Fail    | circle           | cross          |             19 |          78.69 |
|    36 |         0.5 | Fail    | triangle         | diamond        |             12 |          51.48 |
|    37 |         0.5 | Fail    | square           | triangle       |             14 |          57.57 |
|    38 |         0.5 | Fail    | asterisk         | diamond        |             12 |          50.49 |
|    39 |         0.5 | Fail    | diamond          | square         |             27 |         109.53 |
|    40 |         0.5 | Fail    | circle           | cross          |             12 |          51.50 |
|    41 |         0.5 | Success | square           | square         |              7 |          32.95 |
|    42 |         0.5 | Success | triangle         | triangle       |             36 |         139.89 |
|    43 |         0.5 | Success | asterisk         | asterisk       |             18 |          69.94 |
|    44 |         0.5 | Fail    | cross            | diamond        |             10 |          46.58 |
|    45 |         0.5 | Fail    | circle           | square         |             14 |          62.60 |
|    46 |         0.5 | Fail    | square           | diamond        |             15 |          57.15 |
|    47 |         0.5 | Success | asterisk         | asterisk       |             18 |          72.38 |
|    48 |         0.5 | Success | circle           | circle         |             13 |          55.00 |
|    49 |         0.5 | Fail    | cross            | circle         |             23 |          97.71 |
|    50 |         0.5 | Fail    | diamond          | triangle       |             17 |          75.41 |
```
