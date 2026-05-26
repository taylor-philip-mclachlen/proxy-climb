-- Stage 0 — 100c (baseline nginx → apache)
nginx (:80)
Requests/sec: 22,768.83
Avg latency: 4.58 ms
Max latency: 77.37 ms
Transfer/sec: 5.19 MB/s
apache (:8080)
Requests/sec: 58,475.14
Avg latency: 3.24 ms
Max latency: 39.43 ms
Errors: 22 read errors
Transfer/sec: 12.45 MB/s

-- Stage 1 — 100c
nginx (:80)
Requests/sec: 15,232.68
Avg latency: 16.34 ms
Max latency: 145.88 ms
Transfer/sec: 6.09 MB/s
apache (:8080)
Requests/sec: 59,550.35
Avg latency: 2.89 ms
Max latency: 28.44 ms
Transfer/sec: 11.87 MB/s

-- Stage 2 — 100c
nginx (:443)
Requests/sec: 34,188.59
Avg latency: 3.32 ms
Max latency: 163.57 ms
Transfer/sec: 16.04 MB/s
apache (:8080)
Requests/sec: 58,774.80
Avg latency: 2.98 ms
Max latency: 31.79 ms
Transfer/sec: 11.71 MB/s


-- Stage 3.0 — 100c
nginx (:443)
Requests/sec: 30,523.55
Avg latency: 3.75 ms
Max latency: 93.14 ms
Transfer/sec: 14.32 MB/s
apache (:8080)
Requests/sec: 50,879.68
Avg latency: 3.08 ms
Max latency: 30.49 ms
Transfer/sec: 10.14 MB/s

-- Stage 3.5 — 100c (iptables)
nginx (:443)
Requests/sec: 30,267.98
Avg latency: 3.90 ms
Max latency: 121.96 ms
Transfer/sec: 14.20 MB/s
apache (:8080)
Requests/sec: 52,369.11
Avg latency: 2.99 ms
Max latency: 30.17 ms
Transfer/sec: 10.44 MB/s


--Summary
biggest changes come from config (not load)
Stage 1 is worst performer at 100c
Stage 2–3.5 stabilize performance around ~30k RPS
apache (backend)
very stable across all 100c runs (~50–59k RPS)
latency barely changes
behaves like a “steady sink”
