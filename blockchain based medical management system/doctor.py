from datetime import datetime

class Doctor:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.appointments = []

    def login(self, entered_password):
        return self.password == entered_password

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

# Rest of the Doctor class code
