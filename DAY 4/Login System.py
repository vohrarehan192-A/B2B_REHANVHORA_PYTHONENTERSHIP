CORRECT_USERNAME = "REHAN"
CORRECT_PASSWORD = "@123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
  print("Login Successful")
else:
  print("Login Failed")