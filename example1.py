try:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if password != "admin123":
        raise ValueError("Invalid password")
    print("Login successful")
except ValueError as ve:
    print(ve)