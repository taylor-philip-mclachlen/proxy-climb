omen 15-ax252nr: Starting Mini-Bench...

 Testing Server: 127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: https://127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ https://127.0.0.1:443
  2 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    40.25ms   66.36ms 825.51ms   96.11%
    Req/Sec    16.35k     4.64k   28.02k    84.97%
  284005 requests in 10.04s, 133.29MB read
  Non-2xx or 3xx responses: 322
Requests/sec:  28291.80
Transfer/sec:     13.28MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001309882s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 1000
--------------------------------

 Testing Server: 127.0.0.1:8080
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: http://127.0.0.1:8080
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ http://127.0.0.1:8080
  2 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    36.92ms   48.15ms 226.48ms   80.39%
    Req/Sec    27.09k     4.39k   37.53k    62.76%
  530788 requests in 10.07s, 105.80MB read
  Socket errors: connect 0, read 65480, write 0, timeout 0
Requests/sec:  52696.14
Transfer/sec:     10.50MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001117314s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 1000
--------------------------------
All tasks complete.

