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
