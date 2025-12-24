
from traffic_simulator import simulate_traffic
from detector import detect_ddos
from decision_engine import decide
from mitigation import apply_mitigation

def run(profile):
    traffic = simulate_traffic(profile=profile, duration=3)
    alerts = detect_ddos(traffic)
    decision = decide(alerts)
    mitigation = apply_mitigation(decision)

    print(f"\n=== {profile.upper()} ATTACK ===")

    for alert in alerts:
        print("-", alert)

    print("Decision:", decision)
    print("Mitigation:", mitigation)

if __name__ == "__main__":
    for profile in ["naive", "distributed"]:
        run(profile)
