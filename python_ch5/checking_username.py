current_users = ['john', 'sarah', 'alex', 'eric', 'admin']
new_users = ['JOHN', 'mary', 'Alex', 'david', 'lisa']

# Create a lowercase copy of current_users for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available!")