omen 15-ax252nr: Starting Mini-Bench...

 Testing Server: 127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: https://127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ https://127.0.0.1:443
  2 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.90ms    5.95ms 121.96ms   97.51%
    Req/Sec    15.43k     2.32k   17.99k    92.93%
  305125 requests in 10.08s, 143.17MB read
Requests/sec:  30267.98
Transfer/sec:     14.20MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001325992s
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
    Latency     2.99ms    3.41ms  30.17ms   82.14%
    Req/Sec    26.40k     1.42k   29.83k    77.50%
  525296 requests in 10.03s, 104.70MB read
Requests/sec:  52369.11
Transfer/sec:     10.44MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001777796s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 100
--------------------------------
All tasks complete.

