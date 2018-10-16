# Wellframe Tech Challenge
A simple medication management API

# Design
I created this API using Python, Django, and the Django REST Framework.
There are three models used in this API: Patient, Medication, and Prescription.
Patient contains information about a patient such as their name and age. Medication
contains information about an available medication such as the name of the medication.
Prescription maps patients to available medications.

# Installation:

1. Create a virtual environment.
  
    ```
    python3 -m pip install --user virtualenv          #macOS and Linux
    py -m pip install --user virtualenv               #Windows
    ```
    ```
    python3 -m virtualenv venv                        #macOS and Linux
    py -m virtualenv venv                             #Windows
    ```
2. Activate your virtual environment
    ```
    source venv/bin/activate                          #macOS and Linux
    .\venv\Scripts\activate                           #Windows
    ```
3. Install dependencies.
    ```
    pip install -r requirements.txt
    ```
    
# Startup
 1. Initialize the database
 ```
 python manage.py migrate
 ```
 2. Start the server
 ```
 python manage.py runserver
 ```

# Documentation
 http://localhost:8000/docs/
 
# API Root
http://localhost:8000/api/v1 

# Example Usage:

1. Adding a new medication
```
curl -i -X POST -H "Content-Type:application/json" http://localhost:8000/api/v1/medications -d '{"name":"Advil"}'
```
2. Adding a new patients
```
curl -i -X POST -H "Content-Type:application/json" http://localhost:8000/api/v1/patients -d '{"name":"Bob"}'
```
3. Assign a prescription to a patient
```
curl -i -X POST -H "Content-Type:application/json" http://localhost:8000/api/v1/patients/{patient_id}/prescriptions -d '{"patient":"PATIENT_ID", "medication":"MEDICATION_ID"}'
```
4. Remove a prescription assigned to a patient
```
curl -i -X DELETE -H "Content-Type:application/json" http://localhost:8000/api/v1/patients/{patient_id}/prescriptions/{prescription_id}
```
