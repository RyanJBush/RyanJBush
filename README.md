# Ryan Bush

Selected projects in LLM reliability, local analytics, retrieval evaluation, agent workflow tooling and tool-call authorization, text-origin evaluation and content provenance, demand forecasting, and sensor anomaly detection. Each project links to a demo and the evidence behind its results.

### Self-Healing LLM Gateway

Built a local text-generation gateway with bounded retries, approved fallback providers, and per-provider circuit breakers. A two-second deadline includes calls and retry waits; sanitized traces explain routing and recovery decisions.

On the same seven-request deterministic failure schedule, the gateway completed 7/7 requests with 11 provider calls, compared with 2/7 and seven calls for a direct-primary baseline. These are stub results with simulated timings. All 382 tests and 31 acceptance assertions passed on Windows and Ubuntu with Python 3.11–3.13. Real LLM providers, macOS, and load beyond five concurrent requests remain unverified.

[Repository](https://github.com/RyanJBush/Self-Healing-LLM-Gateway) · [Demo preview](https://github.com/RyanJBush/Self-Healing-LLM-Gateway/blob/4efd14e5bce54a1d66018bbb4641cc07e9ff9114/docs/media/acceptance-preview.png) · [Verified results](https://github.com/RyanJBush/Self-Healing-LLM-Gateway/blob/4efd14e5bce54a1d66018bbb4641cc07e9ff9114/evidence/verification.md) · [Passing CI run](https://github.com/RyanJBush/Self-Healing-LLM-Gateway/actions/runs/42944790109) · [Release v0.2.2](https://github.com/RyanJBush/Self-Healing-LLM-Gateway/releases/tag/v0.2.2)

### Enterprise Text-to-SQL Analytics Agent

Built a local analytics assistant using Ollama and Qwen3 4B to propose SQL over a synthetic sales database. A restricted SQLite executor enforces approved reads, row limits, and a query work budget. The demo shows a correct joined revenue answer, a clarification question, and a blocked schema read.

Seven local acceptance cases passed. The test suite recorded 182 passes and three optional Anthropic SDK skips. Earlier model mistakes are retained with the results.

[Repository](https://github.com/RyanJBush/Enterprise-Text-to-SQL-Analytics-Agent) · [51-second demo](https://github.com/RyanJBush/Enterprise-Text-to-SQL-Analytics-Agent/blob/d9278eb98efcf2e73f3a07b0579efa34855ef1b6/docs/media/text2sql-demo.mp4) · [Verified results](https://github.com/RyanJBush/Enterprise-Text-to-SQL-Analytics-Agent/blob/d9278eb98efcf2e73f3a07b0579efa34855ef1b6/evidence/results.md) · [Exact test output](https://github.com/RyanJBush/Enterprise-Text-to-SQL-Analytics-Agent/blob/d9278eb98efcf2e73f3a07b0579efa34855ef1b6/evidence/test-output.txt)

### Retrieval Evaluation Harness

Built a reproducible comparison of BM25 and a pinned embedding model, with per-query relevance metrics, CPU latency exports, and a side-by-side viewer. On the bundled synthetic fixture, Recall@5 was 0.714 for BM25 and 1.000 for embeddings across seven scored queries.

[Repository](https://github.com/RyanJBush/Retrieval-Evaluation-Harness) · [Saved results](https://github.com/RyanJBush/Retrieval-Evaluation-Harness/blob/5daa6003131c1ce3e11a1673c976c24dac2c80c7/examples/demo/summary.csv) · [Passing CI run](https://github.com/RyanJBush/Retrieval-Evaluation-Harness/actions/runs/42416440729) · [Viewer screenshot](https://github.com/RyanJBush/Retrieval-Evaluation-Harness/blob/5daa6003131c1ce3e11a1673c976c24dac2c80c7/evidence/browser/after_desktop_q02_k3.png)

### SwarmOS

Built a deterministic Planner–Implementer–Reviewer workflow that applies a fixed patch in a disposable Git repository, gates approval on an acceptance test, and stores verifiable execution traces in SQLite. The paired demo completed 3/3 runs per arm, with three memory hits when enabled and zero when disabled.

[Recorded results](https://github.com/RyanJBush/Autonomous-Coding-Agent-with-MCP-and-Multi-Agent-Collaboration/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/demo-evidence.json) · [Passing CI run](https://github.com/RyanJBush/Autonomous-Coding-Agent-with-MCP-and-Multi-Agent-Collaboration/actions/runs/42434894375) · [Captioned demo](https://github.com/RyanJBush/Autonomous-Coding-Agent-with-MCP-and-Multi-Agent-Collaboration/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/swarmos-demo.webm) · [Timeline screenshot](https://github.com/RyanJBush/Autonomous-Coding-Agent-with-MCP-and-Multi-Agent-Collaboration/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/timeline.png)

### 3D Multi-Agent Trace Visualizer

Built a local viewer that validates a multi-agent execution trace, replays it deterministically, and shows it as an accessible 2D event table or a Three.js agent graph. Both views share one replay controller and event inspector, so switching views keeps the replay position and selection. Trace files are read in the browser, and the built page blocks network requests (`connect-src 'none'`).

All 265 tests passed in GitHub CI on the current commit. Recorded scripted Chromium checks with software WebGL passed 32/32 for the 2D view, 40/40 for the 3D view (including the no-WebGL fallback and context loss), and 24/24 for layout at 1280 px and 375 px. The bundled trace is synthetic. Real SwarmOS trace ingestion, screen readers, GPU rendering performance, and Firefox/Safari are untested, and no usability gain has been measured.

[Repository](https://github.com/RyanJBush/3D-Multi-Agent-Swarm-Command-Centre) · [Passing CI run](https://github.com/RyanJBush/3D-Multi-Agent-Swarm-Command-Centre/actions/runs/44882351001) · [Synthetic trace](https://github.com/RyanJBush/3D-Multi-Agent-Swarm-Command-Centre/blob/5f8a05c16bfd42ea367e71d58362e4e6ab69806f/fixtures/synthetic-trace.json) · [Browser check record](https://github.com/RyanJBush/3D-Multi-Agent-Swarm-Command-Centre/blob/5f8a05c16bfd42ea367e71d58362e4e6ab69806f/README.md#commands) · [Known limitations](https://github.com/RyanJBush/3D-Multi-Agent-Swarm-Command-Centre/blob/5f8a05c16bfd42ea367e71d58362e4e6ab69806f/README.md#known-limitations)

### Prompt-Injection Guardrails

Built a default-deny permission gate that checks each agent-proposed tool call against a fixed task policy: three allowed tools, exact argument fields, and one allowed path or test name per tool. Paths must resolve inside the workspace, and denied calls never reach the recording mock executor. The gate does not read prompt or issue text and uses no LLM, so it is an authorization layer, not a prompt-injection detector.

In three scripted synthetic cases, the gate blocked 1/1 unauthorized calls (an injected read of a fake secret) and incorrectly blocked 0/9 authorized calls, including in a case that only quotes the injected text; 3/3 tasks completed. All 115 tests passed in GitHub CI on Windows and Ubuntu with Python 3.12 and 3.13. No model-driven runs or real tool runtimes have been tested.

[Repository](https://github.com/RyanJBush/Prompt-Injection-Guardrails) · [Passing CI run](https://github.com/RyanJBush/Prompt-Injection-Guardrails/actions/runs/44890676079) · [Scripted cases and output](https://github.com/RyanJBush/Prompt-Injection-Guardrails/blob/140c2f66a721967de1deb932015f08077741c9e3/README.md#issue-text-vs-the-scripted-tool-proposal) · [Metrics definitions](https://github.com/RyanJBush/Prompt-Injection-Guardrails/blob/140c2f66a721967de1deb932015f08077741c9e3/README.md#metrics-and-what-completed-means) · [Known limitations](https://github.com/RyanJBush/Prompt-Injection-Guardrails/blob/140c2f66a721967de1deb932015f08077741c9e3/README.md#limits)

### Litmus

Built a local evidence workbench that reports text-origin signals, writing-pattern observations, and image Content Credentials (C2PA) as separate records, each with its reasons and limits. It does not assign an "AI percentage". Text origin uses a Binoculars-style score from pinned Qwen2.5-0.5B base and Instruct models on a local GPU, and the browser interface binds only to 127.0.0.1.

On a frozen held-out subset of RAID (3,361 texts in 675 source groups), clean-text AUROC was 0.80358 (grouped 95% interval 0.776–0.829). At the development-selected threshold, it flagged 66.37% of machine texts with a 4.59% false-positive rate; homoglyph edits cut detection to 8.59%. The subset comes from RAID's train.csv, not the official test set. In a fresh clone, a read-only verifier reproduced the saved metrics and 752 model-free tests passed; GPU tests were not part of that check. Dependency advisories in the model stack are unresolved, so the release is not security-cleared.

[Repository](https://github.com/RyanJBush/AI-Generated-Content-Detection-and-Authenticity-Analyzer) · [Interface screenshot](https://github.com/RyanJBush/AI-Generated-Content-Detection-and-Authenticity-Analyzer/blob/d7ec4b00b0bf658146de86b110937b013094fb9a/eval/results/readiness/desktop.png) · [Held-out results](https://github.com/RyanJBush/AI-Generated-Content-Detection-and-Authenticity-Analyzer/blob/d7ec4b00b0bf658146de86b110937b013094fb9a/README.md#held-out-evaluation-r1-g-scientific-results-independently-reviewed) · [Full metrics](https://github.com/RyanJBush/AI-Generated-Content-Detection-and-Authenticity-Analyzer/blob/d7ec4b00b0bf658146de86b110937b013094fb9a/eval/results/r1g/metrics.json) · [Security status](https://github.com/RyanJBush/AI-Generated-Content-Detection-and-Authenticity-Analyzer/blob/d7ec4b00b0bf658146de86b110937b013094fb9a/docs/RELEASE-READINESS.md)

### PJM Energy Demand Forecasting

Built a checksum-pinned EIA-930 backtest. A frozen ridge model reduced MAE by 25.3% against a 168-hour weekly baseline on 1,389 comparable hours in November–December 2024. The weekly baseline won on the October tuning block and on the ridge model's worst day, December 25.

[Repository](https://github.com/RyanJBush/PJM-Energy-Demand-Forecasting) · [Results and reproduction commands](https://github.com/RyanJBush/PJM-Energy-Demand-Forecasting/blob/c0264db3950c5fdfb32d7d6418eb09a4761443f9/README.md#result-on-the-shared-scoring-set) · [December 25 failure-case chart](https://github.com/RyanJBush/PJM-Energy-Demand-Forecasting/blob/c0264db3950c5fdfb32d7d6418eb09a4761443f9/docs/worst_day_2024-12-25.svg)

### Smart Grid Sensor Anomaly Detection

Built a reproducible voltage replay comparing fixed limits with a causal rolling median/MAD detector. On one held-out synthetic fixture, fixed limits detected 6 of 6 faults with 5 unmatched alerts. Rolling MAD detected 5 of 6 with 4 unmatched alerts and missed a sustained voltage shift.

[Repository and demo](https://github.com/RyanJBush/Smart-Grid-Sensor-Anomaly-Detection) · [Held-out report](https://github.com/RyanJBush/Smart-Grid-Sensor-Anomaly-Detection/blob/e67ee00ec3031deac3ff59ea2ec23530ef69b1f6/results/heldout/heldout_report.md) · [Replay chart](https://github.com/RyanJBush/Smart-Grid-Sensor-Anomaly-Detection/blob/e67ee00ec3031deac3ff59ea2ec23530ef69b1f6/results/heldout/heldout_chart.png) · [Passing CI run](https://github.com/RyanJBush/Smart-Grid-Sensor-Anomaly-Detection/actions/runs/42674141699/attempts/2)
