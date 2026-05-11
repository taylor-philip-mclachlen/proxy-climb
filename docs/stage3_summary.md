stage 3 proxy climb

the idea going into stage 3 is firewall, for added security. then golang tooling for more help with the logic/backend to help apache with all the packets from nginx. 

visual concept thusfar. 
-packet layer iptables(firewall)
--proxy layer Nginx (SSL, caching) 
---logic level go tooling (routing and packets) 
----backend level Apache (polising the packets) 

we will see how this plays out. and we will once again run the ./main
to get benchmarks. 

The event MPM is the correct choice for your architecture because:

worker threads are no longer blocked waiting on keepalive sockets
idle connections get offloaded
concurrency handling becomes dramatically better than prefork
memory efficiency improves under high connection counts

This was essential for surviving the 1000c tests.

smart server 3, should change to 5 or 8? 

Found typo on httpd.conf header -x

increased nginx worker connections to 8096 fot max celling 

potential bottleneck with prosy-set-header "";-> keep-alive;  NGINX Tweek..

stage 4 we will fine tune furthur. firewall and go next

thoughts on firewall: two options iptables / nftables 
nftables wins for scalibilty iptables for documentation and compatibility 
maybe iptables vs nftables benchmark later? 
