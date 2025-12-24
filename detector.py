from collections import defaultdict

def detect_ddos(events, rps_threshold=10, ip_threshold=5):
    """
    events: lista di eventi (ip, timestamp)
    rps_threshold: soglia richieste/sec
    ip_threshold: soglia richieste per IP
    """
    alerts = []

    if not events:
        return alerts

    # calcolo RPS
    start = events[0]["timestamp"]
    end = events[-1]["timestamp"]
    duration = max(end - start, 1)

    rps = len(events) / duration

    if rps > rps_threshold:
        alerts.append(f"High traffic detected: {rps:.2f} req/sec")

    # conteggio per IP
    ip_counter = defaultdict(int)
    for e in events:
        ip_counter[e["ip"]] += 1

    for ip, count in ip_counter.items():
        if count > ip_threshold:
            alerts.append(f"Suspicious IP {ip}: {count} requests")

    return alerts
