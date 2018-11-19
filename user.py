user_db = []
from datetime import datetime

class User:
    def __init__(self):
        self.db = user_db  
        
    
    def create_user(self,user_id,status="logged out",login_time,logout_time):
        payload = {
            "user_id": len(self.db)+1
            "statue=s":status,
            "login_time":login_time,
            "last_logout":logout_time
        }
        self.db.append(payload)
        

    



    


