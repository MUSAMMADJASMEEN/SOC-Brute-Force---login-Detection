from collections import Counter

LOG_FILE = "logs/login.log"
THRESHOLD = 5

failed_ips = []

with open(LOG_FILE, "r") as file:
    for line in file:
        if "FAILED_LOGIN" in line:
            parts = line.split()

            for part in parts:
                if part.startswith("ip="):
                    ip = part.split("=")[1]
                    failed_ips.append(ip)

ip_counts = Counter(failed_ips)

print("=== SOC BRUTE-FORCE DETECTION ===")

alerts_found = False

for ip, count in ip_counts.items():
    if count >= THRESHOLD:
        alerts_found = True

        print("\nSECURITY ALERT")
        print("----------------")
        print("Possible brute-force attack detected")
        print("Source IP:", ip)
        print("Failed attempts:", count)
        print("Severity: HIGH")

if not alerts_found:
    print("\nNo brute-force activity detected.")
