omen 15-ax252nr: Starting Mini-Bench...

 Testing Server: 127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: https://127.0.0.1:443
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ https://127.0.0.1:443
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   367.86us  401.45us  14.40ms   96.16%
    Req/Sec    14.74k     1.57k   17.07k    79.50%
  293384 requests in 10.01s, 137.66MB read
Requests/sec:  29323.41
Transfer/sec:     13.76MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001201979s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 10
--------------------------------

 Testing Server: 127.0.0.1:8080
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: http://127.0.0.1:8080
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ http://127.0.0.1:8080
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   179.61us   86.67us   1.59ms   82.45%
    Req/Sec    26.87k   786.41    28.38k    84.00%
  534546 requests in 10.00s, 106.55MB read
Requests/sec:  53453.08
Transfer/sec:     10.65MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001083495s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 10
--------------------------------
All tasks complete.

