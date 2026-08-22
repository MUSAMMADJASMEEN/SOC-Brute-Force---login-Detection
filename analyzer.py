from collections import Counter

LOG_FILE = "logs/login.log"
ALERT_FILE = "logs/alerts.log"
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
alerts = []

for ip, attempts in ip_counts.items():

    print("Source IP:", ip)
    print("Failed attempts:", attempts)

    if attempts >= THRESHOLD:
        alerts_found = True

        alert = (
            "SECURITY ALERT\n"
            "----------------\n"
            f"Possible brute-force attack detected\n"
            f"Source IP: {ip}\n"
            f"Failed attempts: {attempts}\n"
            "Severity: HIGH\n"
        )

        print(alert)
        alerts.append(alert)

    else:
        print("Status: Normal")

    print()

if alerts_found:
    with open(ALERT_FILE, "a") as file:
        for alert in alerts:
            file.write(alert)
            file.write("\n")

    print("Alerts saved to:", ALERT_FILE)

else:
    print("No brute-force activity detected.")

print("=== Analysis Complete ===")
