import time
import threading
from utils import get_apps_from_api, simulate_random_login
from analyzer import analyzer_app_config, analyze_login
from remediation import remediate_app, remediate_login
from alerter import send_email_alert
from dashboard import add_event, run_dashboard
from datetime import datetime
def main():



    print("\n Sarting SSPM + ITDR Security Monitor...\n")

    #starts dashboard in background
    threading.Thread(target=run_dashboard, daemon=True).start()


    while True:
        #scanning apps
        apps = get_apps_from_api()
        print("Scanning SaaS Apps (SSPM)...")
        for app in apps:
            risks = analyzer_app_config(app)
            if risks:
                print(f"Risks detected in {app.name}:")
                for risk in risks:
                    print(f"    {risk}")
                    send_email_alert(f"SSPM alert: {app.name}", risk)
                    
                actions = remediate_app(app)
                add_event(f"ITDR Threat: {risk}")
                if actions:
                    print("Remediation actions for {app.name}:")
                    for action in actions:
                        print(f"    {action}")
                    add_event(f"Remediation: {action}")

         # monitoring logins

        print("\n Monitoring logins (ITDR)...")
        login = simulate_random_login()
        print(f"login attempt: {login.username} from {login.country} at {login.login_time_hour}h using {login.device}")
        risks = analyze_login(login)
        if risks:
            print(f"Threats detected from {login.username:}")
            for risk in risks:
                print(f"    {risk}")
                send_email_alert(f"ITDR Alert: {login.username}", risk)
            action = remediate_login(login)
            add_event(f"SSPM Risk: {risk}")
            if actions:
                print(f"Remediation actions for for {login.username}:")
                for action in actions:
                    print(f"    {action}")
                add_event(f"Remediation: {action}")

        else:
            print("No suspicious login detected.")


        print("\n Waiting for next scan...\n")
        time.sleep(10)      #10 seconds between scans

if __name__ == "__main__":
    main()
