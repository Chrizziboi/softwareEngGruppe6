class admin:
    def __init__(self, adminID, adminname):
        self.adminID = int(adminID)
        self.adminname = str(adminname)

    def get_admin_info(self):
        return f"UserID: {self.adminID}, Username: {self.adminname}."

    def admin_login(self, login):
        login = True
        if login == True:
            print("Sucessfully logged in.")
        else:
            print("couldn't log in.")