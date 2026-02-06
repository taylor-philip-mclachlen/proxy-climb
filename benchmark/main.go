package main

import (
	"fmt"
	"net"
	"os/exec"
	"time"
)

// --- 1. THE DIRECTOR ---
func main() {
	fmt.Println("omen 15-ax252nr: Starting Mini-Bench...")

	targets := []string{
		"127.0.0.1:80",
		"127.0.0.1:8080",
	}
	for _, addr := range targets {
		conn, err := net.DialTimeout("tcp", addr, 1*time.Second)
		if err != nil {
			fmt.Printf(" %s is unreachable: %v\n", addr, err)
			continue
		}
		conn.Close()
		fmt.Printf("\n Testing Server: %s\n", addr)

		// Task A: Run the external tool
		runBenchmark("http://" + addr)

		// Task B: Run the performance timer
		runCooldown(5)
	}

	fmt.Println("All tasks complete.")
}

// --- 2. THE BENCHMARK EXPERT ---
func runBenchmark(url string) {
	// Note: We removed the "./" because wrk is now in your /usr/local/bin
	cmd := exec.Command("wrk", "-t2", "-c100", "-d10s", url)
	output, _ := cmd.CombinedOutput()

	fmt.Println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	fmt.Printf("TARGET: %s\n", url)
	fmt.Println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	fmt.Printf("%s\n", output)
}

// --- 3. THE TIMER EXPERT ---
func runCooldown(totalSeconds int) {
	fmt.Printf("Starting %d-second cooldown...\n", totalSeconds)
	start := time.Now()

	for i := 1; i <= totalSeconds; i++ {
		fmt.Printf("Step %d...\n", i)
		time.Sleep(1 * time.Second)
	}

	elapsed := time.Since(start)
	fmt.Printf("Total duration: %v\n", elapsed)
	// Add this before the "All tasks complete" line

	fmt.Println("--------------------------------")
	fmt.Printf("Benchmark complete on Omen 15.\n")
	fmt.Printf("Nginx Workers: 4 | Connections: 100\n")
	fmt.Println("--------------------------------")

}
