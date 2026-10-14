print("PASSWORD MANAGER")

print("1. Search for Record")
print("2. Create Record")
print("3. List all Records")
print("4. Delete Account")
print("5. Exit")

selection = int(input("Enter an option here: "))

if selection == 2:
    website = input("Enter the website here: ")
    username = input(f"Enter your username on {website} here: ")
    password = input(f"Enter your password on {website} here: ")
