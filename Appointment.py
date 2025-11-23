
import patients       # uses patients.patients_db
import doctors        # uses doctors.doctors_db

appointments_db = {}        # appointment_id -> details
next_appointment_id = 1     # auto-increment ID


def create_appointment():
    """Book an appointment between a patient and a doctor"""
    global next_appointment_id

    # basic safety checks
    if not patients.patients_db:
        print("\nNo patients found. Please add a patient first.")
        return

    if not doctors.doctors_db:
        print("\nNo doctors found. Please add a doctor first.")
        return

    print("\n--- Book Appointment ---")

    # list patients
    print("\nExisting Patients:")
    for pid, p in patients.patients_db.items():
        print(f"  ID {pid} -> {p['name']} ({p['disease']})")

    patient_id = int(input("Enter Patient ID: "))

    if patient_id not in patients.patients_db:
        print("Invalid Patient ID.")
        return

    # list doctors
    print("\nAvailable Doctors:")
    for did, d in doctors.doctors_db.items():
        print(f"  ID {did} -> {d['name']} ({d['specialization']})")

    doctor_id = int(input("Enter Doctor ID: "))

    if doctor_id not in doctors.doctors_db:
        print("Invalid Doctor ID.")
        return

    date = input("Enter appointment date (DD-MM-YYYY): ")
    time = input("Enter appointment time (HH:MM): ")

    appointments_db[next_appointment_id] = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time
    }

    print(f"\nAppointment booked successfully with ID: {next_appointment_id}")
    print_appointment(next_appointment_id)

    next_appointment_id += 1


def print_appointment(aid):
    """Print a single appointment nicely"""
    app = appointments_db[aid]
    p = patients.patients_db.get(app["patient_id"], {})
    d = doctors.doctors_db.get(app["doctor_id"], {})

    print(f"\nAppointment ID: {aid}")
    print(f"  Patient : {p.get('name', 'Unknown')} (ID {app['patient_id']})")
    print(f"  Doctor  : {d.get('name', 'Unknown')} (ID {app['doctor_id']})")
    print(f"  Date    : {app['date']}")
    print(f"  Time    : {app['time']}")


def view_all_appointments():
    """Show all appointments"""
    print("\n--- All Appointments ---")
    if not appointments_db:
        print("No appointments booked yet.")
        return

    for aid in appointments_db:
        print_appointment(aid)


def view_appointments_by_patient():
    """Show appointments for a specific patient ID"""
    pid = int(input("\nEnter Patient ID: "))
    found = False

    for aid, app in appointments_db.items():
        if app["patient_id"] == pid:
            if not found:
                print(f"\nAppointments for Patient ID {pid}:")
            print_appointment(aid)
            found = True

    if not found:
        print("No appointments found for this patient.")


def cancel_appointment():
    """Cancel an appointment by ID"""
    print("\n--- Cancel Appointment ---")
    aid = int(input("Enter Appointment ID to cancel: "))

    if aid in appointments_db:
        del appointments_db[aid]
        print("Appointment cancelled successfully.")
    else:
        print("Appointment ID not found.")