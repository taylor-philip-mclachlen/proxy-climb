omen 15-ax252nr: Starting Mini-Bench...

 Testing Server: 127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: https://127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ https://127.0.0.1:443
  2 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    72.42ms  170.53ms   1.52s    94.15%
    Req/Sec    14.15k     4.55k   26.73k    85.23%
  250332 requests in 10.08s, 117.50MB read
  Non-2xx or 3xx responses: 528
Requests/sec:  24827.06
Transfer/sec:     11.65MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001515636s
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
    Latency    25.67ms   36.69ms 231.72ms   85.62%
    Req/Sec    21.48k     4.31k   32.02k    71.13%
  420417 requests in 10.05s, 83.80MB read
  Socket errors: connect 0, read 134776, write 0, timeout 0
Requests/sec:  41830.62
Transfer/sec:      8.34MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.00170174s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 1000
--------------------------------
All tasks complete.

