import random
import time

ATTACK_PROFILES = {
    "naive": {
        "distributed": False,
        "rate": 8
    },
    "distributed": {
        "distributed": True,
        "rate": 15
    }
}


def random_ip(distributed):
    if distributed:
        return f"10.0.{random.randint(0,5)}.{random.randint(1,254)}"
    return "10.0.0.10"

def generate_event(distributed):
    return {
        "ip": random_ip(distributed),
        "timestamp": time.time()
    }

def simulate_traffic(profile="naive", duration=3):
    if profile not in ATTACK_PROFILES:
        raise ValueError("Unknown attack profile")

    config = ATTACK_PROFILES[profile]
    distributed = config["distributed"]
    rate = config["rate"]

    events = []

    for _ in range(rate * duration):
        events.append(generate_event(distributed))
        time.sleep(1 / rate)

    return events

