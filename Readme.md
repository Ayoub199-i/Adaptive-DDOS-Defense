# Adaptive DDoS Defense System (Python)

##  Overview
Questo progetto implementa un **mini sistema di difesa DDoS adattivo**, sviluppato interamente in Python.
L’obiettivo è simulare il comportamento di un sistema di sicurezza difensivo (blue team), capace di:

- simulare traffico e attacchi DDoS
- rilevare anomalie
- prendere decisioni difensive
- applicare contromisure (simulate)

Il progetto è **safe-by-design**: non genera traffico reale né esegue attacchi veri.

---

---

##  Attack Profiles

Il sistema supporta diversi profili di attacco:

### Naive Attack
- singolo IP
- alto numero di richieste
- tipico di attacchi semplici o script kiddie

### Distributed Attack
- IP multipli
- alto traffico globale
- simula una botnet o DDoS distribuito

---

##  Detection Logic

Il detection engine genera alert basandosi su:

- **Requests Per Second (RPS)**  
  → identifica attacchi distribuiti ad alto volume

- **Requests per IP**  
  → identifica flood da singolo host

---

  Decision Engine

Gli alert vengono analizzati per classificare l’attacco e scegliere la risposta:

| Scenario | Attack Type | Action |
|--------|------------|--------|
| IP sospetto | Naive | block_ip |
| Alto traffico | Distributed | rate_limit |
| Entrambi | Hybrid | challenge_clients |

---

##  Mitigation

Le mitigazioni sono simulate

 Nessuna modifica reale a firewall o rete.

---

##  How to Run

```bash
python main.py





