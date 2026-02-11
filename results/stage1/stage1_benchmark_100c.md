omen 15-ax252nr: Starting Mini-Bench...                 19:18 [27/190]
                                                                      
 Testing Server: 127.0.0.1:80                                         
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                      
TARGET: http://127.0.0.1:80                                           
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                      
Running 10s test @ http://127.0.0.1:80                                
  2 threads and 100 connections                                       
  Thread Stats   Avg      Stdev     Max   +/- Stdev                   
    Latency    16.34ms   26.40ms 145.88ms   87.41%                    
    Req/Sec     7.68k     6.00k   17.63k    35.00%                    
  152712 requests in 10.03s, 61.02MB read                             
Requests/sec:  15232.68                                               
Transfer/sec:      6.09MB                                             
                                                                      
Starting 5-second cooldown...                                         
Step 1...                                                             
Step 2...                                                             
Step 3...                                                             
Step 4...                                                             
Step 5...                                                             
Total duration: 5.00161952s                                           
--------------------------------                                      
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 100
--------------------------------
 Testing Server: 127.0.0.1:8080                                [0/190]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TARGET: http://127.0.0.1:8080
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running 10s test @ http://127.0.0.1:8080
  2 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.89ms    3.38ms  28.44ms   82.08%
    Req/Sec    30.03k     1.05k   32.64k    72.50%
  597698 requests in 10.04s, 119.13MB read
Requests/sec:  59550.35
Transfer/sec:     11.87MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.00085826s
--------------------------------
Benchmark complete on Omen 15.
Nginx Workers: 4 | Connections: 100
--------------------------------
All tasks complete.

