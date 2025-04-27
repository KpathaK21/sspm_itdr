# fake API + fake login generator

import random
from models import SaaSApp, userLogin

def get_apps_from_api():
    print("Pulling SaaS apps from simulated API...")

    return[
        SaaSApp("Salesforce", True, 7, 45),
        SaaSApp("Slack", False, 2, 10),
        SaaSApp("Zoom", True, 3, 90),
    ]

def simulate_random_login():

    username = ["alice", "bob", "charlie", "diana"]
    countries = ["USA", "Germany", "Brazil", "UK", "Russia"]
    devices = ["Laptopn", "Mobile Phone", "work PC", "Tablet"]

    return userLogin(
        username=random.choice(username),
        country=random.choice(countries),
        login_time_hour=random.randint(0,23),
        device=random.choice(devices)
    )
