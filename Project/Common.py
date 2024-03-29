import csv
import DBOperations
from turtle import window_height, window_width

# Function to validate DOB year 
def validateDOByear(date):
    if date.isnumeric():
        if int(date)<=2012 and int(date)>=1920:
            return True
    return False

# Function to check for null on any input 
def validateNull(input):
    if input:
        return True
    return False

# Function to validate a given mobile number
def validateMobile(mobile):
    if mobile.isnumeric():
        if len(mobile)==10:
            return True
    return False

# Function to validate days
def validateDays(days):
    if int(days)<=30:
        return True
    return False

# Function to validate int value
def validateInt(num):
    if num.isnumeric():
        return True
    return False

# Function to validate check box 
def validateCb(cbList):
    if any(cbList):
        return True
    return False

# Function to obtain medicine category and medicine names from csv file
# populate a global dictionary object
dict_medcat={}
# open csv file for write
f=open("medicine.csv","r")
reader=csv.reader(f)
for row in reader:
    if row!=[]:
        if row[0] not in dict_medcat:
            dict_medcat[row[0]]=[row[1]]
        else:
            dict_medcat[row[0]].append(row[1])
f.close()

# Function to center the window on the desktop
def centerwindow(root, windowWidth,windowHeight):
    window_sw = root.winfo_screenwidth()
    window_sh = root.winfo_screenheight()
    
    # Gets both half the screen width/height and window width/height
    x = (window_sw/2) - (windowWidth/2)
    y = (window_sh/2) - (windowHeight/2)
    
    # Positions the window in the center of the page.
    root.geometry('%dx%d+%d+%d' % (windowWidth,windowHeight,x,y))

# Function to validate phone during key press event. Limits to enter number and 10 digits
def validate(P):
    if len(P)==0 or len(P)<=10 and P.isdigit():
        return True
    else:
        return False 

# Function to validate year during key press event. Limits to enter number and 4 digits
def validate_year(P):
    if len(P)==0 or len(P)<=4 and P.isdigit():
        return True
    else:
        return False 

# Function to check if the given mobile number is present in PatientDetails table
def refill_validate(mob):
    RConn=DBOperations.openDbConnection()
    RCursor=RConn.cursor()
    RQuery="SELECT MobileNumber from PatientDetails where MobileNumber="+mob
    RCursor.execute(RQuery)
    RList=RCursor.fetchall()
    DBOperations.closeDbConnection(RConn)
    if len(RList)>0:
        return True
    else:
        return False

# get distinct category values from meds_db for use in combox box
def getCategoryValues():
    prescConn=DBOperations.openDbConnection()
    prescCursor=prescConn.cursor()
    getCategoriesQuery=("SELECT distinct(Category) FROM Meds_db ORDER BY Category")
    prescCursor.execute(getCategoriesQuery)
    list=prescCursor.fetchall()
    DBOperations.closeDbConnection(prescConn)
    return list