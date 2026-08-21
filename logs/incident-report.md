# Incident Report — Possible Brute-Force Attack

## 1. Incident Summary

A series of failed login attempts was detected against the `admin` account.

The activity originated from the same source IP address and exceeded the configured detection threshold.

## 2. Detection

- **Alert:** Possible Brute-Force Attack
- **Severity:** High
- **Source IP:** 192.168.1.50
- **Target Account:** admin
- **Failed Attempts:** 5
- **Detection Threshold:** 5 failed attempts

## 3. Investigation

The authentication log was reviewed for repeated failed login attempts.

Five failed login attempts were observed from `192.168.1.50` within a short period.

The repeated attempts against the same account are consistent with possible password-guessing or brute-force activity.

The available simulated log data does not prove that the account was successfully compromised.

## 4. Indicators of Compromise

| Indicator | Value |
|---|---|
| Source IP | 192.168.1.50 |
| Username | admin |
| Event | FAILED_LOGIN |
| Failed Attempts | 5 |

## 5. Recommended Response

1. Review additional authentication logs.
2. Check whether a successful login occurred after the failed attempts.
3. Verify whether the activity was authorized.
4. Review the affected account for suspicious activity.
5. Follow the organization's approved incident-response process.
6. Consider additional protective controls if malicious activity is confirmed.

## 6. Conclusion

The activity triggered a high-severity alert because the number of failed login attempts reached the configured threshold.

Further investigation is required before confirming that the account was compromised.

## 7. Data Source

This project uses simulated authentication logs created for cybersecurity education and portfolio demonstration.
