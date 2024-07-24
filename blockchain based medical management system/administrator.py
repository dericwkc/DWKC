class Administrator:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, entered_password):
        return self.password == entered_password

    def view_all_appointments(self, users):
        print("\nAll Appointments:")
        for user in users:
            if isinstance(user, Doctor) and user.appointments:
                print(f"\nAppointments for Doctor {user.username}:")
                for i, (patient, appointment) in enumerate(user.appointments, 1):
                    print(f"{i}. Patient: {patient}, {appointment}")

# Rest of the Administrator class code
