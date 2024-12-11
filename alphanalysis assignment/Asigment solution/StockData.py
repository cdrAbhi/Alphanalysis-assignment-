import yfinance as y

print("*"*50)


# Function to create the stock data record
def CreateRecord(sdate, edate, total_invest, weightage, ticker):
    try:
        # Download the stock data
        data = y.download(ticker, start=sdate, end=edate, interval="1d")
        
        if data.empty:
            print(f"No data available for ticker: {ticker}")
            return

        # Initialize list with the ticker and weightage
        l = [ticker, weightage]

        # Iterate through the DataFrame rows
        for index, row in data.iterrows():
            date = index.strftime("%Y-%m-%d")  # Convert index to string (date)
            cPrice = float(row['Close'])  # Get the closing price

            # If the date matches the end date, break after recording
            num_shares = (total_invest * weightage) / cPrice  # Calculate number of shares
            l.append(num_shares)  # Append date, price, and shares
        return l
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")


