#  SSPM + ITDR Security Monitor Dashboard

## Overview

This project monitors **SaaS security risks** and **identity-based threats** by scanning SaaS applications and login activities.  
Detected risks and suspicious behavior are **logged live** to a real-time dashboard running on `localhost:5050`.

It combines:
- **SSPM** (SaaS Security Posture Management): scanning app configurations for risks
- **ITDR** (Identity Threat Detection and Response): monitoring user logins for suspicious behavior
- **Real-time Dashboard**: displays detected events live in the browser

---

## Features

-  **Live Monitoring** of SaaS application risks and login threats
-  **Automated Detection** and **Alerting** via email
-  **Real-Time Dashboard** showing security events as they happen
-  **Simulated API and Logins** for testing the system
-  **Scalable foundation** for building a full security monitoring solution

---

## Project Structure

| Folder/File | Purpose |
|:---|:---|
| `main.py` | Main control loop for monitoring SaaS apps and logins |
| `utils.py` | Simulated SaaS app API and login event generator |
| `analyzer.py` | Analyzes app configurations and login behaviors |
| `remediation.py` | Suggests remediation actions |
| `alerter.py` | Sends email alerts when risks are detected |
| `dashboard.py` | Hosts the real-time event dashboard (Flask server) |
| `static/` | Frontend files (JavaScript for fetching live events) |
| `templates/` | HTML layout for dashboard view |

---

## How It Works

1. **Start Monitoring**:  
   Run `python3 main.py`.  
   The system begins scanning apps and monitoring login activities.

2. **Detect Risks and Threats**:  
   When a misconfiguration or suspicious login is found, the system:
   - Prints the risk in the terminal
   - Sends an email alert
   - Adds the event to the live dashboard

3. **View Live Dashboard**:  
   Open your browser and visit:  

http://localhost:5050

You will see live updates as new risks and events are detected.

---

## Installation

1. Clone this repository:
```bash
git clone git@github.com:KpathaK21/sspm_itdr.git
cd sspm_itdr


2. Install required Python packages:

pip install flask

3. Run the monitor:

python3 main.py
