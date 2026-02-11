omen 15-ax252nr: Starting Mini-Bench...                                
                                                                       
 Testing Server: 127.0.0.1:80                                          
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                       
TARGET: http://127.0.0.1:80                                            
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                       
Running 10s test @ http://127.0.0.1:80                                 
  2 threads and 1000 connections                                       
  Thread Stats   Avg      Stdev     Max   +/- Stdev                    
    Latency   103.42ms  121.80ms   1.10s    85.10%                     
    Req/Sec     7.55k     5.43k   14.03k    47.98%                     
  148840 requests in 10.04s, 59.50MB read                              
  Non-2xx or 3xx responses: 251                                        
Requests/sec:  14818.80                                                
Transfer/sec:      5.92MB                                              
                                                                       
Starting 5-second cooldown...                                          
Step 1...                                                              
Step 2...                                                              
Step 3...                                                              
Step 4...                                                              
Step 5...                                                              
Total duration: 5.002226394s                                           
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
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    39.13ms   73.11ms   1.71s    90.30%
    Req/Sec    26.28k     4.93k   38.77k    61.11%
  519415 requests in 10.09s, 103.53MB read
  Socket errors: connect 0, read 89314, write 0, timeout 0
Requests/sec:  51498.14
Transfer/sec:     10.26MB

Starting 5-second cooldown...
Step 1...
Step 2...
Step 3...
Step 4...
Step 5...
Total duration: 5.00145269s
--------------------------------
Benchmark complete on Omen 15.Nginx Workers: 4 | Connections: 1000                                   
--------------------------------                                       
         
