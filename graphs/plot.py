import matplotlib.pyplot as plt
import numpy as np

# --- DATA CONFIGURATION ---
stages_100c = ['Stage 0', 'Stage 1', 'Stage 2', 'Stage 3.0', 'Stage 3.5']
nginx_req_100c = [22768.83, 15232.68, 34188.59, 30523.55, 30267.98]
apache_req_100c = [58475.14, 59550.35, 58774.80, 50879.68, 52369.11]
nginx_lat_100c = [4.58, 16.34, 3.32, 3.75, 3.90]
apache_lat_100c = [3.24, 2.89, 2.98, 3.08, 2.99]
nginx_tx_100c = [5.19, 6.09, 16.04, 14.32, 14.20]
apache_tx_100c = [12.45, 11.87, 11.71, 10.14, 10.44]

stages_1000c = ['Stage 1', 'Stage 2', 'Stage 3.0', 'Stage 3.5']
nginx_req_1000c = [14818, 28291, 24996, 24996]
apache_req_1000c = [51498, 52696, 39199, 39199]
nginx_lat_1000c = [103, 40, 64, 64]
apache_lat_1000c = [39, 36, 15, 15]
nginx_err_1000c = [251, 322, 501, 501]
apache_err_1000c = [89000, 65000, 155000, 155000]

width = 0.35

# ==========================================
# CHART 1: 100c PERFORMANCE DASHBOARD
# ==========================================
x_100c = np.arange(len(stages_100c))
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Throughput
rects1 = axs[0].bar(x_100c - width/2, nginx_req_100c, width, label='nginx', color='#2ecc71')
rects2 = axs[0].bar(x_100c + width/2, apache_req_100c, width, label='apache', color='#e74c3c')
axs[0].set_ylabel('Requests / Second')
axs[0].set_title('Throughput (Higher is Better)')
axs[0].set_xticks(x_100c)
axs[0].set_xticklabels(stages_100c)
axs[0].legend()
axs[0].grid(axis='y', linestyle='--', alpha=0.5)
axs[0].bar_label(rects1, padding=3, fmt='%.0f', fontsize=8)
axs[0].bar_label(rects2, padding=3, fmt='%.0f', fontsize=8)

# Latency
rects1 = axs[1].bar(x_100c - width/2, nginx_lat_100c, width, label='nginx', color='#2ecc71')
rects2 = axs[1].bar(x_100c + width/2, apache_lat_100c, width, label='apache', color='#e74c3c')
axs[1].set_ylabel('Avg Latency (ms)')
axs[1].set_title('Average Latency (Lower is Better)')
axs[1].set_xticks(x_100c)
axs[1].set_xticklabels(stages_100c)
axs[1].legend()
axs[1].grid(axis='y', linestyle='--', alpha=0.5)
axs[1].bar_label(rects1, padding=3, fmt='%.2fms', fontsize=8)
axs[1].bar_label(rects2, padding=3, fmt='%.2fms', fontsize=8)

# Transfer Rate
rects1 = axs[2].bar(x_100c - width/2, nginx_tx_100c, width, label='nginx', color='#2ecc71')
rects2 = axs[2].bar(x_100c + width/2, apache_tx_100c, width, label='apache', color='#e74c3c')
axs[2].set_ylabel('Transfer Rate (MB/s)')
axs[2].set_title('Data Transfer (Higher is Better)')
axs[2].set_xticks(x_100c)
axs[2].set_xticklabels(stages_100c)
axs[2].legend()
axs[2].grid(axis='y', linestyle='--', alpha=0.5)
axs[2].bar_label(rects1, padding=3, fmt='%.2f MB/s', fontsize=8)
axs[2].bar_label(rects2, padding=3, fmt='%.2f MB/s', fontsize=8)

plt.suptitle('Reverse Proxy Benchmark: nginx vs apache (100 Concurrent Connections)', fontsize=14, weight='bold', y=1.02)
plt.tight_layout()
plt.savefig('benchmark_100c_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()


# ==========================================
# CHART 2: CONCURRENCY COMPARISON (100c vs 1000c)
# ==========================================
x_comp = np.arange(len(stages_1000c))
nginx_req_100c_sub = nginx_req_100c[1:] # Skip Stage 0 for a clean comparison
apache_req_100c_sub = apache_req_100c[1:]

fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Nginx Comparison
rects1 = axs[0].bar(x_comp - width/2, nginx_req_100c_sub, width, label='100c', color='#a8e6cf')
rects2 = axs[0].bar(x_comp + width/2, nginx_req_1000c, width, label='1000c', color='#3d84a8')
axs[0].set_ylabel('Requests / Second')
axs[0].set_title('nginx Throughput by Concurrency Level')
axs[0].set_xticks(x_comp)
axs[0].set_xticklabels(stages_1000c)
axs[0].legend()
axs[0].grid(axis='y', linestyle='--', alpha=0.5)
axs[0].bar_label(rects1, padding=3, fmt='%.0f', fontsize=8)
axs[0].bar_label(rects2, padding=3, fmt='%.0f', fontsize=8)

# Apache Comparison
rects1 = axs[1].bar(x_comp - width/2, apache_req_100c_sub, width, label='100c', color='#ffaaa6')
rects2 = axs[1].bar(x_comp + width/2, apache_req_1000c, width, label='1000c', color='#ff8b94')
axs[1].set_ylabel('Requests / Second')
axs[1].set_title('apache Throughput by Concurrency Level')
axs[1].set_xticks(x_comp)
axs[1].set_xticklabels(stages_1000c)
axs[1].legend()
axs[1].grid(axis='y', linestyle='--', alpha=0.5)
axs[1].bar_label(rects1, padding=3, fmt='%.0f', fontsize=8)
axs[1].bar_label(rects2, padding=3, fmt='%.0f', fontsize=8)

plt.suptitle('Throughput Degradation under Load (100c vs 1000c)', fontsize=14, weight='bold', y=1.02)
plt.tight_layout()
plt.savefig('concurrency_load_comparison.png', dpi=300, bbox_inches='tight')
plt.close()


# ==========================================
# CHART 3: ORIGINAL 1000c DASHBOARD WITH LOG ERRORS
# ==========================================
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Throughput
rects1 = axs[0].bar(x_comp - width/2, nginx_req_1000c, width, label='nginx (:443)', color='#2ecc71')
rects2 = axs[0].bar(x_comp + width/2, apache_req_1000c, width, label='apache (:8080)', color='#e74c3c')
axs[0].set_ylabel('Requests / Second')
axs[0].set_title('Throughput (Higher is Better)')
axs[0].set_xticks(x_comp)
axs[0].set_xticklabels(stages_1000c)
axs[0].legend()
axs[0].grid(axis='y', linestyle='--', alpha=0.5)
axs[0].bar_label(rects1, padding=3, fmt='%d', fontsize=9)
axs[0].bar_label(rects2, padding=3, fmt='%d', fontsize=9)

# Latency
rects1 = axs[1].bar(x_comp - width/2, nginx_lat_1000c, width, label='nginx (:443)', color='#2ecc71')
rects2 = axs[1].bar(x_comp + width/2, apache_lat_1000c, width, label='apache (:8080)', color='#e74c3c')
axs[1].set_ylabel('Average Latency (ms)')
axs[1].set_title('Average Latency (Lower is Better)')
axs[1].set_xticks(x_comp)
axs[1].set_xticklabels(stages_1000c)
axs[1].legend()
axs[1].grid(axis='y', linestyle='--', alpha=0.5)
axs[1].bar_label(rects1, padding=3, fmt='%dms', fontsize=9)
axs[1].bar_label(rects2, padding=3, fmt='%dms', fontsize=9)

# Errors
rects1 = axs[2].bar(x_comp - width/2, nginx_err_1000c, width, label='nginx (:443)', color='#2ecc71')
rects2 = axs[2].bar(x_comp + width/2, apache_err_1000c, width, label='apache (:8080)', color='#e74c3c')
axs[2].set_ylabel('Error Count (Log Scale)')
axs[2].set_title('Total Errors (Lower is Better)')
axs[2].set_xticks(x_comp)
axs[2].set_xticklabels(stages_1000c)
axs[2].set_yscale('log')
axs[2].legend()
axs[2].grid(axis='y', linestyle='--', alpha=0.5)

for rect in rects1:
    height = rect.get_height()
    axs[2].annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)
for rect in rects2:
    height = rect.get_height()
    label = f'{height/1000:.0f}k' if height >= 1000 else f'{height}'
    axs[2].annotate(label, xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

plt.suptitle('Reverse Proxy Benchmark: nginx vs apache (1000 Concurrent Connections)', fontsize=14, weight='bold', y=1.02)
plt.tight_layout()
plt.savefig('benchmark_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("All 3 benchmark images generated successfully!")
