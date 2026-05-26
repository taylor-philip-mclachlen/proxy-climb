FINAL 1000c COMPARISON (ALL STAGES)

nginx :443 (frontend path)
Stage	Req/sec	Avg Lat	Max Lat	Std Dev	Errors
Stage 1	14,818	103ms	1.10s	121ms	251
Stage 2	28,291	40ms	825ms	66ms	322
Stage 3.0	24,996	64ms	1.34s	143ms	501
Stage 3.5	24,996	64ms	1.34s	143ms	501

apache :8080 (backend)
Stage	Req/sec	Avg Lat	Max Lat	Std Dev	Errors
Stage 1	51,498	39ms	1.71s	73ms	89k
Stage 2	52,696	36ms	226ms	48ms	65k
Stage 3.0	39,199	15ms	230ms	17ms	155k
Stage 3.5	39,199	15ms	230ms	17ms	155k
