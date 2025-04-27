def remediate_app(app):

    actions = []

    if app.is_public:
        app.is_public = False
        actions.append("Made app private")
    if app.admin_count > 5:
        app.admin_count = 3 
        actions.append("reduced admin count")
    if app.last_config_check > 30:
        app.last_config_check = 0
        actions.append("updated config check date")

    return actions

def remediate_login(login):

    actions = []

    if login.country not in ["USA", "Canada", "UK"]:
        actions.append(f"Locked user {login.username} due to risky country login.")
    if login.login_time_hour < 6 or login.login_time_hour > 22:
        actions.append(f"flagged user {login.username} for abnormal login time.")
    if login.device not in ["laptop", "work PC"]:
        actions.append(f"flagged user {login.username} for risky device.")

    return actions
