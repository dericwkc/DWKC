from doctor import Doctor
from patient import Patient
from administrator import Administrator

def register_user():
    print("\nUser Registration:")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    return username, password

def login_user(users):
    print("\nUser Login:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user.username == username and user.login(password):
            return user
    return None

def choose_user_type():
    print("\nChoose User Type:")
    print("1. Doctor")
    print("2. Patient")
    print("3. Administrator")

    try:
        choice = int(input("Enter the corresponding number: "))
        if choice == 1:
            return Doctor
        elif choice == 2:
            return Patient
        elif choice == 3:
            return Administrator
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def main():
    users = []
    doctors = []

    while True:
        print("\nWelcome to the Blockchain-Based Medical Management System")
        print("1. Register an Account")
        print("2. Login to an Existing Account")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                user_role = choose_user_type()
                if user_role:
                    if user_role == Doctor:
                        username, password = register_user()
                        user = Doctor(username, password)
                        doctors.append(user)
                    else:
                        username, password = register_user()
                        user = user_role(username, password)
                    users.append(user)
                    print(f"User {user.username} registered as {user.__class__.__name__}.")

            elif choice == 2:
                logged_in_user = login_user(users)
                if logged_in_user:
                    print(f"Logged in as {logged_in_user.__class__.__name__}")
                    if isinstance(logged_in_user, Doctor):
                        logged_in_user.view_appointments(users)
                    elif isinstance(logged_in_user, Patient):
                        logged_in_user.book_appointment(doctors)
                    elif isinstance(logged_in_user, Administrator):
                        logged_in_user.view_all_appointments(users)
                else:
                    print("Login failed. Please check your credentials.")

            elif choice == 3:
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
