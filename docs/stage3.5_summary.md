Iptables has been tested and somewhat optimized for the next more openended and possibly complex phase of the proxy. 

the concept is to build some go tooling to support the nginx httpd handshake. 

im taking a pragmatic perspective as i think is required when writting code, in my very limited expertise. im looking at this from a memory managment and concurrency point of view. 

this is where my exploration of golang and embedded C is gonig to prove its worth. 

currently as of stage 3.0 we have nginx:443 talking directly to apache:8080, the plan is to build a bff (backend for frontend). i think this will bridge the differnt natures of teh high concurrency of nginx and the more porcess heavy httpd. 

the main idea is to target better results on our 100c result, but our 1000c celing is goign to give us a good idea for the possibility of goroutunes and better memory managment. 



-------
Stage 3.5 Notes & Corrections
1. The "Handshake" Issue
Your Thought: Use Go to help the 443 → 8080 handshake.

Correction: Technically, the "Handshake" (TLS) is finished at Nginx. What Go is actually helping with is Connection State. Apache likes to keep threads open (expensive); Go can "multiplex" (cheap). Go acts as a translator between Nginx’s fast-paced "event" world and Apache’s slower "process" world.

2. Routing Routine (The Mid-Layer)
Your Thought: Create a routing routine to assist Apache.

Correction: This is exactly what Go’s ServeMux and Goroutines are for. Think of the Go layer as a "Smart Buffer."

Nginx is the high-speed lobby.

Go is the organized concierge desk.

Apache is the heavy-duty kitchen.

If the kitchen (Apache) is backed up, the concierge (Go) holds the tickets in memory without bothering the kitchen until a stove is free.

3. Learning C and Go (Embedded Mindset)
Your Thought: Using Go as a step-by-step learning tool for system abstractions.

Insight: Since you want to learn C for embedded systems, focus on Memory Alignment and Buffer Sizes in Go. Even though Go handles memory for you, understanding how it copies bytes from a "Request" to a "Response" is the bridge to C's memcpy() and manual pointer arithmetic.

🗺 Where to go from here (Next Session)
When you pick this back up, your goal is to move from Architecture to Code Implementation. Here is your 3-step roadmap:

Step 1: The "Proxy Pass" Plumbing
You need to change your stack's flow. Instead of Nginx → Apache, you will configure:

Nginx: Listen on :443, proxy to :8081 (Go).

Go: Listen on :8081, proxy to :8080 (Apache).

Goal: Prove that the traffic still flows through all three layers.

Step 2: The Go "Telemetry" Tool
Instead of just passing traffic, write 5 lines of Go code to log the latency of Apache.

Why? This gives you a "Measurable Abstraction." You will see exactly how many milliseconds Apache takes to respond versus how long Nginx thinks the whole trip takes.

Step 3: Identify the "Context Switch"
In your next documentation, try to track the CPU usage per process.

Nginx (C-based) will have low CPU but high context switches.

Go will show how its "Scheduler" handles those 100 connections.

C/Embedded Link: This is where you learn about the Scheduler. In C/Embedded, you often have to write your own simple scheduler; in Go, you get to watch one of the best in the world handle your traffic.

🏁 Summary for your Git Abstract
Stage 3.5 Goal: Decouple connection management from request execution. Introduce a Golang mid-layer to manage upstream persistence to Apache, reducing backend socket churn and providing a programmable logic layer for future request routing.

Take the break—system architecture is mentally taxing. When you're back, we can look at the specific Go code to bridge those ports.

One quick question to leave you with: When we start the Go layer, do you want to focus on "Standard Library" Go (using only what comes in the box) or "High-Performance" Go (using specialized libraries)? Standard Library is usually better for learning the fundamentals of C-style networking.

The Stage 3.5 "Hybrid" Architecture
In this setup, your stack looks like this:

Nginx (Frontend)

Go BFF (Logic/Routing)

C Logger (Sidecar utility via Unix Socket or UDP)

Apache (Backend execution) 
