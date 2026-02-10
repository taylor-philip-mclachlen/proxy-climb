## System Tuning & OS-Level Concepts

Understanding how your proxy performs requires knowledge of OS-level networking parameters. These settings directly impact connection handling and performance:

### `ulimit` - File Descriptor Limits

File descriptors are OS-level resources representing open files, sockets, and connections. Each connection through your proxy consumes file descriptors on both client and server sides.

**Check current limits:**
```bash
ulimit -n  # soft limit
ulimit -Hn # hard limit
```

**Why it matters for proxies:**
- Each incoming client connection = 1 FD
- Each outgoing backend connection = 1 FD
- Total FDs needed ≈ 2 × (concurrent connections) + overhead
- Default limits (often 1024) severely restrict proxy capacity

**Increase limits (temporary):**
```bash
ulimit -n 65536
```

**Increase limits (permanent):**
Edit `/etc/security/limits.conf`:
```
*  soft  nofile  65536
*  hard  nofile  65536
```

**Example:** With 1024 limit, your proxy can handle ~500 concurrent connections max.

### `backlog` - TCP Connection Queue

The backlog is the OS-level queue where incoming connections wait to be accepted by your proxy application.

**Check current TCP backlog:**
```bash
cat /proc/sys/net/ipv4/tcp_max_syn_backlog
cat /proc/sys/net/core/somaxconn
```

**Why it matters:**
- When your proxy can't accept connections fast enough, they queue here
- If the backlog fills, new connections are dropped
- Larger backlog = more tolerance for connection spikes

**Listen backlog in your proxy:**
- Go's `http.Server` uses `net.Listen()` which respects the backlog
- Configure at socket level (typically set in Go with proper socket options)

**Example scenarios:**
- Small backlog (128): Requests drop during traffic spikes
- Large backlog (1024+): Traffic spikes absorbed, requests queue but don't drop

### `somaxconn` - System-Wide Maximum Listen Queue

The maximum backlog value that any application can set. Acts as a system-wide ceiling for connection queuing.

**Check current value:**
```bash
cat /proc/sys/net/core/somaxconn
```

**Default:** Usually 128 (very low for modern servers)

**Increase system-wide (temporary):**
```bash
sudo sysctl -w net.core.somaxconn=4096
```

**Increase system-wide (permanent):**
Edit `/etc/sysctl.conf` or create `/etc/sysctl.d/99-custom.conf`:
```bash
net.core.somaxconn=4096
net.ipv4.tcp_max_syn_backlog=4096
net.ipv4.ip_local_port_range=1024 65535
```

Apply changes:
```bash
sudo sysctl -p
```

## How These Interact

1. **Connection arrives** → queued in OS backlog (limited by `somaxconn`)
2. **Your proxy accepts** → uses a file descriptor (limited by `ulimit`)
3. **Proxy connects to backend** → uses another file descriptor
4. **Connection closes** → file descriptor returned to pool

If any layer is too restrictive, you become the bottleneck.


