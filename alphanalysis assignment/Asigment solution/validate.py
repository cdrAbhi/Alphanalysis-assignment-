import datetime

# Function to validate date format: YYYY-MM-DD
def validateDate(s):
    c=True
    while c:
        date = input(f"Enter {s} (YYYY-MM-DD): ")
        sdl = list(date.split("-"))
        
        # Ensure that the date has the correct format (YYYY-MM-DD)
        if len(sdl) != 3:
            print("Invalid format! Please enter the date in YYYY-MM-DD format.")
            continue
        
        # Check if the year is a valid number and greater than 1999
        elif not sdl[0].isnumeric() or int(sdl[0]) < 2000:
            print("Invalid YEAR value! YEAR must be greater than 1999.")
            continue
        
        # Check if the month is valid (between 1 and 12)
        elif not sdl[1].isnumeric() or int(sdl[1]) < 1 or int(sdl[1]) > 12:
            print("Invalid MONTH value! MONTH must be between 1 and 12.")
            continue
        
        # Check if the day is valid (between 1 and 31) based on the month
        elif not sdl[2].isnumeric() or int(sdl[2]) < 1 or int(sdl[2]) > 31:
            print("Invalid DAY value! DAY must be between 1 and 31.")
            continue
        else :
        # Now check if the date is actually valid by trying to parse it
            c=False
    return date 
        

# Function to validate total amount (numeric, greater than 0)
def ValidateTotalAmountValue():
    c=True
    while c:
        totalAmount = input("Enter Total_investment_amount: ")
        
        # Check if the total amount is numeric
        if not totalAmount.isnumeric():
            print("Invalid input! Please enter a numeric value.")
            continue
        
        # Check if the amount is greater than 0
        elif int(totalAmount) <= 0:
            print("Invalid amount value! Amount must be greater than or equal to 1.")
            continue
        else:
            c=False
    return totalAmount

# sdate = validateDate("Start_Date")
# edate = validateDate("End_Date")
# total_investment = ValidateTotalAmountValue()

# print(f"Start Date: {sdate} and type:{type(sdate)}\n, End Date: {edate} and type:{type(edate)}\n, Total Investment: {total_investment} and type:{type(total_investment)}")