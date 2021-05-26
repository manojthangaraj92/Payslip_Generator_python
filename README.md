### PROJECT PAYSLIP


**Project Overview:**

The main objective of the project is to generate a payslip for each employee in the employee text file ‘Emp1.txt’. 
The hours worked details with the respective staff ID is enclosed in the file ‘Hours.txt’. The tax rate for all 
employee is written in the file ‘tax.txt’ file. For each line in the hours text file, the designed program should 
be able to create a separate payslip matching the staff id from the hours text file to employee file. 

The brief of this program is as follows. I have imported the datetime library to print the date and time at the end of each payslip.
We defined a functions for read the tax file, employee file and finally print all the employee payslip. For the tax file, The file 
should have only standard tax followed by higher tax in tab spaced limit and nothing else should be included and Nothing else.

For the employee file, it should have only the values of staffid, surname, firstname, ppsnumber, standard hours, hourly rate, overtime,
tax credit and standard band. Each line should have the only values and nothing else.

For the hours worked file, it should have a date in the format of DD/MM/YYYY, staff id, hours worked and nothing else.

I used for loop to loop through employee and hours file to store them in data structure. 
Under the for loop of hours text file, we used IF, Else statements to calculate the gross pay and net pay, tax deductions of the employee.
 Finally printing all the details required under the same for loop for each line in the hours text file.

 payslip.py contains modular coding which has all functions

 ExecutePayslip.py is the file need to be executed to check the results.

 Emp1.txt, tax.txt, Hours.txt files are ones to be taken into processing.