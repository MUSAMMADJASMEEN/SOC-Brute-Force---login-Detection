from collections import Counter
from datetime import datetime

LOG_FILE = "logs/login.log"
ALERT_FILE = "logs/alerts.txt"
THRESHOLD = 5

failed_logins = []
successful_logins = []

# Read authentication logs
with open(LOG_FILE, "r") as file:
    for line in file:
        parts = line.split()

        if len(parts) < 5:
            continue

        timestamp_text = parts[0] + " " + parts[1]

        try:
            timestamp = datetime.strptime(timestamp_text, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue

        event_type = parts[2]

        username = ""
        ip = ""

        for part in parts:
            if part.startswith("username="):
                username = part.split("=", 1)[1]

            if part.startswith("ip="):
                ip = part.split("=", 1)[1]

        if event_type == "FAILED_LOGIN":
            failed_logins.append((timestamp, username, ip))

        elif event_type == "SUCCESS_LOGIN":
            successful_logins.append((timestamp, username, ip))


# Count failed attempts by source IP
failed_ips = [ip for _, _, ip in failed_logins]
ip_counts = Counter(failed_ips)

print("=== SOC BRUTE-FORCE DETECTION ===")

alerts = []

for ip, attempts in ip_counts.items():

    print("Source IP:", ip)
    print("Failed attempts:", attempts)

    if attempts >= THRESHOLD:

        # Find the last failed login from this IP
        ip_failed = [
            event for event in failed_logins
            if event[2] == ip
        ]

        last_failed = max(ip_failed, key=lambda x: x[0])

        # Check for a successful login after the failed attempts
        success_after_failure = [
            event for event in successful_logins
            if event[2] == ip and event[0] > last_failed[0]
        ]

        if success_after_failure:
            compromise_status = (
                "Successful login detected after failed attempts - "
                "possible account compromise."
            )
        else:
            compromise_status = (
                "No successful login detected after failed attempts."
            )

        alert = (
            "SOC SECURITY ALERT\n"
            "===================\n"
            "Alert ID: ALERT-001\n"
            "Type: Possible Brute-Force Attack\n"
            f"Source IP: {ip}\n"
            f"Failed Login Attempts: {attempts}\n"
            "Severity: HIGH\n"
            "Status: OPEN\n\n"
            f"Assessment: {compromise_status}\n\n"
            "Recommended SOC Actions:\n"
            "1. Investigate the source IP.\n"
            "2. Review surrounding authentication events.\n"
            "3. Check whether the target account may be compromised.\n"
            "4. Follow the organization's incident-response procedures.\n"
        )

        print(alert)
        alerts.append(alert)

    else:
        print("Status: Normal")

    print()


# Save alerts
with open(ALERT_FILE, "w") as file:
    if alerts:
        for alert in alerts:
            file.write(alert)
            file.write("\n")

        print("Alerts saved to:", ALERT_FILE)

    else:
        file.write("No brute-force activity detected.\n")
        print("No brute-force activity detected.")


print("=== Analysis Complete ===")
