import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
    ]

creds = ServiceAccountCredentials.from_json_keyfile_name('/workspace/237_sales_report/data/mykeys.json', scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open('237_Sales_Report')
sheet = workbook.sheet1
for cell in sheet.range('A2:A6'):
    print(cell.value)
