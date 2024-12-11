import csv
from StockData import CreateRecord;

def recordlist(sdate,edate,total_investment):
    try :
        with open("C:\\Users\Refurbished Lappify\\Downloads\\movie-Download\\Micro-soft-Edge\\trading data fetch Assigment\\alphanalysis assignment\\Stocks.csv","r") as fp:
            csvdr=csv.DictReader(fp) # here csvdr is an object of <class, csv.DictReader>
            record=[]
            for row in csvdr:
                ticker = row['Ticker']  # Extract the 'Ticker' value
                weightage = float(row['Weightage'])  # Extract and convert 'Weightage' to float
                l = CreateRecord(sdate,edate,total_investment,weightage,ticker)
                record.append(l)   
            return record    
    except Exception as err:
        print("Error during Creating record :",err)
        
