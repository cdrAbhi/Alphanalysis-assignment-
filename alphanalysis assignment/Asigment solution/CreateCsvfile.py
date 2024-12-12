#Program for creating CSV File by using CSV module
#CSVWriterEx1.py----csv.writer()
#Step-1--->Take Header Names Or Col Names
import csv
from getRecord import recordlist ;
import validate
from getListDate import generate_date_list;

option = """This program generates a CSV file with stock data based on the following parameters:
- "TICKER"
- "WEIGHTAGE"
- "TOTAL_INVESTMENT"
- "STARTDATE"
- "ENDDATE"

================================================
Example CSV Output Format:
"TICKER"           "WEIGHTAGE"   "2024-10-01"
------------------------------------------------
ADANIPORTS.NS,     0.0082,        0.055877342419080066
APOLLOHOSP.NS,     0.0061,        0.00852747302553894
ASIANPAINT.NS,     0.0195,        0.059499288812462074
------------------------------------------------

To generate the CSV, please provide the following inputs in the specified format:

------------------------------------------------
Start Date (yyyy-mm-dd): 2024-10-01 
End Date (yyyy-mm-dd): 2024-10-15
Total Investment Amount: 1000
"""

print(option)

sdate = validate.validateDate("Start_Date")
edate = validate.validateDate("End_Date")
total_investment = int(validate.ValidateTotalAmountValue())

colnames = ["TICKER","WEIGHTAGE"]
colnames.extend(generate_date_list(sdate,edate))

#Step-2---->Take Records--always in the form of Lists in List
records= recordlist(sdate,edate,total_investment)# Lists of list

#Step-3--Choose the file name and open in write mode
filepath=f"C:\\Users\\Refurbished Lappify\\Downloads\\movie-Download\\Micro-soft-Edge\\trading data fetch Assigment\\alphanalysis assignment\\Stocks-table[{sdate}] to [{edate}].csv"

try :
    with open(filepath,"w") as fp:
        csvwr=csv.writer(fp) # here csvwr is an object of <class, csv.Writer>
        #Step-4---Write Header Name
        csvwr.writerow(colnames)

        #Step-5---write Records
        csvwr.writerows(records)

        print("=====CSV File Created--Verify=====")
except Exception as err:
    print("Error in CSV file Creation",err)
