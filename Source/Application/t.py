import login

login_manager_instance = login.LoginManager()

# Validate credentials
status = login_manager_instance.validateCredentials("admin", "password")
print(f"Login Status: {status}")  # Should print "Login Status: ADMIN"

# Register a user (empty function in this example)
login_manager_instance.registerUser("new_user", "new_password")