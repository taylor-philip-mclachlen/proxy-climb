Stage 2 Summary: Proxy Hardening & SSL Implementation
Overview

While Stages 0 and 1 established the functional baseline, Stage 2 focused on security hardening, transition to HTTPS, and performance optimization of the proxy layer.
Core Security Implementation

    SSL/TLS Termination: * Transitioned from port :80 to :443.

        Implemented SSL Termination at the Nginx level. This ensures data is encrypted in transit while allowing Nginx to handle the heavy lifting of decryption before passing traffic to the Apache backend.

        Benefits:

            Encryption: Protects data from eavesdropping.

            Authentication: Validates server identity via SSL certificates.

            Integrity (MACs): Uses Message Authentication Codes to ensure data isn't tampered with during transit.

    Certificate Management:

        Generated a 2048-bit RSA self-signed certificate using OpenSSL.

        Note: Encountered sync issues with existing keys; resolved by overwriting/verifying paths in /etc/ssl/.

    Automatic Redirection:

        Configured a global :80 to :443 redirect to prevent users from accessing the site over an unencrypted connection.

Configuration Hardening
Apache (httpd) Updates:

    Timeout 30 & KeepaliveTimeout 5: Optimized to reduce the duration a process remains "hung" on an idle connection, freeing up resources faster.

    TraceEnable Off: Disabled TRACE requests to mitigate Cross-Site Tracking (XST) risks.

Nginx Updates:

    HSTS (Strict-Transport-Security): Enforced HTTPS at the browser level for 1 year.

    Buffer Overflow Protection: Adjusted client_body_buffer_size and header limits to mitigate memory exhaustion attacks.

    Cipher Strength: Enabled ssl_prefer_server_ciphers to force the use of the server's strong cipher suite.

    Curve Optimization: Utilized ssl_ecdh_curve secp384r1. This optimizes the Elliptic Curve Diffie-Hellman (ECDH) key exchange, providing high security with better computational efficiency than standard RSA exchanges.

    HTTP/2 Transition: Updated to Nginx 1.25.x+ syntax (http2 on;) to improve resource multiplexing and load speeds.

Benchmark & Versioning

    Updated the Go benchmark tool to support https:// protocol and handle port 443 targets.

    Verified the stack on Nginx 1.25.5 (latest mainline features).

    Next Step: Execute high-concurrency benchmarks at 10c, 100c, and 1000c to analyze the "SSL Tax" on the Omen 15 hardware.
