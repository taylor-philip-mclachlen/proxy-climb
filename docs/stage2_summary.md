stage 2 summary: 

stage 1 and 0 set up a good baseline for whats to come. stage 2 will focus on hardening the security of the proxy. 
heres the starting idea 

finalize security headers.
set up https. :80 -> :443 
ssl/tls  certification.
run benchmark, 10c 100c and 1000c 
---

firstly lets look at the benifits off https vs http. and why ssl certification is important. 
firstly encryption, http dose not encrypt the data. that also means that the data the server recieves is encrypted so this is where nginx will have to do the "ssl termination". 
the second big benifit is the autentication of ssl and a legitimate site will have a authentic certificate so the site user know that this is your server and not a fake. 
also MAC's "message authentication codes" which stops data in transfer from being altered. 


command for openssl key:sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout /etc/ssl/private/nginx-selfsigned.key \
-out /etc/ssl/certs/nginx-selfsigned.crt \
-subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=localhost"

i had already created these keys so i ran into the issue of them not 
sycing because they already existed. 

ok so ssl cert is working. because i use openssl the browser dosenot like that we self certified. 

reguardless we now just add some new headers to nginx and httpd to finalize stage 2. 

httpd new headers: 

-Timeout 30&& KeepaliveTimeout 5 #reduces the tie httpd is hungup
-TraceEnable off # reduce attack suraface for cross site tracking

nginx header:
-ssl certification / https 
-Strict-Transport-Security #this stops nginx from useing http
-Buffer overflow #reduces surface for memory exhastion attack
-ssl session ticketing #
-ssl_prefer_server_ciphers on; #forces stronger cipher suits
-enabled http2 which should improve reasource loading times  
-ssl stapling should impove the handshake time 
-changed the ssl_ciphers to ssl_ecdh_curve which from what i read is a cipher algorith that is more efficient then using all the differnt key exchange, authenticate, e.t.c 

had some difficulty with http2. turns out the syntax is: 
http2 on;

well moving on i cleaned up the nginx.conf. and lastly im adding a
:80 redirect so you cant get stuck on http connection.

had to alter the benchmark. runBenchmark section was getting 404s because of the change to :443. 


this is the end of stage 2. we hardened the server. moved to ssl cert443 for nginx. added some security headers and cleaned up the 
.conf for both nginx & httpd. also uodated to nginx 1.29.5

now we add the bench marks 10c - 100c - 1000c and start stage 3


