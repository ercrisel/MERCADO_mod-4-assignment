'''Module 2: Individual Programming Assignment 1

Useful Business Calculations

This assignment covers your basic proficiency with Python.
'''

def savings(gross_pay, tax_rate, expenses):
    #Calculate take home pay after tax and expenses is deducted.
    tax_deduction = int(gross_pay * tax_rate)
    take_home_pay = gross_pay - tax_deduction - expenses
    
    return take_home_pay

def material_waste(total_material, material_units, num_jobs, job_consumption):
    #Calculate the total material waste
    total_consumed = num_jobs * job_consumption
    remaining_material = total_material - total_consumed
    
    #Format the output as a string with units
    material_waste = str(remaining_material) + material_units
    
    return material_waste

def interest(principal, rate, periods):
    rate = float(rate/100)
    interest = principal * rate * periods
    final_value = principal + interest
    
    return final_value

def body_mass_index(weight, height):
    #Convert weight from pounds to kilograms (1 lbs = 0.45359237 kg)
    weight_kg = weight * 0.45359237

    #Convert height from feet and inches to meters
    height_ft, height_in = height
    height_m = (int(height_ft) * 0.3048) + (int(height_in) * 0.0254)

    #Calculate BMI
    body_mass_index = weight_kg/(height_m**2)
    body_mass_index = format(body_mass_index,".2f")

    return body_mass_index

while(True):
    print("\nSelect a Computational Function")
    print("[1] Savings")
    print("[2] Material Waste")
    print("[3] Interest")
    print("[4] Body Mass Index")

    select = None

    while(True):
        #Determine FUNCTION SELECTION using user-provided input
        select = int(input(">> "))
        if not(select <= 4 and select >= 1):
            print("\n[SYSTEM]: Please input a number from the available options.")
        else:
            break

    if select == 1:  
        print("\n[FUNCTION: SAVINGS]")
        #Determine GROSS PAY using user-provided input
        print("\nInput the Gross Pay | E.g. 12500")
        while(True):
            gross_pay = int(input(">> "))
            if not(gross_pay >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        #Determine TAX RATE using user-provided input
        print("\nInput the Tax Rate | E.g. 0.13")
        while(True):
            tax_rate = float(input(">> "))
            if not(tax_rate < 1 and tax_rate > 0):
                print("\n[SYSTEM]: Please input a number between 0 and 1.")
            else:
                break
        #Determine EXPENSES using user-provided input
        print("\Input the Expenses | E.g. 3400")
        while(True):
            expenses = int(input(">> "))
            if not(expenses >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        #Returns
        print("\nCentavos Remaining: " + str(savings(gross_pay, tax_rate, expenses)) + '\u00a2')
    elif select == 2:
        print("\n[FUNCTION: MATERIAL WASTE]")
        #Determine TOTAL MATERIAL using user-provided input
        print("\nInput the Total Material | E.g. 97000")
        while(True):
            total_material = int(input(">> "))
            if not(total_material >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        #Determine MATERIAL UNIT using user-provided input
        print("\nInput the Material Unit | E.g. Kg, Lbs, or L")
        while(True):
            material_units = str(input(">> "))
            if not(type(material_units) == str):
                print("\n[SYSTEM]: Please input a string.")
            else:
                break
        #Determine NUMBER OF JOBS using user-provided input
        print("Input the Number of Jobs | E.g. 13")
        while(True):
            num_jobs = int(input(">> "))
            if not(num_jobs >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        #Determine JOB CONSUMPTION using user-provided input
        print("Input the Job Consumption | E.g. 710")
        while(True):
            job_consumption = int(input(">> "))
            if not(job_consumption >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        #Return
        print("\nRemaining Materials: " + material_waste(total_material, material_units, num_jobs, job_consumption))
    elif select == 3:
        print("\n[FUNCTION: INTEREST]")
        #Determine PRINCIPAL using user-provided input
        print("Input the Principal | E.g. 3600")
        while(True):
            principal = int(input(">> "))
            if not(principal >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        #Determine RATE using user-provided input
        print("Input the rate | E.g. 3% or 0.3")
        while(True):
            rate = input(">> ")
            if(rate.endswith('%')):
                rate = rate.replace("%", "")
                rate = float(int(rate)/100)
                if not(rate >= 0):
                        print("\n[SYSTEM]: Please input a percentage greater than or equal to 0.")
                else:
                    break
            else:
                try:
                    rate = float(rate)
                    if not(rate >= 0):
                        print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
                    else:
                        break
                except ValueError:
                    print("\n[SYSTEM]: Please input a percentage or decimal.")
        #Determine PERIODS using user-provided input
        print("Input the Periods")
        while(True):
            periods = input(">> ")
            if not(periods >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        #Returns
        
        print("\Final Investment Value: " + str(interest(principal, rate, periods)))
    elif select == 4:
        print("\nYou've selected BODY MASS INDEX.")

        #Determine WEIGHT using user-provided input
        print("Input the Weight (in pounds)")
        while(True):
            weight = float(input(">> "))
            if not(weight >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
            
        #Determine HEIGHT using user-provided input
        print("Input the Height (in feet and inches) | Ex. 4'10")
        while(True):
            height = str(input(">> "))
            if not(type(height) == str):
                print("\n[SYSTEM]: Please input the right format.")
            else:
                break

        #Split height (in feet and inches) into a list
        height_list = height.split("'")

        #Display Body Mass Index Calculation
        bmi = body_mass_index(weight, height_list)
        print("\nBody Mass Index: " + (str(bmi)))
        if (bmi < 18.5):
            print("Category: Underweight")
        elif (bmi >= 18.5 and bmi <= 24.9):
            print("Category: Healthy Weight")
        elif (bmi >= 25.0 and bmi <= 29.9):
            print("Category: Overweight")
        elif (bmi > 30.0):
            print("Category: Obesity")

    print("\nInitiate program execution once more?")
    print("[1] Yes")
    print("[2] No")
    
    while(True):
        select = int(input(">> "))
        if not(select <= 2 and select >= 1):
            print("\nPlease input a number from the available options.")
        else:
            break

    if(select == 1):
        continue
    elif(select == 2):
        break