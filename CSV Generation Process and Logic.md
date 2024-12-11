**CSV file Generation Process and Logic**
==========================================
![image](https://github.com/user-attachments/assets/861ca8aa-47ea-42cf-b904-971310e65c20)

![image](https://github.com/user-attachments/assets/bf292005-8b5c-49e9-8aba-88a2dc8bc712)


### **Objective:**
The program generates a CSV file with a timetable-like format containing stock data based on user input for:
- Start date
- End date
- Total investment amount

The program fetches daily stock data from Yahoo Finance and calculates the number of shares that can be purchased for each stock based on its weightage and closing price.

### **Overview of the Code Structure:**

1. **`CreateCsvfile.py`:**
   - Handles user interaction, validates input, and generates the final CSV file.
   - Uses the `csv` module to write data into a CSV format.

2. **`getRecord.py`:**
   - Extracts data from a predefined `Stocks.csv` file.
   - Calls `StockData.CreateRecord` to fetch and compute stock-related data.

3. **`StockData.py`:**
   - Interfaces with the Yahoo Finance API to download daily stock data.
   - Computes the number of shares that can be purchased based on weightage and closing price.

4. **`validate.py`:**
   - Contains helper functions to validate user inputs for dates and total investment amount.

---

### **Detailed Process Explanation:**

#### **Step 1: Accept User Input**
- **Purpose:** Gather essential data from the user.
  - Start Date: Ensure it is in `YYYY-MM-DD` format and greater than 1999.
  - End Date: Similar validation as Start Date.
  - Total Investment: Must be a positive numeric value.

- **Validation Logic:**
  - Input dates are validated for proper format and logical constraints (e.g., valid day, month, year).
  - Total investment must be numeric and greater than 0.

#### **Step 2: Define CSV Structure**
- **Header Creation:**
  - Columns include:
    - Ticker
    - Weightage
    - Dates (based on the user-specified range).
  - Dynamically generated date columns are appended based on the input range.

#### **Step 3: Read Stock Data**
- The `getRecord.py` file reads stock tickers and weightage from a predefined `Stocks.csv` file.
- The data is passed to `StockData.CreateRecord` for processing.

#### **Step 4: Fetch Stock Data and Calculate Shares**
- **Yahoo Finance API:**
  - Fetches daily stock data (e.g., closing price) for the specified date range.
- **Calculations:**
  - Investment per stock = (Total Investment) * (Weightage).
  - Number of shares = Investment per stock / Closing Price.

#### **Step 5: Write Data to CSV**
- **Filepath:** A unique file path is generated for every execution.
- **CSV Writing:**
  - The header row is written first.
  - Each row contains:
    - Stock ticker
    - Weightage
    - Number of shares for each date.

#### **Error Handling:**
- **Input Validation:**
  - Ensures date and amount inputs are in the correct format.
- **Data Fetching:**
  - Handles cases where stock data might be missing or incomplete.
  - Skips tickers with no available data.

---

### **Code Insights and Best Practices:**

1. **Modular Design:**
   - Code is split into multiple files, each handling a specific task:
     - Input validation
     - Data fetching
     - CSV creation.

2. **Error Handling:**
   - Comprehensive checks for user input.
   - Exception handling for external API calls (e.g., Yahoo Finance).

3. **Dynamic Header Creation:**
   - Adjusts column headers based on user-provided date range.

4. **Reusable Functions:**
   - Validation and record generation functions are generic and reusable for other datasets.

5. **Professional Output:**
   - The program generates a structured timetable-like CSV file with clear and labeled columns.

---

### **How to Run the Program:**
1. Execute `CreateCsvfile.py`.
2. Provide the requested inputs:
   - Start date
   - End date
   - Total investment amount.
3. Verify the generated CSV file in the specified output directory.

### **Dependencies:**
- `yfinance` for fetching stock data.
- `csv` for writing to CSV files.
- `pandas` for any future data manipulation (optional).

---

### **Expected Output:**
A CSV file with the following structure:
```
Ticker          Weightage   YYYY-MM-DD   YYYY-MM-DD   ...
ADANIPORTS.NS   0.0082      100.0        102.5       ...
APOLLOHOSP.NS   0.0061      50.0         51.0        ...
```
Each date column represents the number of shares that can be purchased for the corresponding ticker on that date.

