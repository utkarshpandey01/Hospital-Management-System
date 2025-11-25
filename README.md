🏥 Hospital Management System 

The Hospital Management System (HMS) is a modular, Python-based project designed to simplify and automate the daily activities of a hospital. It provides a clean and structured way to manage patients, doctors, and appointments using intuitive menus and functions. This system helps healthcare staff focus more on patient care and less on administrative work.


 Project Overview 💡

Hospitals deal with large amounts of information every day—patients, doctors, schedules, and appointments. Managing all this manually can be slow and prone to errors.
This project solves that problem by offering a simple yet powerful HMS that performs essential administrative tasks with speed and accuracy.


 Data Handling & Structure 🔧

The system is built using modular Python code, meaning each major function (Patients, Doctors, Appointments) lives in its own independent module.

Currently, the project uses Python dictionaries and lists as its internal database. This makes the system lightweight and easy to run anywhere, without requiring external databases like SQL.

Note: Since data stays in memory, it resets when the program closes. This is perfect for demonstration and learning purposes.


 Core Features (Patient & Doctor Management)

The Patient and Doctor modules support all basic CRUD operations — just like real hospital software. Users can easily:
	1.	Add new patient or doctor records.
	2.	View all existing entries in an organised list.
	3.	Search for any patient or doctor using their unique ID.
	4.	Update details of an existing record.
	5.	Delete a record that is no longer needed.

These operations allow staff to maintain accurate, up-to-date information at all times.


 Smart Appointment Management System 🔗

Appointments are the heart of any hospital workflow.
In this system, the appointment module connects patients and doctors with intelligent matching.

 Intelligent Doctor Matching 🧠

When a patient reports a symptom or issue (e.g., “Heart Pain”), the system automatically looks for the most suitable doctor speciality (e.g., Cardiologist).
This ensures the patient gets the appropriate care without manual searching.

 Patient-Friendly Features 
	•	View Appointments: Patients can instantly check their upcoming appointments using their Patient ID.
	•	Check Doctor Schedules: The system displays a doctor’s schedule so patients can understand availability before booking.
	•	Smart Cancellations: If the assigned doctor has too many appointments or is unavailable at the requested time, the system allows the patient to cancel or reschedule.

These features make the system more realistic and patient-centric.


Technical Implementation 🖥️ 
	•	Language: Python
	•	Architecture: Modular (separate files for Patient, Doctor, Appointment modules)
	•	Data Storage: In-memory (lists & dictionaries)
	•	Execution:
	•	Run main.py to start the system
	•	Use the interactive menu to navigate features
	•	Exit Option: A dedicated program exit choice allows for safe termination of the application.


🚀 How to Run the Project
	1.	Download or clone the repository.
	2.	Open the project folder and run the main file: 
        python main.py
  	3.  Choose from the menu to manage Patients, Doctors, or Appointments.
	4.	Follow on-screen instructions for smooth navigation.
  



