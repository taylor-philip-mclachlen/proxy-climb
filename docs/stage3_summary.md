 Stage 3 Proxy Climb Report

System: Omen 15-ax252nr
Goal: Evaluate firewall impact and system behavior under increasing proxy stack complexity
Stack: IPTables → Nginx → Go layer (planned) → Apache backend

1. Architecture Overview
1.1 Target Pipeline Design
Packet Layer:     IPTables (Firewall / Filtering)
Proxy Layer:      Nginx (TLS termination, caching, reverse proxy)
Logic Layer:      Go tooling (routing, request logic) [planned]
Backend Layer:    Apache HTTP Server (request processing)
1.2 Design Intent
Firewall enforces packet hygiene and access control
Nginx handles:
TLS termination
connection multiplexing
caching (if enabled)
Go layer intended for:
routing decisions
application-level request logic
Apache handles backend request processing (“final execution layer”)

2. System Configuration Changes
2.1 Firewall Configuration (iptables baseline)

Policy model:

INPUT: DROP
OUTPUT: ACCEPT
FORWARD: DROP

Rules:

Allow loopback traffic
Allow established connections
Drop invalid packets
Allow SSH (22)
Allow HTTPS (443)
Optional rate limiting and connection limiting on 443

Key rules:

iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP

iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

iptables -A INPUT -p tcp --syn --dport 443 -m limit --limit 30/s --limit-burst 60 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -m connlimit --connlimit-above 40 -j DROP
Stage 3: Architecture Design


firewall layer (iptables/nftables)


Nginx (TLS, caching, reverse proxy)


Go (application routing layer)


Apache (backend processing)



Stage 3: Configuration Changes


nginx worker tuning


event MPM enabled


conntrack rules added


loopback handling


connection limits applied



Stage 3: Benchmark Results
100 connections (baseline)


no firewall vs firewall comparison


stable metrics


~10–13% overhead


1000 connections (stress)

2.2 Nginx Configuration Changes
Increased worker connections to 8096
Event-based concurrency model enabled
High connection capacity tuning for stress testing
2.3 Apache Configuration
Event MPM enabled

Rationale:

Improves keepalive handling
Reduces thread blocking
Improves concurrency efficiency under load
2.4 Conntrack Observations
nf_conntrack_max: 262144
nf_conntrack_count: ~125 (low, stable)

Conclusion:

No conntrack saturation observed in normal runs
2.5 Optional Optimization Tested

Loopback bypass (NOTRACK):

iptables -t raw -I PREROUTING -i lo -j NOTRACK
iptables -t raw -I OUTPUT -o lo -j NOTRACK

Purpose:

Remove loopback traffic from state tracking overhead

3.  Benchmark Results
3.1 100 Connections (Baseline Load)
HTTPS (:443)
Metric	No IPTables	IPTables	Delta
Requests/sec	34,188	30,523	-10.7%
Avg Latency	3.32ms	3.75ms	+12.9%
Transfer/sec	16.04MB	14.32MB	-10.7%
HTTP (:8080)
Metric	No IPTables	IPTables	Delta
Requests/sec	58,774	50,879	-13.4%
Avg Latency	2.98ms	3.08ms	+3.4%
Transfer/sec	11.71MB	10.14MB	-13.4%
3.2 1000 Connections (Stress Load)
HTTPS (:443)
Metric	Value
Requests/sec	24,997
Avg Latency	64.67ms
Max Latency	1.34s
Errors	501 non-2xx/3xx
Transfer/sec	11.73MB
HTTP (:8080)
Metric	Value
Requests/sec	39,199
Avg Latency	15.56ms
Max Latency	230ms
Read Errors	155,446
Transfer/sec	7.81MB

4.  Scaling Comparison (100c → 1000c)
HTTPS
RPS: 30,523 → 24,997 (-17.4%)
Latency: 3.9ms → 64.67ms (~16× increase)
Max latency spike: 121ms → 1.34s
Stability: degraded under load
HTTP
RPS: 52,369 → 39,199 (-25.1%)
Latency: 2.99ms → 15.56ms (~5× increase)
Read errors: none → massive spike (155k)
Clear queue saturation behavior

5.  Key Findings
5.1 Firewall Impact
Stable overhead at realistic load:
~10–13% throughput reduction
minimal latency increase
Does NOT dominate performance under load
5.2 System Behavior at Scale

At 1000 connections:

Latency spikes dominate throughput analysis
Kernel + socket queue saturation occurs
Error rates increase significantly
Behavior shifts away from firewall influence

Conclusion:

system is no longer firewall-bound at high concurrency

5.3 Conntrack Impact
Conntrack usage remains low (~125 entries)
No evidence of table exhaustion
Firewall overhead is processing-based, not capacity-based
5.4 Primary Bottleneck Identified

At 1000 connections:

kernel socket backlog pressure
nginx worker contention
TLS CPU amplification (HTTPS)
accept queue saturation

6.  Interpretation Summary
6.1 Performance Model
Load Level	Behavior
100c	Stable, realistic measurement zone
1000c	Kernel + proxy saturation zone
6.2 Firewall Role
Adds predictable overhead (~10–20%)
Does not scale bottleneck behavior
Becomes negligible compared to kernel limits at high load
6.3 System Conclusion
Firewall is not the limiting factor
Nginx and kernel networking stack dominate high-concurrency behavior
Apache MPM Event improves backend efficiency but does not resolve upstream saturation
Go layer remains conceptual and should focus on logic routing, not packet handling

7.  Stage 4 Direction
7.1 Planned Focus Areas
Kernel tuning:
socket backlog
SYN queue limits
connection handling thresholds
Proxy optimization:
nginx worker scaling
upstream connection reuse
TLS optimization
Firewall benchmarking expansion:
iptables vs nftables direct comparison
loopback bypass evaluation
7.2 Open Questions
Where does true saturation begin (200c? 500c? 2000c?)
How much of 1000c degradation is kernel vs nginx?
Does nftables materially improve throughput under identical rulesets?

8.  Final Conclusion

Stage 3 demonstrates:

A stable multi-layer proxy architecture at realistic load (100c)
Predictable firewall overhead (~10–20%)
Strong evidence that high concurrency failure (1000c) is caused by kernel/network stack saturation rather than firewall inefficiency
Clear separation between:
application performance limits
system-level concurrency limits
