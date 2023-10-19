class admin:
    def __init__(self, adminID, adminname): #parameter password for a system that would use password
        self.adminID = int(adminID)
        self.adminname = str(adminname)
        #self.login = bool(login)


    def get_admin_info(self):
        return f"UserID: {self.adminID}, Username: {self.adminname}."

'''  def admin_login(self, login):
        if login == True:#alt; password == entered_password
            print("Sucessfully logged in.")
        else:
            print("couldn't log in.")'''