Stage 0: Foundations & The Baseline Hypothesis
1. The Environment Setup

    Hardware: Omen 15-ax252nr (Intel i7-7700HQ) | 4 Cores | 8 Threads.

    OS: Arch Linux (Targeting /srv/http/ to bypass user-home permission constraints).

    Tooling: Switched from JMeter (Java overhead) to wrk and ab (C-based performance) for lighter, more accurate local testing.

2. The "From Scratch" Component

I moved away from default package configs to a minimal, manual setup to understand the core requirements.

    Module Discovery: Identified the "Big 4" modules needed for a functional Apache (httpd) worker:

        mpm_event_module: The engine for request processing.

        proxy_module: Enables the "Reverse Proxy" capability.

        ssl_module: For future-proofing HTTPS.

        rewrite_module: For URL manipulation.

    Lesson Learned: Module paths must be absolute and descriptive in a minimal config to avoid "File not found" errors during startup.

3. Metrics of Success

Instead of just "is it fast?", I am tracking:

    Throughput (Req/Sec): Total capacity.

    Latency (Mean): Responsiveness.

    Percentiles (P95, P99): Identifying the "Tail Latency" or pain points for the slowest 5% of users.

4. The Orchestrator (Go)

I shifted from shell scripts to Go for benchmarking.

    Go Run vs. Build: Learned the difference between the JIT-like behavior of go run and the portable binary produced by go build.

    Structure: Using a "Director" (Main) and "Experts" (Functions) pattern to keep the code organized.

5. The Baseline Hypothesis

    "In a raw, untuned state, Nginx will pay a 'Proxy Tax' of ~40-60% throughput compared to direct Apache access, but it will act as a stabilizer, reducing jitter and socket errors compared to hitting the backend directly."
