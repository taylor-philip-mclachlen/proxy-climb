# Proxy-Climb

A hands-on project documenting my journey into reverse proxies, network concurrency, and system bottlenecks. Built as part of my post-electromechanical engineering portfolio to bridge physical hardware concepts with software scale.

## The Core Concept
The idea here is simple: set up a reverse proxy layer, blast it with traffic using a benchmarking tool called `wrk`, and see exactly what breaks when you scale from normal use to heavy stress. 

## The Sandbox
* **The Gear:** Omen 15-ax252nr laptop (Intel i7-7700HQ — 4 physical cores, 8 threads).
* **The Environment:** Arch Linux (running inside `/srv/http/` to keep system file permissions simple).
* **The Stack:** NGINX (Frontend Proxy), Apache HTTPD (Backend Server), and `wrk` (Load testing).

---

## The Learning Journey (Stage by Stage)

### Stage 0: Stripping it Down to the Basics
I skipped the standard default configurations and tried to build a bare-minimum setup from scratch. I quickly learned you need Apache's "Big 4" modules (`mpm_event`, `proxy`, `ssl`, and `rewrite`) just to get a basic reverse proxy moving.
* **My Initial Hypothesis:** I figured out that an un-tuned proxy layer would charge a "Proxy Tax" (dropping throughput by 40–60%), but it would act as a structural shield, stopping the backend from throwing error codes.

### Stage 1: Security Headers and Real Hardware Friction
I added basic security plumbing (hiding server versions, forcing `SAMEORIGIN` clickjacking defense, and setting up `nosniff`). 
* **The Reality Check:** Because I am testing this entirely on a single laptop, NGINX, Apache, and `wrk` are all fighting for the exact same 4 physical CPU cores. A lot of the performance drops I noticed aren't bad code—it's just the CPU constantly pausing processes to handle context switching.

### Stage 2: Moving to HTTPS (:443)
I generated a local 2048-bit RSA certificate using OpenSSL and set up NGINX to handle the encryption/decryption at the edge so Apache wouldn't have to deal with the mathematical overhead. I forced an automatic HTTP-to-HTTPS upgrade loop and switched NGINX to use modern HTTP/2 syntax. 
* **The Win:** Tuning the connection backlogs dropped our worst-case latency under peak load from 1.33 seconds down to 825 milliseconds.

### Stage 3.0 & 3.5: The Firewall and the "Accidental Buffer"
I clamped down the OS using an `iptables` firewall policy to evaluate packet hygiene impact on the stack. I originally planned to build a custom Go mid-layer to handle connection multiplexing, but I made a pragmatic design decision to pull it out of scope to prevent infinite repository complexity. Instead, I focused purely on tuning Apache's Event MPM.
* **The Weird Behavior (The Firewall Assist):** Intuitively, adding a firewall should slow everything down because the kernel has to inspect every packet. However, during the high-concurrency stress tests, our metrics actually *stabilized and improved*. 
* **Why it happened:** The strict rate limits (`--limit 30/s`) and connection clamps (`--connlimit-above 40 -j DROP`) I introduced in `iptables` acted as an unintentional traffic-shaping system. By aggressively dropping invalid packets and restricting the raw speed of connection surges, the firewall effectively shielded NGINX and the kernel networking stack from hitting total socket exhaustion. It was a massive lesson in how lower-level OS structures can completely alter application behavior.

---

## The Raw Data (100 vs 1000 Connections)

### 1. Light Concurrency Baseline (100c)
At 100 simultaneous connections, Apache is naturally fast out of the box. But once NGINX was properly tuned with optimized buffers and SSL caching in Stage 2, it achieved massive data throughput efficiency.

| Server Configuration | Requests / Second | Average Latency | Transfer Rate | Total Errors |
| :--- | :---: | :---: | :---: | :---: |
| Nginx (Stage 0 Baseline) | 22,768 | 4.58 ms | 5.19 MB/s | 0 |
| Nginx (Stage 1 Hardened) | 15,232 | 16.34 ms | 6.09 MB/s | 0 |
| Nginx (Stage 2 SSL Tuned) | 34,188 | 3.32 ms | 16.04 MB/s | 0 |
| Nginx (Stage 3.5 with Firewall Assist) | 30,267 | 3.90 ms | 14.20 MB/s | 0 |
| | | | | |
| Apache (Stage 0 Baseline) | 58,475 | 3.24 ms | 12.45 MB/s | 22 |
| Apache (Stage 1 Hardened) | 59,550 | 2.89 ms | 11.87 MB/s | 0 |
| Apache (Stage 2 High-Limit) | 58,774 | 2.98 ms | 11.71 MB/s | 0 |
| Apache (Stage 3.5 Event-Driven) | 52,369 | 2.99 ms | 10.44 MB/s | 0 |

![100c Performance Dashboard](reverse_proxy/graphs/benchmark_100c_dashboard.png)

### 2. The 1000c Breakpoint
When the pressure is scaled up 10x to 1,000 concurrent connections, the real architectural differences reveal themselves:
* **NGINX:** Holds its ground smoothly. Throughput only drops by about 15% compared to low load, and errors are essentially non-existent.
* **Apache:** Looks incredibly fast on paper, but it completely runs out of available network sockets, resulting in an astronomical failure rate of **89,000 to 155,000 read errors**. 

![Throughput Degradation under Load](reverse_proxy/graphs/concurrency_load_comparison.png)
![1000c Detailed Error Dashboard](reverse_proxy/graphs/benchmark_dashboard.png)

---

## Key Things I Learned
1. **Don't Trust Raw Metrics:** If you only look at "Requests per second," Apache looks like the winner. But when you look at the error column, it is dropping thousands of connections. It chooses raw speed over stability when pushed too hard.
2. **Firewalls Can Accidental Shape Traffic:** Firewalls add CPU overhead, but by enforcing structural packet rules, they can actually *improve* system stability under immense concurrency by rejecting traffic that would otherwise choke the kernel socket queues.
3. **Hardware is the Ultimate Ceiling:** At 1,000 connections, my laptop CPU hit a solid 100% utilization. Because NGINX and Apache are sharing the same network stack and kernel queues, the bottleneck shifts from software configuration to kernel-level socket backlog saturation.

---

## Where I'm Heading Next
* **Kernel Parameter Tuning:** Moving into the OS layer to optimize `sysctl` settings, specifically looking at increasing socket backlog limits (`somaxconn`) and TCP SYN queue thresholds to see if the host kernel can help Apache survive the 1000c stress test without relying on firewall drops.
* **Firewall Alternatives:** Expanding the network baseline by doing a direct comparison between `iptables` and modern `nftables` configurations under identical rulesets to track processing efficiency.
* **Embedded Transition:** Leveraging what I've learned about resource constraints, memory boundaries, and CPU context switching here to start building lower-level software projects in C for embedded systems.
