omen 15-ax252nr: Starting Mini-Bench...

 Testing Server: 127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: https://127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ https://127.0.0.1:443
  2 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.75ms    5.00ms  93.14ms   95.97%
    Req/Sec    15.58k     3.97k   21.40k    68.37%
  305802 requests in 10.02s, 143.48MB read
Requests/sec:  30523.55
Transfer/sec:     14.32MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001894055s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 100
--------------------------------

 Testing Server: 127.0.0.1:8080
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: http://127.0.0.1:8080
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ http://127.0.0.1:8080
  2 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.08ms    3.50ms  30.49ms   82.15%
    Req/Sec    25.70k     2.70k   30.59k    69.50%
  511291 requests in 10.05s, 101.91MB read
Requests/sec:  50879.68
Transfer/sec:     10.14MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.00086295s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 100
--------------------------------
All tasks complete.

