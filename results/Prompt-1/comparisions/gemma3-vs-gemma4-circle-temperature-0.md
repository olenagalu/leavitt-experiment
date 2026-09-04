# Gemma 3 and Gemma 4 results: circle topology at temperature 0

## Source files

| Model | Study report | Detailed circle/temperature-0 report |
| --- | --- | --- |
| Gemma 3 | [Clean 50-trial data](../gemma3-50trials-clean/gemma3-50trials-data.txt) | [Circle, temperature 0](../gemma3-50trials-raw/circle-study/circle/temperature-0/report.md) |
| Gemma 4 (`gemma4:e2b-it-qat`) | [Leavitt study](../gemma4-circle-1st/report.md) | [Circle, temperature 0](../gemma4-circle-1st/circle/temperature-0/report.md) |

## Experimental settings

| Setting | Gemma 3 | Gemma 4 |
| --- | --- | --- |
| Topology | Circle | Circle |
| Temperature | 0 | 0 |
| Number of trials | 50 | 50 |

## Outcome results

| Metric | Gemma 3 | Gemma 4 |
| --- | --- | --- |
| Successful trials | 10/50 | 19/50 |
| Success rate | 20.0% | 38.0% |
| Average total messages | 12.36 | 17.44 |

## Time comparison

Total trial time is measured from each trial's recorded start timestamp through its completion timestamp. Experiment time begins with the first valid experiment message. The total and average rows are sums and averages across the same 50 circle-topology trials at temperature 0.

| Timing metric | Gemma 3 | Gemma 4 |
| --- | ---: | ---: |
| Total time for 50 trials | 3,147.45 s (52 min 27.45 s) | 40,555.71 s (11 h 15 min 55.71 s) |
| Average total time per trial | 62.95 s | 811.11 s |
| Longest total trial | 265.22 s (trial 1) | 1,736.27 s (trial 26) |
| Total experiment time for 50 trials | 2,867.64 s (47 min 47.64 s) | 39,171.51 s (10 h 52 min 51.51 s) |
| Average experiment time per trial | 57.35 s | 783.43 s |
| Longest experiment time | 214.90 s (trial 1) | 1,663.18 s (trial 26) |
| Average time per recorded response | Not recorded | 43.484 s (922 responses) |
| Longest recorded response | Not recorded | 120.412 s (Agent5, trial 7) |

Gemma 3 did not store per-response durations. Its message `elapsed` values are not a reliable substitute because they omit the first response and include inter-turn scheduling time, so no Gemma 3 response-time estimate is reported.

## Recipient-choice results

| Sender | Recipient | Gemma 3 choices | Gemma 3 probability | Gemma 4 choices | Gemma 4 probability |
| --- | --- | --- | --- | --- | --- |
| Agent1 | Agent2 | 10/138 | 7.2% | 95/188 | 50.5% |
| Agent1 | Agent5 | 128/138 | 92.8% | 93/188 | 49.5% |
| Agent2 | Agent1 | 102/131 | 77.9% | 87/172 | 50.6% |
| Agent2 | Agent3 | 29/131 | 22.1% | 85/172 | 49.4% |
| Agent3 | Agent2 | 107/110 | 97.3% | 78/166 | 47.0% |
| Agent3 | Agent4 | 3/110 | 2.7% | 88/166 | 53.0% |
| Agent4 | Agent3 | 84/117 | 71.8% | 104/180 | 57.8% |
| Agent4 | Agent5 | 33/117 | 28.2% | 76/180 | 42.2% |
| Agent5 | Agent1 | 90/122 | 73.8% | 76/164 | 46.3% |
| Agent5 | Agent4 | 32/122 | 26.2% | 88/164 | 53.7% |

## Fallback routes

| Model | Sender | Fallback source | Count |
| --- | --- | --- | --- |
| Gemma 3 | - | No fallback routes recorded | 0 |
| Gemma 4 | Agent2 | `server_assigned` | 1 |
| Gemma 4 | Agent5 | `server_assigned` | 1 |
