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

- `logs/login.log` - Simulated authentication logs
- `analyzer.py` - Python detection script
- `alerts.txt` - Example SOC alerts
- `incident-report.md` - Investigation report
- `README.md` - Project documentation

## Detection Rule

If an IP address generates **5 or more failed login attempts**, the system creates a **HIGH severity** alert.

## Example Alert

```text
Possible Brute-Force Attack
Source IP: 192.168.1.50
Failed Attempts: 5
Severity: HIGH
