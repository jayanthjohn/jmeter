import csv
import sys
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_sheet.py <spreadsheet_id>")
        sys.exit(1)

    spreadsheet_id = sys.argv[1]
    sheet_name = "Sheet1"  # You can make this dynamic too if needed

    creds = Credentials.from_service_account_file(
        'service-account.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    service = build('sheets', 'v4', credentials=creds)

    with open('output.csv', newline='') as f:
        reader = csv.reader(f)
        values = list(reader)

    # Optional: clear old data
    service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range=f'{sheet_name}!A1:Z1000'
    ).execute()

    body = {'values': values}

    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f'{sheet_name}!A1',
        valueInputOption='RAW',
        body=body
    ).execute()

    print(f"{result.get('updatedCells')} cells updated in Google Sheet.")

if __name__ == "__main__":
    main()
