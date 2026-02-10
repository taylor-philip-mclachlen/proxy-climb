./main
omen 15-ax252nr: Starting Mini-Bench...

 Testing Server: 127.0.0.1:80
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: http://127.0.0.1:80
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ http://127.0.0.1:80
  2 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.58ms    3.26ms  77.37ms   96.57%
    Req/Sec    11.47k     1.27k   13.26k    95.00%
  228174 requests in 10.02s, 52.01MB read
Requests/sec:  22768.83
Transfer/sec:      5.19MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.001020156s
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
    Latency     3.24ms    4.00ms  39.43ms   82.94%
    Req/Sec    29.55k     1.40k   33.61k    68.50%
  588106 requests in 10.06s, 125.18MB read
  Socket errors: connect 0, read 22, write 0, timeout 0
Requests/sec:  58475.14
Transfer/sec:     12.45MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.00122029s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 100
--------------------------------
All tasks complete.

