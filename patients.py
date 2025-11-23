patients_db = {}        # main database dictionary
next_patient_id = 1     # auto-increment unique ID
def add_patient():
    """Add a new patient"""
    global next_patient_id

    print("\n--- Add Patient ---")
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter gender (M/F/O): ")
    disease = input("Enter disease/issue: ")

    patients_db[next_patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease
    }

    print(f"\nPatient added successfully with ID: {next_patient_id}")
    next_patient_id += 1


def view_all_patients():
    """Show all patient records"""
    print("\n--- All Patients ---")

    if not patients_db:
        print("No patients found.")
        return

    for pid, details in patients_db.items():
        print(f"\nID: {pid}")
        print(f"  Name   : {details['name']}")
        print(f"  Age    : {details['age']}")
        print(f"  Gender : {details['gender']}")
        print(f"  Disease: {details['disease']}")


def search_patient():
    """Search patient by ID"""
    print("\n--- Search Patient ---")
    pid = int(input("Enter patient ID: "))

    if pid in patients_db:
        d = patients_db[pid]
        print(f"\nID: {pid}")
        print(f"  Name   : {d['name']}")
        print(f"  Age    : {d['age']}")
        print(f"  Gender : {d['gender']}")
        print(f"  Disease: {d['disease']}")
    else:
        print("Patient not found.")


def update_patient():
    """Update patient details"""
    print("\n--- Update Patient ---")
    pid = int(input("Enter patient ID: "))

    if pid not in patients_db:
        print("Patient not found.")
        return

    name = input("Enter new name (leave blank to keep same): ")
    age_input = input("Enter new age (leave blank to keep same): ")
    gender = input("Enter new gender (leave blank to keep same): ")
    disease = input("Enter new disease (leave blank to keep same): ")

    if name:
        patients_db[pid]["name"] = name
    if age_input:
        patients_db[pid]["age"] = int(age_input)
    if gender:
        patients_db[pid]["gender"] = gender
    if disease:
        patients_db[pid]["disease"] = disease

    print("Patient record updated successfully.")


def delete_patient():
    """Delete patient by ID"""
    print("\n--- Delete Patient ---")
    pid = int(input("Enter patient ID: "))

    if pid in patients_db:
        del patients_db[pid]
        print("Patient deleted successfully.")
    else:
        print("Patient not found.")