# SOC Brute-Force Login Detection

## Project Overview

This is a personal SOC Analyst project that detects possible brute-force login attacks by analyzing simulated authentication logs.

The project demonstrates log analysis, detection rules, alert generation, and incident reporting.

## Skills Demonstrated

- Python
- Log Analysis
- Brute-Force Detection
- Security Alerts
- Incident Reporting
- SOC Investigation

## Project Structure

- `logs/login.log` -  Authentication log data
- `analyzer.py` - Python detection script
- `logs/alerts.txt` - Generated SOC security alerts
- `logs/incident-report.md` - Investigation report
- `README.md` - Project documentation

## Detection Rule

If an IP address generates **5 or more failed login attempts**, the system creates a **HIGH severity** alert.

## Example Alert

```text
Possible Brute-Force Attack
Source IP: 192.168.1.50
Failed Attempts: 5
```
## Detection Example

The analyzer detects repeated failed login attempts from the same source IP address.

### Detection Details

- Source IP: `192.168.1.50`
- Target Account: `admin`
- Failed Login Attempts: `5`
- Detection Threshold: `5`
- Alert Type: Possible Brute-Force Attack
- Severity: HIGH
- Status: OPEN

## Investigation Finding

Five failed login attempts from `192.168.1.50` targeting the `admin` account were followed by a successful login from the same source IP at `10:15:20`, approximately 7 seconds after the final failed attempt.

This pattern increases suspicion of possible account compromise, but the simulated logs alone do not confirm malicious activity.
### SOC Analyst Response

1. Investigate the source IP address.
2. Review surrounding authentication events.
3. Check whether a successful login occurred after the failed attempts.
4. Determine whether the target account may be compromised.
5. Follow the organization's incident-response procedures.

### Automation

GitHub Actions runs the analyzer and saves the generated security alerts as a workflow artifact.

Detection flow:

`Authentication Logs → Python Analyzer → Detection Rule → Security Alert → GitHub Actions Artifact`

## Sample Detection Result

- **Alert ID:** ALERT-001
- **Alert Type:** Possible Brute-Force Attack
- **Source IP:** `192.168.1.50`
- **Target Account:** `admin`
- **Failed Attempts:** 5
- **Severity:** HIGH
- **Status:** OPEN

### SOC Assessment

Five failed login attempts were detected from the same source IP, followed by a successful login approximately 7 seconds after the final failure. This pattern is suspicious and may indicate possible account compromise.

The simulated log data does not independently confirm malicious activity.

### Recommended SOC Actions

1. Investigate the source IP.
2. Review surrounding authentication logs.
3. Verify whether the successful login was authorized.
4. Review the `admin` account for suspicious activity.

> This project uses simulated authentication data for cybersecurity education and portfolio demonstration.
