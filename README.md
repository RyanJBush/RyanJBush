# Ryan Bush

Selected projects in retrieval evaluation, agent workflow tooling, and demand forecasting. Each project links to a demo and the evidence behind its results.

### Retrieval Evaluation Harness

Built a reproducible comparison of BM25 and a pinned embedding model, with per-query relevance metrics, CPU latency exports, and a side-by-side viewer. On the bundled synthetic fixture, Recall@5 was 0.714 for BM25 and 1.000 for embeddings across seven scored queries.

[Saved results](https://github.com/RyanJBush/retrieval-eval-harness/blob/5daa6003131c1ce3e11a1673c976c24dac2c80c7/examples/demo/summary.csv) · [Passing CI run](https://github.com/RyanJBush/retrieval-eval-harness/actions/runs/42416440729) · [Viewer screenshot](https://github.com/RyanJBush/retrieval-eval-harness/blob/5daa6003131c1ce3e11a1673c976c24dac2c80c7/evidence/browser/after_desktop_q02_k3.png)

### SwarmOS

Built a deterministic Planner–Implementer–Reviewer workflow that applies a fixed patch in a disposable Git repository, gates approval on an acceptance test, and stores verifiable execution traces in SQLite. The paired demo completed 3/3 runs per arm, with three memory hits when enabled and zero when disabled.

[Recorded results](https://github.com/RyanJBush/swarmos/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/demo-evidence.json) · [Passing CI run](https://github.com/RyanJBush/swarmos/actions/runs/42434894375) · [Captioned demo](https://github.com/RyanJBush/swarmos/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/swarmos-demo.webm) · [Timeline screenshot](https://github.com/RyanJBush/swarmos/blob/f956d12f9bc65be3006e0d99f581ac0009a9040e/docs/media/timeline.png)

### PJM Demand Forecasting

Built a checksum-pinned EIA-930 backtest. A frozen ridge model reduced MAE by 25.3% against a 168-hour weekly baseline on 1,389 comparable hours in November–December 2024. The weekly baseline won on the October tuning block and on the ridge model's worst day, December 25.

[Results and reproduction commands](https://github.com/RyanJBush/pjm-demand-forecast/blob/c0264db3950c5fdfb32d7d6418eb09a4761443f9/README.md#result-on-the-shared-scoring-set) · [December 25 failure-case chart](https://github.com/RyanJBush/pjm-demand-forecast/blob/c0264db3950c5fdfb32d7d6418eb09a4761443f9/docs/worst_day_2024-12-25.svg)
