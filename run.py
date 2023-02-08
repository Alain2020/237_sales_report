import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
    ]

creds = ServiceAccountCredentials.from_json_keyfile_name('/workspace/237_sales_report/data/mykeys.json', scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open('237_Sales_Report')

def get_sales_data():
    """
    Get sales figures input from the user.
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")


get_sales_data()