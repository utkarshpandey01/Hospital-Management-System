
# main database dictionary
doctors_db = {}
next_doctor_id = 1       # auto-increment unique ID


def add_doctor():
    """Add a new doctor"""
    global next_doctor_id

    print("\n--- Add Doctor ---")
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")
    phone = input("Enter contact number: ")

    doctors_db[next_doctor_id] = {
        "name": name,
        "specialization": specialization,
        "phone": phone
    }

    print(f"\nDoctor added successfully with ID: {next_doctor_id}")
    next_doctor_id += 1


def view_all_doctors():
    """Show all doctor records"""
    print("\n--- All Doctors ---")

    if not doctors_db:
        print("No doctors found.")
        return

    for did, details in doctors_db.items():
        print(f"\nID: {did}")
        print(f"  Name          : {details['name']}")
        print(f"  Specialization: {details['specialization']}")
        print(f"  Phone         : {details['phone']}")


def search_doctor():
    """Search doctor by ID"""
    print("\n--- Search Doctor ---")
    did = int(input("Enter doctor ID: "))

    if did in doctors_db:
        d = doctors_db[did]
        print(f"\nID: {did}")
        print(f"  Name          : {d['name']}")
        print(f"  Specialization: {d['specialization']}")
        print(f"  Phone         : {d['phone']}")
    else:
        print("Doctor not found.")


def update_doctor():
    """Update doctor details"""
    print("\n--- Update Doctor ---")
    did = int(input("Enter doctor ID: "))

    if did not in doctors_db:
        print("Doctor not found.")
        return

    name = input("Enter new name (leave blank to keep same): ")
    specialization = input("Enter new specialization (leave blank to keep same): ")
    phone = input("Enter new phone (leave blank to keep same): ")

    if name:
        doctors_db[did]["name"] = name
    if specialization:
        doctors_db[did]["specialization"] = specialization
    if phone:
        doctors_db[did]["phone"] = phone

    print("Doctor record updated successfully.")


def delete_doctor():
    """Delete doctor by ID"""
    print("\n--- Delete Doctor ---")
    did = int(input("Enter doctor ID: "))

    if did in doctors_db:
        del doctors_db[did]
        print("Doctor deleted successfully.")
    else:
        print("Doctor not found.")