omen 15-ax252nr: Starting Mini-Bench...

 Testing Server: 127.0.0.1:80
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: http://127.0.0.1:80
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ http://127.0.0.1:80
  2 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    53.59ms   72.05ms   1.06s    98.44%
    Req/Sec    10.76k   627.88    12.56k    88.38%
  211946 requests in 10.06s, 48.31MB read
Requests/sec:  21061.64
Transfer/sec:      4.80MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001617902s
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
    Latency    10.01ms    7.16ms  68.75ms   84.27%
    Req/Sec    21.89k     2.43k   30.55k    73.96%
  430016 requests in 10.05s, 91.45MB read
  Socket errors: connect 0, read 176093, write 0, timeout 0
Requests/sec:  42804.40
Transfer/sec:      9.10MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001382744s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 1000
--------------------------------
All tasks complete.

