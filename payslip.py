#!/usr/bin/env python
# coding: utf-8

# # CA1 PROGRAMMING ESSENTIALS
# 
# ### PROJECT PAYSLIP
# 
# **Module Title:** Programming Essentials
# 
# **Module Code:** B8IT102
# 
# **Module Leader:** Paul Laird
# 
# **Student Name:** Manoj Kumar Thangaraj
# 
# **Student Code:** 10570753
# 
# **Project Overview:**
# 
# The main objective of the project is to generate a payslip for each employee in the employee text file ‘Emp1.txt’. The hours worked details with the respective staff ID is enclosed in the file ‘Hours.txt’. The tax rate for all employee is written in the file ‘tax.txt’ file. For each line in the hours text file, the designed program should be able to create a separate payslip matching the staff id from the hours text file to employee file. The brief of this program is as follows. I have imported the datetime library to print the date and time at the end of each payslip. We defined a function payslip to bring all contents inside the function payslip. We read each file and assigned a key to all values in the files and stored it in dictionary data structure. I used for loop to loop through employee and hours file to store them in data structure. Under the for loop of hours text file, we used IF, Else statements to calculate the gross pay and net pay, tax deductions of the employee. Finally printing all the details required under the same for loop for each line in the hours text file.

# In[26]:


#to begin the exercise, let's import the libraries needed. For this particular exercise, datetime library is needed to print
#date time at the end.

import datetime       #importing datetime

def read_tax(file):     #defining a function
    '''This function takes in the standard tax format file which is tab space limited and 
    only have two values which is standard tax and higher tax.
    Args: tax file
    Returns: tax in dictionary format'''
    
    tax = dict()
    with open(file,'r') as m:   #opening the file
        tax_file=m.readline().split()       #read the line and split the tab spaced texts using .split function and assign the key to the values in the line.
        tax['standard_rate']=float(tax_file[0])  #assing a appropriate key for each value
        tax['higher_rate']=float(tax_file[1])
    return tax                                  #returns a tax dict

def read_employee(file):      #defining a function
    '''This function takes in the employee and output employee details in dictionary
    Args: Employee file
    Returns: Employee in dict'''
    
    employee=dict()                       #create the empty dictionary for employee 
    with open(file,'r') as f:   #opening the file
        for items in f.readlines():   #read the lines by using for loop and assign the keys to all the values in the text file
            x=items.strip().split('\t')
            employee[x[0]]={'staffid':x[0],'surname':x[1],'firstname':x[2],'ppsnumber':x[3],'std_hours':float(x[4]),'hourly_rate':float(x[5]),'overtime':float(x[6]),'taxcredit':float(x[7]),'std_band':float(x[8])}
    return employee              #returns a employee dict

def reciept(file, tax, employee):              #defining a function
    '''This function calculates the salary details for all employees
    Args: Hours worked file
    Returns: None'''
    
    hoursworked=dict()                    #create an empty dictionary for hours worked.
    with open(file,'r') as k:  #opening the file
        for newline in k.readlines(): #reading all the lines by using for loop and assign keys to the values in the text in the file
            y=newline.strip().split()
            hoursworked['Date']=y[0]
            hoursworked['staffid']=y[1] 
            hoursworked['hours_worked']=float(y[2])
            staff_id=hoursworked['staffid']
            hours = hoursworked['hours_worked']
            if hoursworked['staffid'] in employee: #checking if the value assgined to the staffid in hourswroked file is present in employee and if so,
                std_hours = employee[staff_id]['std_hours']  #assigning the variable 'std_hours' to the key,value in the employee dict
                overtime_hours = hours-std_hours             #begining the calculation for the payslip.std_hours,hours is defined from above. the overtime hours is the difference between them.

                if hours <= std_hours:  #an if statement under the if statement, to do the calcualtion. if the hours worked from hours textfile is less than or equal to the standard hours of the employee
                    regular_pay = hours*employee[staff_id]['hourly_rate'] #regular pay should be the hours times the hourly rate of the employee
                    overtime_hours=0       #in such case, overtime hours is zero
                    ot_pay = 0             #the pay should also be zero
                    grosspay=regular_pay   #grosspay should be equal to regualr pay as there is no overtime.

                else:                      #otherwise, regualr pay is standard hours times the employee hourly rate found in the dict.
                    regular_pay = std_hours*employee[staff_id]['hourly_rate']
                    ot_pay = overtime_hours*employee[staff_id]['overtime'] #overtime pay should be overtime hours times overtime rate
                    grosspay=regular_pay+ot_pay           #grosspay is the addition of regular and overtime

                if grosspay <= employee[staff_id]['std_band']: #calculation of taxes begins at this point, standard band is set for each employee and if the grosspay less than or equal to
                    higherband = 0                             #higherband tax for them is zero
                    standardband_tax = grosspay*(tax['standard_rate']/100) #standardband tax is calculated from the grosspay and standard tax percentage
                    higherband_tax=0                           #higherband tax is also zero since there no higherband amount calculated

                else:                                                    #otherwise,
                    higherband = grosspay-employee[staff_id]['std_band'] #its the difference of grosspay from the standard band of the employee
                    higherband_tax = higherband*(tax['higher_rate']/100) #higherband tax is calculated with higherband amount and the tax percentage from the tax file 
                    standardband_tax = (employee[staff_id]['std_band'])*((tax['standard_rate'])/100) #this time standard band tax is the employee standard band and standard tax rate

                    total_deductions = standardband_tax+higherband_tax-employee[staff_id]['taxcredit'] #total deductions are the sum of std band and higher band minus the tax credit belongs to the employee
                    total_deductions=max(0,total_deductions) #max function is used here particularly to avoid if the employee worked very low hours, so that the tax credit could be avoided.
                    Netpay = grosspay-total_deductions       #netpay is what employee recieves finally, which is difference of grosspay and total deductions
                print("\nPAYSLIP")  #printing the required format as follows,fill in the all the values of the key in employee and calculation through the for loop and if,else statements.
                print("StaffID: ",employee[staff_id]['staffid'])
                print("Staff Name: ",(employee[staff_id]['firstname'] +" "+employee[staff_id]['surname']))
                print("PPSN: ",employee[staff_id]['ppsnumber'])
                print("Date: ",hoursworked['Date'])
                print("Hours\t\tRate\tTotal")
                print("Regular {}\t{}\t{}".format((hours-overtime_hours),employee[staff_id]['hourly_rate'],regular_pay)) #hours-overtime hours is just to make sure it prints the regualr hours correctly
                print("Overtime {}\t{}\t{}\n".format(overtime_hours,employee[staff_id]['overtime'],ot_pay))
                print("Gross Pay\t\t",grosspay)
                print("\t\t\tRate\tTotal")
                print("Standard Band\t{}\t{}%\t{}".format(min(regular_pay,employee[staff_id]["std_band"]),tax["standard_rate"],standardband_tax)) #min function is used to make it prints the standard band correctly
                print("Higher Rate\t{}\t{}%\t{}\n".format(higherband,tax["higher_rate"],higherband_tax))
                print("Tax Credit\t",employee[staff_id]["taxcredit"])
                print("\nTotal deductions",total_deductions)
                print("Net Pay\t\t",Netpay)
                print('\n')
                print(datetime.datetime.now().strftime('%A %d %B %Y'))  #datetime format to printed on string format
            else:
                print("Staff record not found for staff_id: %s"%staff_id) #if no records found on the employee dict, this should print the following message


# In[ ]:




