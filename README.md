# Hospital Management System


🏥 Hospital Management System (HMS)
This project provides a comprehensive system for managing the essential operations of a hospital. The system is modular, organized into several key management components:

1. Patient Management
2. Doctor Management
3. Appointment Management
4. Exit

💻 Data Management
Each management component is built using dedicated Python modules. Currently, data persistence (the database) is handled entirely using Python dictionaries and lists.

✨ Core Functionalities (Patient & Doctor Modules)
The Patient Management and Doctor Management modules support standard CRUD (Create, Read, Update, Delete) operations, allowing users to:

1. Add a new patient or doctor record.
2. View All patients or doctors currently in the system.
3. Search for a patient or doctor using their unique ID.
4. Update an existing patient or doctor record.
5. Delete a patient or doctor record.

🔗 Appointment Management System
The Appointment Management System is a critical, distinct component that links the Patient and Doctor modules.

This system facilitates the scheduling process by matching patients with appropriately specialized doctors. For example, if a patient reports "Heart Pain," the system will logically assign them a doctor specializing in the Cardiology field.

Patient-Specific Appointment Features:
Patients can view all their existing appointments by searching using their Patient ID.

The system allows patients to view the doctor's general schedule (appointments with other patients).

Based on the doctor's availability, a patient can cancel their appointment if the doctor is determined to be too busy or unavailable.
