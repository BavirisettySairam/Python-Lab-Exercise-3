# Simulating a database
user_database = []

# Creating lambda expressions

# Creating a new user record.
create_user = lambda full_name, email: {
    "full_name": full_name,
    "email": email,
}

# Inserting the user record into the list.
insert_user = lambda user: user_database.append(user) if user else print("Error: Invalid user record.")

# Fetching all user records from the list.
fetch_user_data = lambda: [user for user in user_database if user]

# Example usage:
try:
    user1 = create_user("John Doe", "john@example.com")
    insert_user(user1)
    user2 = create_user("Jane Doe", "jane@example.com")
    insert_user(user2)
    
    print("Registered users:")
    for user in fetch_user_data():
        print(f"Name: {user['full_name']}")
        print(f"Email: {user['email']}")
        print("=" * 15)
except Exception as e:
    print(f"Error: {str(e)}")