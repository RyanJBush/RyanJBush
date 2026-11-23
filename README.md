# Ryan Bush

Selected projects in LLM reliability, local analytics, retrieval evaluation, agent workflow tooling, text-origin evaluation and content provenance, demand forecasting, and sensor anomaly detection. Each project links to a demo and the evidence behind its results.

### Self-Healing LLM Gateway

Built a local text-generation gateway with bounded retries, approved fallback providers, and per-provider circuit breakers. A two-second deadline includes calls and retry waits; sanitized traces explain routing and recovery decisions.

On the same seven-request deterministic failure schedule, the gateway completed 7/7 requests with 11 provider calls, compared with 2/7 and seven calls for a direct-primary baseline. These are stub results with simulated timings. All 382 tests and 31 acceptance assertions passed on Windows and Ubuntu with Python 3.11–3.13. Real LLM providers, macOS, and load beyond five concurrent requests remain unverified.

[Repository](https://github.com/RyanJBush/self-healing-llm-gateway) · [Demo preview](https://github.com/RyanJBush/self-healing-llm-gateway/blob/4efd14e5bce54a1d66018bbb4641cc07e9ff9114/docs/media/acceptance-preview.png) · [Verified results](https://github.com/RyanJBush/self-healing-llm-gateway/blob/4efd14e5bce54a1d66018bbb4641cc07e9ff9114/evidence/verification.md) · [Passing CI run](https://github.com/RyanJBush/self-healing-llm-gateway/actions/runs/42944790109) · [Release v0.2.2](https://github.com/RyanJBush/self-healing-llm-gateway/releases/tag/v0.2.2)

### Enterprise Text-to-SQL Analytics Agent

Built a local analytics assistant using Ollama and Qwen3 4B to propose SQL over a synthetic sales database. A restricted SQLite executor enforces approved reads, row limits, and a query work budget. The demo shows a correct joined revenue answer, a clarification question, and a blocked schema read.

Seven local acceptance cases passed. The test suite recorded 182 passes and three optional Anthropic SDK skips. Earlier model mistakes are retained with the results.

[Repository](https://github.com/RyanJBush/enterprise-text-to-sql-agent) · [51-second demo](https://github.com/RyanJBush/enterprise-text-to-sql-agent/blob/d9278eb98efcf2e73f3a07b0579efa34855ef1b6/docs/media/text2sql-demo.mp4) · [Verified results](https://github.com/RyanJBush/enterprise-text-to-sql-agent/blob/d9278eb98efcf2e73f3a07b0579efa34855ef1b6/evidence/results.md) · [Exact test output](https://github.com/RyanJBush/enterprise-text-to-sql-agent/blob/d9278eb98efcf2e73f3a07b0579efa34855ef1b6/evidence/test-output.txt)

### Retrieval Evaluation Harness

Built a reproducible comparison of BM25 and a pinned embedding model, with per-query relevance metrics, CPU latency exports, and a side-by-side viewer. On the bundled synthetic fixture, Recall@5 was 0.714 for BM25 and 1.000 for embeddings across seven scored queries.

[Repository](https://github.com/RyanJBush/Retrieval-Evaluation-Harness) · [Saved results](https://github.com/RyanJBush/Retrieval-Evaluation-Harness/blob/5daa6003131c1ce3e11a1673c976c24dac2c80c7/examples/demo/summary.csv) · [Passing CI run](https://github.com/RyanJBush/Retrieval-Evaluation-Harness/actions/runs/42416440729) · [Viewer screenshot](https://github.com/RyanJBush/Retrieval-Evaluation-Harness/blob/5daa6003131c1ce3e11a1673c976c24dac2c80c7/evidence/browser/after_desktop_q02_k3.png)

### SwarmOS

Built a deterministic Planner–Implementer–Reviewer workflow that applies a fixed patch in a disposable Git repository, gates approval on an acceptance test, and stores verifiable execution traces in SQLite. The paired demo completed 3/3 runs per arm, with three memory hits when enabled and zero when disabled.

[Recorded results](https://github.com/RyanJBush/swarmos/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/demo-evidence.json) · [Passing CI run](https://github.com/RyanJBush/swarmos/actions/runs/42434894375) · [Captioned demo](https://github.com/RyanJBush/swarmos/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/swarmos-demo.webm) · [Timeline screenshot](https://github.com/RyanJBush/swarmos/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/timeline.png)

### Litmus

Built a local evidence workbench that reports text-origin signals, writing-pattern observations, and image Content Credentials (C2PA) as separate records, each with its reasons and limits. It does not assign an "AI percentage". Text origin uses a Binoculars-style score from pinned Qwen2.5-0.5B base and Instruct models on a local GPU, and the browser interface binds only to 127.0.0.1.

On a frozen held-out subset of RAID (3,361 texts in 675 source groups), clean-text AUROC was 0.80358 (grouped 95% interval 0.776–0.829). At the development-selected threshold, it flagged 66.37% of machine texts with a 4.59% false-positive rate; homoglyph edits cut detection to 8.59%. The subset comes from RAID's train.csv, not the official test set. In a fresh clone, a read-only verifier reproduced the saved metrics and 752 model-free tests passed; GPU tests were not part of that check. Dependency advisories in the model stack are unresolved, so the release is not security-cleared.

[Repository](https://github.com/RyanJBush/AI-Generated-Content-Detection-and-Authenticity-Analyzer) · [Interface screenshot](https://github.com/RyanJBush/AI-Generated-Content-Detection-and-Authenticity-Analyzer/blob/d7ec4b00b0bf658146de86b110937b013094fb9a/eval/results/readiness/desktop.png) · [Held-out results](https://github.com/RyanJBush/AI-Generated-Content-Detection-and-Authenticity-Analyzer/blob/d7ec4b00b0bf658146de86b110937b013094fb9a/README.md#held-out-evaluation-r1-g-scientific-results-independently-reviewed) · [Full metrics](https://github.com/RyanJBush/AI-Generated-Content-Detection-and-Authenticity-Analyzer/blob/d7ec4b00b0bf658146de86b110937b013094fb9a/eval/results/r1g/metrics.json) · [Security status](https://github.com/RyanJBush/AI-Generated-Content-Detection-and-Authenticity-Analyzer/blob/d7ec4b00b0bf658146de86b110937b013094fb9a/docs/RELEASE-READINESS.md)

### PJM Demand Forecasting

Built a checksum-pinned EIA-930 backtest. A frozen ridge model reduced MAE by 25.3% against a 168-hour weekly baseline on 1,389 comparable hours in November–December 2024. The weekly baseline won on the October tuning block and on the ridge model's worst day, December 25.

[Results and reproduction commands](https://github.com/RyanJBush/PJM-Energy-Demand-Forecasting/blob/c0264db3950c5fdfb32d7d6418eb09a4761443f9/README.md#result-on-the-shared-scoring-set) · [December 25 failure-case chart](https://github.com/RyanJBush/PJM-Energy-Demand-Forecasting/blob/c0264db3950c5fdfb32d7d6418eb09a4761443f9/docs/worst_day_2024-12-25.svg)

### Smart Grid Sensor Anomaly Detection

Built a reproducible voltage replay comparing fixed limits with a causal rolling median/MAD detector. On one held-out synthetic fixture, fixed limits detected 6 of 6 faults with 5 unmatched alerts. Rolling MAD detected 5 of 6 with 4 unmatched alerts and missed a sustained voltage shift.

[Repository and demo](https://github.com/RyanJBush/smart-grid-sensor-anomaly-detection) · [Held-out report](https://github.com/RyanJBush/smart-grid-sensor-anomaly-detection/blob/e67ee00ec3031deac3ff59ea2ec23530ef69b1f6/results/heldout/heldout_report.md) · [Replay chart](https://github.com/RyanJBush/smart-grid-sensor-anomaly-detection/blob/e67ee00ec3031deac3ff59ea2ec23530ef69b1f6/results/heldout/heldout_chart.png) · [Passing CI run](https://github.com/RyanJBush/smart-grid-sensor-anomaly-detection/actions/runs/42674141699/attempts/2)
