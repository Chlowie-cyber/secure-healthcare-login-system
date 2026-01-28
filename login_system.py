import hashlib
import csv
from datetime import datetime

## Hash password function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

## Log Login attempts
def log_attempt(username, success):
    with open("login_logs.txt", "a") as log:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "SUCCESS" if success else "FAILED"
        log.write(f"{time} | {username} | {status}\n")

## Authenticate user
def authenticate(username, password):
    hashed = hash_password(password)

    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for user in reader:
            if user["username"] == username and user["password"] == hashed:
                log_attempt(username, True)
                return user["role"]
            
    log_attempt(username, False)
    return None

## Main program
username = input("Username: ")
password = input("Password: ")

role = authenticate(username, password)

if role:
    print(f"Login successful! Role: {role}")
else:
    print("Login failed.")