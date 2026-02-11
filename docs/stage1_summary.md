Stage 1: Summary of "Solid Soil"

Here is a refined version of your notes. You can copy this directly into your project documentation.
Stage 1: Infrastructure Hardening & Baseline

Objective: Establish a secure, high-performance "Control Group" using Nginx and Apache.
1. Security Architecture (The "Shield")

I implemented a defense-in-depth strategy by obfuscating server identity and enforcing browser-side security via headers.
Header	Implementation	Purpose
Server Identity	server_tokens off (Nginx) / Prod (Apache)	Prevents version leakage (Information Disclosure).
X-Frame-Options	SAMEORIGIN	Mitigates Clickjacking by preventing external iFraming.
X-Content-Type	nosniff	Disables MIME-sniffing; prevents execution of non-executable types.
CSP	default-src 'self'	Prevents XSS by whitelisting the origin as the only trusted source.
Referrer-Policy	no-referrer-when-downgrade	Protects user privacy during external navigation.
2. Performance Tuning (The "Plumbing")

To ensure the benchmark measures the proxy logic and not a configuration bottleneck:

    Connection Pooling: Enabled HTTP/1.1 and keepalive (65s) across the entire stack (wrk <-> Nginx <-> Apache).

    Worker Optimization: * Nginx: 4 workers (matching physical cores) with 2048 connections.

        Apache (MPM Event): Raised ServerLimit to 25 and MaxRequestWorkers to 1200 to accommodate the -c1000 stress test.

    Identity Restoration: Implemented mod_remoteip in Apache to ensure Nginx correctly passes the client's real IP via X-Forwarded-For.

3. Final Thoughts & Pivot

    Scope Creep identified: I realized that constantly tweaking the benchmark mid-stage was delaying progress. I am locking the configs now.

    Hardware Contention: The Omen 15 (i7-7700HQ) is a single-host environment. The "Proxy Tax" observed is largely CPU Context Switching because Nginx, Apache, and wrk are all fighting for the same physical cores.

    Benchmark Protocol: 1000c proved to be a "Stress Test" (revealing OS/Hardware limits). In Stage 2, I will implement a Scaling Matrix (10c, 100c, 1000c) to document how the system behaves under different load intensities.
