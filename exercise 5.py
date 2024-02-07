def authenticate():
    # Define the correct username and password
    correct_username = "python"
    correct_password = "rules"

    # Initialize attempts counter
    attempts = 0

    # Loop for authentication attempts
    while attempts < 5:
        # Get username and password from the user
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if the credentials are correct
        if username == correct_username and password == correct_password:
            print("Welcome!")
            return  # Exit the function as authentication is successful
        else:
            print("Incorrect username or password. Please try again.")
            attempts += 1

    # If reached here, five attempts are exhausted
    print("Access denied.")

# Call the function to start authentication process
authenticate()
