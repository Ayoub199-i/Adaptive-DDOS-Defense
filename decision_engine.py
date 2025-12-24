def decide(alerts):
    decision = {
        "attack_type": "normal",
        "action": "allow"
    }

    has_ip_alert = any("Suspicious IP" in a for a in alerts)
    has_volume_alert = any("High traffic" in a for a in alerts)

    if has_ip_alert and not has_volume_alert:
        decision["attack_type"] = "naive"
        decision["action"] = "block_ip"

    elif has_volume_alert and not has_ip_alert:
        decision["attack_type"] = "distributed"
        decision["action"] = "rate_limit"

    elif has_ip_alert and has_volume_alert:
        decision["attack_type"] = "hybrid"
        decision["action"] = "challenge_clients"

    return decision
