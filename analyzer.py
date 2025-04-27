def analyzer_app_config(app):
    risks = []

    if app.is_public:
        risks.append("App is publicly accessible.")
    if app.admin_count > 5:
        risks.append(f"Too many admins: {app.admin_count}")
    if app.last_config_check > 30:
        risks.append(f"config not checked in {app.last_config_check} days")

    return risks

def analyze_login(login):
    risks = []

    if login.country not in ["USA", "Canada", "UK"]:
        risks.append(f"login from unsual country: {login.country}")
    if login.login_time_hour < 6 or login.login_time_hour > 22:
        risks.append(f"login at unsual ime: {login.login_time_hour}h")
    if login.device not in ["Laptop", "Work PC"]:
        risks.append(f"login from unknown device: {login.device}")

    return risks
