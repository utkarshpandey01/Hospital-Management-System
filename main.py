# main.py

"""Main menu loop"""

import patients
import doctors
import Appointment


def patient_menu():
    while True:
        print("\n========= PATIENT MANAGEMENT =========")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient by ID")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            patients.add_patient()
        elif choice == "2":
            patients.view_all_patients()
        elif choice == "3":
            patients.search_patient()
        elif choice == "4":
            patients.update_patient()
        elif choice == "5":
            patients.delete_patient()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")


def doctor_menu():
    while True:
        print("\n========= DOCTOR MANAGEMENT =========")
        print("1. Add Doctor")
        print("2. View All Doctors")
        print("3. Search Doctor by ID")
        print("4. Update Doctor")
        print("5. Delete Doctor")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            doctors.add_doctor()
        elif choice == "2":
            doctors.view_all_doctors()
        elif choice == "3":
            doctors.search_doctor()
        elif choice == "4":
            doctors.update_doctor()
        elif choice == "5":
            doctors.delete_doctor()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")


def appointment_menu():
    while True:
        print("\n========= APPOINTMENT MANAGEMENT =========")
        print("1. Book Appointment")
        print("2. View All Appointments")
        print("3. View Appointments by Patient ID")
        print("4. Cancel Appointment")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            Appointment.create_appointment()
        elif choice == "2":
            Appointment.view_all_appointments()
        elif choice == "3":
            Appointment.view_appointments_by_patient()
        elif choice == "4":
            Appointment.cancel_appointment()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


def main_menu():
    while True:
        print("\n=========== HOSPITAL MANAGEMENT SYSTEM ===========")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_menu()
        elif choice == "2":
            doctor_menu()
        elif choice == "3":
            appointment_menu()
        elif choice == "4":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main_menu()