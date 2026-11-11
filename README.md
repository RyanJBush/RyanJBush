# Ryan Bush

Selected projects in local analytics, retrieval evaluation, agent workflow tooling, demand forecasting, and sensor anomaly detection. Each project links to a demo and the evidence behind its results.

### Enterprise Text-to-SQL Analytics Agent

Built a local analytics assistant using Ollama and Qwen3 4B to propose SQL over a synthetic sales database. A restricted SQLite executor enforces approved reads, row limits, and a query work budget. The demo shows a correct joined revenue answer, a clarification question, and a blocked schema read.

Seven local acceptance cases passed. The test suite recorded 182 passes and three optional Anthropic SDK skips. Earlier model mistakes are retained with the results.

[Repository](https://github.com/RyanJBush/enterprise-text-to-sql-agent) · [51-second demo](https://github.com/RyanJBush/enterprise-text-to-sql-agent/blob/d9278eb98efcf2e73f3a07b0579efa34855ef1b6/docs/media/text2sql-demo.mp4) · [Verified results](https://github.com/RyanJBush/enterprise-text-to-sql-agent/blob/d9278eb98efcf2e73f3a07b0579efa34855ef1b6/evidence/results.md) · [Exact test output](https://github.com/RyanJBush/enterprise-text-to-sql-agent/blob/d9278eb98efcf2e73f3a07b0579efa34855ef1b6/evidence/test-output.txt)

### Retrieval Evaluation Harness

Built a reproducible comparison of BM25 and a pinned embedding model, with per-query relevance metrics, CPU latency exports, and a side-by-side viewer. On the bundled synthetic fixture, Recall@5 was 0.714 for BM25 and 1.000 for embeddings across seven scored queries.

[Saved results](https://github.com/RyanJBush/retrieval-eval-harness/blob/5daa6003131c1ce3e11a1673c976c24dac2c80c7/examples/demo/summary.csv) · [Passing CI run](https://github.com/RyanJBush/retrieval-eval-harness/actions/runs/42416440729) · [Viewer screenshot](https://github.com/RyanJBush/retrieval-eval-harness/blob/5daa6003131c1ce3e11a1673c976c24dac2c80c7/evidence/browser/after_desktop_q02_k3.png)

### SwarmOS

Built a deterministic Planner–Implementer–Reviewer workflow that applies a fixed patch in a disposable Git repository, gates approval on an acceptance test, and stores verifiable execution traces in SQLite. The paired demo completed 3/3 runs per arm, with three memory hits when enabled and zero when disabled.

[Recorded results](https://github.com/RyanJBush/swarmos/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/demo-evidence.json) · [Passing CI run](https://github.com/RyanJBush/swarmos/actions/runs/42434894375) · [Captioned demo](https://github.com/RyanJBush/swarmos/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/swarmos-demo.webm) · [Timeline screenshot](https://github.com/RyanJBush/swarmos/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/timeline.png)

### PJM Demand Forecasting

Built a checksum-pinned EIA-930 backtest. A frozen ridge model reduced MAE by 25.3% against a 168-hour weekly baseline on 1,389 comparable hours in November–December 2024. The weekly baseline won on the October tuning block and on the ridge model's worst day, December 25.

[Results and reproduction commands](https://github.com/RyanJBush/pjm-demand-forecast/blob/c0264db3950c5fdfb32d7d6418eb09a4761443f9/README.md#result-on-the-shared-scoring-set) · [December 25 failure-case chart](https://github.com/RyanJBush/pjm-demand-forecast/blob/c0264db3950c5fdfb32d7d6418eb09a4761443f9/docs/worst_day_2024-12-25.svg)

### Smart Grid Sensor Anomaly Detection

Built a reproducible voltage replay comparing fixed limits with a causal rolling median/MAD detector. On one held-out synthetic fixture, fixed limits detected 6 of 6 faults with 5 unmatched alerts. Rolling MAD detected 5 of 6 with 4 unmatched alerts and missed a sustained voltage shift.

[Repository and demo](https://github.com/RyanJBush/smart-grid-sensor-anomaly-detection) · [Held-out report](https://github.com/RyanJBush/smart-grid-sensor-anomaly-detection/blob/e67ee00ec3031deac3ff59ea2ec23530ef69b1f6/results/heldout/heldout_report.md) · [Replay chart](https://github.com/RyanJBush/smart-grid-sensor-anomaly-detection/blob/e67ee00ec3031deac3ff59ea2ec23530ef69b1f6/results/heldout/heldout_chart.png) · [Passing CI run](https://github.com/RyanJBush/smart-grid-sensor-anomaly-detection/actions/runs/42674141699/attempts/2)
