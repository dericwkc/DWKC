from datetime import datetime

class Patient:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.appointments = []

    def login(self, entered_password):
        return self.password == entered_password

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

# Rest of the Patient class code
