def apply_mitigation(decision):
    action = decision["action"]

    if action == "block_ip":
        return "Applied IP blocking rule (simulated)"

    if action == "rate_limit":
        return "Enabled global rate limiting (simulated)"

    if action == "challenge_clients":
        return "Enabled CAPTCHA / challenge-response (simulated)"

    return "No mitigation needed"
