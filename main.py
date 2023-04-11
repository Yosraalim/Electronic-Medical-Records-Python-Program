# Developed By: Yosra Alim
# Date: March 17th
# Description: My Information System for Electronic Medical Records!

print('-----------------------------------------------------------------------------')

from typing import List, Dict, Optional

def formatLine(lis):
        checkedFormat = []
        
        checkedFormat.append(int(lis[0]))
        checkedFormat.append(str(lis[1]))
        checkedFormat.append(float(lis[2]))
        checkedFormat.append(int(lis[3]))
        checkedFormat.append(int(lis[4]))
        checkedFormat.append(int(lis[5]))
        checkedFormat.append(int(lis[6]))
        checkedFormat.append(int(lis[7]))

        return checkedFormat
def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}
    #######################
    #### PUT YOUR CODE HERE
    import csv
    
    try:
        with open(fileName, "r") as file:
            file = csv.reader(file)
            noLine = 0
            
            for line in file:
                noLine += 1
                try:
                    newLine = formatLine(line)
                except:
                    print(f"Invalid data type in line: {noLine}")
                    continue
                
                #do the checks
                if len(newLine) !=8:
                    print(f"Invalid number of fields([numFields]) in line: {noLine}" )

                if not 30<= newLine[2] <= 43:
                    print(f"Invalid temperature value ([temp]) in line: {noLine}")
                    continue 

                if not 30<= newLine[3] <= 200:
                    print(f"Invalid heart rate value ([hr]) in line: {noLine}")
                    continue 
                
                if not 5<= newLine[4] <= 60:
                    print(f"Invalid respiratory rate value ([rr]) in line: {noLine}")
                    continue 
                
                if not 50<= newLine[5] <= 250:
                    print(f"Invalid systolic blood pressure value ([sbp]) in line: {noLine}")
                    continue 
                if not 30<= newLine[6] <= 150:
                    print(f"Invalid diastolic blood pressure value ([dbp]) in line: {noLine}")
                    continue 

                if not 80<= newLine[7] <= 100:
                    print(f"Invalid oxygen saturation value ([spo2]) in line: {noLine}")
                    continue 
                
                if newLine[0] in patients:
                    patients[newLine[0]].append(newLine)
                else:
                    patients[newLine[0]] = [newLine]
    except FileNotFoundError:
        print(f"The file {fileName} could not be found.")
    #######################
    
    return patients


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    #######################
    #### PUT YOUR CODE HERE
    if patientId == 0:
        records = patients
        for patient, patientRecord in records.items():
            print(f"Patient ID: {patient}")
            for record in patientRecord:
                print(f"    Date: {record[1]}")
                print(f"      Temperature: {record[2]}")
                print(f"      Heart Rate: {record[3]}")
                print(f"      Respiratory Rate: {record[4]}")
                print(f"      Systolic Blood Pressure: {record[5]}")
                print(f"      Diastolic Blood Pressure: {record[6]}")
                print(f"      Oxygen Saturation: {record[7]}")
                print()
    
    else:
        
        if patientId in patients:
            patientRecords = patients[patientId]
            print(f"Patient ID: {patientId}")
            for record in patientRecords:
                print(f"    Date: {record[1]}")
                print(f"      Temperature: {record[2]}")
                print(f"      Heart Rate: {record[3]}")
                print(f"      Respiratory Rate: {record[4]}")
                print(f"      Systolic Blood Pressure: {record[5]}")
                print(f"      Diastolic Blood Pressure: {record[6]}")
                print(f"      Oxygen Saturation: {record[7]}")
                print()
        else:
            print( f"Patient with ID {patientId} not found.")
            return
    return 
    #######################


def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """

    #######################
    #### PUT YOUR CODE HERE
    #if type(patientId) != int:
    if not int(patientId) and int(patientId) != 0: 
        print("Error: 'patientId' should be an integer.")
        return False
    elif int(patientId) != 0 and int(patientId) not in patients:
        print(f"No data found for patient with ID {patientId}.")
        return False
    elif type(patients) != dict:
        print("Error: 'patients' should be a dictionary.")
        return False
    patientId = int(patientId)
    temp = 0.0
    heart_rate = 0
    resp_rate = 0
    sys = 0
    dis = 0
    oxy = 0
    count = 0
    if patientId == 0:
        print("Vital Signs for All patients:")
        for patient_id, patient_visits in patients.items():

            for visit in patient_visits:
                count += 1
                temp += float(visit[2])
                heart_rate += int(visit[3])
                resp_rate += int(visit[4])
                sys += int(visit[5])
                dis += int(visit[6])
                oxy += int(visit[7])
        

        print(f"  Average Temperature: {round(temp/count, 2)}°C")
        print(f"  Average Heart Rate: {round(heart_rate/count, 2)}bpm")
        print(f"  Average Respiratory Rate: {round(resp_rate/count, 2)}bpm")
        print(f"  Average Systolic Blood Pressure: {round(sys/count, 2)}mmHg")
        print(f"  Average Diastolic Blood Pressure: {round(dis/count, 2)}mmHg")
        print(f"  Average Oxygen Saturation: {round(oxy/count, 2)}%")
        print()

        return 
    elif patientId in patients:
        print(f"Vital Signs for Patient {patientId}:")
        for visit in patients[patientId]:
            count += 1
            temp += visit[2]
            heart_rate += visit[3]
            resp_rate += visit[4]
            sys += visit[5]
            dis += visit[6]
            oxy += visit[7]

        print(f"  Average Temperature: {round(temp / count, 2)}°C")
        print(f"  Average Heart Rate: {round(heart_rate / count, 2)}bpm")
        print(f"  Average Respiratory Rate: {round(resp_rate / count, 2)}bpm")
        print(f"  Average Systolic Blood Pressure: {round(sys / count, 2)}mmHg")
        print(f"  Average Diastolic Blood Pressure: {round(dis / count, 2)}mmHg")
        print(f"  Average Oxygen Saturation: {round(oxy / count, 2)}%")
        print()

        return 
    else:
        print(f"No data found for patient with ID {patientId}.")
        return 
    #######################



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    #######################
    #### PUT YOUR CODE HERE
    try:
        # inspect that the date is in the right format
        if  date[4] != '-'  or  len(date) != 10 or date[7] != '-':
            print("Invalid date format. Please enter date in the format 'yyyy-mm-dd'.")
            return
        

        # Make sure the date can exist 
        year  = int(date[:4])
        month = int(date[5:7])
        day = int(date[-2:])
        if month < 1 or month > 12 or day < 1 or day > 31 or (day > 30 and (month == 4 or month == 6 or month == 9 or month == 11)) or (day > 29 and month == 2) or (day > 28 and month == 2 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))):
            print("Invalid date. Please enter a valid date.")

            return
        
        #Temperature in the correct range check
        if  temp > 42 or temp < 35:
            print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
            return
        
        # Heat rate in the correct range.
        if  hr > 180 or  hr < 30:
            print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm." )

            return
        
        #Respiratory rate
        if rr < 5 or rr > 40:
            print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
            return
        
        #systolic blood pressure
        if sbp < 70 or sbp > 200:
            print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
            return
        
        # diastolic blood pressure
        if dbp < 40 or dbp > 120:

            print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")

            return
        
        # Verify oxygen in the correct range
        if spo2 > 100  or spo2 < 70 :

            print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
            return
        
        # write to file 
        with open(fileName, 'a') as f:

            f.write(f"{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}\n")
        
        # Add to the dictionary 
        if patientId in patients:
            patients[patientId].append((date, temp, hr, rr, sbp, dbp, spo2))
        else:
            patients[patientId] = [(date, temp, hr, rr, sbp, dbp, spo2)]
        
        # Output the success message
        print(f"Visit is saved successfully for Patient #{patientId}" )
        
    except Exception:

        print(" An unexpected error occurred while adding new data.")
    #######################



def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    #######################
    #### PUT YOUR CODE HERE
     #validate dictionary is not empty
    if not patients:  

        return []

    
    for patient_id, patient_visits in patients.items():

        for visit in patient_visits:
            try:
                visit_date = visit[1]
                visit_year  = int(visit_date[:4])
                visit_month = int(visit_date[5:7])
            except:
                continue 
            
            #skip visits not in the specified year
            if year and visit_year != year:
                continue  
            #skip visits not in the specified month
            if month and  visit_month != month:

                continue  
            
            visits.append((patient_id, visit[1:]))
    #######################
    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    #######################
    #### PUT YOUR CODE HERE
    followUp = set()
    for patient, patientRecord in patients.items():
            
            for record in patientRecord:
                
                if record[3] > 100 or record[3] < 60:
                    followUp.add(patient)
                    break
                
                if record[5] > 140:
                    followUp.add(patient)
                    break
                
                if record[6] > 90:
                    followUp.add(patient)
                    break

                if record[7] < 90:
                    followUp.add(patient)
                    break
    
    followup_patients = list(followUp)
    #######################
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    #######################
    #### PUT YOUR CODE HERE
    if patientId not in patients:
        print(f"No data found for patient with ID {patientId}")

        return

    #delete the record 
    del patients[patientId]

    with open(filename, "w") as file:
        for patient, patientVisits in patients.items():

            for visit in patientVisits:

                if patient == patientId:
                    continue
                patientVisitsRecords = [visit[0], visit[1],visit[2],visit[3],visit[4],visit[5],visit[6],visit[7]]
                #join
                patientVisitsRecords = ','.join(map(str, patientVisitsRecords))
                #write to the file
                file.write(f"{patientVisitsRecords}\n")

    print(f"Data for patient {patientId} has been deleted.")
    #######################




###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
