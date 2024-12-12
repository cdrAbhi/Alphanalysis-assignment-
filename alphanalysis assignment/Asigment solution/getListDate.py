import pandas as pd

def generate_date_list(start_date, end_date):
    """
    Generate a list of dates from start_date to end_date in 'yyyy-mm-dd' format.
    :param start_date: str, start date in 'yyyy-mm-dd' format
    :param end_date: str, end date in 'yyyy-mm-dd' format
    :return: list of dates in 'yyyy-mm-dd' format
    """
    try:
        # Use pandas.date_range to generate the date range
        date_range = pd.date_range(start=start_date, end=end_date)
        # Convert to a list of strings in 'yyyy-mm-dd' format
        date_list = [date.strftime('%Y-%m-%d') for date in date_range]
        return date_list
    except Exception as e:
        print(f"Error generating date list: {e}")
        return []

# # Example Usage
# start_date = "2024-10-01"
# end_date = "2024-10-10"
# date_list = generate_date_list(start_date, end_date)
# print(date_list)
