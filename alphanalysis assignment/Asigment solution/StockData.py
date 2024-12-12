import yfinance as y
import pandas as pd
from getListDate import generate_date_list;

print("*" * 50)


# Function to create the stock data record
def CreateRecord(sdate, edate, total_invest, weightage, ticker):
    try: 

        # Initialize list with the ticker and weightage
        l = [ticker, weightage]

        listdate = generate_date_list(sdate,edate)
        i=0
        # Download the stock data
        data = y.download(ticker, start=sdate, end=edate, interval="1d")
        
        if data.empty:
            print(f"No data available for ticker: {ticker}")
            return
        
        pday=int(sdate.split("-")[2]);
        # Iterate through the DataFrame rows
        for index, row in data.iterrows():


            date = index.strftime("%Y-%m-%d")  # Convert index to string (date)
            cPrice = row['Close']  # Get the closing price
            
            if listdate[i]!=date:
                while listdate[i]!=date:
                    l.append("Data Not Found")
                    # print(f"{listdate[i]}: Num_Shares : N/A")
                    i+=1
                i+=1    
            else:
                i+=1        

            # Handle cases where cPrice might be a Series
            if isinstance(cPrice, pd.Series):
                cPrice = cPrice.iloc[0]
  
            try:
                cPrice = float(cPrice)  # Convert to float
                # Calculate number of shares
                num_shares = float((total_invest * weightage) / cPrice)
                # print(f"{date}: Num_Shares : {num_shares}")
                l.append(num_shares)  # Append number of shares
            except Exception as calc_error:
                print(f"{date}: Error in calculation - {calc_error}")
                l.append("Calc_Error")  # Append an error marker
        
        while(i!=len(listdate)):
            l.append("Data Not Found") 
            i+=1
        # Print the final list for debugging
        # print(ticker, " : ", l)    
        return l
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
