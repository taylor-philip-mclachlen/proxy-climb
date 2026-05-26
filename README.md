# Proxy-climb

Incremental Reverse Proxy Learning and Documentation:

## Overview

This is my first project. The concept is simple, set up a reverse proxy and use wrk to test performance.

## Goals
- Measure response times through a reverse proxy
- Identify bottlenecks under concurrent load
- Document setup and reproducible tests
- Understand OS-level system tuning for network performance

## Tech Stack 
- Load Testing: wrk
- OS: Manjaro Linux 26.0.2
- Hardware: Omen 15-ax252nr (Intel i7-7700HQ)
- Cores: 4 Physical, 8 Logical

## System Tuning & OS-Level Concepts
-NGINX 1.29.5
-APACHE 2.4.66
-wrk 4.2.0
-go 1.25.7 
## Setup 

## Running Tests 

## Results
## 🚀 Reverse Proxy Benchmarks ($100\text{c}$ Baseline vs $1000\text{c}$ Stress Test)

This section maps performance adjustments across progressive infrastructure changes, starting with a plain baseline up through specialized configuration optimization.

### 1. Low Concurrency Benchmark ($100\text{c}$)
At 100 concurrent requests, **apache** shows exceptional native speed, though **nginx** achieves significant transfer rate gains once optimizations/SSL are dialed in during Stage 2.

| Server / Stage | Requests/sec | Avg Latency | Max Latency | Transfer Rate | Errors |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **nginx** Stage 0 | 22,768.83 | 4.58 ms | 77.37 ms | 5.19 MB/s | 0 |
| **nginx** Stage 1 | 15,232.68 | 16.34 ms | 145.88 ms | 6.09 MB/s | 0 |
| **nginx** Stage 2 | 34,188.59 | 3.32 ms | 163.57 ms | 16.04 MB/s | 0 |
| **nginx** Stage 3.0 | 30,523.55 | 3.75 ms | 93.14 ms | 14.32 MB/s | 0 |
| **nginx** Stage 3.5 | 30,267.98 | 3.90 ms | 121.96 ms | 14.20 MB/s | 0 |
| | | | | | |
| **apache** Stage 0 | 58,475.14 | 3.24 ms | 39.43 ms | 12.45 MB/s | 22 |
| **apache** Stage 1 | 59,550.35 | 2.89 ms | 28.44 ms | 11.87 MB/s | 0 |
| **apache** Stage 2 | 58,774.80 | 2.98 ms | 31.79 ms | 11.71 MB/s | 0 |
| **apache** Stage 3.0 | 50,879.68 | 3.08 ms | 30.49 ms | 10.14 MB/s | 0 |
| **apache** Stage 3.5 | 52,369.11 | 2.99 ms | 30.17 ms | 10.44 MB/s | 0 |

![100c Performance Dashboard](benchmark_100c_dashboard.png)

---

### 2. Concurrency Scaling Comparison ($100\text{c}$ vs $1000\text{c}$)
When the network concurrency spikes tenfold to $1000\text{c}$, raw application behaviors drift dramatically. 

* **nginx Scaling**: nginx handles the stress test gracefully, dropping less than $15\%$ of its throughput between $100\text{c}$ and $1000\text{c}$ while keeping errors nearly non-existent ($< 501$ total errors).
* **apache Scaling**: While apache reports maintaining high raw throughput speeds, it yields an astronomical failure rate ($89\text{k}$ to $155\text{k}$ connection errors). It drops structural stability under high load.

![Throughput Degradation under Load](concurrency_load_comparison.png) 


## Learning Notes
This project documents the journey of understanding reverse proxies from first principles, including both application-level code and the underlying OS/network behavior that governs real-world performance.
