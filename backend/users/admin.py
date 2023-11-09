class admin:
    def __init__(self, adminID, adminname): #parameter password for a system that would use password
        self.adminID = int(adminID)
        self.adminname = str(adminname)
        #self.password = str(password)


    def get_admin_info(self):
        return f"AdminID: {self.adminID}, Username: {self.adminname}."

'''  def admin_login(self, password):
        if login == True:#alt; password == entered_password
            print("Sucessfully logged in.")
        else:
            print("couldn't log in.")
'''