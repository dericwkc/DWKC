from datetime import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, entered_password):
        return self.password == entered_password

    def __str__(self):
        return self.username

class Doctor(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.appointments = []

    def view_appointments(self, users):
        if not self.appointments:
            print("You have no appointments scheduled.")
        else:
            print("Your Appointments:")
            for i, (patient, appointment) in enumerate(self.appointments, 1):
                print(f"{i}. Patient: {patient}, {appointment}")
                print("\nAppointments Booked by Patients:")
                for user in users:
                    if isinstance(user, Patient):
                        for appt in user.appointments:
                            if appt[0] == self.username:
                                print(f"- {user.username}: {appt[1]}")

class Patient(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.appointments = []

    def book_appointment(self, doctors):
        if not doctors:
            print("No doctors available for booking.")
            return

        print("\nAvailable Doctors:")
        for i, doctor in enumerate(doctors, 1):
            print(f"{i}. {doctor.username}")

        try:
            doctor_choice = int(input("Select a doctor by entering the corresponding number: ")) - 1
            doctor = doctors[doctor_choice]
            date = input("Enter the appointment date (YYYY-MM-DD): ")
            time = input("Enter the appointment time (HH:MM AM/PM): ")
            appointment_datetime = datetime.strptime(date + " " + time, "%Y-%m-%d %I:%M %p")
            
            if appointment_datetime < datetime.now():
                print("Invalid appointment time. Please choose a future date and time.")
                return

            appointment = (doctor.username, f"Date: {date}, Time: {time}")
            self.appointments.append(appointment)
            doctor.appointments.append((self.username, f"Date: {date}, Time: {time}"))
            print(f"Appointment booked with Doctor {doctor.username} on {date} at {time}")
        except (ValueError, IndexError):
            print("Invalid choice or input. Appointment booking failed.")

class Administrator(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def view_all_appointments(self, users):
        print("\nAll Appointments:")
        for user in users:
            if isinstance(user, Doctor) and user.appointments:
                print(f"\nAppointments for Doctor {user.username}:")
                for i, (patient, appointment) in enumerate(user.appointments, 1):
                    print(f"{i}. Patient: {patient}, {appointment}")

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
                    print(f"Logged in as {logged_in_user}")
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
