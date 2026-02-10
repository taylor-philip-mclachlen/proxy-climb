# Phase 0: The Baseline Hypothesis

## Environment
- Hardware: Omen 15-ax252nr (Intel i7-7700HQ)
- Cores: 4 Physical, 8 Logical
- Os: Arch 64.0.2 
 
## The Constraints (Control Variables)
1. Worker Processes (4): Locked to match physical core count to minimize context switching.
2. Ulimit (1000): Set to prevent OS-level file descriptor exhaustion during concurrent tests.
3. Threads (2): Balanced load to allow the CPU to manage both the 'attacker' (wrk) and 'defender' (Nginx/Apache).
4. wrk: benchamarking 2 threads @ 1000c per ms for 5 seconds.
5. nginx:port 80 // httpd(apache):port 8080

## The Hypothesis
In a baseline  proxy setup (no caching/tuning):
- Throughput: Nginx will show ~40-60% of the raw throughput of Apache due to the "Proxy Tax" (double-handling the request).
- Latency: Nginx will have higher average latency but lower **jitter** (Standard Deviation) than Apache.
- Reliability: Nginx will handle 100+ connections with zero errors, while Apache may begin to show "Read Errors" when hit directly.
