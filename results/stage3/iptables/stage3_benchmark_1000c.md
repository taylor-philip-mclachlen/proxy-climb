omen 15-ax252nr: Starting Mini-Bench...

 Testing Server: 127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: https://127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ https://127.0.0.1:443
  2 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    64.67ms  143.03ms   1.34s    94.49%
    Req/Sec    14.45k     4.64k   29.36k    84.39%
  251307 requests in 10.05s, 117.96MB read
  Non-2xx or 3xx responses: 501
Requests/sec:  24996.98
Transfer/sec:     11.73MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.002034145s
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
    Latency    15.56ms   17.69ms 230.29ms   85.94%
    Req/Sec    20.01k     2.01k   25.65k    68.56%
  395108 requests in 10.08s, 78.75MB read
  Socket errors: connect 0, read 155446, write 0, timeout 0
Requests/sec:  39199.08
Transfer/sec:      7.81MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001397297s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 1000
--------------------------------
All tasks complete.

