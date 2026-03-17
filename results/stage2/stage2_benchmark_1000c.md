omen 15-ax252nr: Starting Mini-Bench...

 Testing Server: 127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: https://127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ https://127.0.0.1:443
  2 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    61.56ms  139.80ms   1.33s    94.62%
    Req/Sec    15.64k     5.42k   32.58k    85.06%
  274107 requests in 10.10s, 128.67MB read
  Non-2xx or 3xx responses: 605
Requests/sec:  27149.01
Transfer/sec:     12.74MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001277438s
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
    Latency    19.14ms   23.91ms 227.24ms   82.73%
    Req/Sec    21.82k     3.91k   34.88k    71.65%
  427855 requests in 10.06s, 85.28MB read
  Socket errors: connect 0, read 179572, write 0, timeout 0
Requests/sec:  42523.44
Transfer/sec:      8.48MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001468413s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 1000
--------------------------------
All tasks complete.

