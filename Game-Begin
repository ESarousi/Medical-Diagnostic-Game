import math
import random

P1 = {
    'ID': 1,
    'Name': 'John Smith',
    'Age': 62,
    'Sex': 'Male',
    'Allergies': ['Oxycodone'],
    'Reactions': 'Hives',
    'Chief Complaint': 'Vomiting',
    'Complaints': ['Abdominal Pain', 'Lethargy', 'Jaundice', 'Lack of Appetite', 'Dark Urine'],
    'Diagnosis': 'Liver Cancer',
    'Weight': 244,
    'Height': 65,
    'Blood Glucose': 141,
    'Blood Pressure': 136,
    'Temperature': 99.4
     }

P2 = {
    'ID': 2,
    'Name': 'Sally Samson',
    'Age': 49,
    'Sex': 'Female',
    'Allergies': [None],
    'Reactions': None,
    'Chief Complaint': 'Trouble Breathing',
    'Complaints': ['Sore Throat', 'Congestion', 'Fatigue', 'Headache', 'Lost of Taste'],
    'Diagnosis': 'COVID-19',
    'Weight': 157,
    'Height': 61,
    'Blood Glucose': 105,
    'Blood Pressure': 113,
    'Temperature': 101.7
     }

P3 = {
    'ID': 3,
    'Name': 'Michael Jordanson',
    'Age': 36,
    'Sex': 'Male',
    'Allergies': 'Penicillin',
    'Reactions': 'Anaphylaxis',
    'Chief Complaint': 'Cramping in Leg',
    'Complaints': ['', 'Lethargy', 'Dry Mouth', 'Nausea'],
    'Diagnosis': 'Diabetes Mellitus Type 2',
    'Weight': 257,
    'Height': 68,
    'Blood Glucose': 225,
    'Blood Pressure': 150,
    'Temperature': 98.4
     }

Patient_List = [P1, P2, P3]

def game_begin():
    patient = random.choice(Patient_List)
    def menu():
        choice = input('''What do you want to do? 
        Your choices are:
        C = Check Patient Sheet
        T = Talk to Patient
        M = Prescribe Medication
        D = Perform a Diagnostic Test
        S = Perform Surgery''')

        if choice.lower() == "c":
            patient_sheet(patient, 0)
        if choice.lower() == "t":
            patient_discussion(patient, 0)
        if choice.lower() == "m":
            prescribe_medication(patient)
        if choice.lower() == "d":
            diagnostic_test(patient)
        if choice.lower() == "s":
            perform_surgery(patient)
        else:
            print("You've chosen an invalid action. Please try again. ")
            menu()
    menu()
