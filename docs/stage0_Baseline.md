# Phase 0: The Baseline Hypothesis

## Environment
- **Hardware:** Omen 15-ax252nr (Intel i7-7700HQ)
- **Cores:** 4 Physical, 8 Logical
- **OS:** Linux (Fedora/CentOS/RHEL derivative)

## The Constraints (Control Variables)
1. **Worker Processes (4):** Locked to match physical core count to minimize context switching.
2. **Ulimit (4096):** Set to prevent OS-level file descriptor exhaustion during concurrent tests.
3. **Threads (2):** Balanced load to allow the CPU to manage both the 'attacker' (wrk) and 'defender' (Nginx/Apache).

## The Hypothesis
In a "naked" proxy setup (no caching/tuning):
- **Throughput:** Nginx will show ~40-60% of the raw throughput of Apache due to the "Proxy Tax" (double-handling the request).
- **Latency:** Nginx will have higher average latency but lower **jitter** (Standard Deviation) than Apache.
- **Reliability:** Nginx will handle 100+ connections with zero errors, while Apache may begin to show "Read Errors" when hit directly.
