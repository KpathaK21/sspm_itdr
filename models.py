#defining data structures

class SaaSApp:
    def __init__(self, name, is_public, admin_count, last_config_check):
        self.name = name
        self.is_public = is_public
        self.admin_count = admin_count
        self.last_config_check = last_config_check

class userLogin:
    def __init__(self, username, country, login_time_hour, device):
        self.username = username
        self.country = country
        self.login_time_hour = login_time_hour
        self.device = device 
