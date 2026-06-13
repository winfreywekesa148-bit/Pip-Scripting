#import 
from datetime import datetime

log_data = ["User logged in", "User updated profile", "Report exported"]

#log in
def __init__ (self, username, password):
    self.username = username
    self.password = password

def authenticate():
    username = input("Enter username: ")
    password = int(input("Enter password: "))

filename = (f"log_{datetime.now().strftime('%Y%m%d')}.txt")

def date(self, date):
    self.date = date
    

with open(filename, "w") as file:
    for entry in log_data:
        file.write(f"{entry}\n")

print(f"Log written to {filename}")
