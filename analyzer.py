from collections import Counter

LOG_FILE = "logs/login.log"
THRESHOLD = 5

failed_ips = []

with open(LOG_FILE, "r") as file:
    for line in file:
        if "FAILED_LOGIN" in line:
            parts = line.split()
            for part in parts:
                if part.startswith("IP="):
                    ip = part.replace("IP=", "")
                    failed_ips.append(ip)

counts = Counter(failed_ips)

print("=== SOC BRUTE-FORCE DETECTION ===")

for ip, attempts in counts.items():
    print("Source IP:", ip)
    print("Failed attempts:", attempts)

    if attempts >= THRESHOLD:
        print("ALERT: Possible brute-force attack")
        print("Severity: HIGH")
    else:
        print("Status: Normal")

    print()

print("=== Analysis Complete ===")
